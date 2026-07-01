"""
core/shap_core.py -- exact Shapley values for the loan model.

With only five features the Shapley values can be computed exactly (no
sampling): for every coalition S we evaluate the value function

    v(S) = E_background[ f( x_S := instance_S , x_{~S} := background_{~S} ) ]

and combine coalitions with the classic Shapley weights. The defining property
-- local accuracy / additivity -- is  sum_i phi_i = f(instance) - E[f] -- and
is asserted in the tests. This is the exact small-n analogue of Kernel SHAP.
"""
from __future__ import annotations

from itertools import combinations, chain

import numpy as np

from core import loan_model_core as L


def _powerset(items):
    items = list(items)
    return chain.from_iterable(combinations(items, r) for r in range(len(items) + 1))


def _coalition_values(model, instance, background):
    """v(S) for every coalition S, batched over the background sample."""
    n = len(instance)
    bg = np.asarray(background, dtype=float)
    values = {}
    for S in _powerset(range(n)):
        S = frozenset(S)
        # Rows = background with the coalition's features overwritten by instance.
        rows = bg.copy()
        if S:
            idx = list(S)
            rows[:, idx] = np.asarray(instance)[idx]
        values[S] = float(model.predict_proba(rows)[:, 1].mean())
    return values


def shapley_values(model, instance, background, feature_names=None):
    """
    Exact Shapley attributions for a single instance.

    Returns dict with per-feature phi, the base value E[f], the model output
    f(instance), and the additivity residual (~0 to numerical precision).
    """
    instance = np.asarray(instance, dtype=float)
    names = feature_names or L.FEATURES
    n = len(instance)
    v = _coalition_values(model, instance, background)

    # Precompute Shapley coalition weights |S|! (n-|S|-1)! / n!
    from math import factorial
    w = {s: factorial(s) * factorial(n - s - 1) / factorial(n) for s in range(n)}

    phi = np.zeros(n)
    full = frozenset(range(n))
    for i in range(n):
        others = [j for j in range(n) if j != i]
        acc = 0.0
        for S in _powerset(others):
            S = frozenset(S)
            acc += w[len(S)] * (v[S | {i}] - v[S])
        phi[i] = acc

    base_value = v[frozenset()]          # E[f] over background
    fx = v[full]                         # f(instance)
    return {
        "features": list(names),
        "phi": phi,
        "base_value": base_value,
        "prediction": fx,
        "additivity_residual": float(fx - base_value - phi.sum()),
        # Convenience for the force-plot: sorted by |contribution|.
        "order": list(np.argsort(-np.abs(phi))),
    }


def force_plot_data(result):
    """
    Turn Shapley output into left-to-right force-plot segments: start at the
    base value, stack each feature's signed contribution to reach f(instance).
    """
    phi = result["phi"]
    names = result["features"]
    order = result["order"]
    segments = []
    cursor = result["base_value"]
    for i in order:
        segments.append({
            "feature": names[i],
            "value": float(phi[i]),
            "start": float(cursor),
            "end": float(cursor + phi[i]),
            "direction": "up" if phi[i] >= 0 else "down",
        })
        cursor += phi[i]
    return {
        "base_value": result["base_value"],
        "output_value": result["prediction"],
        "segments": segments,
    }
