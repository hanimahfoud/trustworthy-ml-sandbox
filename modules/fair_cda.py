"""
modules/fair_cda.py -- Practice demo: counterfactual data augmentation (CDA).

The reader types a sentence; the deterministic dictionary-based swap produces
its gender-counterfactual, which would be added to the training set to break a
model's reliance on the sensitive attribute.
"""
from __future__ import annotations

import streamlit as st

import components as C
from core import fairness_core as F
from i18n import t


def render(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "pf_cda_eyebrow"), t(lang, "pf_cda"))
        C.demo_intro(t(lang, "pf_cda_what"), t(lang, "pf_cda_why"),
                 t(lang, "pf_cda_expect"),
                 labels=(t(lang, "di_what"), t(lang, "di_why"),
                         t(lang, "di_expect")))

        text = st.text_input(t(lang, "pf_cda_input"), t(lang, "pf_cda_default"))
        swapped, n = F.cda_swap(text, lang)

        col_a, col_b = st.columns(2)
        with col_a:
            C.measure(f"<p><b>{t(lang, 'pf_cda_cap_before')}</b></p>"
                      f"<p style='font-family:var(--mono)'>{text}</p>")
        with col_b:
            C.measure(f"<p><b>{t(lang, 'pf_cda_cap_after')}</b></p>"
                      f"<p style='font-family:var(--mono)'>{swapped}</p>")

        C.readout_strip([
            {"k": t(lang, "pf_cda_changes"), "v": str(n),
             "color": "teal" if n > 0 else "crimson"},
        ])
        C.key_idea(t(lang, "pf_cda_image_note"))
