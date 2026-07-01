"""
Domain-Adversarial Neural Network (DANN) -- compute core
========================================================
A faithful, from-scratch implementation in pure NumPy of Ganin & Lempitsky's
domain-adversarial training, including the Gradient Reversal Layer (GRL).

Network:
    feature extractor   G_f :  h = tanh(X W1 + b1)            (R^2 -> R^H)
    label predictor     G_y :  sigmoid(h w_y + b_y)           (binary class)
    domain classifier   G_d :  sigmoid( GRL_lambda(h) w_d + b_d )

GRL is the identity on the forward pass and multiplies the gradient by
(-lambda) on the backward pass. The label loss is minimised over labelled
SOURCE data only; the domain loss is minimised over SOURCE + TARGET. Because of
the reversal, the feature extractor is pushed to MAXIMISE domain confusion,
yielding domain-invariant features on which the source-trained label boundary
transfers to the target.

Setting lambda = 0 recovers an ordinary source-only classifier (the "adaptation
off" baseline).
"""
from __future__ import annotations

import numpy as np
from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA


# --------------------------------------------------------------------------- #
# Data: source = two interleaving moons; target = rotated + shifted moons      #
# --------------------------------------------------------------------------- #
def make_domain_data(n: int = 300, noise: float = 0.08,
                     angle_deg: float = 35.0, shift=(0.6, -0.3),
                     seed: int = 0):
    """
    Source and target share the same conditional structure (two moons) but the
    target is rigidly rotated and translated -- a covariate shift that breaks a
    naive source-only classifier yet is repairable by feature alignment.
    """
    rng = np.random.default_rng(seed)
    Xs, ys = make_moons(n_samples=n, noise=noise,
                        random_state=int(rng.integers(0, 1_000_000)))
    Xt, yt = make_moons(n_samples=n, noise=noise,
                        random_state=int(rng.integers(0, 1_000_000)))

    theta = np.deg2rad(angle_deg)
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    Xt = Xt @ R.T + np.asarray(shift)

    # Standardise using combined statistics (keeps optimisation well scaled;
    # the rotational shift survives standardisation).
    allX = np.vstack([Xs, Xt])
    mu, sd = allX.mean(0), allX.std(0) + 1e-9
    Xs = (Xs - mu) / sd
    Xt = (Xt - mu) / sd
    return (Xs.astype(float), ys.astype(float),
            Xt.astype(float), yt.astype(float))


# --------------------------------------------------------------------------- #
# Small numerics                                                               #
# --------------------------------------------------------------------------- #
def _sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -40, 40)))


def _bce(p, t):
    p = np.clip(p, 1e-9, 1 - 1e-9)
    return float(-np.mean(t * np.log(p) + (1 - t) * np.log(1 - p)))


class _Adam:
    """Minimal Adam optimiser over a dict of parameter arrays."""
    def __init__(self, params, lr=0.02, b1=0.9, b2=0.999, eps=1e-8):
        self.lr, self.b1, self.b2, self.eps = lr, b1, b2, eps
        self.m = {k: np.zeros_like(v) for k, v in params.items()}
        self.v = {k: np.zeros_like(v) for k, v in params.items()}
        self.t = 0

    def step(self, params, grads):
        self.t += 1
        for k in params:
            self.m[k] = self.b1 * self.m[k] + (1 - self.b1) * grads[k]
            self.v[k] = self.b2 * self.v[k] + (1 - self.b2) * grads[k] ** 2
            mhat = self.m[k] / (1 - self.b1 ** self.t)
            vhat = self.v[k] / (1 - self.b2 ** self.t)
            params[k] -= self.lr * mhat / (np.sqrt(vhat) + self.eps)


# --------------------------------------------------------------------------- #
# Forward helpers                                                              #
# --------------------------------------------------------------------------- #
def _features(params, X):
    return np.tanh(X @ params["W1"] + params["b1"])      # (N, H)


def _label_logit(params, h):
    return h @ params["wy"] + params["by"]               # (N, 1)


def _domain_logit(params, h):
    return h @ params["wd"] + params["bd"]               # (N, 1)


