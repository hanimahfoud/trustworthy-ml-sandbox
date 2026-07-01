"""Unit tests for the fairness engine."""
import numpy as np

from core import fairness_core as F


def test_dataset_has_different_base_rates():
    d = F.make_fairness_dataset(seed=0)
    a = d["y_true"][d["group"] == "A"].mean()
    b = d["y_true"][d["group"] == "B"].mean()
    assert a > b            # A advantaged base rate by construction
    assert 0.4 < a < 0.8 and 0.25 < b < 0.55


def test_confusion_counts_are_consistent():
    d = F.make_fairness_dataset(seed=1)
    c = F.group_confusion(d, 0.5, 0.5)
    for g in ("A", "B"):
        cg = c[g]
        assert cg["tp"] + cg["fp"] + cg["tn"] + cg["fn"] == cg["n"]
        assert 0.0 <= cg["tpr"] <= 1.0 and 0.0 <= cg["fpr"] <= 1.0


def test_single_threshold_is_unfair():
    """With measurement bias, one global threshold disadvantages group B."""
    d = F.make_fairness_dataset(seed=2)
    c = F.group_confusion(d, 0.5, 0.5)
    assert c["A"]["acceptance"] > c["B"]["acceptance"]


def test_demographic_parity_thresholds_equalize_acceptance():
    d = F.make_fairness_dataset(seed=3)
    ta, tb = F.thresholds_for_demographic_parity(d, 0.5)
    c = F.group_confusion(d, ta, tb)
    assert abs(c["A"]["acceptance"] - c["B"]["acceptance"]) < 0.05


def test_impossibility_enforcing_parity_breaks_equalized_odds():
    """The headline result: equalizing acceptance (DP) leaves a large
    equalized-odds gap, because with different base rates the false-positive
    rates must diverge. You cannot have both at once."""
    d = F.make_fairness_dataset(seed=3)
    ta, tb = F.thresholds_for_demographic_parity(d, 0.5)
    m = F.fairness_metrics(d, ta, tb)
    assert m["demographic_parity_gap"] < 0.05      # DP satisfied
    assert m["equalized_odds_gap"] > 0.10          # ...but equalized odds is not


def test_impossibility_enforcing_equal_opportunity_breaks_parity():
    """The reverse: matching TPR (equal opportunity) leaves an acceptance gap."""
    d = F.make_fairness_dataset(seed=3)
    ta, tb = F.thresholds_for_equal_opportunity(d, 0.5)
    m = F.fairness_metrics(d, ta, tb)
    assert m["equal_opportunity_gap"] < 0.06       # EO satisfied
    assert m["demographic_parity_gap"] > 0.05      # ...but parity is not


def test_equal_opportunity_thresholds_equalize_tpr():
    d = F.make_fairness_dataset(seed=3)
    ta, tb = F.thresholds_for_equal_opportunity(d, 0.5)
    c = F.group_confusion(d, ta, tb)
    assert abs(c["A"]["tpr"] - c["B"]["tpr"]) < 0.06


def test_mmd_zero_for_same_distribution_positive_for_shifted():
    rng = np.random.default_rng(0)
    x = rng.normal(0, 1, 400)
    y = rng.normal(0, 1, 400)
    z = rng.normal(2, 1, 400)
    assert F.mmd_rbf(x, x) < 1e-9
    assert F.mmd_rbf(x, y) < F.mmd_rbf(x, z)
    assert F.mmd_rbf(x, z) > 0.0


def test_cda_swap_gender_terms():
    out, n = F.cda_swap("He is a great nurse and his work is good.", "en")
    assert n >= 2
    assert "She" in out and "her" in out.lower()
    ar, na = F.cda_swap("الممرض قام بعمله بشكل ممتاز", "ar")
    assert na >= 1 and "الممرضة" in ar


def test_rule_based_simulations_are_deterministic():
    assert F.implicit_bias_judge(3, chose_neutral=True) == 2
    assert F.implicit_bias_judge(3, chose_neutral=False) == -1
    assert F.implicit_bias_judge(1, chose_neutral=False) == 0
    assert F.constitutional_revise(biased=True, rule_active=True) == "revised"
    assert F.constitutional_revise(biased=True, rule_active=False) == "no_constitution"
