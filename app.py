"""
app.py -- Trustworthy Machine Learning · interactive sandbox.

Layout (per the author's wireframe):
  * a left SIDEBAR "contents rail": Part (Theory/Practice) → Section (I–VI) →
    Page → Download PDF.  It starts expanded on desktop and closed on mobile
    (initial_sidebar_state="auto"); the styled toggle pill reopens it.
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
from modules import pdf_export, quiz

# "auto" keeps the contents rail expanded on desktop but starts it CLOSED on
# phones, so the page content is visible immediately; the styled toggle pill
# (see theme.py) reopens it. "expanded" was covering the whole screen on
# mobile, which made the site feel broken on first load.
st.set_page_config(
    page_title="Trustworthy ML",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="auto",
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

MODE_KEYS = ["mode_theory", "mode_practice", "mode_quiz"]
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
ss.setdefault("theme", "dark")

# Guard against stale widget-state recovery: when the language changes, every
# radio/selectbox whose *formatted* options are translated gets a new widget
# identity, and on the following interaction Streamlit can hand back the old
# option LABEL (a str) instead of the option value. Coerce anything invalid
# back to a safe default BEFORE the widgets are created, or the script
# crashes (e.g. `ss.page_idx >= len(pages)` with page_idx == "The Bias–...").
if ss.lang not in LANG_CODES:
    ss.lang = "en"
if ss.theme not in THEME_CODES:
    ss.theme = "dark"
if ss.mode not in MODE_KEYS:
    ss.mode = "mode_theory"
if ss.section not in nav.SECTIONS:
    ss.section = "sec1"


def _go_section(sec: str, mode: str | None = None):
    """Callback: jump to a section (from a card or the site-map), optionally
    opening it directly in Theory or Practice mode. Setting session_state here
    -- before the sidebar widgets are (re)created on the upcoming rerun -- is
    what makes the sidebar radio pick up the new value instead of overriding
    it back (the classic Streamlit widget-key gotcha)."""
    st.session_state["section"] = sec
    st.session_state["page_idx"] = 0
    st.session_state["overlay"] = None
    if mode is not None:
        st.session_state["mode"] = mode


def _toggle_overlay(name: str):
    st.session_state["overlay"] = None if st.session_state.get("overlay") == name else name


def _set_lang(code: str):
    """Callback for the sidebar language pills: 'lang' is also the top-bar
    selectbox's widget key, and assigning it in a callback (before that widget
    is recreated on the rerun) keeps the two controls in sync."""
    st.session_state["lang"] = code


def _set_page(delta_or_value, absolute=False):
    st.session_state["page_idx"] = delta_or_value if absolute else \
        st.session_state["page_idx"] + delta_or_value


def _go_page(sec: str, mode: str, idx: int):
    """Callback for the site-map leaves: jump straight to one specific page
    (section + Theory/Practice mode + page index) and close the overlay.
    The _prev_* trackers must be updated too, otherwise the sidebar's
    "section/mode changed" guard sees a change and resets page_idx to 0,
    clobbering the page the user actually clicked."""
    st.session_state["section"] = sec
    st.session_state["mode"] = mode
    st.session_state["page_idx"] = idx
    st.session_state["_prev_section"] = sec
    st.session_state["_prev_mode"] = mode
    st.session_state["overlay"] = None


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

# render INSIDE the sidebar (the helper emits via st.markdown; without this
# context it lands as stray text at the top of the main page)
with sb:
    C.sidebar_nameplate(t(lang, "sidebar_name"), t(lang, ss.section + "_title"))
    # language picker: three pills right under the nameplate, mirroring the
    # top-bar selectbox (the active language is the "primary" button)
    with st.container(key="sidebar-lang"):
        st.markdown(f'<div class="rail-label">🌐 {t(lang, "lang_pick")}</div>',
                    unsafe_allow_html=True)
        lcols = st.columns(len(LANGS))
        for lcol, (code, name) in zip(lcols, LANGS):
            with lcol:
                st.button(name, key=f"sblang_{code}", use_container_width=True,
                          type="primary" if code == lang else "secondary",
                          on_click=_set_lang, args=(code,))

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
pages = {"mode_theory": nav.THEORY, "mode_practice": nav.PRACTICE,
         "mode_quiz": nav.QUIZ}[ss.mode][ss.section]
if not isinstance(ss.page_idx, int) or not (0 <= ss.page_idx < len(pages)):
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
#  TOP CONTROL BAR (main panel): 7 uniform controls in one row     #
#  choose-section (opens sidebar) · language · theme · PDF ·       #
#  About · Contact · Site map                                      #
# =============================================================== #
# st.container(key=...) puts a real ``st-key-topbar`` class on the wrapping
# DOM node, so theme.py can style everything inside it reliably (a raw
# ``st.markdown('<div ...>')`` is auto-closed by the browser and never
# actually wraps the widgets that follow it).
with st.container(key="topbar"):
    tb = st.columns(7)
    with tb[0]:
        st.button(t(lang, "open_sections"), key="btn_open_sections",
                  use_container_width=True,
                  on_click=_toggle_overlay, args=("sections",))
    with tb[1]:
        st.button(f"🗺 {t(lang, 'roadmap_label')}", key="btn_map",
                  use_container_width=True,
                  on_click=_toggle_overlay, args=("map",))
    with tb[2]:
        st.button(f"ⓘ {t(lang, 'nav_about')}", key="btn_about",
                  use_container_width=True,
                  on_click=_toggle_overlay, args=("about",))
    with tb[3]:
        st.button(f"✉ {t(lang, 'nav_contact')}", key="btn_contact",
                  use_container_width=True,
                  on_click=_toggle_overlay, args=("contact",))
    with tb[4]:
        st.download_button(
            f"⬇ {t(lang, 'pdf_button')}", data=_pdf_bytes(lang, ss.section),
            file_name=f"TrustworthyML_{ss.section}_{lang}.pdf",
            mime="application/pdf", use_container_width=True, key="pdf_top")
    with tb[5]:
        st.selectbox(t(lang, "lang_label"), LANG_CODES,
                     format_func=lambda c: f"🌐 {NAME_OF[c]}", key="lang",
                     label_visibility="collapsed")
    with tb[6]:
        st.selectbox(t(lang, "theme_label"), THEME_CODES,
                     format_func=lambda k: f"🌓 {t(lang, 'theme_' + k)}",
                     key="theme", label_visibility="collapsed")

# Simple sections-list overlay -- a compact, guaranteed-reliable set of
# section buttons (distinct from the visual tree in the Site-map overlay).
if ss.overlay == "sections":
    with st.container(key="nav-sections"):
        scols = st.columns(3)
        for i, s in enumerate(nav.SECTIONS):
            with scols[i % 3]:
                st.button(f"{SECTION_ICONS.get(s,'◆')} {t(lang, s + '_title')}",
                          key=f"pick_{s}", use_container_width=True,
                          on_click=_go_section, args=(s,))

# Site-map overlay: a glowing interactive tree. The root fans out into six
# branch-cards, one per section, each listing EVERY theory and practice page
# as a real button that jumps straight to that page.
if ss.overlay == "map":
    with st.container(key="sitemap"):
        C.sitemap_head(t(lang, "roadmap_title"), t(lang, "hero_title"))
        for row_start in range(0, len(nav.SECTIONS), 3):
            mcols = st.columns(3)
            for mc, s in zip(mcols, nav.SECTIONS[row_start:row_start + 3]):
                with mc, st.container(key=f"rm-{s}"):
                    st.button(f"{SECTION_ICONS.get(s,'◆')} {t(lang, s + '_title')}",
                              key=f"rmh_{s}", use_container_width=True,
                              on_click=_go_section, args=(s,))
                    C.sitemap_group(t(lang, "choose_theory"))
                    with st.container(key=f"rmt-{s}"):
                        for i, k in enumerate(nav.THEORY[s]):
                            st.button(t(lang, k), key=f"rmt_{s}_{i}",
                                      use_container_width=True,
                                      on_click=_go_page,
                                      args=(s, "mode_theory", i))
                    C.sitemap_group(t(lang, "choose_practice"))
                    with st.container(key=f"rmp-{s}"):
                        for i, k in enumerate(nav.PRACTICE[s]):
                            st.button(t(lang, k), key=f"rmp_{s}_{i}",
                                      use_container_width=True,
                                      on_click=_go_page,
                                      args=(s, "mode_practice", i))
                    with st.container(key=f"rmq-{s}"):
                        st.button(f"{t(lang, 'choose_quiz')} · "
                                  f"{t(lang, 'quiz_page')}",
                                  key=f"rmq_{s}", use_container_width=True,
                                  on_click=_go_page, args=(s, "mode_quiz", 0))
    with st.container(key="nav-map"):
        mcols = st.columns(len(nav.SECTIONS))
        for mc, s in zip(mcols, nav.SECTIONS):
            with mc:
                st.button(f"{SECTION_ICONS.get(s,'◆')} {t(lang, s + '_title')}",
                          key=f"map_{s}", use_container_width=True,
                          on_click=_go_section, args=(s,))

# About / Contact overlay panels
if ss.overlay == "about":
    C.info_panel(t(lang, "about_title"), t(lang, "about_body"))
    C.info_panel(t(lang, "ack_title"), t(lang, "ack_body"))
elif ss.overlay == "contact":
    rows = [
        (t(lang, "contact_author"), t(lang, "name_author")),
        (t(lang, "contact_supervisor"), t(lang, "name_supervisor")),
        (t(lang, "contact_institution"), t(lang, "contact_inst_val")),
        (t(lang, "contact_phone"), t(lang, "contact_phone_val")),
        (t(lang, "contact_apps"), t(lang, "contact_apps_val")),
        (t(lang, "contact_email"), "hani_mahfoud@comp.iust.ac.ir"),
    ]
    links = [
        (t(lang, "contact_whatsapp_btn"), "https://wa.me/989309456655"),
        (t(lang, "contact_email_btn"), "mailto:hani_mahfoud@comp.iust.ac.ir"),
    ]
    C.info_panel(t(lang, "contact_title"), t(lang, "contact_body"),
                 rows=rows, links=links, note=t(lang, "contact_support_note"))


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

# acknowledgment to the supervisor — a book-style dedication under the hero
C.dedication(t(lang, "ack_title"), t(lang, "ack_body"))

# =============================================================== #
#  SECTION CARDS — click a card to jump to that section            #
# =============================================================== #
st.markdown(f'<p class="landing-prompt" style="text-align:center;color:var(--muted);'
            f'font-family:var(--mono);font-size:.82rem;letter-spacing:.04em;'
            f'margin:4px 0 12px 0">{t(lang, "landing_prompt")}</p>',
            unsafe_allow_html=True)
with st.container(key="landing-grid"):
    for row_start in range(0, len(nav.SECTIONS), 3):
        row = nav.SECTIONS[row_start:row_start + 3]
        cols = st.columns(len(row))
        for col, sec in zip(cols, row):
            with col:
                active = "  ●" if sec == ss.section else ""
                # gold medal on sections whose exam has been passed
                badge = "  🏅" if ss.get("qz_best", {}).get(sec, 0) >= quiz.PASS \
                    else ""
                label = (f"{SECTION_ICONS.get(sec,'◆')}  "
                         f"{t(lang, sec + '_title')}{active}{badge}\n\n"
                         f"{t(lang, 'sc_desc_' + sec)}")
                st.button(label, key=f"card_{sec}", use_container_width=True,
                          on_click=_go_section, args=(sec,))
                # mini Theory / Practice / Exam buttons -- jump into a mode
                with st.container(key=f"modes-{sec}"):
                    mc1, mc2, mc3 = st.columns(3)
                    with mc1:
                        st.button(t(lang, "choose_theory"), key=f"card_th_{sec}",
                                  use_container_width=True,
                                  on_click=_go_section, args=(sec, "mode_theory"))
                    with mc2:
                        st.button(t(lang, "choose_practice"), key=f"card_pr_{sec}",
                                  use_container_width=True,
                                  on_click=_go_section,
                                  args=(sec, "mode_practice"))
                    with mc3:
                        st.button(t(lang, "choose_quiz"), key=f"card_qz_{sec}",
                                  use_container_width=True,
                                  on_click=_go_section,
                                  args=(sec, "mode_quiz"))

# =============================================================== #
#  ROUTED CONTENT — per-section masthead + the selected page       #
# =============================================================== #
sub_key, col_key = _MAST[ss.section]
C.masthead(
    t(lang, "masthead_eyebrow"), t(lang, ss.section + "_title"),
    t(lang, sub_key),
    [t(lang, "colophon_1"), t(lang, col_key), t(lang, "colophon_3")],
)

if ss.mode == "mode_quiz":
    quiz.render(lang, ss.section)
elif ss.mode == "mode_theory":
    THEORY_RENDER[ss.section][page](lang)
else:
    PRACTICE_RENDER[ss.section][page](lang)

# --- footer (copyright) ---
C.footer(t(lang, "footer_text"))
