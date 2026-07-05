"""
modules/fair_multiturn.py -- Practice demo: implicit-bias multi-turn simulator.

A transparent, rule-based simulation of FairEmtBench (explicitly NOT a live
LLM). The reader chains leading turns to build a biased context, then picks the
model's final reply; a deterministic judge scores whether it resisted the
implicit bias or fell for the premise built up over the turns.
"""
from __future__ import annotations

import streamlit as st

import components as C
from core import fairness_core as F
from i18n import t


def render(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "pf_multiturn_eyebrow"), t(lang, "pf_multiturn"))
        C.demo_intro(t(lang, "pf_multiturn_what"), t(lang, "pf_multiturn_why"),
                 t(lang, "pf_multiturn_expect"),
                 labels=(t(lang, "di_what"), t(lang, "di_why"),
                         t(lang, "di_expect")))

        t1 = st.checkbox(t(lang, "pf_multiturn_t1"), value=True)
        t2 = st.checkbox(t(lang, "pf_multiturn_t2"), value=True)
        t3 = st.checkbox(t(lang, "pf_multiturn_t3"), value=True)
        steps = int(t1) + int(t2) + int(t3)

        reply = st.radio(
            t(lang, "pf_multiturn_reply"),
            ["pf_multiturn_neutral", "pf_multiturn_biased"],
            format_func=lambda k: t(lang, k))
        chose_neutral = reply == "pf_multiturn_neutral"

        score = F.implicit_bias_judge(steps, chose_neutral)
        good = chose_neutral

        C.readout_strip([
            {"k": t(lang, "pf_multiturn_steps"), "v": str(steps)},
            {"k": t(lang, "pf_multiturn_score"), "v": f"{score}",
             "color": "teal" if good else "crimson"},
        ])
        verdict = "pf_multiturn_verdict_good" if good else "pf_multiturn_verdict_bad"
        C.measure(f"<p><b>{t(lang, 'pf_multiturn_judge')}:</b> "
                  f"{t(lang, verdict)}</p>")
        if good:
            C.key_idea(t(lang, verdict))
        else:
            C.warn(t(lang, verdict))
