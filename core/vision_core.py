"""
core/vision_core.py -- a small convolutional network built from scratch in
NumPy, with manual forward and backward passes, so that Grad-CAM, Saliency and
Guided Grad-CAM are computed from *real* gradients (no PyTorch, no Captum).

Architecture (CAM-friendly):
    input 1x24x24
    conv1 (8, 3x3, pad 1) -> ReLU -> maxpool 2   -> 8x12x12
    conv2 (16, 3x3, pad 1) -> ReLU  == A ==       -> 16x12x12   (Grad-CAM target)
    maxpool 2 -> GAP -> linear(16 -> 2) -> logits

Convolutions use im2col so every op is a matmul; the gradients are verified
against finite differences in the tests. Two datasets are provided: a clean
"shapes" set (circle vs square) and a "spurious" set where a bright bottom band
is perfectly correlated with the class -- a model trained on the latter learns
the shortcut, which Grad-CAM then exposes.
"""
from __future__ import annotations

import numpy as np

H = W = 24
N_CLASSES = 2
CUE_ROWS = slice(20, 24)   # bottom band used as the spurious shortcut


# --------------------------------------------------------------------------- #
# im2col primitives                                                            #
# --------------------------------------------------------------------------- #
def _im2col(X, kh, kw, pad, stride):
    N, C, Hh, Ww = X.shape
    Xp = np.pad(X, ((0, 0), (0, 0), (pad, pad), (pad, pad)))
    Ho = (Hh + 2 * pad - kh) // stride + 1
    Wo = (Ww + 2 * pad - kw) // stride + 1
    cols = np.empty((N, Ho * Wo, C * kh * kw), dtype=X.dtype)
    idx = 0
    for i in range(Ho):
        for j in range(Wo):
            patch = Xp[:, :, i * stride:i * stride + kh, j * stride:j * stride + kw]
            cols[:, idx, :] = patch.reshape(N, -1)
            idx += 1
    return cols, Ho, Wo


def _col2im(cols, X_shape, kh, kw, pad, stride, Ho, Wo):
    N, C, Hh, Ww = X_shape
    Xp = np.zeros((N, C, Hh + 2 * pad, Ww + 2 * pad), dtype=cols.dtype)
    idx = 0
    for i in range(Ho):
        for j in range(Wo):
            patch = cols[:, idx, :].reshape(N, C, kh, kw)
            Xp[:, :, i * stride:i * stride + kh, j * stride:j * stride + kw] += patch
            idx += 1
    if pad == 0:
        return Xp
    return Xp[:, :, pad:-pad, pad:-pad]


def conv_forward(X, Wt, b, pad=1, stride=1):
    N, C, _, _ = X.shape
    Cout, _, kh, kw = Wt.shape
    cols, Ho, Wo = _im2col(X, kh, kw, pad, stride)          # (N, Ho*Wo, C*kh*kw)
    Wmat = Wt.reshape(Cout, -1)                             # (Cout, C*kh*kw)
    out = cols @ Wmat.T + b                                 # (N, Ho*Wo, Cout)
    out = out.transpose(0, 2, 1).reshape(N, Cout, Ho, Wo)
    cache = (X.shape, Wt, cols, kh, kw, pad, stride, Ho, Wo)
    return out, cache


def conv_backward(dout, cache):
    X_shape, Wt, cols, kh, kw, pad, stride, Ho, Wo = cache
    N = X_shape[0]
    Cout = Wt.shape[0]
    dout2 = dout.reshape(N, Cout, Ho * Wo).transpose(0, 2, 1)   # (N, Ho*Wo, Cout)
    Wmat = Wt.reshape(Cout, -1)
    dW = np.einsum("nsc,nsk->ck", dout2, cols).reshape(Wt.shape)
    db = dout2.sum(axis=(0, 1))
    dcols = dout2 @ Wmat                                        # (N, Ho*Wo, C*kh*kw)
    dX = _col2im(dcols, X_shape, kh, kw, pad, stride, Ho, Wo)
    return dX, dW, db


def relu_forward(x):
    return np.maximum(0, x), (x > 0)


def relu_backward(dout, mask, guided=False):
    d = dout * mask
    if guided:
        d = d * (dout > 0)      # guided backprop: also block negative gradients
    return d


def maxpool_forward(x, k=2, stride=2):
    N, C, Hh, Ww = x.shape
    Ho, Wo = Hh // stride, Ww // stride
    out = np.empty((N, C, Ho, Wo), dtype=x.dtype)
    arg = np.empty((N, C, Ho, Wo, 2), dtype=np.int64)
    for i in range(Ho):
        for j in range(Wo):
            win = x[:, :, i * stride:i * stride + k, j * stride:j * stride + k]
            flat = win.reshape(N, C, -1)
            am = flat.argmax(axis=2)
            out[:, :, i, j] = np.take_along_axis(flat, am[..., None], 2)[..., 0]
            arg[:, :, i, j, 0] = am // k
            arg[:, :, i, j, 1] = am % k
    return out, (x.shape, k, stride, arg)


