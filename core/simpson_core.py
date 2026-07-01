"""
Simpson's Paradox -- compute core
=================================
A confounder (disease *severity*) influences BOTH which treatment a patient
receives AND the patient's chance of recovery. This induces Simpson's paradox:

    Treatment B has a higher recovery rate than A *within every severity group*,
    yet a lower recovery rate than A *overall*,

because B is administered disproportionately to the hard (severe, low-recovery)
cases. This is the structure of the classic kidney-stone study (Charig et al.,
1986).

The model is fully parametric. The "allocation skew" ``s`` in [0, 1] controls how
strongly severity drives treatment choice:
  * s = 0  -> treatment independent of severity: NO paradox (B wins everywhere).
  * s -> 1 -> A concentrated on mild cases, B on severe cases: STRONG paradox.

Causal graph (confounding triangle):
        Severity --> Treatment ,  Severity --> Outcome ,  Treatment --> Outcome.

The correct causal question -- "does B cause better recovery than A?" -- is
answered by the within-group (severity-adjusted) comparison, not the aggregate.

Plain NumPy; exercised by tests/test_simpson_core.py.
"""
from __future__ import annotations

import numpy as np

# Default recovery rates. B is better than A by ``delta`` in BOTH groups.
R_A_MILD = 0.85
R_A_SEVERE = 0.30
DELTA = 0.05
N_MILD = 350
N_SEVERE = 350


def compute(skew: float = 0.75,
            r_a_mild: float = R_A_MILD,
            r_a_severe: float = R_A_SEVERE,
            delta: float = DELTA,
            n_mild: int = N_MILD,
            n_severe: int = N_SEVERE) -> dict:
    """
    Build the full 2x2x2 contingency table (treatment x severity x outcome)
    for a given allocation skew and return rates, aggregates and paradox flags.
    """
    skew = float(np.clip(skew, 0.0, 0.98))
    r_b_mild = min(r_a_mild + delta, 0.999)
    r_b_severe = min(r_a_severe + delta, 0.999)

    # Fraction of each severity group assigned to treatment A.
    pA_mild = 0.5 + 0.5 * skew          # mild cases lean toward A
    pA_severe = 0.5 - 0.5 * skew        # severe cases lean toward B

    # Cell sizes (rounded to whole patients for display).
    nA_mild = int(round(n_mild * pA_mild))
    nB_mild = n_mild - nA_mild
    nA_severe = int(round(n_severe * pA_severe))
    nB_severe = n_severe - nA_severe

    # Recoveries per cell.
    recA_mild = int(round(nA_mild * r_a_mild))
    recB_mild = int(round(nB_mild * r_b_mild))
    recA_severe = int(round(nA_severe * r_a_severe))
    recB_severe = int(round(nB_severe * r_b_severe))

    def rate(rec, n):
        return (rec / n) if n > 0 else float("nan")

    # Per-group (severity-adjusted) rates.
    grp = {
        "mild": {
            "A": {"rec": recA_mild, "n": nA_mild, "rate": rate(recA_mild, nA_mild)},
            "B": {"rec": recB_mild, "n": nB_mild, "rate": rate(recB_mild, nB_mild)},
        },
        "severe": {
            "A": {"rec": recA_severe, "n": nA_severe, "rate": rate(recA_severe, nA_severe)},
            "B": {"rec": recB_severe, "n": nB_severe, "rate": rate(recB_severe, nB_severe)},
        },
    }

    # Aggregate (marginal) rates.
    totA = nA_mild + nA_severe
    totB = nB_mild + nB_severe
    recA = recA_mild + recA_severe
    recB = recB_mild + recB_severe
    agg = {
        "A": {"rec": recA, "n": totA, "rate": rate(recA, totA)},
        "B": {"rec": recB, "n": totB, "rate": rate(recB, totB)},
    }

    b_better_mild = grp["mild"]["B"]["rate"] > grp["mild"]["A"]["rate"]
    b_better_severe = grp["severe"]["B"]["rate"] > grp["severe"]["A"]["rate"]
    a_better_overall = agg["A"]["rate"] > agg["B"]["rate"]
    paradox = bool(b_better_mild and b_better_severe and a_better_overall)

    return {
        "skew": skew,
        "groups": grp,
        "aggregate": agg,
        "b_better_in_both_groups": bool(b_better_mild and b_better_severe),
        "a_better_overall": bool(a_better_overall),
        "paradox": paradox,
        # convenience scalars
        "agg_rate_A": agg["A"]["rate"],
        "agg_rate_B": agg["B"]["rate"],
    }


def paradox_curve(r_a_mild: float = R_A_MILD, r_a_severe: float = R_A_SEVERE,
                  delta: float = DELTA, n_mild: int = N_MILD,
                  n_severe: int = N_SEVERE, n_points: int = 60):
    """
    Aggregate A and B recovery rates as a function of the allocation skew, plus
    the (constant) within-group B rates, for the 'how the paradox switches on'
    figure. Returns dict of arrays.
    """
    skews = np.linspace(0.0, 0.95, n_points)
    aggA, aggB = [], []
    for s in skews:
        r = compute(s, r_a_mild, r_a_severe, delta, n_mild, n_severe)
        aggA.append(r["agg_rate_A"])
        aggB.append(r["agg_rate_B"])
    # The skew at which A overtakes B overall (paradox onset), if any.
    aggA = np.array(aggA); aggB = np.array(aggB)
    onset = None
    cross = np.where(np.diff(np.sign(aggA - aggB)))[0]
    if len(cross):
        onset = float(skews[cross[0] + 1])
    return {
        "skews": skews,
        "agg_A": aggA,
        "agg_B": aggB,
        "onset_skew": onset,
    }


def causal_dag():
    """
    Node positions and directed edges of the confounding triangle, for plotting.
    Severity is the confounder (a common cause of Treatment and Outcome).
    """
    nodes = {
        "Severity":  (0.5, 1.0),
        "Treatment": (0.0, 0.0),
        "Outcome":   (1.0, 0.0),
    }
    edges = [
        ("Severity", "Treatment"),   # confounder -> treatment assignment
        ("Severity", "Outcome"),     # confounder -> recovery
        ("Treatment", "Outcome"),    # causal effect of interest
    ]
    return {"nodes": nodes, "edges": edges, "confounder": "Severity"}
