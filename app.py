"""
app.py -- Trustworthy Machine Learning · interactive sandbox.

Entry point: builds the journal masthead and the sidebar "contents rail"
(language + theme + section + Theory/Practice toggle + page navigation),
injects the theme with the correct text direction, offers a printable PDF of
the current section, and routes to the selected theory plate or interactive
demo. All compute lives in core/; all prose in i18n.py; nav keys in nav.py.
"""
from __future__ import annotations

import streamlit as st

import components as C
import nav
from i18n import LANGS, is_rtl, t
from modules import theory, theory_xai, theory_fair, theory_robust, theory_privacy, theory_align
from modules import (
    bias_variance,
    counterfactual,
    domain_adaptation,
    sam_optimizer,
    simpsons_paradox,
)
from modules import xai_loan, recourse_xai, cv_scanner, spurious
from modules import fair_scales, fair_cda, fair_multiturn, fair_constitution
from modules import rob_evasion, rob_tradeoff, rob_smoothing, rob_jailbreak
from modules import pp_backdoor, pp_coin, pp_laplace, pp_leak
from modules import pa_hacking, pa_grpo, pa_jailbreak, pa_agency
from modules import pdf_export

st.set_page_config(
    page_title="Trustworthy ML",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- render registries, per section ---------------------------------------- #
THEORY_RENDER = {"sec1": theory.SECTIONS, "sec2": theory_xai.SECTIONS_XAI,
                 "sec3": theory_fair.SECTIONS_FAIR,
                 "sec4": theory_robust.SECTIONS_ROBUST,
                 "sec5": theory_privacy.SECTIONS_PRIVACY,
                 "sec6": theory_align.SECTIONS_ALIGN}
PRACTICE_RENDER = {
    "sec1": {
        "pr_bv": bias_variance.render,
        "pr_dann": domain_adaptation.render,
        "pr_sam": sam_optimizer.render,
        "pr_simpson": simpsons_paradox.render,
        "pr_cf": counterfactual.render,
    },
    "sec2": {
        "px_loan": xai_loan.render,
        "px_recourse": recourse_xai.render,
        "px_cv": cv_scanner.render,
        "px_spurious": spurious.render,
    },
    "sec3": {
        "pf_scales": fair_scales.render,
        "pf_cda": fair_cda.render,
        "pf_multiturn": fair_multiturn.render,
        "pf_constitution": fair_constitution.render,
    },
    "sec4": {
        "prb_evasion": rob_evasion.render,
        "prb_tradeoff": rob_tradeoff.render,
        "prb_smoothing": rob_smoothing.render,
        "prb_jailbreak": rob_jailbreak.render,
    },
    "sec5": {
        "pp_backdoor": pp_backdoor.render,
        "pp_coin": pp_coin.render,
        "pp_laplace": pp_laplace.render,
        "pp_leak": pp_leak.render,
    },
    "sec6": {
        "pa_hacking": pa_hacking.render,
        "pa_grpo": pa_grpo.render,
        "pa_jailbreak": pa_jailbreak.render,
        "pa_agency": pa_agency.render,
    },
}

MODE_KEYS = ["mode_theory", "mode_practice"]
LANG_CODES = [c for c, _ in LANGS]
NAME_OF = dict(LANGS)
THEME_CODES = ["light", "dark"]

BOTPRESS_URL = (
    "https://cdn.botpress.cloud/webchat/v3.6/shareable.html?configUrl="
    "https://files.bpcontent.cloud/2026/07/01/08/20260701082723-ZJ4IWTNT.json"
)


@st.cache_data(show_spinner=False)
def _pdf_bytes(lang: str, section: str) -> bytes:
    return pdf_export.build_pdf(lang, section)


sb = st.sidebar
name_slot = sb.empty()

# --- language (first, to fix direction before theming) ---
prelim = st.session_state.get("lang", "en")
sb.markdown(f'<div class="rail-label">{t(prelim, "lang_label")}</div>',
            unsafe_allow_html=True)
lang = sb.radio("language", options=LANG_CODES, format_func=lambda c: NAME_OF[c],
                index=LANG_CODES.index(prelim) if prelim in LANG_CODES else 0,
                key="lang", label_visibility="collapsed")

# --- theme ---
sb.markdown(f'<div class="rail-label">{t(lang, "theme_label")}</div>',
            unsafe_allow_html=True)
theme = sb.radio("theme", options=THEME_CODES,
                 format_func=lambda k: t(lang, "theme_" + k),
                 key="theme", label_visibility="collapsed", horizontal=True)

from theme import inject_theme  # noqa: E402
inject_theme(theme, "rtl" if is_rtl(lang) else "ltr", lang)

with name_slot.container():
    C.sidebar_nameplate(t(lang, "sidebar_name"), t(lang, "sidebar_sub"))

# --- section (I / II) ---
sb.markdown(f'<div class="rail-label">{t(lang, "section_label")}</div>',
            unsafe_allow_html=True)
section = sb.radio("section", options=nav.SECTIONS,
                   format_func=lambda k: t(lang, k + "_title"),
                   key="section", label_visibility="collapsed")

# --- Theory / Practice ---
sb.markdown(f'<div class="rail-label">{t(lang, "mode_label")}</div>',
            unsafe_allow_html=True)
mode = sb.radio("mode", options=MODE_KEYS, format_func=lambda k: t(lang, k),
                key="mode", label_visibility="collapsed")

# --- page navigation (separate state per section+mode) ---
sb.markdown(f'<div class="rail-label">{t(lang, "nav_label")}</div>',
            unsafe_allow_html=True)
if mode == "mode_theory":
    keys = nav.THEORY[section]
    page = sb.radio("page", options=keys, format_func=lambda k: t(lang, k),
                    key=f"{section}_theory_page", label_visibility="collapsed")
else:
    keys = nav.PRACTICE[section]
    page = sb.radio("page", options=keys, format_func=lambda k: t(lang, k),
                    key=f"{section}_practice_page", label_visibility="collapsed")

# --- printable PDF of the current section ---
sb.markdown(f'<div class="rail-label">PDF</div>', unsafe_allow_html=True)
sb.download_button(
    t(lang, "pdf_button"), data=_pdf_bytes(lang, section),
    file_name=f"TrustworthyML_{section}_{lang}.pdf", mime="application/pdf",
    use_container_width=True)

# --- assistant (floating "Ask me" bubble, bottom-right) ---
C.chatbot(BOTPRESS_URL, label=t(lang, "assistant_label"))

# --- masthead (subtitle + colophon vary by section) ---
if section == "sec1":
    subtitle = t(lang, "masthead_subtitle")
    colophon = [t(lang, "colophon_1"), t(lang, "colophon_2"), t(lang, "colophon_3")]
elif section == "sec2":
    subtitle = t(lang, "masthead_subtitle_2")
    colophon = [t(lang, "colophon_1"), t(lang, "colophon_2b"), t(lang, "colophon_3")]
elif section == "sec3":
    subtitle = t(lang, "masthead_subtitle_3")
    colophon = [t(lang, "colophon_1"), t(lang, "colophon_3b"), t(lang, "colophon_3")]
elif section == "sec4":
    subtitle = t(lang, "masthead_subtitle_4")
    colophon = [t(lang, "colophon_1"), t(lang, "colophon_4b"), t(lang, "colophon_3")]
elif section == "sec5":
    subtitle = t(lang, "masthead_subtitle_5")
    colophon = [t(lang, "colophon_1"), t(lang, "colophon_5b"), t(lang, "colophon_3")]
else:
    subtitle = t(lang, "masthead_subtitle_6")
    colophon = [t(lang, "colophon_1"), t(lang, "colophon_6b"), t(lang, "colophon_3")]

C.masthead(
    t(lang, "masthead_eyebrow"), t(lang, "masthead_title"), subtitle, colophon,
    byline=[
        {"label": t(lang, "byline_supervisor"), "name": t(lang, "name_supervisor")},
        {"label": t(lang, "byline_author"), "name": t(lang, "name_author")},
    ],
)

# --- route ---
if mode == "mode_theory":
    THEORY_RENDER[section][page](lang)
else:
    PRACTICE_RENDER[section][page](lang)
