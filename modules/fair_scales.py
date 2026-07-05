"""
modules/fair_scales.py -- Practice demo: the Fairness Scales dashboard.

1000 applicants across two groups with different base rates. The reader moves
each group's decision threshold (or auto-sets group B to enforce demographic
parity / equal opportunity) and the three fairness gaps update live -- showing
that closing one gap opens another.
"""
from __future__ import annotations

import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import fairness_core as F
from i18n import t


@st.cache_data(show_spinner=False)
def _data():
    return F.make_fairness_dataset(seed=0)


def render(lang):
    d = _data()

    with st.container(border=True):
        C.plate_header(t(lang, "pf_scales_eyebrow"), t(lang, "pf_scales"))
        C.demo_intro(t(lang, "pf_scales_what"), t(lang, "pf_scales_why"),
                 t(lang, "pf_scales_expect"),
                 labels=(t(lang, "di_what"), t(lang, "di_why"),
                         t(lang, "di_expect")))

        c1, c2 = st.columns(2)
        with c1:
            thr_a = st.slider(t(lang, "pf_scales_thr_a"), 0.05, 0.95, 0.50, 0.01)
        with c2:
            presets = ["pf_scales_preset_manual", "pf_scales_preset_dp",
                       "pf_scales_preset_eo"]
            preset = st.selectbox(t(lang, "pf_scales_preset"), presets,
                                  format_func=lambda k: t(lang, k))

        if preset == "pf_scales_preset_dp":
            _, thr_b = F.thresholds_for_demographic_parity(d, thr_a)
        elif preset == "pf_scales_preset_eo":
            _, thr_b = F.thresholds_for_equal_opportunity(d, thr_a)
        else:
            thr_b = st.slider(t(lang, "pf_scales_thr_b"), 0.05, 0.95, 0.50, 0.01)

        m = F.fairness_metrics(d, thr_a, thr_b)
        c = m["confusion"]

        # Figure 1: per-group rates
        cats = ["Acceptance", "TPR", "FPR"]
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(name="group A", x=cats,
                              y=[c["A"]["acceptance"], c["A"]["tpr"], c["A"]["fpr"]],
                              marker_color=P.TEAL))
        fig1.add_trace(go.Bar(name="group B", x=cats,
                              y=[c["B"]["acceptance"], c["B"]["tpr"], c["B"]["fpr"]],
                              marker_color=P.CRIMSON))
        fig1.update_layout(barmode="group")
        P.style_2d(fig1, x_title="", y_title="rate", height=300)

        # Figure 2: the three fairness gaps
        gaps = [m["demographic_parity_gap"], m["equal_opportunity_gap"],
                m["equalized_odds_gap"]]
        fig2 = go.Figure(go.Bar(
            x=["DP gap", "Equal-opp gap", "Equalized-odds gap"], y=gaps,
            marker_color=[P.TEAL if g < 0.05 else P.CRIMSON for g in gaps]))
        P.style_2d(fig2, x_title="", y_title="gap (0 = fair)", height=300,
                   legend=False)

        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig1, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "pf_scales_cap_rates"))
        with col2:
            st.plotly_chart(fig2, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "pf_scales_cap_metrics"))

        C.readout_strip([
            {"k": "threshold A", "v": f"{thr_a:.2f}"},
            {"k": "threshold B", "v": f"{thr_b:.2f}"},
            {"k": "DP gap", "v": f"{gaps[0]:.3f}",
             "color": "teal" if gaps[0] < 0.05 else "crimson"},
            {"k": "Equal-opp gap", "v": f"{gaps[1]:.3f}",
             "color": "teal" if gaps[1] < 0.05 else "crimson"},
            {"k": "Equalized-odds gap", "v": f"{gaps[2]:.3f}",
             "color": "teal" if gaps[2] < 0.05 else "crimson"},
        ])
        C.warn(t(lang, "pf_scales_note"))
