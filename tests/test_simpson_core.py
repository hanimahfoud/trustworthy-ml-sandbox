"""Unit tests for core.simpson_core."""
import numpy as np
from core import simpson_core as SP


def test_no_paradox_at_zero_skew():
    r = SP.compute(skew=0.0)
    # With no confounding, B is better both within groups and overall.
    assert r["b_better_in_both_groups"] and not r["a_better_overall"]
    assert not r["paradox"]


def test_paradox_at_high_skew():
    r = SP.compute(skew=0.8)
    assert r["paradox"]
    assert r["b_better_in_both_groups"] and r["a_better_overall"]


def test_within_group_B_always_better():
    # B is constructed to beat A by delta in every group, at every skew.
    for s in [0.0, 0.3, 0.6, 0.9]:
        r = SP.compute(skew=s)
        assert r["groups"]["mild"]["B"]["rate"] > r["groups"]["mild"]["A"]["rate"]
        assert r["groups"]["severe"]["B"]["rate"] > r["groups"]["severe"]["A"]["rate"]


def test_counts_are_consistent():
    r = SP.compute(skew=0.7)
    g = r["groups"]
    nA = g["mild"]["A"]["n"] + g["severe"]["A"]["n"]
    nB = g["mild"]["B"]["n"] + g["severe"]["B"]["n"]
    assert nA == r["aggregate"]["A"]["n"]
    assert nB == r["aggregate"]["B"]["n"]
    # recoveries never exceed group sizes
    for grp in ["mild", "severe"]:
        for t in ["A", "B"]:
            assert 0 <= g[grp][t]["rec"] <= g[grp][t]["n"]


def test_paradox_onset_exists_and_is_small():
    c = SP.paradox_curve()
    assert c["onset_skew"] is not None and 0.0 < c["onset_skew"] < 0.3
    # aggregate B starts above A and ends below A (the switch).
    assert c["agg_B"][0] > c["agg_A"][0]
    assert c["agg_B"][-1] < c["agg_A"][-1]


def test_dag_structure():
    d = SP.causal_dag()
    assert d["confounder"] == "Severity"
    assert ("Severity", "Treatment") in d["edges"]
    assert ("Severity", "Outcome") in d["edges"]
    assert ("Treatment", "Outcome") in d["edges"]


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
