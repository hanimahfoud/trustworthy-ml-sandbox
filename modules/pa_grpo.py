"""
modules/pa_grpo.py -- Practice demo: GRPO reasoning visualizer.

Pose an arithmetic problem; the "model" emits K candidate expressions; a real
rule-based verifier (an arithmetic evaluator) accepts only those that compute
the right value, and GRPO's group-relative advantage rewards them. No human
labels -- exactly GRPO's recipe (DeepSeek-R1 style).
"""
from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import alignment_core as A
from i18n import t

# a fixed pool of candidate "reasonings" for a target; some right, some wrong
_POOL = {
    42: ["6*7", "42", "6*7+1", "40", "(6*7)", "42", "7*6", "6*8", "5*8", "43"],
    100: ["10*10", "100", "99+1", "10^2", "50*2", "100", "10*9", "101", "25*4", "90"],
    24: ["4!", "24", "6*4", "4*5", "3*8", "24", "12*2", "23", "8*3", "25"],
}


def render(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "pa_grpo_eyebrow"), t(lang, "pa_grpo"))
        C.demo_intro(t(lang, "pa_grpo_what"), t(lang, "pa_grpo_why"),
                     t(lang, "pa_grpo_expect"),
                     labels=(t(lang, "di_what"), t(lang, "di_why"),
                             t(lang, "di_expect")))

        c1, c2 = st.columns(2)
        with c1:
            target = st.selectbox(t(lang, "pa_grpo_problem"),
                                  [("6 × 7 = ?", 42), ("? = 100", 100),
                                   ("4! = ?", 24)],
                                  format_func=lambda x: x[0])[1]
        with c2:
            k = st.slider(t(lang, "pa_grpo_k"), 4, 8, 8, 1)

        cands = [c for c in _POOL[target] if A._safe_eval_arithmetic(c) is not None][:k]
        # ensure exactly k by padding with a wrong candidate if needed
        while len(cands) < k:
            cands.append(str(target + 7))
        r = A.grpo_group_score(cands, target=target)

        colors = [P.TEAL if rr == 1 else P.CRIMSON for rr in r["rewards"]]
        fig = go.Figure(go.Bar(
            x=[f"y{i+1}: {cands[i]}" for i in range(len(cands))],
            y=r["advantages"], marker_color=colors,
            text=[f"r={int(rr)}" for rr in r["rewards"]], textposition="outside"))
        P.style_2d(fig, x_title="candidate", y_title="group-relative advantage",
                   height=340, legend=False)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "pa_grpo_cap"))

        C.readout_strip([
            {"k": t(lang, "pa_grpo_majority"),
             "v": f"{r['majority']:.0f}" if r["majority"] is not None else "—",
             "color": "teal"},
            {"k": t(lang, "pa_grpo_consistency"), "v": f"{r['consistency']:.2f}"},
            {"k": t(lang, "pa_grpo_correct"), "v": f"{r['n_correct']}/{len(cands)}",
             "color": "teal"},
        ])
        C.key_idea(t(lang, "pa_grpo_note"))
