"""
modules/simpsons_paradox.py -- Simpson's paradox engine.

Treatment B beats A within both the mild and severe groups, yet once severity
is confounded with assignment the pooled totals can reverse. Sliding the
allocation skew rebuilds the full 2×2×2 table; the within-group bars, the
pooled bars, the onset curve and the confounding DAG all update, and the
paradox flag is read straight from the computed rates.
"""
from __future__ import annotations

import streamlit as st
import plotly.graph_objects as go

import components as C
import plotting as P
from core import simpson_core as SI
from i18n import t

DEFAULT_SKEW = 0.75


@st.cache_data(show_spinner=False)
def _curve():
    return SI.paradox_curve()


def _pct(rate) -> float:
    return 100.0 * float(rate)


def render(lang: str) -> None:
    C.eyebrow(t(lang, "pr_simpson_eyebrow"))
    C.section_title(t(lang, "pr_simpson"))
    C.measure(f"<p>{t(lang, 'pr_simpson_intro')}</p>")

    with st.container(border=True):
        skew = st.slider(t(lang, "pr_simpson_ctrl_skew"), 0.0, 0.95,
                         DEFAULT_SKEW, 0.05)

    r = SI.compute(float(skew))
    curve = _curve()
    g = r["groups"]
    agg = r["aggregate"]

    # ---- Figures 1 & 2: within-group and pooled rates ----
    c_left, c_right = st.columns(2)
    with c_left:
        with st.container(border=True):
            f1 = go.Figure()
            f1.add_trace(go.Bar(
                x=["Mild", "Severe"],
                y=[_pct(g["mild"]["A"]["rate"]), _pct(g["severe"]["A"]["rate"])],
                name="A", marker_color=P.CRIMSON))
            f1.add_trace(go.Bar(
                x=["Mild", "Severe"],
                y=[_pct(g["mild"]["B"]["rate"]), _pct(g["severe"]["B"]["rate"])],
                name="B", marker_color=P.TEAL))
            P.style_2d(f1, x_title="Severity group",
                       y_title="Recovery rate (%)", height=360)
            f1.update_layout(barmode="group")
            f1.update_yaxes(range=[0, 100])
            st.plotly_chart(f1, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "pr_simpson_cap_groups"))

    with c_right:
        with st.container(border=True):
            f2 = go.Figure()
            f2.add_trace(go.Bar(
                x=["A (overall)", "B (overall)"],
                y=[_pct(agg["A"]["rate"]), _pct(agg["B"]["rate"])],
                marker_color=[P.CRIMSON, P.TEAL],
                text=[f"{_pct(agg['A']['rate']):.1f}%",
                      f"{_pct(agg['B']['rate']):.1f}%"],
                textposition="outside"))
            P.style_2d(f2, x_title="Pooled treatment",
                       y_title="Recovery rate (%)", height=360, legend=False)
            f2.update_yaxes(range=[0, 100])
            st.plotly_chart(f2, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "pr_simpson_cap_agg"))

    # ---- Figures 3 & 4: onset curve and confounding DAG ----
    d_left, d_right = st.columns(2)
    with d_left:
        with st.container(border=True):
            f3 = go.Figure()
            f3.add_trace(go.Scatter(
                x=curve["skews"], y=[_pct(v) for v in curve["agg_A"]],
                mode="lines", name="A", line=dict(color=P.CRIMSON, width=2.5)))
            f3.add_trace(go.Scatter(
                x=curve["skews"], y=[_pct(v) for v in curve["agg_B"]],
                mode="lines", name="B", line=dict(color=P.TEAL, width=2.5)))
            if curve["onset_skew"] is not None:
                f3.add_vline(x=curve["onset_skew"],
                             line=dict(color=P.GOLD, width=1.5, dash="dash"))
            f3.add_vline(x=skew, line=dict(color=P.INK, width=1.2, dash="dot"))
            P.style_2d(f3, x_title="Allocation skew",
                       y_title="Pooled recovery rate (%)", height=360)
            st.plotly_chart(f3, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "pr_simpson_cap_curve"))

    with d_right:
        with st.container(border=True):
            dag = SI.causal_dag()
            f4 = P.causal_dag_figure(
                dag["nodes"], dag["edges"],
                node_colors={"Severity": P.CRIMSON, "Treatment": P.INK,
                             "Outcome": P.INK},
                edge_colors={("Treatment", "Outcome"): P.TEAL},
                label_positions={"Severity": "top center",
                                 "Treatment": "bottom center",
                                 "Outcome": "bottom center"},
                height=360)
            st.plotly_chart(f4, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "pr_simpson_cap_dag"))

    # ---- readouts ----
    onset = curve["onset_skew"]
    C.readout_strip([
        {"k": "AGG RATE A", "v": f"{_pct(agg['A']['rate']):.1f}%", "color": "crimson"},
        {"k": "AGG RATE B", "v": f"{_pct(agg['B']['rate']):.1f}%", "color": "teal"},
        {"k": "ONSET SKEW", "v": "—" if onset is None else f"{onset:.2f}"},
        {"k": "PARADOX", "v": "YES" if r["paradox"] else "NO",
         "color": "crimson" if r["paradox"] else "teal"},
    ])

    # ---- status ----
    if r["paradox"]:
        C.warn(t(lang, "pr_simpson_on"))
    else:
        C.key_idea(t(lang, "pr_simpson_off"))