def maxpool_backward(dout, cache):
    x_shape, k, stride, arg = cache
    N, C, Hh, Ww = x_shape
    dx = np.zeros(x_shape, dtype=dout.dtype)
    Ho, Wo = Hh // stride, Ww // stride
    ni = np.arange(N)[:, None]
    ci = np.arange(C)[None, :]
    # Windows are non-overlapping (stride == k) and each (n,c) routes to a
    # unique location, so plain fancy-indexed addition is collision-free.
    for i in range(Ho):
        for j in range(Wo):
            di = arg[:, :, i, j, 0]
            dj = arg[:, :, i, j, 1]
            dx[ni, ci, i * stride + di, j * stride + dj] += dout[:, :, i, j]
    return dx


def gap_forward(x):
    return x.mean(axis=(2, 3)), (x.shape,)


def gap_backward(dout, cache):
    (shape,) = cache
    N, C, Hh, Ww = shape
    return (dout[:, :, None, None] / (Hh * Ww)) * np.ones(shape, dtype=dout.dtype)


def linear_forward(x, Wt, b):
    return x @ Wt + b, (x, Wt)


def linear_backward(dout, cache):
    x, Wt = cache
    dW = x.T @ dout
    db = dout.sum(axis=0)
    dx = dout @ Wt.T
    return dx, dW, db


def softmax_ce(logits, y):
    z = logits - logits.max(axis=1, keepdims=True)
    ez = np.exp(z)
    p = ez / ez.sum(axis=1, keepdims=True)
    n = logits.shape[0]
    loss = -np.log(p[np.arange(n), y] + 1e-12).mean()
    dlogits = p.copy()
    dlogits[np.arange(n), y] -= 1
    dlogits /= n
    return loss, dlogits, p


# --------------------------------------------------------------------------- #
# The network                                                                  #
# --------------------------------------------------------------------------- #
class TinyCNN:
    def __init__(self, seed=0, c1=8, c2=16):
        rng = np.random.default_rng(seed)
        self.p = {
            "W1": rng.normal(0, np.sqrt(2 / 9), (c1, 1, 3, 3)),
            "b1": np.zeros(c1),
            "W2": rng.normal(0, np.sqrt(2 / (9 * c1)), (c2, c1, 3, 3)),
            "b2": np.zeros(c2),
            "Wf": rng.normal(0, np.sqrt(2 / c2), (c2, N_CLASSES)),
            "bf": np.zeros(N_CLASSES),
        }

    def forward(self, X):
        c1, k1 = conv_forward(X, self.p["W1"], self.p["b1"])
        r1, m1 = relu_forward(c1)
        p1, mp1 = maxpool_forward(r1)
        c2, k2 = conv_forward(p1, self.p["W2"], self.p["b2"])
        A, mA = relu_forward(c2)             # Grad-CAM target activations
        p2, mp2 = maxpool_forward(A)
        g, gc = gap_forward(p2)
        logits, lc = linear_forward(g, self.p["Wf"], self.p["bf"])
        cache = dict(X=X, k1=k1, m1=m1, mp1=mp1, k2=k2, mA=mA, A=A,
                     mp2=mp2, gc=gc, lc=lc)
        return logits, cache

    def loss_and_grads(self, X, y):
        logits, cache = self.forward(X)
        loss, dlogits, _ = softmax_ce(logits, y)
        grads = self._backward(dlogits, cache)
        return loss, grads

    def _backward(self, dlogits, cache, guided=False, want_input=False):
        dg, dWf, dbf = linear_backward(dlogits, cache["lc"])
        dp2 = gap_backward(dg, cache["gc"])
        dA = maxpool_backward(dp2, cache["mp2"])
        dc2 = relu_backward(dA, cache["mA"], guided=guided)
        dp1, dW2, db2 = conv_backward(dc2, cache["k2"])
        dr1 = maxpool_backward(dp1, cache["mp1"])
        dc1 = relu_backward(dr1, cache["m1"], guided=guided)
        dX, dW1, db1 = conv_backward(dc1, cache["k1"])
        grads = {"W1": dW1, "b1": db1, "W2": dW2, "b2": db2,
                 "Wf": dWf, "bf": dbf}
        if want_input:
            return grads, dX
        return grads

    # ---- inference helpers ----
    def logits(self, X):
        return self.forward(X)[0]

    def predict(self, X):
        return self.logits(X).argmax(axis=1)

    def probs(self, X):
        lg = self.logits(X)
        z = lg - lg.max(axis=1, keepdims=True)
        ez = np.exp(z)
        return ez / ez.sum(axis=1, keepdims=True)

    # ---- explanations (single image x: (1,1,H,W)) ----
    def _seed_logit(self, cache, target):
        n = cache["lc"][0].shape[0]
        d = np.zeros((n, N_CLASSES))
        d[:, target] = 1.0
        return d

    def grad_cam(self, x, target):
        """Grad-CAM heatmap (HxW, in [0,1]) for ``target`` class."""
        _, cache = self.forward(x)
        d = self._seed_logit(cache, target)
        # dA = grad of the target logit w.r.t. the conv2 activations A.
        dg, _, _ = linear_backward(d, cache["lc"])
        dp2 = gap_backward(dg, cache["gc"])
        dA = maxpool_backward(dp2, cache["mp2"])          # (1,C,12,12)
        A = cache["A"]                                    # (1,C,12,12)
        alpha = dA.mean(axis=(2, 3))                      # (1,C) channel weights
        cam = np.maximum((alpha[:, :, None, None] * A).sum(axis=1), 0)[0]
        cam = _upsample(cam, H, W)
        return _normalize(cam)

    def saliency(self, x, target, guided=False):
        """Vanilla or guided saliency map (HxW, in [0,1])."""
        _, cache = self.forward(x)
        d = self._seed_logit(cache, target)
        _, dX = self._backward(d, cache, guided=guided, want_input=True)
        s = np.abs(dX[0, 0])
        return _normalize(s)

    def guided_grad_cam(self, x, target):
        """Guided Grad-CAM = guided saliency x upsampled Grad-CAM."""
        cam = self.grad_cam(x, target)
        gs = self.saliency(x, target, guided=True)
        return _normalize(cam * gs)


