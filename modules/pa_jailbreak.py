"""
modules/pa_jailbreak.py -- Practice demo: Gandalf-style jailbreak challenge.

A transparent, rule-based simulation (explicitly NOT a live LLM). The assistant
hides a secret and refuses to reveal it; the reader picks a prompt-injection
tactic and sees which framings defeat a naive guard.
"""
from __future__ import annotations

import streamlit as st

import components as C
from core import alignment_core as A
from i18n import t


def render(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "pa_jailbreak_eyebrow"), t(lang, "pa_jailbreak"))
        C.demo_intro(t(lang, "pa_jailbreak_what"), t(lang, "pa_jailbreak_why"),
                     t(lang, "pa_jailbreak_expect"),
                     labels=(t(lang, "di_what"), t(lang, "di_why"),
                             t(lang, "di_expect")))

        tactics = {
            "direct": "pa_jailbreak_t_direct",
            "authority": "pa_jailbreak_t_authority",
            "story_acrostic": "pa_jailbreak_t_story_acrostic",
            "roleplay": "pa_jailbreak_t_roleplay",
            "spell_check": "pa_jailbreak_t_spell_check",
        }
        keys = list(tactics.keys())
        tactic = st.selectbox(t(lang, "pa_jailbreak_tactic"), keys,
                              format_func=lambda k: t(lang, tactics[k]))

        leaked, _ = A.jailbreak_attempt(tactic)
        C.readout_strip([
            {"k": "guardrail", "v": "bypassed" if leaked else "held",
             "color": "crimson" if leaked else "teal"},
            {"k": "secret", "v": A.SECRET_WORD if leaked else "•••••••",
             "color": "crimson" if leaked else "teal"},
        ])
        if leaked:
            C.warn(t(lang, "pa_jailbreak_leak") + " — " +
                   t(lang, "pa_jailbreak_success"))
        else:
            C.key_idea(t(lang, "pa_jailbreak_refuse"))
        C.measure(f"<p>{t(lang, 'pa_jailbreak_note')}</p>")
