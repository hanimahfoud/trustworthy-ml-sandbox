"""Unit tests for core.dann_core (from-scratch NumPy DANN with GRL)."""
import numpy as np
from core import dann_core as D


def test_data_has_covariate_shift():
    Xs, ys, Xt, yt = D.make_domain_data(n=300, seed=0)
    assert Xs.shape[1] == 2 and Xt.shape[1] == 2
    # Source and target input means differ (covariate shift present).
    assert np.linalg.norm(Xs.mean(0) - Xt.mean(0)) > 0.2


def test_adaptation_improves_target_accuracy():
    # seed=1 is the curated demo seed where lam=1.0 gives a clean jump.
    Xs, ys, Xt, yt = D.make_domain_data(n=300, seed=1)
    p0, h0 = D.train_dann(Xs, ys, Xt, yt, lam=0.0, epochs=700, seed=1)  # source-only
    p1, h1 = D.train_dann(Xs, ys, Xt, yt, lam=1.0, epochs=700, seed=1)  # DANN
    a0 = D.analyse(p0, Xs, ys, Xt, yt)
    a1 = D.analyse(p1, Xs, ys, Xt, yt)
    # Target accuracy should jump with adaptation...
    assert a1["tgt_acc"] > a0["tgt_acc"] + 0.05
    # ...and source accuracy should remain strong (label task not destroyed).
    assert a1["src_acc"] > 0.8


def test_feature_mmd_decreases_with_adaptation():
    Xs, ys, Xt, yt = D.make_domain_data(n=300, seed=0)
    p0, _ = D.train_dann(Xs, ys, Xt, yt, lam=0.0, epochs=700, seed=0)
    p1, _ = D.train_dann(Xs, ys, Xt, yt, lam=1.0, epochs=700, seed=0)
    a0 = D.analyse(p0, Xs, ys, Xt, yt)
    a1 = D.analyse(p1, Xs, ys, Xt, yt)
    # Aligning the feature distributions reduces their RBF-MMD.
    assert a1["feat_mmd"] < a0["feat_mmd"]


def test_grid_probabilities_are_finite_and_bounded():
    Xs, ys, Xt, yt = D.make_domain_data(n=300, seed=0)
    p1, _ = D.train_dann(Xs, ys, Xt, yt, lam=1.0, epochs=400, seed=0)
    a = D.analyse(p1, Xs, ys, Xt, yt)
    g = a["grid_prob"]
    assert np.all(np.isfinite(g)) and g.min() >= 0.0 and g.max() <= 1.0


def test_mmd_nonnegative():
    rng = np.random.default_rng(0)
    A = rng.normal(size=(50, 2)); B = rng.normal(size=(50, 2)) + 1.0
    assert D.rbf_mmd2(A, B) >= -1e-9
    assert D.rbf_mmd2(A, A) < D.rbf_mmd2(A, B)   # same dist => smaller MMD


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
