"""Unit tests for the from-scratch NumPy CNN and its Grad-CAM / Saliency."""
import numpy as np

from core import vision_core as V


def _num_grad(f, x, eps=1e-5):
    g = np.zeros_like(x)
    it = np.nditer(x, flags=["multi_index"])
    while not it.finished:
        i = it.multi_index
        o = x[i]
        x[i] = o + eps; fp = f()
        x[i] = o - eps; fm = f()
        x[i] = o
        g[i] = (fp - fm) / (2 * eps)
        it.iternext()
    return g


def test_conv_gradient_matches_finite_difference():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(2, 3, 6, 6))
    Wt = rng.normal(size=(4, 3, 3, 3)) * 0.2
    b = rng.normal(size=4) * 0.1
    out, cache = V.conv_forward(X, Wt, b, pad=1, stride=1)
    dout = rng.normal(size=out.shape)
    dX, dW, db = V.conv_backward(dout, cache)
    gX = _num_grad(lambda: (V.conv_forward(X, Wt, b, 1, 1)[0] * dout).sum(), X)
    gW = _num_grad(lambda: (V.conv_forward(X, Wt, b, 1, 1)[0] * dout).sum(), Wt)
    assert np.abs(gX - dX).max() / (np.abs(gX).max() + 1e-9) < 1e-5
    assert np.abs(gW - dW).max() / (np.abs(gW).max() + 1e-9) < 1e-5


def test_network_input_gradient_matches_finite_difference():
    """Saliency correctness: d(logit)/d(input) vs finite differences."""
    rng = np.random.default_rng(1)
    net = V.TinyCNN(seed=1)
    x = rng.uniform(0, 1, size=(1, 1, V.H, V.W))
    _, cache = net.forward(x)
    d = net._seed_logit(cache, 1)
    _, dX = net._backward(d, cache, want_input=True)
    gnum = _num_grad(lambda: net.forward(x)[0][0, 1], x)
    assert np.abs(gnum - dX).max() / (np.abs(gnum).max() + 1e-9) < 1e-5


def test_clean_model_trains_and_localizes():
    net, acc = V.train_cnn(spurious=False, seed=0, epochs=20, n_train=650)
    assert acc >= 0.95
    Xt, yt, bb = V.make_shapes_dataset(40, spurious=False, seed=99)
    assert (net.predict(Xt) == yt).mean() >= 0.9
    # Grad-CAM should concentrate on the shape far above its area share.
    inb, area = [], []
    for i in range(20):
        cam = net.grad_cam(Xt[i:i + 1], int(yt[i]))
        y0, y1, x0, x1 = bb[i]
        m = np.zeros((V.H, V.W), bool); m[y0:y1, x0:x1] = True
        inb.append(V.cam_energy_in_region(cam, m)); area.append(m.mean())
    assert np.mean(inb) > 2.0 * np.mean(area)


def test_spurious_model_reveals_shortcut():
    snet, sacc = V.train_cnn(spurious=True, seed=0, epochs=20, n_train=650)
    assert sacc >= 0.95
    Xs, ys, bbs = V.make_shapes_dataset(80, spurious=True, seed=99)
    cue = np.zeros((V.H, V.W), bool); cue[V.CUE_ROWS, :] = True
    band, shape = [], []
    for i in range(len(ys)):
        if ys[i] != 0:
            continue
        cam = snet.grad_cam(Xs[i:i + 1], 0)
        y0, y1, x0, x1 = bbs[i]
        sm = np.zeros((V.H, V.W), bool); sm[y0:y1, x0:x1] = True
        band.append(V.cam_energy_in_region(cam, cue))
        shape.append(V.cam_energy_in_region(cam, sm))
    # The shortcut band attracts more Grad-CAM energy than the actual object.
    assert np.mean(band) > np.mean(shape)


def test_explanations_return_normalized_maps():
    net, _ = V.train_cnn(spurious=False, seed=0, epochs=6, n_train=200)
    Xt, yt, _ = V.make_shapes_dataset(4, spurious=False, seed=7)
    x = Xt[0:1]
    for m in (net.grad_cam(x, 0), net.saliency(x, 0),
              net.saliency(x, 0, guided=True), net.guided_grad_cam(x, 0)):
        assert m.shape == (V.H, V.W)
        assert 0.0 <= m.min() and m.max() <= 1.0 + 1e-9
