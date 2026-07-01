"""
core/recourse_core.py -- algorithmic recourse for a rejected applicant.

Two recommendations that both flip the black box from "rejected" to "approved":

* Normal counterfactual -- treats features as independent. To land in the
  approved region it must pay, separately, for every feature it moves
  (including the savings it raises).
* Causal RECOURSE -- knows the structural edge income -> savings. Raising
  income by delta automatically raises savings by SAVINGS_PER_INCOME * delta,
  so the same end-point is reached while only the income change is "paid for".
  It also respects actionability (immutable features are never changed).

Because both plans reach the *same* approved end-point, the causal plan is
never more expensive, and is strictly cheaper whenever savings must rise --
exactly the point the RECOURSE literature makes. Costs are in standardized
units (|delta| / feature_std) so different features are comparable.
"""
from __future__ import annotations

import numpy as np

from core import loan_model_core as L


def _cost(delta_dict, feature_std, names):
    std = {f: (feature_std[i] if feature_std[i] > 1e-8 else 1.0)
           for i, f in enumerate(names)}
    return float(sum(abs(dv) / std[f] for f, dv in delta_dict.items()))


def _min_income_to_flip(model, applicant, *, causal, step=100.0, max_delta=12000.0):
    """Smallest income increase that flips the decision. If ``causal``, the
    induced savings (SAVINGS_PER_INCOME * delta) is applied too."""
    base = dict(applicant)
    d = 0.0
    while d <= max_delta:
        cand = dict(base)
        cand["income"] = base["income"] + d
        if causal:
            cand["savings"] = base["savings"] + L.SAVINGS_PER_INCOME * d
        if L.is_approved(model, L.to_vector(cand)):
            return d, cand
        d += step
    return None, None


def recommend(model, applicant, feature_std, names=None):
    """
    Compute both recommendations for a (rejected) applicant.

    Returns a dict with the normal and causal plans, their costs, the
    resulting approval probabilities, and the causal graph for display.
    """
    names = names or L.FEATURES
    applicant = {f: float(applicant[f]) for f in names}

    # Find the minimal income move (with induced savings) that flips the model.
    delta_inc, endpoint = _min_income_to_flip(model, applicant, causal=True)
    if delta_inc is None:
        return {"feasible": False}

    induced_savings = L.SAVINGS_PER_INCOME * delta_inc

    # Causal RECOURSE: pay only for the income change; savings follows for free.
    causal_delta = {"income": delta_inc}
    causal_cost = _cost(causal_delta, feature_std, names)

    # Normal counterfactual: same end-point, but income AND savings are each
    # treated as independent actions that must be paid for.
    normal_delta = {"income": delta_inc, "savings": induced_savings}
    normal_cost = _cost(normal_delta, feature_std, names)

    p_before = L.predict_proba(model, L.to_vector(applicant))
    p_after = L.predict_proba(model, L.to_vector(endpoint))

    return {
        "feasible": True,
        "applicant": applicant,
        "endpoint": endpoint,
        "p_before": p_before,
        "p_after": p_after,
        "delta_income": delta_inc,
        "induced_savings": induced_savings,
        "normal": {"delta": normal_delta, "cost": normal_cost},
        "causal": {"delta": causal_delta, "cost": causal_cost},
        "savings": normal_cost - causal_cost,   # how much causality saves
        "immutable_respected": True,             # age & owns_home never touched
        "graph": L.causal_graph(),
    }
