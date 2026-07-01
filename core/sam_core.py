"""
Sharpness-Aware Minimisation (SAM) -- compute core
==================================================
Foret et al., "Sharpness-Aware Minimization for Efficiently Improving
Generalization" (ICLR 2021). SAM does not minimise the loss at a point; it
minimises the WORST-CASE loss inside an L2 ball of radius ``rho``:

        min_w  E(w),    where   E(w) = max_{||eps|| <= rho} L(w + eps).

E(w) is the "sharpness-aware" (worst-case) objective. A sharp/narrow minimum
has a high worst-case loss -- the loss shoots up within the rho-ball -- so it is
*raised* (effectively erased) on E, while a wide/flat minimum stays low. SAM
therefore prefers flat minima, which generalise better to unseen data.

This module builds a transparent 2-D landscape with a NARROW, deep *local*
minimum (a "sharp" basin) and a WIDE *global* minimum (a "flat" basin), and lets
us compare two optimisers honestly:

  * Plain gradient descent on the true loss  L(w)   -> falls into the SHARP basin.
  * Descent on SAM's worst-case objective    E(w)   -> settles in the FLAT basin.

Descending E(w) is the exact full-ball SAM objective; the familiar two-step
first-order SAM update (ascend to ``w + rho * g/||g||``, then descend) is a
one-step approximation of it and is provided as ``sam_first_order_trajectory``.

Everything here is plain NumPy and is exercised by the unit tests in
``tests/test_sam_core.py``.
"""
from __future__ import annotations

import numpy as np

# --- Landscape parameters (validated so the demonstration is robust) --------
SHARP_C = np.array([-1.05, 0.0])   # centre of the narrow, deep local minimum
SHARP_A = 1.65                     # depth of the sharp basin
SHARP_S = 0.24                     # width (std) of the sharp basin  -- NARROW
FLAT_C = np.array([1.30, 0.0])     # centre of the wide global minimum
FLAT_A = 2.05                      # depth of the flat basin (deeper => global)
FLAT_S = 0.78                      # width (std) of the flat basin   -- WIDE
CONFINE = 0.055                    # gentle global bowl, keeps surface bounded

DOMAIN = (-2.6, 2.6)               # plotting / clamping range
START = np.array([-0.50, 0.0])     # curated start: on the rim of the sharp basin
DEFAULT_RHO = 0.55                 # default neighbourhood radius for SAM


# --- True loss surface and its analytic gradient ----------------------------
def loss(x, y):
    """Scalar loss surface (vectorised over NumPy arrays)."""
    rs = (x - SHARP_C[0]) ** 2 + (y - SHARP_C[1]) ** 2
    rf = (x - FLAT_C[0]) ** 2 + (y - FLAT_C[1]) ** 2
    sharp = -SHARP_A * np.exp(-rs / (2 * SHARP_S ** 2))
    flat = -FLAT_A * np.exp(-rf / (2 * FLAT_S ** 2))
    return sharp + flat + CONFINE * (x ** 2 + y ** 2)


def grad(w):
    """Analytic gradient of the true loss at a single point w = (x, y)."""
    x, y = w
    rs = (x - SHARP_C[0]) ** 2 + (y - SHARP_C[1]) ** 2
    rf = (x - FLAT_C[0]) ** 2 + (y - FLAT_C[1]) ** 2
    es = np.exp(-rs / (2 * SHARP_S ** 2))
    ef = np.exp(-rf / (2 * FLAT_S ** 2))
    gx = (SHARP_A * es * (x - SHARP_C[0]) / SHARP_S ** 2
          + FLAT_A * ef * (x - FLAT_C[0]) / FLAT_S ** 2
          + 2 * CONFINE * x)
    gy = (SHARP_A * es * (y - SHARP_C[1]) / SHARP_S ** 2
          + FLAT_A * ef * (y - FLAT_C[1]) / FLAT_S ** 2
          + 2 * CONFINE * y)
    return np.array([gx, gy])


def _clamp(w):
    return np.clip(w, DOMAIN[0], DOMAIN[1])


# --- SAM worst-case (effective) objective -----------------------------------
def effective_loss(x, y, rho=DEFAULT_RHO, n_dirs=24):
    """
    E(w) = max_{||eps||<=rho} L(w+eps), approximated by sampling the rho-sphere
    in ``n_dirs`` directions plus the centre. Vectorised over arrays.
    """
    Z = loss(x, y)
    Z = Z.copy() if np.ndim(Z) else np.asarray(Z, dtype=float)
    for a in np.linspace(0, 2 * np.pi, n_dirs, endpoint=False):
        Z = np.maximum(Z, loss(x + rho * np.cos(a), y + rho * np.sin(a)))
    return Z


def effective_grad(w, rho=DEFAULT_RHO, h=1e-3):
    """Central finite-difference gradient of the effective objective E(w)."""
    x, y = w
    gx = (effective_loss(x + h, y, rho) - effective_loss(x - h, y, rho)) / (2 * h)
    gy = (effective_loss(x, y + h, rho) - effective_loss(x, y - h, rho)) / (2 * h)
    return np.array([float(gx), float(gy)])


