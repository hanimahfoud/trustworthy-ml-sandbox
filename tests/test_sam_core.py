"""Unit tests for core.sam_core -- verifies the SAM demonstration is sound."""
import numpy as np
from core import sam_core as S


def test_flat_is_global_min():
    # The flat basin must be the true global minimum; sharp is a local min.
    assert S.loss(*S.FLAT_C) < S.loss(*S.SHARP_C) - 0.1
    X, Y, Z = S.surface_grid(res=400)
    i = np.unravel_index(np.argmin(Z), Z.shape)
    assert abs(X[i] - S.FLAT_C[0]) < 0.2 and abs(Y[i] - S.FLAT_C[1]) < 0.2


def test_sharp_basin_is_sharper():
    # Worst-case rise in the rho-ball is much larger at the sharp minimum.
    sh = S.sharpness(S.SHARP_C, rho=0.55)
    fl = S.sharpness(S.FLAT_C, rho=0.55)
    assert sh > 1.2 and fl < 0.8 and sh > 2.5 * fl


def test_sgd_falls_into_sharp():
    traj = S.sgd_trajectory(S.START, lr=0.06, steps=180)
    assert S.basin_of(traj[-1]) == "sharp"


def test_sam_escapes_to_flat_at_default_rho():
    traj = S.sam_trajectory(S.START, lr=0.06, rho=S.DEFAULT_RHO, steps=180)
    assert S.basin_of(traj[-1]) == "flat"


def test_rho_zero_reduces_to_sgd():
    # With no neighbourhood, SAM == SGD and also lands in the sharp basin.
    sam0 = S.sam_trajectory(S.START, lr=0.06, rho=0.0, steps=180)
    assert S.basin_of(sam0[-1]) == "sharp"


def test_rho_sweep_monotone_story():
    # Small rho -> sharp/stuck; large rho -> flat. Check the transition exists.
    ends = {r: S.basin_of(S.sam_trajectory(S.START, rho=r, steps=180)[-1])
            for r in [0.0, 0.30, 0.55, 0.75]}
    assert ends[0.0] != "flat"
    assert ends[0.55] == "flat" and ends[0.75] == "flat"


def test_effective_fills_in_sharp_basin():
    # As rho grows, the effective value at the sharp centre rises toward / past 0
    # while the flat centre stays clearly negative.
    e_sharp = S.effective_loss(S.SHARP_C[0], S.SHARP_C[1], rho=0.55)
    e_flat = S.effective_loss(S.FLAT_C[0], S.FLAT_C[1], rho=0.55)
    assert e_sharp > -0.2 and e_flat < -1.0


def test_compute_demo_keys_and_finiteness():
    d = S.compute_demo(rho=0.55)
    for k in ["true_surface", "eff_surface", "sgd_traj", "sam_traj"]:
        assert k in d
    assert np.all(np.isfinite(d["true_surface"][2]))
    assert np.all(np.isfinite(d["eff_surface"][2]))
    assert d["sgd_basin"] == "sharp" and d["sam_basin"] == "flat"


if __name__ == "__main__":
    import traceback
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = 0
    for fn in fns:
        try:
            fn(); print("PASS", fn.__name__); passed += 1
        except Exception:
            print("FAIL", fn.__name__); traceback.print_exc()
    print(f"\n{passed}/{len(fns)} passed")
