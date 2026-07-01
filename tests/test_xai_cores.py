"""Unit tests for the Section II tabular-XAI cores."""
import numpy as np

from core import loan_model_core as L
from core import shap_core as SH
from core import lime_core as LI
from core import recourse_core as RC


# --------------------------------------------------------------------------- #
# loan_model_core                                                             #
# --------------------------------------------------------------------------- #
def test_default_applicant_rejected():
    m, X, y, std = L.train_model(0)
    assert L.predict_proba(m, L.DEFAULT_APPLICANT) < 0.5


def test_income_increases_approval():
    m, X, y, std = L.train_model(0)
    a0 = dict(L.DEFAULT_APPLICANT)
    a1 = dict(L.DEFAULT_APPLICANT)
    a1["income"] += 4000
    a1["savings"] += L.SAVINGS_PER_INCOME * 4000
    assert L.predict_proba(m, a1) > L.predict_proba(m, a0)


def test_causal_graph_edge():
    g = L.causal_graph()
    assert ("income", "savings") in g["edges"]


# --------------------------------------------------------------------------- #
# shap_core -- exact Shapley + additivity                                     #
# --------------------------------------------------------------------------- #
def test_shap_additivity():
    m, X, y, std = L.train_model(0)
    bg = X[:120]
    r = SH.shapley_values(m, L.to_vector(L.DEFAULT_APPLICANT), bg)
    # local accuracy: base + sum(phi) == prediction (exact, to float precision)
    assert abs(r["additivity_residual"]) < 1e-9
    assert abs(r["prediction"] - r["base_value"] - r["phi"].sum()) < 1e-9


def test_shap_rejected_is_net_negative():
    m, X, y, std = L.train_model(0)
    bg = X[:120]
    r = SH.shapley_values(m, L.to_vector(L.DEFAULT_APPLICANT), bg)
    # A strongly rejected applicant sits well below the background base rate.
    assert r["prediction"] < r["base_value"]
    idx = {f: i for i, f in enumerate(r["features"])}
    # Low income and high debt should both push the decision toward rejection.
    assert r["phi"][idx["income"]] < 0
    assert r["phi"][idx["debt"]] < 0


def test_shap_force_plot_reaches_output():
    m, X, y, std = L.train_model(0)
    bg = X[:120]
    r = SH.shapley_values(m, L.to_vector(L.DEFAULT_APPLICANT), bg)
    fp = SH.force_plot_data(r)
    assert abs(fp["segments"][-1]["end"] - fp["output_value"]) < 1e-9


# --------------------------------------------------------------------------- #
# lime_core -- sign recovery on a controlled linear black box                 #
# --------------------------------------------------------------------------- #
class _LinearBox:
    """Transparent sigmoid-linear model: income (+), debt (-), rest ~0."""
    def __init__(self, w):
        self.w = np.asarray(w, dtype=float)

    def predict_proba(self, X):
        X = np.asarray(X, dtype=float)
        z = X @ self.w
        p = 1.0 / (1.0 + np.exp(-z))
        return np.column_stack([1 - p, p])


def test_lime_recovers_signs():
    w = np.array([0.0, 2.0, -2.0, 0.0, 0.0])  # age, income, debt, savings, home
    box = _LinearBox(w)
    std = np.ones(5)
    rng = np.random.default_rng(1)
    bg = rng.normal(0, 1, size=(200, 5))
    bg[:, 4] = (bg[:, 4] > 0).astype(float)
    instance = np.zeros(5)
    r = LI.explain(box, instance, bg, feature_std=std, n_samples=1500, seed=1)
    idx = {f: i for i, f in enumerate(r["features"])}
    c = r["coefficients"]
    assert c[idx["income"]] > 0          # positive-weight feature
    assert c[idx["debt"]] < 0            # negative-weight feature
    # Zero-weight features should be much smaller than the driving ones.
    assert abs(c[idx["age"]]) < abs(c[idx["income"]])
    assert abs(c[idx["savings"]]) < abs(c[idx["income"]])


def test_lime_runs_on_real_model():
    m, X, y, std = L.train_model(0)
    r = LI.explain(m, L.to_vector(L.DEFAULT_APPLICANT), X[:200],
                   feature_std=std, n_samples=800, seed=0)
    assert len(r["coefficients"]) == len(L.FEATURES)
    assert r["local_r2"] <= 1.0


# --------------------------------------------------------------------------- #
# recourse_core -- causal plan is cheaper and both flip the decision          #
# --------------------------------------------------------------------------- #
def test_recourse_feasible_and_flips():
    m, X, y, std = L.train_model(0)
    r = RC.recommend(m, L.DEFAULT_APPLICANT, std)
    assert r["feasible"]
    assert r["p_before"] < 0.5 <= r["p_after"]


def test_recourse_causal_cheaper():
    m, X, y, std = L.train_model(0)
    r = RC.recommend(m, L.DEFAULT_APPLICANT, std)
    # Causal recourse gets the induced savings "for free" -> strictly cheaper.
    assert r["causal"]["cost"] < r["normal"]["cost"]
    assert r["induced_savings"] > 0


def test_recourse_respects_immutability():
    m, X, y, std = L.train_model(0)
    r = RC.recommend(m, L.DEFAULT_APPLICANT, std)
    # Only income (and, causally, savings) may move; age & home are untouched.
    assert set(r["causal"]["delta"].keys()) == {"income"}
    assert set(r["normal"]["delta"].keys()) == {"income", "savings"}
    assert r["endpoint"]["age"] == L.DEFAULT_APPLICANT["age"]
    assert r["endpoint"]["owns_home"] == L.DEFAULT_APPLICANT["owns_home"]
