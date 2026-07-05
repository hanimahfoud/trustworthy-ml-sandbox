"""
modules/xai_loan.py -- Practice demo: explain one loan decision two ways at once.

A RandomForest (core.loan_model_core) decides the loan; the reader sets the
applicant with sliders, and both a LIME local surrogate and exact Shapley
values are computed live on every change. Nothing is scripted.
"""
from __future__ import annotations

import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import loan_model_core as L
from core import lime_core as LIME
from core import shap_core as SH
from i18n import t


@st.cache_resource(show_spinner=False)
def _model():
    model, X, y, std = L.train_model(0)
    return model, X, y, std


def _bar(names, vals, x_title):
    fig = go.Figure(go.Bar(
        x=vals, y=names, orientation="h",
        marker_color=[P.TEAL if v >= 0 else P.CRIMSON for v in vals]))
    P.style_2d(fig, x_title=x_title, y_title="", height=300, legend=False)
    return fig


def render(lang):
    model, X, y, std = _model()

    with st.container(border=True):
        C.plate_header(t(lang, "px_loan_eyebrow"), t(lang, "px_loan"))
        C.demo_intro(t(lang, "px_loan_what"), t(lang, "px_loan_why"),
                 t(lang, "px_loan_expect"),
                 labels=(t(lang, "di_what"), t(lang, "di_why"),
                         t(lang, "di_expect")))

        c1, c2, c3 = st.columns(3)
        with c1:
            age = st.slider(t(lang, "px_loan_age"), 18, 75,
                            int(L.DEFAULT_APPLICANT["age"]))
            income = st.slider(t(lang, "px_loan_income"), 0, 8000,
                               int(L.DEFAULT_APPLICANT["income"]), step=100)
        with c2:
            debt = st.slider(t(lang, "px_loan_debt"), 0, 15000,
                             int(L.DEFAULT_APPLICANT["debt"]), step=100)
            savings = st.slider(t(lang, "px_loan_savings"), 0, 15000,
                                int(L.DEFAULT_APPLICANT["savings"]), step=100)
        with c3:
            owns = st.selectbox(t(lang, "px_loan_home"), [0, 1],
                                format_func=lambda v: ["—", "✓"][v])

        applicant = {"age": float(age), "income": float(income),
                     "debt": float(debt), "savings": float(savings),
                     "owns_home": float(owns)}
        x = L.to_vector(applicant)
        p_approve = L.predict_proba(model, x)
        approved = p_approve >= 0.5

        key = "px_loan_decision_approved" if approved else "px_loan_decision_rejected"
        badge_color = "teal" if approved else "crimson"
        C.readout_strip([
            {"k": t(lang, key).split(":")[0], "v": t(lang, key).split(": ")[1],
             "color": badge_color},
            {"k": "P(approved)", "v": f"{p_approve:.3f}",
             "color": badge_color},
        ])

        bg = X[:200]
        lime_r = LIME.explain(model, x, bg, std, n_samples=800, seed=0,
                              feature_names=L.FEATURES)
        shap_r = SH.shapley_values(model, x, bg, feature_names=L.FEATURES)

        col_l, col_s = st.columns(2)
        with col_l:
            st.plotly_chart(_bar(lime_r["features"], list(lime_r["coefficients"]),
                                 "LIME weight → approval"),
                            use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "px_loan_cap_lime"))
        with col_s:
            st.plotly_chart(_bar(shap_r["features"], list(shap_r["phi"]),
                                 "SHAP φ → approval"),
                            use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "px_loan_cap_shap"))

        C.readout_strip([
            {"k": "SHAP base value", "v": f"{shap_r['base_value']:.3f}"},
            {"k": "Σφ + base", "v": f"{shap_r['base_value'] + sum(shap_r['phi']):.3f}"},
            {"k": "additivity residual", "v": f"{shap_r['additivity_residual']:.1e}"},
            {"k": "LIME local R²", "v": f"{lime_r['local_r2']:.2f}"},
        ])
        C.key_idea(t(lang, "px_loan_note"))
