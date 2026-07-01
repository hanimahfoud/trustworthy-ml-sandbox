"""
core/loan_model_core.py -- the shared "black box" for all tabular XAI demos.

A deterministic synthetic loan dataset with a genuine causal structure
(income -> savings) and a nonlinear RandomForest classifier trained on it.
LIME, SHAP and RECOURSE all explain THIS one model, so the three views are
mutually consistent. Pure NumPy / scikit-learn -- no torch, unit-testable.

Features (order fixed by FEATURES):
    age            years            immutable
    income         $ / month        actionable (causal parent of savings)
    debt           $                actionable
    savings        $                actionable (causal child of income)
    owns_home      {0, 1}           immutable
Label: 1 = loan approved, 0 = rejected.
"""
from __future__ import annotations

import numpy as np
from sklearn.ensemble import RandomForestClassifier

FEATURES = ["age", "income", "debt", "savings", "owns_home"]
IMMUTABLE = {"age", "owns_home"}
# Structural coefficient of the income -> savings edge (used by RECOURSE).
SAVINGS_PER_INCOME = 1.5

# A realistic applicant that the trained model rejects (used by every demo).
DEFAULT_APPLICANT = {
    "age": 40.0, "income": 2000.0, "debt": 2500.0,
    "savings": 1500.0, "owns_home": 0.0,
}

_N = 1600


def make_dataset(seed: int = 0):
    """Deterministic synthetic loan data with income -> savings causality."""
    rng = np.random.default_rng(seed)
    age = rng.uniform(21, 70, _N)
    income = np.clip(rng.normal(3500, 1400, _N), 800, 12000)
    debt = np.clip(rng.normal(1200, 900, _N), 0, 6000)
    # savings is caused by income (parent) minus a debt drag, plus noise.
    savings = np.clip(SAVINGS_PER_INCOME * income + rng.normal(0, 1500, _N)
                      - 0.3 * debt, 0, 40000)
    p_home = 1.0 / (1.0 + np.exp(-(savings - 8000) / 4000.0))
    owns_home = (rng.uniform(0, 1, _N) < p_home).astype(float)

    X = np.column_stack([age, income, debt, savings, owns_home])

    # Ground-truth approval score: income & savings help, debt hurts, owning a
    # home helps, being very young hurts slightly. Threshold at the median for
    # a balanced target. A RandomForest recovers this as a nonlinear boundary.
    score = (3.5e-4 * income + 4.0e-5 * savings - 6.0e-4 * debt
             + 0.15 * owns_home - 0.02 * (age < 25)
             + rng.normal(0, 0.05, _N))
    y = (score > np.median(score)).astype(int)
    return X, y


def train_model(seed: int = 0):
    """Train the black-box classifier; return (model, X, y, feature_std)."""
    X, y = make_dataset(seed)
    model = RandomForestClassifier(
        n_estimators=200, max_depth=8, min_samples_leaf=8,
        random_state=seed, n_jobs=1,
    ).fit(X, y)
    feature_std = X.std(axis=0)
    return model, X, y, feature_std


def to_vector(applicant: dict) -> np.ndarray:
    """Dict -> feature vector in FEATURES order."""
    return np.array([float(applicant[f]) for f in FEATURES], dtype=float)


def predict_proba(model, x) -> float:
    """P(approved) for a single applicant vector (or dict)."""
    if isinstance(x, dict):
        x = to_vector(x)
    x = np.asarray(x, dtype=float).reshape(1, -1)
    return float(model.predict_proba(x)[0, 1])


def is_approved(model, x, threshold: float = 0.5) -> bool:
    return predict_proba(model, x) >= threshold


def causal_graph() -> dict:
    """The one structural edge the RECOURSE demo reasons about."""
    return {
        "nodes": {"income": (0.0, 0.0), "savings": (1.0, 0.0)},
        "edges": [("income", "savings")],
        "coefficient": SAVINGS_PER_INCOME,
    }
