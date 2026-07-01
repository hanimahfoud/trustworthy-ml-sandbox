"""
core/fairness_core.py -- the compute engine for Section III (Fairness & Bias).

Everything here is real, deterministic and unit-tested:

* a synthetic hiring/credit dataset for two groups with *different base rates*
  (the precondition of the fairness impossibility theorem);
* per-group confusion at chosen thresholds and the three headline metrics
  (demographic parity, equal opportunity, equalized odds);
* post-processing thresholds that equalize acceptance (demographic parity) and
  that equalize true-positive rate (equal opportunity) -- the tool that lets the
  reader watch one metric break as the other is enforced;
* an RBF Maximum-Mean-Discrepancy between two score distributions (the quantity
  MinDiff penalizes);
* deterministic counterfactual text swapping (CDA) for English, Arabic, Persian.

No LLM is called. The multi-turn and constitutional demos in the UI are
explicitly rule-based educational simulations built on the deterministic
helpers at the bottom of this file.
"""
from __future__ import annotations

import numpy as np

GROUPS = ("A", "B")


def _sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def make_fairness_dataset(seed: int = 0, n: int = 1000,
                          base_rate_a: float = 0.60,
                          base_rate_b: float = 0.40,
                          measurement_bias: float = 0.55):
    """
    Two groups of applicants. ``y_true`` is genuine qualification (1 = qualified)
    with *different* base rates per group. ``score`` is a model's confidence in
    [0,1]: informative about qualification but shifted down for group B by
    ``measurement_bias`` (a measurement/representation bias), so an unadjusted
    single threshold is unfair.

    Returns a dict with arrays: group ('A'/'B'), y_true (0/1), score (float).
    """
    rng = np.random.default_rng(seed)
    half = n // 2
    group = np.array(["A"] * half + ["B"] * (n - half))
    y = np.empty(n, dtype=int)
    y[:half] = (rng.random(half) < base_rate_a).astype(int)
    y[half:] = (rng.random(n - half) < base_rate_b).astype(int)

    # latent signal: qualified applicants score higher; group B is shifted down.
    shift = np.where(group == "B", -measurement_bias, 0.0)
    z = 1.8 * (y - 0.5) * 2.0 + shift + rng.normal(0, 1.0, n)
    score = _sigmoid(z)
    return {"group": group, "y_true": y, "score": score}


def group_confusion(data, thr_a: float, thr_b: float):
    """Per-group confusion counts and rates at the two thresholds."""
    out = {}
    thr = {"A": thr_a, "B": thr_b}
    for g in GROUPS:
        m = data["group"] == g
        y = data["y_true"][m]
        s = data["score"][m]
        pred = (s >= thr[g]).astype(int)
        tp = int(np.sum((pred == 1) & (y == 1)))
        fp = int(np.sum((pred == 1) & (y == 0)))
        tn = int(np.sum((pred == 0) & (y == 0)))
        fn = int(np.sum((pred == 0) & (y == 1)))
        n = max(len(y), 1)
        pos = max(tp + fn, 1)
        neg = max(fp + tn, 1)
        out[g] = {
            "tp": tp, "fp": fp, "tn": tn, "fn": fn,
            "acceptance": (tp + fp) / n,
            "tpr": tp / pos,
            "fpr": fp / neg,
            "fnr": fn / pos,
            "n": n,
        }
    return out


def fairness_metrics(data, thr_a: float, thr_b: float):
    """The three headline fairness gaps plus the underlying per-group rates."""
    c = group_confusion(data, thr_a, thr_b)
    dp_gap = abs(c["A"]["acceptance"] - c["B"]["acceptance"])
    eo_gap = abs(c["A"]["tpr"] - c["B"]["tpr"])
    eodds_gap = max(abs(c["A"]["tpr"] - c["B"]["tpr"]),
                    abs(c["A"]["fpr"] - c["B"]["fpr"]))
    return {
        "confusion": c,
        "demographic_parity_gap": dp_gap,
        "equal_opportunity_gap": eo_gap,
        "equalized_odds_gap": eodds_gap,
    }


def _acceptance(data, g, thr):
    m = data["group"] == g
    return float(np.mean(data["score"][m] >= thr))


def _tpr(data, g, thr):
    m = (data["group"] == g) & (data["y_true"] == 1)
    if not np.any(m):
        return 0.0
    return float(np.mean(data["score"][m] >= thr))


