"""
modules/pa_hacking.py -- Practice demo: RLHF reward-hacking simulator.

The optimal KL-regularized policy pi*(a) ∝ ref(a) exp(reward(a)/beta) is
computed in closed form over a tiny vocabulary. Shrinking beta lets the policy
pile probability onto the reward model's over-valued hype tokens -- reward
hacking, shown numerically.
"""
from __future__ import annotations

import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import alignment_core as A
from i18n import t


def render(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "pa_hacking_eyebrow"), t(lang, "pa_hacking"))
        C.demo_intro(t(lang, "pa_hacking_what"), t(lang, "pa_hacking_why"),
                     t(lang, "pa_hacking_expect"),
                     labels=(t(lang, "di_what"), t(lang, "di_why"),
                             t(lang, "di_expect")))

        beta = st.slider(t(lang, "pa_hacking_beta"), 0.0, 1.0, 0.5, 0.05)
        out = A.reward_hacking_demo(beta)

        fig = go.Figure()
        fig.add_trace(go.Bar(x=out["vocab"], y=out["pi"], name="policy π",
                             marker_color=P.CRIMSON))
        fig.add_trace(go.Bar(x=out["vocab"], y=out["ref"], name="reference",
                             marker_color=P.SLATE, opacity=0.5))
        fig.update_layout(barmode="overlay")
        P.style_2d(fig, x_title="", y_title="probability", height=320)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "pa_hacking_cap"))

        hacked = out["hype_mass"] > 0.6
        answer = t(lang, "pa_hacking_hacked") if hacked else t(lang, "pa_hacking_sane")
        C.readout_strip([
            {"k": t(lang, "pa_hacking_answer"), "v": answer,
             "color": "crimson" if hacked else "teal"},
            {"k": t(lang, "pa_hacking_hype"), "v": f"{out['hype_mass']:.2f}",
             "color": "crimson" if hacked else "teal"},
            {"k": t(lang, "pa_hacking_kl"), "v": f"{out['kl']:.2f}"},
            {"k": "β", "v": f"{beta:.2f}"},
        ])
        if hacked:
            C.warn(t(lang, "pa_hacking_note"))
        else:
            C.key_idea(t(lang, "pa_hacking_note"))
