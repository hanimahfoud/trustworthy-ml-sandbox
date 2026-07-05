"""
modules/recourse_xai.py -- Practice demo: naive counterfactual vs causal recourse.

For a rejected applicant, core.recourse_core finds the least-cost income change
that flips the decision, and shows that acting on income (a cause of savings) is
strictly cheaper than moving income and savings independently.
"""
from __future__ import annotations

import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import loan_model_core as L
from core import recourse_core as R
from i18n import t


@st.cache_resource(show_spinner=False)
def _model():
    model, X, y, std = L.train_model(0)
    return model, X, y, std


def render(lang):
    model, X, y, std = _model()

    with st.container(border=True):
        C.plate_header(t(lang, "px_recourse_eyebrow"), t(lang, "px_recourse"))
        C.demo_intro(t(lang, "px_recourse_what"), t(lang, "px_recourse_why"),
                 t(lang, "px_recourse_expect"),
                 labels=(t(lang, "di_what"), t(lang, "di_why"),
                         t(lang, "di_expect")))

        c1, c2 = st.columns(2)
        with c1:
            income = st.slider(t(lang, "px_loan_income"), 0, 6000,
                               int(L.DEFAULT_APPLICANT["income"]), step=100)
        with c2:
            debt = st.slider(t(lang, "px_loan_debt"), 0, 15000,
                             int(L.DEFAULT_APPLICANT["debt"]), step=100)

        applicant = dict(L.DEFAULT_APPLICANT)
        applicant["income"] = float(income)
        applicant["debt"] = float(debt)

        rec = R.recommend(model, applicant, std, names=L.FEATURES)
        if not rec["feasible"]:
            C.warn(t(lang, "px_recourse_infeasible"))
            return

        col_bars, col_dag = st.columns(2)
        with col_bars:
            fig = go.Figure(go.Bar(
                x=["Naive", "Causal"],
                y=[rec["normal"]["cost"], rec["causal"]["cost"]],
                marker_color=[P.CRIMSON, P.TEAL]))
            P.style_2d(fig, x_title="", y_title="effort cost", height=300,
                       legend=False)
            st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "px_recourse_cap_bars"))
        with col_dag:
            g = rec["graph"]
            dag = P.causal_dag_figure(
                g["nodes"], g["edges"],
                labels={"income": "income", "savings": "savings"},
                node_colors={"income": P.INK, "savings": P.TEAL},
                edge_colors={("income", "savings"): P.TEAL}, height=300)
            st.plotly_chart(dag, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "px_recourse_cap_dag"))

        C.readout_strip([
            {"k": "P before", "v": f"{rec['p_before']:.3f}", "color": "crimson"},
            {"k": "P after", "v": f"{rec['p_after']:.3f}", "color": "teal"},
            {"k": "Δ income", "v": f"+{rec['delta_income']:.0f}", "u": "$"},
            {"k": "induced savings", "v": f"+{rec['induced_savings']:.0f}", "u": "$"},
            {"k": "causal saves", "v": f"{rec['savings']:.2f}", "u": "cost"},
        ])
        C.measure(f"<p>{t(lang, 'px_recourse_normal')}<br>"
                  f"{t(lang, 'px_recourse_causal')}</p>")
