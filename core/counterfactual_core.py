"""
Counterfactual inference on a Structural Causal Model (SCM) -- compute core
===========================================================================
The "give the dog to the sad person" example from the course. A person is given
a dog (treatment T in {0,1}) and we observe whether they end up happy
(outcome Y in {0,1}). The effect of the dog depends on a *latent type* U that we
never observe directly:

    Responder   (U = R):   Y = T          -- the dog makes them happy
    Dog-hater   (U = H):   Y = 1 - T       -- the dog makes them unhappy
    Always-sad  (U = S):   Y = 0           -- nothing helps

A counterfactual ("they were given a dog but are sad -- would they have been
happy WITHOUT the dog?") is answered with Pearl's three-step recipe:

    1. ABDUCTION   -- update the distribution over the latent U using the
                      observed evidence (T_obs, Y_obs).
    2. ACTION      -- intervene: replace T with the counterfactual value
                      do(T = T_cf), keeping the abducted U fixed.
    3. PREDICTION  -- compute the outcome distribution under that intervention.

Canonical instance: prior P(R,H,S) = (0.70, 0.10, 0.20), evidence (T=1, Y=0),
intervention do(T=0)  ==>  P(happy) = 1/3.  (Only H and S explain "dog yet sad";
their posterior is 1/3, 2/3; under do(T=0) only H flips to happy.)

Plain Python/NumPy; exercised by tests/test_counterfactual_core.py.
"""
from __future__ import annotations

import numpy as np

# Latent response types: each maps a treatment T in {0,1} to an outcome Y.
TYPES = ("responder", "hater", "always_sad")
LABELS = {
    "responder": "Responder  (Y = T)",
    "hater": "Dog-hater  (Y = 1 - T)",
    "always_sad": "Always-sad  (Y = 0)",
}


def outcome(type_name: str, T: int) -> int:
    """Structural outcome Y for a given latent type under treatment T."""
    if type_name == "responder":
        return int(T)
    if type_name == "hater":
        return int(1 - T)
    if type_name == "always_sad":
        return 0
    raise ValueError(f"unknown type {type_name!r}")


def default_prior() -> dict:
    return {"responder": 0.70, "hater": 0.10, "always_sad": 0.20}


def make_prior(p_hater: float = 0.10, p_always_sad: float = 0.20) -> dict:
    """Build a prior from the two user-set probabilities; responder takes the rest."""
    p_hater = float(np.clip(p_hater, 0.0, 1.0))
    p_always_sad = float(np.clip(p_always_sad, 0.0, 1.0))
    p_resp = max(0.0, 1.0 - p_hater - p_always_sad)
    total = p_resp + p_hater + p_always_sad
    if total <= 0:
        raise ValueError("prior probabilities sum to zero")
    return {"responder": p_resp / total,
            "hater": p_hater / total,
            "always_sad": p_always_sad / total}


def abduction(prior: dict, T_obs: int, Y_obs: int) -> dict:
    """
    Step 1. Posterior over latent types consistent with the observed (T,Y):
        P(U | T_obs, Y_obs) proportional to P(U) * 1[ outcome(U, T_obs) == Y_obs ].
    Returns {"posterior": {...}, "evidence_prob": float, "consistent": [...]}.
    Raises ValueError if no type can explain the evidence (impossible observation).
    """
    weights = {}
    consistent = []
    for t in TYPES:
        ok = (outcome(t, T_obs) == Y_obs)
        weights[t] = prior[t] if ok else 0.0
        if ok and prior[t] > 0:
            consistent.append(t)
    Z = sum(weights.values())
    if Z <= 0:
        raise ValueError(
            "The observation is impossible under the current model/prior "
            "(no latent type produces this outcome for this treatment)."
        )
    posterior = {t: weights[t] / Z for t in TYPES}
    return {"posterior": posterior, "evidence_prob": Z, "consistent": consistent}


def predict(posterior: dict, T_do: int) -> dict:
    """
    Steps 2-3. Under the intervention do(T = T_do), with the abducted posterior
    over U held fixed, return the counterfactual outcome distribution and the
    per-type contributions to P(Y = 1).
    """
    contributions = {t: posterior[t] * outcome(t, T_do) for t in TYPES}
    p_happy = float(sum(contributions.values()))
    return {
        "p_happy": p_happy,
        "p_sad": 1.0 - p_happy,
        "contributions": contributions,
    }


def counterfactual(prior: dict, T_obs: int, Y_obs: int, T_do: int) -> dict:
    """
    Full three-step counterfactual query, returning a structured, step-by-step
    trace suitable for display in the UI.
    """
    abd = abduction(prior, T_obs, Y_obs)
    pred = predict(abd["posterior"], T_do)

    # A readable, exact-fraction-friendly trace.
    steps = []
    steps.append({
        "name": "abduction",
        "evidence": {"T_obs": T_obs, "Y_obs": Y_obs},
        "consistent_types": abd["consistent"],
        "posterior": abd["posterior"],
        "evidence_prob": abd["evidence_prob"],
    })
    steps.append({
        "name": "action",
        "intervention": {"T_do": T_do},
        "note": "Replace the treatment with do(T=%d); keep the abducted U fixed." % T_do,
    })
    steps.append({
        "name": "prediction",
        "contributions": pred["contributions"],
        "p_happy": pred["p_happy"],
        "p_sad": pred["p_sad"],
    })

    return {
        "prior": prior,
        "posterior": abd["posterior"],
        "p_happy": pred["p_happy"],
        "p_sad": pred["p_sad"],
        "contributions": pred["contributions"],
        "fraction": _as_fraction(pred["p_happy"]),
        "steps": steps,
        "response_table": {t: {"T0": outcome(t, 0), "T1": outcome(t, 1)} for t in TYPES},
    }


def _as_fraction(x: float, max_den: int = 50) -> str:
    """Best small-denominator fraction string for a probability (for display)."""
    from fractions import Fraction
    f = Fraction(x).limit_denominator(max_den)
    if f.denominator == 1:
        return str(f.numerator)
    return f"{f.numerator}/{f.denominator}"