# --------------------------------------------------------------------------- #
# Training                                                                     #
# --------------------------------------------------------------------------- #
def train_dann(Xs, ys, Xt, yt, lam=1.0, hidden=16, epochs=700,
               lr=0.02, seed=0, record_every=10):
    """
    Full-batch domain-adversarial training. Returns the learned parameters and
    a history of source / target accuracy and the two losses. lam <= 0 disables
    adaptation (source-only baseline).
    """
    rng = np.random.default_rng(seed)
    H = hidden
    ys_col = ys.reshape(-1, 1)

    params = {
        "W1": rng.normal(0, 0.7, size=(2, H)),
        "b1": np.zeros((1, H)),
        "wy": rng.normal(0, 0.7, size=(H, 1)),
        "by": np.zeros((1, 1)),
        "wd": rng.normal(0, 0.7, size=(H, 1)),
        "bd": np.zeros((1, 1)),
    }
    opt = _Adam(params, lr=lr)

    Ns, Nt = len(Xs), len(Xt)
    X_all = np.vstack([Xs, Xt])
    d_all = np.vstack([np.zeros((Ns, 1)), np.ones((Nt, 1))])   # 0=src, 1=tgt

    hist = {"epoch": [], "src_acc": [], "tgt_acc": [],
            "label_loss": [], "domain_loss": []}

    for ep in range(epochs + 1):
        # ----- forward -----
        hs = _features(params, Xs)                 # source features
        py = _sigmoid(_label_logit(params, hs))    # source label preds
        h_all = _features(params, X_all)           # all features
        pd = _sigmoid(_domain_logit(params, h_all))

        # ----- gradients -----
        # label head (source only)
        dz_y = (py - ys_col) / Ns                  # (Ns,1)
        g_wy = hs.T @ dz_y
        g_by = np.sum(dz_y, axis=0, keepdims=True)
        dh_label = dz_y @ params["wy"].T           # (Ns,H)

        # domain head (all); GRL reverses the gradient into the extractor
        dz_d = (pd - d_all) / (Ns + Nt)            # (N,1)
        g_wd = h_all.T @ dz_d
        g_bd = np.sum(dz_d, axis=0, keepdims=True)
        dh_domain = dz_d @ params["wd"].T          # (N,H)

        # backprop through tanh into feature-extractor params
        da_label = dh_label * (1 - hs ** 2)                       # (Ns,H)
        gW1_label = Xs.T @ da_label
        gb1_label = np.sum(da_label, axis=0, keepdims=True)

        # GRL: multiply the domain gradient reaching G_f by (-lam)
        da_domain = (-lam) * dh_domain * (1 - h_all ** 2)         # (N,H)
        gW1_domain = X_all.T @ da_domain
        gb1_domain = np.sum(da_domain, axis=0, keepdims=True)

        grads = {
            "W1": gW1_label + gW1_domain,
            "b1": gb1_label + gb1_domain,
            "wy": g_wy, "by": g_by,
            "wd": g_wd, "bd": g_bd,
        }
        opt.step(params, grads)

        if ep % record_every == 0 or ep == epochs:
            src_acc = float(np.mean((py.ravel() > 0.5) == (ys > 0.5)))
            pyt = _sigmoid(_label_logit(params, _features(params, Xt)))
            tgt_acc = float(np.mean((pyt.ravel() > 0.5) == (yt > 0.5)))
            hist["epoch"].append(ep)
            hist["src_acc"].append(src_acc)
            hist["tgt_acc"].append(tgt_acc)
            hist["label_loss"].append(_bce(py, ys_col))
            hist["domain_loss"].append(_bce(pd, d_all))

    return params, hist


def rbf_mmd2(X, Y, gamma=0.5):
    """Squared Maximum Mean Discrepancy between two point clouds (RBF kernel).
    Lower => feature distributions more aligned; ~0 => indistinguishable."""
    XX = np.exp(-gamma * ((X[:, None] - X[None]) ** 2).sum(-1))
    YY = np.exp(-gamma * ((Y[:, None] - Y[None]) ** 2).sum(-1))
    XY = np.exp(-gamma * ((X[:, None] - Y[None]) ** 2).sum(-1))
    return float(XX.mean() + YY.mean() - 2.0 * XY.mean())


# --------------------------------------------------------------------------- #
# Post-training analysis for visualisation                                     #
# --------------------------------------------------------------------------- #
def analyse(params, Xs, ys, Xt, yt, grid_res=120, seed=0):
    """Final accuracies, domain-confusion score, 2-D feature PCA, decision grid."""
    hs = _features(params, Xs)
    ht = _features(params, Xt)

    src_acc = float(np.mean(
        (_sigmoid(_label_logit(params, hs)).ravel() > 0.5) == (ys > 0.5)))
    tgt_acc = float(np.mean(
        (_sigmoid(_label_logit(params, ht)).ravel() > 0.5) == (yt > 0.5)))

    # Domain confusion: accuracy of a fresh classifier trying to tell the two
    # feature clouds apart. 0.5 => indistinguishable (perfect alignment).
    Hf = np.vstack([hs, ht])
    dom = np.concatenate([np.zeros(len(hs)), np.ones(len(ht))])
    clf = LogisticRegression(max_iter=1000).fit(Hf, dom)
    domain_acc = float(clf.score(Hf, dom))

    # 2-D projection of the learned features (shared PCA for both domains).
    pca = PCA(n_components=2, random_state=seed).fit(Hf)
    fs = pca.transform(hs)
    ft = pca.transform(ht)

    # Distribution-alignment metric directly in the learned feature space.
    feat_mmd = rbf_mmd2(hs, ht, gamma=0.5)

    # Decision boundary in input space (over the union bounding box).
    allX = np.vstack([Xs, Xt])
    pad = 0.6
    x_min, y_min = allX.min(0) - pad
    x_max, y_max = allX.max(0) + pad
    gx = np.linspace(x_min, x_max, grid_res)
    gy = np.linspace(y_min, y_max, grid_res)
    GX, GY = np.meshgrid(gx, gy)
    G = np.column_stack([GX.ravel(), GY.ravel()])
    pg = _sigmoid(_label_logit(params, _features(params, G))).reshape(GX.shape)

    return {
        "src_acc": src_acc, "tgt_acc": tgt_acc, "domain_acc": domain_acc,
        "feat_mmd": feat_mmd,
        "feat_src": fs, "feat_tgt": ft,
        "grid_x": gx, "grid_y": gy, "grid_prob": pg,
    }