def _best_threshold(data, g, target, fn):
    """Threshold for group g whose fn(g, thr) is closest to target."""
    cands = np.unique(np.concatenate([data["score"][data["group"] == g],
                                      np.array([0.0, 1.01])]))
    vals = np.array([fn(data, g, t) for t in cands])
    return float(cands[int(np.argmin(np.abs(vals - target)))])


def thresholds_for_demographic_parity(data, thr_a: float):
    """Keep A's threshold; pick B's so acceptance rates match (DP)."""
    target = _acceptance(data, "A", thr_a)
    return thr_a, _best_threshold(data, "B", target, _acceptance)


def thresholds_for_equal_opportunity(data, thr_a: float):
    """Keep A's threshold; pick B's so true-positive rates match (EO)."""
    target = _tpr(data, "A", thr_a)
    return thr_a, _best_threshold(data, "B", target, _tpr)


def mmd_rbf(x, y, gamma: float = 4.0):
    """Squared Maximum Mean Discrepancy between two 1-D samples (RBF kernel).

    This is the quantity MinDiff drives toward zero to align two groups' score
    distributions in a reproducing-kernel Hilbert space.
    """
    x = np.asarray(x, float).reshape(-1, 1)
    y = np.asarray(y, float).reshape(-1, 1)

    def k(a, b):
        d2 = (a - b.reshape(1, -1)) ** 2
        return np.exp(-gamma * d2)

    kxx = k(x, x).mean()
    kyy = k(y, y).mean()
    kxy = k(x, y).mean()
    return float(kxx + kyy - 2 * kxy)


# --------------------------------------------------------------------------- #
# Counterfactual Data Augmentation -- deterministic gendered-term swaps        #
# --------------------------------------------------------------------------- #
_PAIRS = {
    "en": [("he", "she"), ("him", "her"), ("his", "her"), ("man", "woman"),
           ("men", "women"), ("male", "female"), ("father", "mother"),
           ("nurse", "male nurse"), ("actor", "actress"), ("waiter", "waitress")],
    "ar": [("هو", "هي"), ("رجل", "امرأة"), ("الرجل", "المرأة"),
           ("معلم", "معلمة"), ("ممرض", "ممرضة"), ("الممرض", "الممرضة"),
           ("طبيب", "طبيبة"), ("مهندس", "مهندسة")],
    "fa": [("او مرد", "او زن"), ("مرد", "زن"), ("پسر", "دختر"),
           ("پرستار مرد", "پرستار زن"), ("معلم", "معلم زن"),
           ("مهندس", "مهندس زن")],
}


def _swap_word(word, pairs):
    low = word.lower()
    for a, b in pairs:
        if low == a.lower():
            return b
        if low == b.lower():
            return a
    return None


def cda_swap(text: str, lang: str = "en"):
    """Swap gendered terms to their counterfactual counterpart. Returns
    (swapped_text, n_changes). Deterministic, dictionary-based."""
    pairs = _PAIRS.get(lang, _PAIRS["en"])
    tokens = text.split()
    changes = 0
    out = []
    for tok in tokens:
        prefix = ""
        core = tok
        suffix = ""
        while core and not core[0].isalnum() and not ord(core[0]) > 127:
            prefix += core[0]; core = core[1:]
        while core and not core[-1].isalnum() and not ord(core[-1]) > 127:
            suffix = core[-1] + suffix; core = core[:-1]
        rep = _swap_word(core, pairs)
        if rep is not None:
            if core[:1].isupper():
                rep = rep[:1].upper() + rep[1:]
            out.append(prefix + rep + suffix)
            changes += 1
        else:
            out.append(tok)
    return " ".join(out), changes


# --------------------------------------------------------------------------- #
# Rule-based educational simulations (explicitly NOT an LLM)                    #
# --------------------------------------------------------------------------- #
def implicit_bias_judge(steps_injected: int, chose_neutral: bool):
    """Deterministic 'judge' score in [-1, 2] for the multi-turn simulator.

    steps_injected: how many leading/implicit prompts the user chained (0-3).
    chose_neutral : whether the final model reply was the fact-based, neutral one.
    Higher is better (2 = principled fact-based; -1 = fell for the bias).
    """
    if chose_neutral:
        return min(2, 2 - 0)          # principled regardless of pressure
    # gave the biased conclusion; the more setup, the worse it reflects
    return max(-1, 1 - steps_injected)


def constitutional_revise(biased: bool, rule_active: bool):
    """Return a label describing the critique/revision outcome for the CAI lab."""
    if not rule_active:
        return "no_constitution"
    return "revised" if biased else "already_compliant"
