"""
app.py -- Trustworthy Machine Learning · interactive sandbox.

Layout (per the author's wireframe):
  * a left SIDEBAR "contents rail": Part (Theory/Practice) → Section (I–VI) →
    Page → Download PDF.  It starts expanded and is fully usable on mobile
    (a "☰ Menu" hint plus Streamlit's native sidebar toggle).
  * a top CONTROL BAR on the main panel: language · theme · site-map · About ·
    Contact — so those controls are reachable even with the sidebar closed.
  * a framed HERO box: course name + summary + author + supervisor.
  * the six sections as elevated cards with summaries; a card opens that section.
  * Previous / Next controls under the routed content.

All compute lives in core/; all prose in i18n.py; nav keys in nav.py.
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

MODE_KEYS = ["mode_theory", "mode_practice"]
LANG_CODES = [c for c, _ in LANGS]
NAME_OF = dict(LANGS)
THEME_CODES = ["light", "dark"]
SECTION_ICONS = {"sec1": "◷", "sec2": "◉", "sec3": "⚖",
                 "sec4": "⛊", "sec5": "🔒", "sec6": "✦"}

BOTPRESS_URL = (
    "https://cdn.botpress.cloud/webchat/v3.6/shareable.html?configUrl="
    "https://files.bpcontent.cloud/2026/07/01/08/20260701082723-ZJ4IWTNT.json"
)

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
ss.setdefault("section", "sec1")
ss.setdefault("mode", "mode_theory")
ss.setdefault("page_idx", 0)
ss.setdefault("overlay", None)          # None | "about" | "contact" | "map"
ss.setdefault("lang", "en")
ss.setdefault("theme", "light")


def _go_section(sec: str):
    """Callback: jump to a section (from a card or the site-map). Setting
    session_state here -- before the sidebar widgets are (re)created on the
    upcoming rerun -- is what makes the sidebar radio pick up the new value
    instead of overriding it back (the classic Streamlit widget-key gotcha)."""
    st.session_state["section"] = sec
    st.session_state["page_idx"] = 0
    st.session_state["overlay"] = None


def _toggle_overlay(name: str):
    st.session_state["overlay"] = None if st.session_state.get("overlay") == name else name


def _set_page(delta_or_value, absolute=False):
    st.session_state["page_idx"] = delta_or_value if absolute else \
        st.session_state["page_idx"] + delta_or_value


# =============================================================== #
#  SIDEBAR — the contents rail (Part → Section → Page)             #
#  Opens on mobile via Streamlit's native ›› arrow (styled below); #
#  language/theme/PDF/About/Contact/Site-map live in the top bar.  #
# =============================================================== #
sb = st.sidebar
lang = ss.lang
theme = ss.theme

from theme import inject_theme  # noqa: E402
inject_theme(theme, "rtl" if is_rtl(lang) else "ltr", lang)

C.sidebar_nameplate(t(lang, "sidebar_name"), t(lang, "sidebar_sub"))

# track previous section/mode to know when to reset the page index
_prev_section = ss.get("_prev_section", ss.section)
_prev_mode = ss.get("_prev_mode", ss.mode)

# Part: Theory / Practice -- widget key == "mode", so it IS ss.mode: no
# separate tracking variable is needed and no stale-override bug can occur.
sb.markdown(f'<div class="rail-label">{t(lang, "mode_label")}</div>',
            unsafe_allow_html=True)
sb.radio("mode", MODE_KEYS, format_func=lambda k: t(lang, k),
         key="mode", label_visibility="collapsed")

# Section: I – VI -- widget key == "section", so it IS ss.section.
sb.markdown(f'<div class="rail-label">{t(lang, "section_label")}</div>',
            unsafe_allow_html=True)
sb.radio("section", nav.SECTIONS, format_func=lambda k: t(lang, k + "_title"),
         key="section", label_visibility="collapsed")

# if the user changed section/mode via the sidebar itself, reset the page
if ss.section != _prev_section or ss.mode != _prev_mode:
    ss.page_idx = 0
ss["_prev_section"] = ss.section
ss["_prev_mode"] = ss.mode

# Page menu (per section + mode) -- widget key == "page_idx", so it IS
# ss.page_idx; clip it to range *before* creating the widget.
pages = nav.THEORY[ss.section] if ss.mode == "mode_theory" \
    else nav.PRACTICE[ss.section]
if ss.page_idx >= len(pages):
    ss.page_idx = 0
sb.markdown(f'<div class="rail-label">{t(lang, "nav_label")}</div>',
            unsafe_allow_html=True)
labels = [t(lang, k) for k in pages]
sb.radio("page", list(range(len(pages))), format_func=lambda i: labels[i],
         key="page_idx", label_visibility="collapsed")

page = pages[ss.page_idx]

# floating assistant
C.chatbot(BOTPRESS_URL, label=t(lang, "assistant_label"))


# =============================================================== #
#  TOP CONTROL BAR (main panel): 6 uniform controls in one row     #
#  language · theme · PDF · About · Contact · Site map             #
# =============================================================== #
st.markdown(
    f'<div class="topbar-hint">👉 {t(lang, "open_sections")}</div>',
    unsafe_allow_html=True)

st.markdown('<div class="topbar-row">', unsafe_allow_html=True)
tb = st.columns(6)
with tb[0]:
    st.selectbox(f"🌐 {t(lang, 'lang_label')}", LANG_CODES,
                 format_func=lambda c: NAME_OF[c], key="lang")
with tb[1]:
    st.selectbox(f"🌓 {t(lang, 'theme_label')}", THEME_CODES,
                 format_func=lambda k: t(lang, "theme_" + k), key="theme")
with tb[2]:
    st.download_button(
        f"⬇ {t(lang, 'pdf_button')}", data=_pdf_bytes(lang, ss.section),
        file_name=f"TrustworthyML_{ss.section}_{lang}.pdf", mime="application/pdf",
        use_container_width=True, key="pdf_top")
with tb[3]:
    st.button(f"ⓘ {t(lang, 'nav_about')}", key="btn_about",
              use_container_width=True, on_click=_toggle_overlay, args=("about",))
with tb[4]:
    st.button(f"✉ {t(lang, 'nav_contact')}", key="btn_contact",
              use_container_width=True, on_click=_toggle_overlay, args=("contact",))
with tb[5]:
    st.button(f"🗺 {t(lang, 'roadmap_label')}", key="btn_map",
              use_container_width=True, on_click=_toggle_overlay, args=("map",))
st.markdown('</div>', unsafe_allow_html=True)

# Site-map overlay (large, clear, clickable navigation)
if ss.overlay == "map":
    meta = [{"title": t(lang, s + "_title"),
             "n_theory": len(nav.THEORY[s]), "n_practice": len(nav.PRACTICE[s]),
             "leaves": [t(lang, k) for k in nav.THEORY[s][:3]]}
            for s in nav.SECTIONS]
    C.roadmap_tree(t(lang, "hero_title"), meta, is_rtl(lang))
    st.markdown('<div class="nav-row">', unsafe_allow_html=True)
    mcols = st.columns(len(nav.SECTIONS))
    for mc, s in zip(mcols, nav.SECTIONS):
        with mc:
            st.button(f"{SECTION_ICONS.get(s,'◆')} {t(lang, s + '_title')}",
                      key=f"map_{s}", use_container_width=True,
                      on_click=_go_section, args=(s,))
    st.markdown('</div>', unsafe_allow_html=True)

# About / Contact overlay panels
if ss.overlay == "about":
    C.info_panel(t(lang, "about_title"), t(lang, "about_body"))
elif ss.overlay == "contact":
    rows = [
        (t(lang, "contact_author"), t(lang, "name_author")),
        (t(lang, "contact_supervisor"), t(lang, "name_supervisor")),
        (t(lang, "contact_institution"), t(lang, "contact_inst_val")),
    ]
    C.info_panel(t(lang, "contact_title"), t(lang, "contact_body"), rows=rows)


# =============================================================== #
#  HERO BOX — course name + summary + author + supervisor          #
# =============================================================== #
C.hero(
    t(lang, "masthead_eyebrow"), t(lang, "hero_title"), t(lang, "hero_summary"),
    practice_note=t(lang, "hero_practice_note"),
    byline=[
        {"label": t(lang, "byline_supervisor"), "name": t(lang, "name_supervisor")},
        {"label": t(lang, "byline_author"), "name": t(lang, "name_author")},
    ],
)

# =============================================================== #
#  SECTION CARDS — click a card to jump to that section            #
# =============================================================== #
st.markdown(f'<p class="landing-prompt" style="text-align:center;color:var(--muted);'
            f'font-family:var(--mono);font-size:.82rem;letter-spacing:.04em;'
            f'margin:4px 0 12px 0">{t(lang, "landing_prompt")}</p>',
            unsafe_allow_html=True)
st.markdown('<div class="landing-grid">', unsafe_allow_html=True)
for row_start in range(0, len(nav.SECTIONS), 3):
    row = nav.SECTIONS[row_start:row_start + 3]
    cols = st.columns(len(row))
    for col, sec in zip(cols, row):
        with col:
            active = "  ●" if sec == ss.section else ""
            label = (f"{SECTION_ICONS.get(sec,'◆')}  {t(lang, sec + '_title')}{active}\n\n"
                     f"{t(lang, 'sc_desc_' + sec)}")
            st.button(label, key=f"card_{sec}", use_container_width=True,
                      on_click=_go_section, args=(sec,))
st.markdown('</div>', unsafe_allow_html=True)

# =============================================================== #
#  ROUTED CONTENT — per-section masthead + the selected page       #
# =============================================================== #
sub_key, col_key = _MAST[ss.section]
C.masthead(
    t(lang, "masthead_eyebrow"), t(lang, ss.section + "_title"),
    t(lang, sub_key),
    [t(lang, "colophon_1"), t(lang, col_key), t(lang, "colophon_3")],
)

if ss.mode == "mode_theory":
    THEORY_RENDER[ss.section][page](lang)
else:
    PRACTICE_RENDER[ss.section][page](lang)

# --- footer (copyright) ---
C.footer(t(lang, "footer_text"))