# --- Trajectories ------------------------------------------------------------
def sgd_trajectory(start=START, lr=0.06, steps=170):
    """Vanilla gradient descent on the true loss L."""
    w = np.array(start, dtype=float)
    traj = [w.copy()]
    for _ in range(steps):
        w = _clamp(w - lr * grad(w))
        traj.append(w.copy())
    return np.array(traj)


def sam_trajectory(start=START, lr=0.06, rho=DEFAULT_RHO, steps=170):
    """
    SAM as descent on its exact objective E(w) (the full worst-case loss).
    Robust and faithful to the algorithm's purpose. At rho=0, E==L and this
    coincides with plain gradient descent.
    """
    w = np.array(start, dtype=float)
    traj = [w.copy()]
    if rho <= 1e-9:
        return sgd_trajectory(start, lr=lr, steps=steps)
    for _ in range(steps):
        w = _clamp(w - lr * effective_grad(w, rho))
        traj.append(w.copy())
    return np.array(traj)


def sam_first_order_trajectory(start=START, lr=0.06, rho=DEFAULT_RHO, steps=170):
    """
    The standard two-step first-order SAM update, provided for completeness:
        eps = rho * grad(w)/||grad(w)||  (ascent to the local worst case)
        w   = w - lr * grad(w + eps).
    Note: on a multi-basin landscape this one-step approximation is attracted to
    the ridge between basins, which is why the demo visualises SAM via its exact
    objective E(w) above rather than this approximation.
    """
    w = np.array(start, dtype=float)
    traj = [w.copy()]
    for _ in range(steps):
        g = grad(w)
        nrm = np.linalg.norm(g) + 1e-12
        eps = rho * g / nrm
        w = _clamp(w - lr * grad(w + eps))
        traj.append(w.copy())
    return np.array(traj)


# --- Surfaces for plotting ---------------------------------------------------
def surface_grid(res=90):
    """(X, Y, Z) mesh of the TRUE loss for 3-D plotting."""
    xs = np.linspace(DOMAIN[0], DOMAIN[1], res)
    ys = np.linspace(DOMAIN[0], DOMAIN[1], res)
    X, Y = np.meshgrid(xs, ys)
    return X, Y, loss(X, Y)


def effective_surface_grid(res=80, rho=DEFAULT_RHO, n_dirs=24):
    """(X, Y, Z) mesh of the SAM worst-case objective E for 3-D plotting."""
    xs = np.linspace(DOMAIN[0], DOMAIN[1], res)
    ys = np.linspace(DOMAIN[0], DOMAIN[1], res)
    X, Y = np.meshgrid(xs, ys)
    return X, Y, effective_loss(X, Y, rho=rho, n_dirs=n_dirs)


# --- Readouts ----------------------------------------------------------------
def sharpness(center, rho=DEFAULT_RHO, n_dirs=64):
    """
    Worst-case rise of the loss within the rho-ball around ``center``:
        sharpness(w) = max_{||eps||<=rho} L(w+eps) - L(w).
    Large => sharp basin; small => flat basin.
    """
    c = np.asarray(center, dtype=float)
    base = float(loss(c[0], c[1]))
    mx = base
    for a in np.linspace(0, 2 * np.pi, n_dirs, endpoint=False):
        mx = max(mx, float(loss(c[0] + rho * np.cos(a), c[1] + rho * np.sin(a))))
    return mx - base


def trajectory_loss(traj):
    """True-loss value along a trajectory (for convergence curves)."""
    return np.array([float(loss(p[0], p[1])) for p in traj])


def basin_of(point, tol=0.5):
    """Label the basin a final point landed in (for readouts)."""
    p = np.asarray(point, dtype=float)
    if np.linalg.norm(p - SHARP_C) < tol:
        return "sharp"
    if np.linalg.norm(p - FLAT_C) < tol:
        return "flat"
    return "other"


def compute_demo(rho=DEFAULT_RHO, lr=0.06, steps=170, start=START,
                 surf_res=80, eff_res=70):
    """
    One call that returns everything the UI module needs for a given rho:
    both surfaces, both trajectories, and the headline readouts.
    """
    Xs, Ys, Zs = surface_grid(res=surf_res)
    Xe, Ye, Ze = effective_surface_grid(res=eff_res, rho=rho)
    sgd = sgd_trajectory(start, lr=lr, steps=steps)
    sam = sam_trajectory(start, lr=lr, rho=rho, steps=steps)
    return {
        "true_surface": (Xs, Ys, Zs),
        "eff_surface": (Xe, Ye, Ze),
        "sgd_traj": sgd,
        "sam_traj": sam,
        "sgd_end": sgd[-1],
        "sam_end": sam[-1],
        "sgd_basin": basin_of(sgd[-1]),
        "sam_basin": basin_of(sam[-1]),
        "sgd_loss_curve": trajectory_loss(sgd),
        "sam_loss_curve": trajectory_loss(sam),
        "sharp_sharpness": sharpness(SHARP_C, rho=rho),
        "flat_sharpness": sharpness(FLAT_C, rho=rho),
        "sharp_loss": float(loss(SHARP_C[0], SHARP_C[1])),
        "flat_loss": float(loss(FLAT_C[0], FLAT_C[1])),
        "sharp_eff": float(effective_loss(SHARP_C[0], SHARP_C[1], rho=rho)),
        "flat_eff": float(effective_loss(FLAT_C[0], FLAT_C[1], rho=rho)),
        "rho": rho,
    }
