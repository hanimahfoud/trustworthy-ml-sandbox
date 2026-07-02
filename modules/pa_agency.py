"""
modules/pa_agency.py -- Practice demo: excessive-agency sandbox.

A simulated inbox contains a spam email with a hidden "delete everything"
instruction (indirect prompt injection). The reader chooses the assistant's
permissions and asks it to summarize; under read-only nothing happens, under
write/delete the injection wipes the inbox. Deterministic, rule-based.
"""
from __future__ import annotations

import streamlit as st

import components as C
from core import alignment_core as A
from i18n import t


def _render_inbox(lang, inbox):
    if not inbox:
        C.measure(f"<p><em>{t(lang, 'pa_agency_empty')}</em></p>")
        return
    rows = "".join(
        f'<div class="readout" style="text-align:left">'
        f'<div class="k">{m["from"]}</div>'
        f'<div class="v" style="font-size:.95rem">{m["subject"]}'
        + ('  🚩' if m["hidden"] else '') + '</div></div>'
        for m in inbox)
    st.markdown(f'<div class="readout-strip">{rows}</div>',
                unsafe_allow_html=True)


def render(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "pa_agency_eyebrow"), t(lang, "pa_agency"))
        C.demo_intro(t(lang, "pa_agency_what"), t(lang, "pa_agency_why"),
                     t(lang, "pa_agency_expect"),
                     labels=(t(lang, "di_what"), t(lang, "di_why"),
                             t(lang, "di_expect")))

        perms = {"read_only": "pa_agency_readonly",
                 "write_delete": "pa_agency_writedelete"}
        agency = st.radio(t(lang, "pa_agency_perm"), list(perms.keys()),
                          format_func=lambda k: t(lang, perms[k]), horizontal=True)
        run = st.checkbox(t(lang, "pa_agency_run"), value=False)

        inbox = A.DEFAULT_INBOX
        result, events, wiped = (inbox, [], False)
        if run:
            result, events, wiped = A.excessive_agency_step(inbox, agency)

        C.measure(f"<p><b>{t(lang, 'pa_agency_inbox')}</b></p>")
        _render_inbox(lang, result)

        if run:
            log = "  →  ".join(events)
            C.figure_caption(log)
            if wiped:
                C.warn(t(lang, "pa_agency_wiped"))
            else:
                C.key_idea(t(lang, "pa_agency_safe"))
        C.measure(f"<p>{t(lang, 'pa_agency_note')}</p>")
