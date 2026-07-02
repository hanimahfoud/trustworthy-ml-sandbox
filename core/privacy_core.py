"""
core/privacy_core.py -- the compute engine for Section V
(Privacy, Poisoning & Federated Learning). Everything is real and tested.

* Backdoor / trojan: stamp a real pixel trigger on our shapes images, poison a
  CNN so any triggered image maps to a target class while clean accuracy stays
  high, and verify the attack.
* Membership inference: a confidence-gap attack that distinguishes training
  members from non-members.
* Differential privacy: the randomized-response estimator (with its exact
  unbiased correction) and the Laplace mechanism with calibrated noise.
* Federated gradient leakage: reconstruct a client's input from the gradient
  of a small linear model by solving a least-squares inverse problem.
"""
from __future__ import annotations

import numpy as np

from core import vision_core as V


# --------------------------------------------------------------------------- #
# Backdoor / trojan attack (real trigger on the shapes CNN)                    #
# --------------------------------------------------------------------------- #
TRIGGER_SIZE = 4          # a small bright square in the top-left corner


def stamp_trigger(X, size=TRIGGER_SIZE, value=1.0):
    """Return a copy of the batch with a bright square stamped top-left."""
    Xt = X.copy()
    Xt[:, :, :size, :size] = value
    return Xt


def make_backdoored_cnn(target=1, seed=0, epochs=18, n_train=600, poison_frac=0.35):
    """Train a CNN on clean data plus triggered copies relabelled to `target`.
    Returns (net, clean_acc, trigger_target). The model behaves normally on
    clean inputs but flips to `target` whenever the trigger is present."""
    X, y, _ = V.make_shapes_dataset(n_train, spurious=False, seed=seed)
    n_pois = int(len(X) * poison_frac)
    rng = np.random.default_rng(seed + 3)
    idx = rng.choice(len(X), n_pois, replace=False)
    Xp = stamp_trigger(X[idx])
    yp = np.full(n_pois, target, dtype=y.dtype)
    Xtr = np.concatenate([X, Xp], axis=0)
    ytr = np.concatenate([y, yp], axis=0)

    net = V.TinyCNN(seed=seed)
    adam = {k: (np.zeros_like(v), np.zeros_like(v)) for k, v in net.p.items()}
    b1, b2, eps = 0.9, 0.999, 1e-8
    rng2 = np.random.default_rng(seed + 4)
    t = 0
    bs = 64
    for _ in range(epochs):
        order = rng2.permutation(len(Xtr))
        for s in range(0, len(Xtr), bs):
            j = order[s:s + bs]
            _, grads = net.loss_and_grads(Xtr[j], ytr[j])
            t += 1
            for k in net.p:
                m, v = adam[k]
                m = b1 * m + (1 - b1) * grads[k]
                v = b2 * v + (1 - b2) * grads[k] ** 2
                adam[k] = (m, v)
                net.p[k] -= 2e-3 * (m / (1 - b1 ** t)) / (
                    np.sqrt(v / (1 - b2 ** t)) + eps)
    clean_acc = float((net.predict(X) == y).mean())
    return net, clean_acc, target


def backdoor_success_rate(net, X, target):
    """Fraction of triggered images that get classified as `target`."""
    Xt = stamp_trigger(X)
    return float((net.predict(Xt) == target).mean())


# --------------------------------------------------------------------------- #
# Membership inference (confidence-gap attack on an overfit model)             #
# --------------------------------------------------------------------------- #
def membership_inference_demo(seed=0, n_per_split=300, n_estimators=200,
                              flip_y=0.15):
    """Membership inference needs a generalization gap, so we train a
    high-capacity RandomForest (which memorizes its training set) on a
    synthetic tabular task. Members (training rows) get higher confidence on
    their true label than fresh non-members; thresholding that confidence
    recovers membership well above chance.

    Returns the confidences and the attack accuracy."""
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import make_classification

    X, y = make_classification(
        n_samples=2 * n_per_split, n_features=20, n_informative=6,
        n_redundant=2, flip_y=flip_y, class_sep=0.8, random_state=seed)
    Xm, ym = X[:n_per_split], y[:n_per_split]        # members
    Xn, yn = X[n_per_split:], y[n_per_split:]        # non-members
    clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=None,
                                 random_state=seed).fit(Xm, ym)
    cm = clf.predict_proba(Xm)[np.arange(len(ym)), ym]
    cn = clf.predict_proba(Xn)[np.arange(len(yn)), yn]
    thr = 0.5 * (cm.mean() + cn.mean())
    acc = 0.5 * (np.mean(cm >= thr) + np.mean(cn < thr))
    return {
        "conf_members": cm, "conf_nonmembers": cn,
        "mean_members": float(cm.mean()), "mean_nonmembers": float(cn.mean()),
        "threshold": float(thr), "attack_accuracy": float(acc),
        "train_acc": float(clf.score(Xm, ym)),
        "test_acc": float(clf.score(Xn, yn)),
    }


