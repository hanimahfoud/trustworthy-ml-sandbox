"""
modules/pp_coin.py -- Practice demo: the coin-flip randomized-response simulator.

Simulate a sensitive survey answered under randomized response and show that
the aggregate rate is recovered while each individual answer stays deniable.
The convergence curve is computed live.
"""
from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import privacy_core as PV
from i18n import t


def render(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "pp_coin_eyebrow"), t(lang, "pp_coin"))
        C.demo_intro(t(lang, "pp_coin_what"), t(lang, "pp_coin_why"),
                     t(lang, "pp_coin_expect"),
                     labels=(t(lang, "di_what"), t(lang, "di_why"),
                             t(lang, "di_expect")))

        c1, c2, c3 = st.columns(3)
        with c1:
            true_rate = st.slider(t(lang, "pp_coin_true"), 0.0, 1.0, 0.15, 0.05)
        with c2:
            n = st.slider(t(lang, "pp_coin_n"), 100, 5000, 2000, 100)
        with c3:
            p_truth = st.slider(t(lang, "pp_coin_ptruth"), 0.1, 0.9, 0.5, 0.1)

        rng = np.random.default_rng(0)
        bits = (rng.random(n) < true_rate).astype(int)
        r = PV.randomized_response(bits, p_truth=p_truth, seed=1)

        # convergence of the estimate as the crowd grows
        sizes = np.linspace(50, n, 40).astype(int)
        ests = []
        for s in sizes:
            rr = PV.randomized_response(bits[:s], p_truth=p_truth, seed=1)
            ests.append(rr["estimated_true_rate"])
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=sizes, y=ests, mode="lines+markers",
                                 name="estimate", line=dict(color=P.CRIMSON, width=2)))
        fig.add_hline(y=true_rate, line_dash="dash", line_color=P.TEAL)
        P.style_2d(fig, x_title="respondents", y_title="estimated yes-rate",
                   height=300)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "pp_coin_cap"))

        C.readout_strip([
            {"k": t(lang, "pp_coin_actual"), "v": f"{true_rate:.2f}",
             "color": "teal"},
            {"k": t(lang, "pp_coin_est"), "v": f"{r['estimated_true_rate']:.3f}",
             "color": "crimson"},
            {"k": "observed (noisy)", "v": f"{r['observed_rate']:.3f}"},
        ])
        C.key_idea(t(lang, "pp_coin_note"))
