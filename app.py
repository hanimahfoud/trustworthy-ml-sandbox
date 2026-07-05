"""
app.py -- Trustworthy Machine Learning · interactive sandbox.

State-based, mobile-first navigation:
  * a LANDING view with a hero band and a grid of clickable section cards;
  * clicking a card opens a "choose view" prompt (Theory / Practice);
  * a SECTION view routes to the selected theory plate or interactive demo,
    with Home / Previous / Next controls and a per-section page menu.

Navigation lives in st.session_state (works seamlessly on mobile, where the
sidebar is awkward). All compute lives in core/; all prose in i18n.py; nav keys
in nav.py. The top of the main panel carries a compact control bar (language,
theme, menu, site-map) so the app is fully usable without opening the sidebar.
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
    initial_sidebar_state="collapsed",
)

# --- render registries, per section ---------------------------------------- #
THEORY_RENDER = {"sec1": theory.SECTIONS, "sec2": theory_xai.SECTIONS_XAI,
                 "sec3": theory_fair.SECTIONS_FAIR,
                 "sec4": theory_robust.SECTIONS_ROBUST,
                 "sec5": theory_privacy.SECTIONS_PRIVACY,
                 "sec6": theory_align.SECTIONS_ALIGN}
PRACTICE_RENDER = {
    "sec1": {"pr_bv": bias_variance.render, "pr_dann": domain_adaptation.render,
             "pr_sam": sam_optimizer.render, "pr_simpson": simpsons_paradox.render,
             "pr_cf": counterfactual.render},
    "sec2": {"px_loan": xai_loan.render, "px_recourse": recourse_xai.render,
             "px_cv": cv_scanner.render, "px_spurious": spurious.render},
    "sec3": {"pf_scales": fair_scales.render, "pf_cda": fair_cda.render,
             "pf_multiturn": fair_multiturn.render,
             "pf_constitution": fair_constitution.render},
    "sec4": {"prb_evasion": rob_evasion.render, "prb_tradeoff": rob_tradeoff.render,
             "prb_smoothing": rob_smoothing.render,
             "prb_jailbreak": rob_jailbreak.render},
    "sec5": {"pp_backdoor": pp_backdoor.render, "pp_coin": pp_coin.render,
             "pp_laplace": pp_laplace.render, "pp_leak": pp_leak.render},
    "sec6": {"pa_hacking": pa_hacking.render, "pa_grpo": pa_grpo.render,
             "pa_jailbreak": pa_jailbreak.render, "pa_agency": pa_agency.render},
}

LANG_CODES = [c for c, _ in LANGS]
NAME_OF = dict(LANGS)
THEME_CODES = ["light", "dark"]
SECTION_ICONS = {"sec1": "◷", "sec2": "◉", "sec3": "⚖",
                 "sec4": "⛊", "sec5": "🔒", "sec6": "✦"}

BOTPRESS_URL = (
    "https://cdn.botpress.cloud/webchat/v3.6/shareable.html?configUrl="
    "https://files.bpcontent.cloud/2026/07/01/08/20260701082723-ZJ4IWTNT.json"
)

# --- masthead subtitle / colophon per section (kept from the journal design) - #
_MAST = {
    "sec1": ("masthead_subtitle", "colophon_2"),
    "sec2": ("masthead_subtitle_2", "colophon_2b"),
    "sec3": ("masthead_subtitle_3", "colophon_3b"),
    "sec4": ("masthead_subtitle_4", "colophon_4b"),
    "sec5": ("masthead_subtitle_5", "colophon_5b"),
    "sec6": ("masthead_subtitle_6", "colophon_6b"),
}


@st.cache_data(show_spinner=False)
def _pdf_bytes(lang: str, section: str) -> bytes:
    return pdf_export.build_pdf(lang, section)


# --- navigation state -------------------------------------------------------- #
ss = st.session_state
ss.setdefault("view", "landing")     # "landing" | "section"
ss.setdefault("section", "sec1")
ss.setdefault("mode", "mode_theory")
ss.setdefault("page_idx", 0)
ss.setdefault("lang", "en")
ss.setdefault("theme", "light")


def go_landing():
    ss.view = "landing"


def open_section(sec: str, mode: str):
    ss.section, ss.mode, ss.page_idx, ss.view = sec, mode, 0, "section"


def _pages(sec: str, mode: str):
    return nav.THEORY[sec] if mode == "mode_theory" else nav.PRACTICE[sec]


# =============================================================== #
#  TOP CONTROL BAR (language + theme + menu + site-map)            #
#  Rendered on the main panel so the app works without the sidebar #
# =============================================================== #
lang = ss.lang
# three compact columns: language | theme | site-map toggle
cbar = st.columns([2, 2, 2])
with cbar[0]:
    lang = st.selectbox(t(lang, "lang_label"), LANG_CODES,
                        index=LANG_CODES.index(ss.lang) if ss.lang in LANG_CODES else 0,
                        format_func=lambda c: NAME_OF[c], key="lang")
with cbar[1]:
    theme = st.selectbox(t(lang, "theme_label"), THEME_CODES,
                         index=THEME_CODES.index(ss.theme) if ss.theme in THEME_CODES else 0,
                         format_func=lambda k: t(lang, "theme_" + k), key="theme")
with cbar[2]:
    show_map = st.toggle(t(lang, "roadmap_label"), value=False, key="show_roadmap")

from theme import inject_theme  # noqa: E402
inject_theme(theme, "rtl" if is_rtl(lang) else "ltr", lang)

# floating assistant (bottom-right)
C.chatbot(BOTPRESS_URL, label=t(lang, "assistant_label"))

# optional site-map tree (toggled, not always open)
if show_map:
    sections_meta = []
    for sec in nav.SECTIONS:
        leaves = [t(lang, k) for k in nav.THEORY[sec][:2]]
        sections_meta.append({
            "title": t(lang, sec + "_title"),
            "n_theory": len(nav.THEORY[sec]),
            "n_practice": len(nav.PRACTICE[sec]),
            "leaves": leaves,
        })
    C.roadmap_tree(t(lang, "hero_title"), sections_meta, is_rtl(lang))


# =============================================================== #
#  LANDING VIEW  —  hero + clickable section cards                 #
# =============================================================== #
def render_landing():
    C.hero(
        t(lang, "masthead_eyebrow"), t(lang, "hero_title"), t(lang, "hero_summary"),
        byline=[
            {"label": t(lang, "byline_supervisor"), "name": t(lang, "name_supervisor")},
            {"label": t(lang, "byline_author"), "name": t(lang, "name_author")},
        ],
    )
    st.markdown(f'<p class="landing-prompt" style="text-align:center;color:var(--muted);'
                f'font-family:var(--mono);font-size:.82rem;letter-spacing:.04em;'
                f'margin:6px 0 14px 0">{t(lang, "landing_prompt")}</p>',
                unsafe_allow_html=True)

    # clickable cards in a 3-column grid (buttons styled as cards via CSS)
    st.markdown('<div class="landing-grid">', unsafe_allow_html=True)
    rows = [nav.SECTIONS[i:i + 3] for i in range(0, len(nav.SECTIONS), 3)]
    for row in rows:
        cols = st.columns(len(row))
        for col, sec in zip(cols, row):
            with col:
                label = (f"{SECTION_ICONS.get(sec,'◆')}  {t(lang, sec + '_title')}\n\n"
                         f"{t(lang, 'sc_desc_' + sec)}")
                if st.button(label, key=f"card_{sec}", use_container_width=True):
                    open_section(sec, "mode_theory")
                    st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# =============================================================== #
#  SECTION VIEW  —  nav controls + page menu + routed content      #
# =============================================================== #
def render_section():
    sec = ss.section
    pages = _pages(sec, ss.mode)
    if ss.page_idx >= len(pages):
        ss.page_idx = 0
    page = pages[ss.page_idx]

    # -- control row: Home | Theory/Practice choice | (page select) --
    st.markdown('<div class="nav-row">', unsafe_allow_html=True)
    top = st.columns([1.2, 1, 1, 3])
    with top[0]:
        if st.button(t(lang, "nav_home"), key="btn_home", use_container_width=True):
            go_landing(); st.rerun()
    with top[1]:
        if st.button(t(lang, "choose_theory"), key="btn_theory",
                     use_container_width=True):
            ss.mode, ss.page_idx = "mode_theory", 0; st.rerun()
    with top[2]:
        if st.button(t(lang, "choose_practice"), key="btn_practice",
                     use_container_width=True):
            ss.mode, ss.page_idx = "mode_practice", 0; st.rerun()
    with top[3]:
        # page menu for the current section+mode
        labels = [t(lang, k) for k in pages]
        sel = st.selectbox(t(lang, "nav_label"), list(range(len(pages))),
                           index=ss.page_idx, format_func=lambda i: labels[i],
                           key=f"pagesel_{sec}_{ss.mode}")
        if sel != ss.page_idx:
            ss.page_idx = sel; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # -- per-section masthead --
    sub_key, col_key = _MAST[sec]
    C.masthead(
        t(lang, "masthead_eyebrow"), t(lang, sec + "_title"),
        t(lang, sub_key),
        [t(lang, "colophon_1"), t(lang, col_key), t(lang, "colophon_3")],
    )

    # -- routed content --
    if ss.mode == "mode_theory":
        THEORY_RENDER[sec][page](lang)
    else:
        PRACTICE_RENDER[sec][page](lang)

    # -- Previous / PDF / Next --
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    st.markdown('<div class="nav-row">', unsafe_allow_html=True)
    bot = st.columns([1.5, 3, 1.5])
    with bot[0]:
        if st.button(t(lang, "nav_prev"), key="btn_prev", use_container_width=True,
                     disabled=(ss.page_idx == 0)):
            ss.page_idx = max(0, ss.page_idx - 1); st.rerun()
    with bot[1]:
        st.download_button(
            t(lang, "pdf_button"), data=_pdf_bytes(lang, sec),
            file_name=f"TrustworthyML_{sec}_{lang}.pdf", mime="application/pdf",
            use_container_width=True)
    with bot[2]:
        if st.button(t(lang, "nav_next"), key="btn_next", use_container_width=True,
                     disabled=(ss.page_idx >= len(pages) - 1)):
            ss.page_idx = min(len(pages) - 1, ss.page_idx + 1); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# --- route by view ---
if ss.view == "landing":
    render_landing()
else:
    render_section()
