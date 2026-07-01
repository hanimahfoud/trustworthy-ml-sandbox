"""
Bias-Variance compute core
===========================
Pure NumPy / scikit-learn. No Streamlit, no plotting. Fully unit-testable.

The empirical decomposition follows the standard pointwise identity for
squared-error regression with target  y = f(x) + eps,  E[eps]=0,  Var[eps]=sigma^2:

    E_{D,eps}[ (y - g_D(x))^2 ]  =  ( f(x) - E_D[g_D(x)] )^2   (bias^2)
                                  +  E_D[ (g_D(x) - E_D[g_D(x)])^2 ]  (variance)
                                  +  sigma^2                          (irreducible noise)

where g_D is the model fitted on a random training set D. We estimate the inner
expectations by Monte-Carlo over many independently drawn training sets.
"""
from __future__ import annotations

import numpy as np
from numpy.polynomial import polynomial as P


# --------------------------------------------------------------------------- #
# Ground-truth target                                                          #
# --------------------------------------------------------------------------- #
def true_function(x: np.ndarray) -> np.ndarray:
    """Smooth non-linear target on [0, 1]:  f(x) = sin(2*pi*x)."""
    return np.sin(2.0 * np.pi * x)


def generate_data(n: int, noise_std: float, rng: np.random.Generator):
    """Draw n points  x ~ U(0,1),  y = f(x) + N(0, noise_std^2)."""
    x = rng.uniform(0.0, 1.0, size=n)
    y = true_function(x) + rng.normal(0.0, noise_std, size=n)
    return x, y


# --------------------------------------------------------------------------- #
# Polynomial regression (numerically stable via numpy's scaled basis)          #
# --------------------------------------------------------------------------- #
def fit_polynomial(x: np.ndarray, y: np.ndarray, degree: int):
    """
    Least-squares polynomial fit. numpy.polynomial.Polynomial.fit maps the
    domain into [-1, 1] internally, which keeps the Vandermonde system well
    conditioned even at high degree.
    Returns a callable predictor.
    """
    poly = P.Polynomial.fit(x, y, deg=degree)
    return poly


def predict(poly, x: np.ndarray) -> np.ndarray:
    return poly(x)


# --------------------------------------------------------------------------- #
# Single train/test fit (for the live curve view)                             #
# --------------------------------------------------------------------------- #
def fit_and_score(degree: int, n_train: int, noise_std: float, seed: int,
                  n_test: int = 400):
    """
    Fit one model on a fresh training set and report train / test MSE, plus the
    smooth fitted curve over a dense grid for plotting.
    """
    rng = np.random.default_rng(seed)
    x_tr, y_tr = generate_data(n_train, noise_std, rng)
    x_te, y_te = generate_data(n_test, noise_std, rng)

    poly = fit_polynomial(x_tr, y_tr, degree)

    train_mse = float(np.mean((predict(poly, x_tr) - y_tr) ** 2))
    test_mse = float(np.mean((predict(poly, x_te) - y_te) ** 2))

    grid = np.linspace(0.0, 1.0, 300)
    curve = predict(poly, grid)
    truth = true_function(grid)

    return {
        "x_train": x_tr, "y_train": y_tr,
        "grid": grid, "curve": curve, "truth": truth,
        "train_mse": train_mse, "test_mse": test_mse,
    }


# --------------------------------------------------------------------------- #
# Error curves vs. model complexity                                            #
# --------------------------------------------------------------------------- #
def error_vs_degree(max_degree: int, n_train: int, noise_std: float,
                    seed: int, n_repeats: int = 40, n_test: int = 400):
    """
    For each degree d = 1..max_degree, average train/test MSE over n_repeats
    independent train/test draws. Returns arrays aligned with degrees.
    """
    degrees = np.arange(1, max_degree + 1)
    train = np.zeros(len(degrees))
    test = np.zeros(len(degrees))

    for i, d in enumerate(degrees):
        tr_acc = np.zeros(n_repeats)
        te_acc = np.zeros(n_repeats)
        for r in range(n_repeats):
            rng = np.random.default_rng(seed + 1000 * r + d)
            x_tr, y_tr = generate_data(n_train, noise_std, rng)
            x_te, y_te = generate_data(n_test, noise_std, rng)
            poly = fit_polynomial(x_tr, y_tr, int(d))
            tr_acc[r] = np.mean((predict(poly, x_tr) - y_tr) ** 2)
            te_acc[r] = np.mean((predict(poly, x_te) - y_te) ** 2)
        train[i] = tr_acc.mean()
        test[i] = te_acc.mean()

    return degrees, train, test


