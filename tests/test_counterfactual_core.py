"""Unit tests for core.counterfactual_core."""
import numpy as np
from core import counterfactual_core as CF


def test_canonical_one_third():
    res = CF.counterfactual(CF.default_prior(), T_obs=1, Y_obs=0, T_do=0)
    assert abs(res["p_happy"] - 1/3) < 1e-9
    assert res["fraction"] == "1/3"
    post = res["posterior"]
    assert abs(post["responder"]) < 1e-12
    assert abs(post["hater"] - 1/3) < 1e-9
    assert abs(post["always_sad"] - 2/3) < 1e-9


def test_abduction_excludes_inconsistent_types():
    # Observing (T=1, Y=0): a responder (Y=T=1) cannot explain a sad outcome.
    abd = CF.abduction(CF.default_prior(), T_obs=1, Y_obs=0)
    assert "responder" not in abd["consistent"]
    assert set(abd["consistent"]) == {"hater", "always_sad"}


def test_impossible_evidence_raises():
    # Always-sad never produces Y=1; with only always-sad mass and Y=1 this is impossible.
    prior = {"responder": 0.0, "hater": 0.0, "always_sad": 1.0}
    try:
        CF.abduction(prior, T_obs=0, Y_obs=1)
        raised = False
    except ValueError:
        raised = True
    assert raised


def test_posterior_normalised():
    for (To, Yo) in [(1, 0), (0, 1), (1, 1), (0, 0)]:
        try:
            abd = CF.abduction(CF.make_prior(0.2, 0.2), To, Yo)
        except ValueError:
            continue
        assert abs(sum(abd["posterior"].values()) - 1.0) < 1e-9


def test_make_prior_responder_takes_remainder():
    p = CF.make_prior(p_hater=0.1, p_always_sad=0.2)
    assert abs(p["responder"] - 0.7) < 1e-9
    assert abs(sum(p.values()) - 1.0) < 1e-9


def test_intervention_changes_outcome():
    # Same evidence, opposite interventions give different counterfactuals.
    base = CF.default_prior()
    keep_dog = CF.counterfactual(base, T_obs=1, Y_obs=0, T_do=1)   # keep the dog
    remove_dog = CF.counterfactual(base, T_obs=1, Y_obs=0, T_do=0) # take it away
    # Keeping the dog: nobody consistent (H,S) is happy with the dog -> 0.
    assert abs(keep_dog["p_happy"] - 0.0) < 1e-9
    assert abs(remove_dog["p_happy"] - 1/3) < 1e-9


def test_response_table_values():
    res = CF.counterfactual(CF.default_prior(), 1, 0, 0)
    rt = res["response_table"]
    assert rt["responder"] == {"T0": 0, "T1": 1}
    assert rt["hater"] == {"T0": 1, "T1": 0}
    assert rt["always_sad"] == {"T0": 0, "T1": 0}


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
