"""
modules/rob_jailbreak.py -- Practice demo: LLM jailbreak game.

A transparent, rule-based simulation of a guardrailed assistant (explicitly NOT
a live LLM). The assistant hides a secret and refuses to reveal it; the reader
picks a prompt-injection tactic and sees which framings defeat a naive guard.
"""
from __future__ import annotations

import streamlit as st

import components as C
from core import robustness_core as R
from i18n import t


def render(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "prb_jailbreak_eyebrow"), t(lang, "prb_jailbreak"))
        C.measure(f"<p>{t(lang, 'prb_jailbreak_intro')}</p>")

        tactics = {
            "direct": "prb_jailbreak_t_direct",
            "authority": "prb_jailbreak_t_authority",
            "roleplay": "prb_jailbreak_t_roleplay",
            "translate": "prb_jailbreak_t_translate",
            "acrostic": "prb_jailbreak_t_acrostic",
        }
        keys = list(tactics.keys())
        tactic = st.selectbox(t(lang, "prb_jailbreak_tactic"), keys,
                              format_func=lambda k: t(lang, tactics[k]))

        leaked, resp = R.jailbreak_attempt(tactic)

        C.readout_strip([
            {"k": "guardrail", "v": "bypassed" if leaked else "held",
             "color": "crimson" if leaked else "teal"},
            {"k": "secret", "v": R.SECRET if leaked else "•••••••••",
             "color": "crimson" if leaked else "teal"},
        ])
        if leaked:
            C.warn(t(lang, "prb_jailbreak_leak") + " — " +
                   t(lang, "prb_jailbreak_success"))
        else:
            C.key_idea(t(lang, "prb_jailbreak_refuse"))
        C.measure(f"<p>{t(lang, 'prb_jailbreak_note')}</p>")