# --------------------------------------------------------------------------- #
# Monte-Carlo bias / variance / noise decomposition                           #
# --------------------------------------------------------------------------- #
def bias_variance_decomposition(degree: int, n_train: int, noise_std: float,
                                seed: int, n_datasets: int = 200,
                                n_eval: int = 200):
    """
    Estimate (bias^2, variance, noise) averaged over a fixed grid of eval
    points, by fitting `n_datasets` models on independent training sets.

    Returns a dict including the pointwise mean prediction so the caller can
    plot the average model and its spread.
    """
    rng_eval = np.random.default_rng(seed)
    x_eval = np.sort(rng_eval.uniform(0.0, 1.0, size=n_eval))
    f_eval = true_function(x_eval)

    preds = np.zeros((n_datasets, n_eval))
    for d in range(n_datasets):
        rng = np.random.default_rng(seed + 7919 * (d + 1))
        x_tr, y_tr = generate_data(n_train, noise_std, rng)
        poly = fit_polynomial(x_tr, y_tr, degree)
        preds[d] = predict(poly, x_eval)

    mean_pred = preds.mean(axis=0)                      # E_D[g_D(x)]
    bias2_point = (mean_pred - f_eval) ** 2             # pointwise bias^2
    var_point = preds.var(axis=0)                       # pointwise variance
    noise = noise_std ** 2                              # irreducible

    bias2 = float(bias2_point.mean())
    variance = float(var_point.mean())
    expected_error = bias2 + variance + noise

    # Empirical check: average test error against *noisy* targets at x_eval.
    rng_chk = np.random.default_rng(seed + 13)
    y_noisy = f_eval[None, :] + rng_chk.normal(
        0.0, noise_std, size=(n_datasets, n_eval))
    measured_error = float(np.mean((preds - y_noisy) ** 2))

    # Spread band (1 std around the mean prediction) for plotting.
    std_pred = preds.std(axis=0)

    return {
        "x_eval": x_eval, "f_eval": f_eval,
        "mean_pred": mean_pred, "std_pred": std_pred,
        "bias2": bias2, "variance": variance, "noise": noise,
        "expected_error": expected_error, "measured_error": measured_error,
        "sample_curves": preds[: min(25, n_datasets)],   # a few for plotting
    }


def composition_vs_degree(max_degree: int, n_train: int, noise_std: float,
                          seed: int, n_datasets: int = 120, n_eval: int = 120):
    """
    Bias^2 / variance / noise at every degree 1..max_degree, returned both as
    raw values and as proportions of the total expected error. The proportion
    view stays readable at any magnitude (variance can be enormous at high
    degree), making the bias->variance shift legible in a single figure.
    """
    degrees = np.arange(1, max_degree + 1)
    bias2 = np.zeros(len(degrees))
    var = np.zeros(len(degrees))
    noise = np.full(len(degrees), noise_std ** 2)

    for i, d in enumerate(degrees):
        dc = bias_variance_decomposition(
            int(d), n_train, noise_std, seed=seed + int(d),
            n_datasets=n_datasets, n_eval=n_eval)
        bias2[i] = dc["bias2"]
        var[i] = dc["variance"]

    total = bias2 + var + noise
    total = np.where(total <= 0, 1e-12, total)
    return {
        "degrees": degrees,
        "bias2": bias2, "variance": var, "noise": noise, "total": total,
        "bias2_pct": 100.0 * bias2 / total,
        "variance_pct": 100.0 * var / total,
        "noise_pct": 100.0 * noise / total,
    }
