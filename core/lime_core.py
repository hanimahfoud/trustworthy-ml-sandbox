"""
core/lime_core.py -- LIME for the loan model.

LIME explains one instance by (1) sampling perturbations around it, (2) asking
the black box for their predictions, (3) weighting each perturbation by its
proximity to the instance with an exponential kernel, and (4) fitting a
weighted linear (Ridge) surrogate. The surrogate's coefficients are the local
attributions. Standardizing the features first makes the coefficients
comparable across features of very different scales.
"""
from __future__ import annotations

import numpy as np
from sklearn.linear_model import Ridge

from core import loan_model_core as L


def explain(model, instance, background, feature_std=None, *,
            n_samples=1000, kernel_width=None, seed=0, feature_names=None):
    """
    Local linear explanation of ``model`` at ``instance``.

    Returns per-feature coefficients (in standardized space), the local
    surrogate intercept, and the surrogate's weighted R^2 (fit quality).
    """
    rng = np.random.default_rng(seed)
    instance = np.asarray(instance, dtype=float)
    bg = np.asarray(background, dtype=float)
    names = feature_names or L.FEATURES
    n = len(instance)

    std = np.asarray(feature_std, dtype=float) if feature_std is not None \
        else bg.std(axis=0)
    std = np.where(std < 1e-8, 1.0, std)

    # Perturb: Gaussian noise scaled by feature std around the instance.
    noise = rng.normal(0, 1, size=(n_samples, n)) * std
    samples = instance + noise
    samples[0] = instance  # keep the instance itself as one sample
    # owns_home is binary: snap the perturbed column back to {0,1}.
    if "owns_home" in names:
        j = names.index("owns_home")
        samples[:, j] = (samples[:, j] > 0.5).astype(float)

    # Black-box predictions to be explained.
    y = model.predict_proba(samples)[:, 1]

    # Proximity weights in standardized space.
    z = (samples - instance) / std
    dist = np.sqrt((z ** 2).sum(axis=1))
    if kernel_width is None:
        kernel_width = np.sqrt(n) * 0.75
    weights = np.exp(-(dist ** 2) / (kernel_width ** 2))

    # Weighted Ridge surrogate on standardized perturbations.
    Zc = (samples - instance) / std
    surrogate = Ridge(alpha=1.0, fit_intercept=True)
    surrogate.fit(Zc, y, sample_weight=weights)

    pred = surrogate.predict(Zc)
    ybar = np.average(y, weights=weights)
    ss_res = np.sum(weights * (y - pred) ** 2)
    ss_tot = np.sum(weights * (y - ybar) ** 2)
    r2 = float(1.0 - ss_res / ss_tot) if ss_tot > 1e-12 else 0.0

    coefs = surrogate.coef_
    return {
        "features": list(names),
        "coefficients": coefs,                       # local attribution
        "intercept": float(surrogate.intercept_),
        "local_r2": r2,
        "prediction": float(L.predict_proba(model, instance)),
        "order": list(np.argsort(-np.abs(coefs))),
    }
