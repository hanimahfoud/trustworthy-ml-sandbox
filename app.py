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
ss.setdefault("overlay", None)          # None | "about" | "contact"


# =============================================================== #
#  SIDEBAR — the contents rail (Part → Section → Page → PDF)       #
# =============================================================== #
sb = st.sidebar

# language first, so we can fix text direction before theming
prelim = ss.get("lang", "en")
sb.markdown(f'<div class="rail-label">{t(prelim, "lang_label")}</div>',
            unsafe_allow_html=True)
lang = sb.radio("language", LANG_CODES, format_func=lambda c: NAME_OF[c],
                index=LANG_CODES.index(prelim) if prelim in LANG_CODES else 0,
                key="lang", label_visibility="collapsed")

sb.markdown(f'<div class="rail-label">{t(lang, "theme_label")}</div>',
            unsafe_allow_html=True)
theme = sb.radio("theme", THEME_CODES, format_func=lambda k: t(lang, "theme_" + k),
                 key="theme", label_visibility="collapsed", horizontal=True)

from theme import inject_theme  # noqa: E402
inject_theme(theme, "rtl" if is_rtl(lang) else "ltr", lang)

C.sidebar_nameplate(t(lang, "sidebar_name"), t(lang, "sidebar_sub"))

# Part: Theory / Practice
sb.markdown(f'<div class="rail-label">{t(lang, "mode_label")}</div>',
            unsafe_allow_html=True)
mode = sb.radio("mode", MODE_KEYS, format_func=lambda k: t(lang, k),
                index=MODE_KEYS.index(ss.mode), key="mode",
                label_visibility="collapsed")
if mode != ss.mode:
    ss.mode = mode
    ss.page_idx = 0

# Section: I – VI
sb.markdown(f'<div class="rail-label">{t(lang, "section_label")}</div>',
            unsafe_allow_html=True)
section = sb.radio("section", nav.SECTIONS,
                   format_func=lambda k: t(lang, k + "_title"),
                   index=nav.SECTIONS.index(ss.section), key="section_radio",
                   label_visibility="collapsed")
if section != ss.section:
    ss.section = section
    ss.page_idx = 0

# Page menu (per section + mode)
pages = nav.THEORY[ss.section] if ss.mode == "mode_theory" \
    else nav.PRACTICE[ss.section]
if ss.page_idx >= len(pages):
    ss.page_idx = 0
sb.markdown(f'<div class="rail-label">{t(lang, "nav_label")}</div>',
            unsafe_allow_html=True)
labels = [t(lang, k) for k in pages]
sel = sb.radio("page", list(range(len(pages))), index=ss.page_idx,
               format_func=lambda i: labels[i], key="page_radio",
               label_visibility="collapsed")
if sel != ss.page_idx:
    ss.page_idx = sel

# Download PDF
sb.markdown('<div class="rail-label">PDF</div>', unsafe_allow_html=True)
sb.download_button(
    t(lang, "pdf_button"), data=_pdf_bytes(lang, ss.section),
    file_name=f"TrustworthyML_{ss.section}_{lang}.pdf", mime="application/pdf",
    use_container_width=True)

page = pages[ss.page_idx]

# floating assistant
C.chatbot(BOTPRESS_URL, label=t(lang, "assistant_label"))


# =============================================================== #
#  TOP CONTROL BAR (main panel): mobile hint · site-map · About    #
# =============================================================== #
st.markdown(
    f'<div class="topbar-hint">☰ {t(lang, "nav_menu")}</div>',
    unsafe_allow_html=True)

tb = st.columns([1.4, 1.4, 1.4, 3])
with tb[0]:
    show_map = st.toggle(t(lang, "roadmap_label"), value=False, key="show_roadmap")
with tb[1]:
    if st.button(t(lang, "nav_about"), key="btn_about", use_container_width=True):
        ss.overlay = None if ss.overlay == "about" else "about"; st.rerun()
with tb[2]:
    if st.button(t(lang, "nav_contact"), key="btn_contact", use_container_width=True):
        ss.overlay = None if ss.overlay == "contact" else "contact"; st.rerun()

# optional site-map tree
if show_map:
    meta = [{"title": t(lang, s + "_title"),
             "n_theory": len(nav.THEORY[s]), "n_practice": len(nav.PRACTICE[s]),
             "leaves": [t(lang, k) for k in nav.THEORY[s][:2]]}
            for s in nav.SECTIONS]
    C.roadmap_tree(t(lang, "hero_title"), meta, is_rtl(lang))

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
            if st.button(label, key=f"card_{sec}", use_container_width=True):
                ss.section = sec
                ss.page_idx = 0
                ss.overlay = None
                st.rerun()
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

# --- Previous / Next under the content ---
st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
st.markdown('<div class="nav-row">', unsafe_allow_html=True)
nrow = st.columns([1.5, 3, 1.5])
with nrow[0]:
    if st.button(t(lang, "nav_prev"), key="btn_prev", use_container_width=True,
                 disabled=(ss.page_idx == 0)):
        ss.page_idx = max(0, ss.page_idx - 1); st.rerun()
with nrow[2]:
    if st.button(t(lang, "nav_next"), key="btn_next", use_container_width=True,
                 disabled=(ss.page_idx >= len(pages) - 1)):
        ss.page_idx = min(len(pages) - 1, ss.page_idx + 1); st.rerun()
st.markdown('</div>', unsafe_allow_html=True)
