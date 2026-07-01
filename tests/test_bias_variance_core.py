"""Unit tests for core.bias_variance_core."""
import numpy as np
from core import bias_variance_core as BV


def test_decomposition_identity_holds():
    # Bias^2 + Variance + Noise must reconstruct the measured expected error.
    for deg in [1, 3, 5, 8, 12]:
        d = BV.bias_variance_decomposition(deg, n_train=40, noise_std=0.22,
                                           seed=0, n_datasets=200, n_eval=200)
        recon = d["bias2"] + d["variance"] + d["noise"]
        assert abs(recon - d["measured_error"]) < 0.05 * (1 + d["measured_error"]), \
            (deg, recon, d["measured_error"])


def test_bias_decreases_variance_increases_with_degree():
    comp = BV.composition_vs_degree(14, n_train=40, noise_std=0.22, seed=0)
    b = np.array(comp["bias2"]); v = np.array(comp["variance"])
    # Bias at degree 1 is much larger than at the sweet spot; variance explodes high.
    assert b[0] > b[3]
    assert v[-1] > v[3]


def test_error_vs_degree_has_u_shape():
    degs, train, test = BV.error_vs_degree(14, n_train=40, noise_std=0.22,
                                           seed=0, n_repeats=40)
    test = np.array(test)
    best = int(np.argmin(test))
    assert 1 < best < len(test) - 1          # minimum is interior (a U / valley)
    assert test[0] > test[best]              # underfitting worse than sweet spot
    assert test[-1] > test[best]             # overfitting worse than sweet spot


def test_train_error_monotone_nonincreasing_trend():
    degs, train, test = BV.error_vs_degree(12, n_train=40, noise_std=0.22,
                                           seed=0, n_repeats=40)
    train = np.array(train)
    assert train[-1] <= train[0] + 1e-6      # more capacity -> lower train error


def test_fit_and_score_shapes_and_finite():
    r = BV.fit_and_score(degree=5, n_train=40, noise_std=0.22, seed=0)
    for k in ["x_train", "y_train", "grid", "curve", "truth"]:
        assert k in r and np.all(np.isfinite(r[k]))
    assert r["train_mse"] >= 0 and r["test_mse"] >= 0


if __name__ == "__main__":
    import traceback
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    p = 0
    for fn in fns:
        try:
            fn(); print("PASS", fn.__name__); p += 1
        except Exception:
            print("FAIL", fn.__name__); traceback.print_exc()
    print(f"\n{p}/{len(fns)} passed")