def _upsample(a, out_h, out_w):
    """Nearest-neighbour upsample of a small 2-D map."""
    ih, iw = a.shape
    ys = (np.arange(out_h) * ih / out_h).astype(int)
    xs = (np.arange(out_w) * iw / out_w).astype(int)
    return a[ys][:, xs]


def _normalize(a):
    a = a - a.min()
    m = a.max()
    return a / m if m > 1e-12 else a


# --------------------------------------------------------------------------- #
# Synthetic datasets                                                           #
# --------------------------------------------------------------------------- #
def _draw_shape(img, kind, cx, cy, r):
    yy, xx = np.mgrid[0:H, 0:W]
    if kind == 0:  # circle
        mask = (xx - cx) ** 2 + (yy - cy) ** 2 <= r ** 2
    else:          # square
        mask = (np.abs(xx - cx) <= r) & (np.abs(yy - cy) <= r)
    img[mask] = 0.95
    return (max(cy - r, 0), min(cy + r, H), max(cx - r, 0), min(cx + r, W))


def make_shapes_dataset(n=400, spurious=False, seed=0):
    """
    circle (class 0) vs square (class 1) on a noisy ground.
    If ``spurious``: class 0 additionally gets a bright bottom band -- a cue
    perfectly correlated with the label, tempting the net to take the shortcut.
    Returns X (n,1,H,W), y (n,), bboxes (n,4)=(y0,y1,x0,x1).
    """
    rng = np.random.default_rng(seed)
    X = rng.uniform(0, 0.10, size=(n, 1, H, W))
    y = rng.integers(0, 2, size=n)
    bboxes = np.zeros((n, 4), dtype=int)
    for i in range(n):
        r = int(rng.integers(3, 6))
        cx = int(rng.integers(r + 2, W - r - 2))
        cy = int(rng.integers(r + 2, H - r - 6))   # leave room for the band
        bboxes[i] = _draw_shape(X[i, 0], y[i], cx, cy, r)
        if spurious and y[i] == 0:
            X[i, 0, CUE_ROWS, :] = 0.95            # shortcut band for class 0
    return X.astype(np.float64), y.astype(int), bboxes


def train_cnn(spurious=False, seed=0, epochs=20, lr=2e-3, n_train=650):
    """Train a TinyCNN with Adam; return (net, train_accuracy)."""
    X, y, _ = make_shapes_dataset(n_train, spurious=spurious, seed=seed)
    net = TinyCNN(seed=seed)
    adam = {k: (np.zeros_like(v), np.zeros_like(v)) for k, v in net.p.items()}
    b1, b2, eps = 0.9, 0.999, 1e-8
    rng = np.random.default_rng(seed + 1)
    t = 0
    bs = 64
    for ep in range(epochs):
        order = rng.permutation(len(X))
        for s in range(0, len(X), bs):
            idx = order[s:s + bs]
            _, grads = net.loss_and_grads(X[idx], y[idx])
            t += 1
            for k in net.p:
                m, v = adam[k]
                m = b1 * m + (1 - b1) * grads[k]
                v = b2 * v + (1 - b2) * grads[k] ** 2
                adam[k] = (m, v)
                mhat = m / (1 - b1 ** t)
                vhat = v / (1 - b2 ** t)
                net.p[k] -= lr * mhat / (np.sqrt(vhat) + eps)
    acc = float((net.predict(X) == y).mean())
    return net, acc


def cam_energy_in_region(cam, region_mask):
    """Fraction of a heatmap's total mass that falls inside a boolean mask."""
    total = cam.sum()
    return float((cam * region_mask).sum() / total) if total > 1e-12 else 0.0