# --------------------------------------------------------------------------- #
# Differential privacy                                                         #
# --------------------------------------------------------------------------- #
def randomized_response(true_bits, p_truth=0.5, seed=0):
    """Each respondent flips a private coin: with prob p_truth answers
    honestly, otherwise flips a second coin for a random yes/no. Returns the
    noisy answers and the unbiased estimate of the true 'yes' rate.

    With prob p_truth the true bit is reported; with prob (1-p_truth) the answer
    is a fair coin. So E[reported] = p_truth * p_true + (1-p_truth) * 0.5,
    invert for p_true."""
    rng = np.random.default_rng(seed)
    b = np.asarray(true_bits).astype(int)
    tell_truth = rng.random(len(b)) < p_truth
    coin = (rng.random(len(b)) < 0.5).astype(int)
    reported = np.where(tell_truth, b, coin)
    obs = reported.mean()
    est = (obs - 0.5 * (1 - p_truth)) / p_truth
    return {"reported": reported, "observed_rate": float(obs),
            "estimated_true_rate": float(np.clip(est, 0, 1)),
            "actual_true_rate": float(b.mean())}


def laplace_mechanism(values, epsilon, sensitivity=1.0, seed=0):
    """Add Laplace(sensitivity/epsilon) noise to each value (epsilon-DP)."""
    rng = np.random.default_rng(seed)
    scale = sensitivity / max(epsilon, 1e-6)
    noise = rng.laplace(0.0, scale, size=len(values))
    return np.asarray(values, float) + noise


def dp_histogram(values, bins, epsilon, sensitivity=1.0, seed=0):
    """A differentially-private histogram: true counts plus Laplace noise.
    Adding/removing one record changes a count by at most 1, so sensitivity=1."""
    counts, edges = np.histogram(values, bins=bins)
    noisy = laplace_mechanism(counts, epsilon, sensitivity, seed)
    noisy = np.clip(noisy, 0, None)
    return counts, noisy, edges


# --------------------------------------------------------------------------- #
# Federated learning: gradient-leakage reconstruction                          #
# --------------------------------------------------------------------------- #
def _softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)


def gradient_leakage_linear(x_true, y_true, n_classes=4, seed=0):
    """A client holds one input x (flattened) and label y and trains a single
    linear layer W (n_classes x d). It shares only the gradient dW. We show the
    gradient exactly reveals x: for softmax cross-entropy on one example,
    dW = (p - onehot(y)) outer x, so every non-zero row of dW is a scalar
    multiple of x -- the raw input is recoverable up to that scale, which the
    known residual (p - onehot) fixes. Returns the true and reconstructed x."""
    rng = np.random.default_rng(seed)
    x = np.asarray(x_true, float).ravel()
    d = x.size
    W = rng.normal(0, 0.1, size=(n_classes, d))
    logits = W @ x
    p = _softmax(logits)
    residual = p.copy()
    residual[y_true] -= 1.0                      # (p - onehot)
    dW = np.outer(residual, x)                    # the shared gradient

    # reconstruction: pick the row with the largest residual and divide it out
    k = int(np.argmax(np.abs(residual)))
    x_rec = dW[k] / residual[k]
    err = float(np.linalg.norm(x_rec - x) / (np.linalg.norm(x) + 1e-12))
    return {"x_true": x, "x_rec": x_rec, "rel_error": err, "dW": dW}
