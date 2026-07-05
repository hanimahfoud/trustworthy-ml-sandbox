"""
modules/fair_constitution.py -- Practice demo: Constitutional AI lab.

A transparent, rule-based simulation of Constitutional AI (explicitly NOT a
live LLM). Two candidate answers are shown; adding a constitutional rule
triggers a self-critique of the biased answer and a revision that complies --
with no human feedback.
"""
from __future__ import annotations

import streamlit as st

import components as C
from core import fairness_core as F
from i18n import t


def render(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "pf_constitution_eyebrow"),
                       t(lang, "pf_constitution"))
        C.demo_intro(t(lang, "pf_constitution_what"), t(lang, "pf_constitution_why"),
                 t(lang, "pf_constitution_expect"),
                 labels=(t(lang, "di_what"), t(lang, "di_why"),
                         t(lang, "di_expect")))

        col_a, col_b = st.columns(2)
        with col_a:
            C.measure(f"<p><b>{t(lang, 'pf_constitution_answer_biased')}</b></p>"
                      f"<p style='font-family:var(--mono)'>"
                      f"{t(lang, 'pf_constitution_a_biased')}</p>")
        with col_b:
            C.measure(f"<p><b>{t(lang, 'pf_constitution_answer_fair')}</b></p>"
                      f"<p style='font-family:var(--mono)'>"
                      f"{t(lang, 'pf_constitution_a_fair')}</p>")

        rule_active = st.checkbox(t(lang, "pf_constitution_button"), value=True)
        if rule_active:
            st.text_input(t(lang, "pf_constitution_rule"),
                          t(lang, "pf_constitution_rule_default"))

        state = F.constitutional_revise(biased=True, rule_active=rule_active)
        if state == "no_constitution":
            C.warn(t(lang, "pf_constitution_none"))
            return

        C.measure(f"<p><b>{t(lang, 'pf_constitution_critique')}:</b> "
                  f"{t(lang, 'pf_constitution_critique_text')}</p>")
        C.key_idea(f"<b>{t(lang, 'pf_constitution_revision')}:</b> "
                   f"{t(lang, 'pf_constitution_a_fair')}")
