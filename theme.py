"""
theme.py -- visual identity for the Trustworthy ML sandbox.

``inject_theme(theme, direction, lang)`` writes the CSS that turns the default
Streamlit page into a scholarly monograph. Three palettes are supported --
``light`` (navy on parchment), ``dark`` (light on charcoal-navy) and
``colored`` (a teal-forward cream journal) -- selected at runtime. The entire
stylesheet is driven by CSS custom properties, so switching theme only swaps
the ``:root`` variable block; every selector below is theme-agnostic.

Latin script uses Playfair Display / Merriweather with IBM Plex Mono for
numerals; Arabic uses Cairo and Persian uses Vazirmatn. Right-to-left layout is
applied for Arabic and Persian. Plotly figures are deliberately kept on light
"figure plates" in every theme (printed-figure convention) for legibility.
"""
from __future__ import annotations

import streamlit as st

# --------------------------------------------------------------------------- #
# Palettes: semantic variables, three themes.                                 #
# --------------------------------------------------------------------------- #
LIGHT = {
    "page": "#F4F2EC", "surface": "#FFFFFF", "surface2": "#FAF8F3",
    "sidebar": "#FCFBF7",
    "text": "#0C2340", "text_body": "#1C2B3A", "muted": "#5E6E7E",
    "border": "#E2DDD1",
    "accent": "#8A1C2B", "good": "#0F6E66", "gold": "#A8842C",
    "masthead": "#0A1F38", "mast_title": "#FBF9F3", "mast_sub": "#C7D0DA",
    "mast_eyebrow": "#C9B98B", "mast_colophon": "#9FB0C0", "mast_rule": "#A8842C",
    "keyidea_bg": "#F0F5F4", "keyidea_text": "#123531",
    "warn_bg": "#F9F1F1", "warn_text": "#4A1820",
    "btn": "#FFFFFF", "btn_hover": "#F7F4EE",
    "link_border": "rgba(15,110,102,.35)",
}

DARK = {
    "page": "#0F1720", "surface": "#18222E", "surface2": "#1E2A38",
    "sidebar": "#131C26",
    "text": "#E9ECF1", "text_body": "#C7CFD8", "muted": "#8C9AA8",
    "border": "#2A3745",
    "accent": "#D2586B", "good": "#35A99C", "gold": "#C9A24A",
    "masthead": "#0A121B", "mast_title": "#F3F1EA", "mast_sub": "#B7C2CE",
    "mast_eyebrow": "#C9A24A", "mast_colophon": "#7E8C9A", "mast_rule": "#C9A24A",
    "keyidea_bg": "#10241E", "keyidea_text": "#B9E2D9",
    "warn_bg": "#2A1418", "warn_text": "#EBB7BE",
    "btn": "#18222E", "btn_hover": "#22303F",
    "link_border": "rgba(53,169,156,.4)",
}

COLORED = {
    "page": "#F4F0E6", "surface": "#FFFFFF", "surface2": "#F6F1E4",
    "sidebar": "#F0EADB",
    "text": "#10302B", "text_body": "#24403B", "muted": "#5E6E68",
    "border": "#D8CFBB",
    "accent": "#A6321F", "good": "#0F6E66", "gold": "#B8862B",
    "masthead": "#0C3B37", "mast_title": "#F6F2E7", "mast_sub": "#CADAD5",
    "mast_eyebrow": "#E0C57A", "mast_colophon": "#9FB8B2", "mast_rule": "#E0C57A",
    "keyidea_bg": "#ECF3F0", "keyidea_text": "#123A33",
    "warn_bg": "#F7EEE9", "warn_text": "#52251A",
    "btn": "#FFFFFF", "btn_hover": "#F6F1E4",
    "link_border": "rgba(15,110,102,.35)",
}

PALETTES = {"light": LIGHT, "dark": DARK, "colored": COLORED}

_FONTS = (
    "@import url('https://fonts.googleapis.com/css2?"
    "family=Playfair+Display:wght@500;600;700;800&"
    "family=Merriweather:ital,wght@0,300;0,400;0,700;1,400&"
    "family=IBM+Plex+Mono:wght@400;500;600&"
    "family=Cairo:wght@400;600;700&"
    "family=Vazirmatn:wght@300;400;500;600;700&display=swap');"
)


def _root(theme: str, lang: str) -> str:
    p = PALETTES.get(theme, LIGHT)
    # Arabic uses Cairo; Persian uses Vazirmatn (covers پ چ ژ گ ک ی).
    if lang == "ar":
        rtl_body = "'Cairo', 'Segoe UI', Tahoma, sans-serif"
        rtl_display = "'Cairo', 'Segoe UI', Tahoma, sans-serif"
    else:  # fa
        rtl_body = "'Vazirmatn', 'Segoe UI', Tahoma, sans-serif"
        rtl_display = "'Vazirmatn', 'Segoe UI', Tahoma, sans-serif"
    vars_ = "".join(f"--{k.replace('_','-')}: {v};" for k, v in p.items())
    return (
        ":root {"
        + vars_
        + "--serif: 'Merriweather', Georgia, 'Times New Roman', serif;"
        + "--display: 'Playfair Display', Georgia, serif;"
        + "--mono: 'IBM Plex Mono', 'SFMono-Regular', Menlo, monospace;"
        + f"--rtl-body: {rtl_body}; --rtl-display: {rtl_display};"
        + "}"
    )


def _base_css() -> str:
    return """
/* ---- Page ground ---- */
[data-testid="stAppViewContainer"] { background: var(--page); }
/* NOTE: stHeader must stay in the DOM (not display:none) because Streamlit's
   native sidebar-open control lives inside it on mobile; hiding the header
   entirely was hiding that control too, which is why the sidebar could not
   be reopened on phones. We blend the header visually instead of removing
   it, and make the toggle itself impossible to miss. */
[data-testid="stHeader"] {
  background: transparent !important; box-shadow: none !important;
  height: 2.6rem !important; min-height: 2.6rem !important;
}
/* Hide Streamlit chrome — but NOT the whole stToolbar: on current Streamlit
   the sidebar-open button ("stExpandSidebarButton") lives INSIDE the toolbar,
   and display:none on it made the sidebar impossible to reopen on mobile.
   Hide only the toolbar's own widgets instead. */
#MainMenu, footer, [data-testid="stDecoration"],
[data-testid="stToolbarActions"], [data-testid="stMainMenu"],
[data-testid="stAppDeployButton"], [data-testid="stStatusWidget"] {
  display: none !important;
}
[data-testid="stToolbar"] { background: transparent !important; }
/* The sidebar-open button inside the toolbar, as the same unmissable pill
   (with the same radiating beacon as the legacy control above) */
[data-testid="stExpandSidebarButton"] {
  display: inline-flex !important; visibility: visible !important; opacity: 1 !important;
  background: var(--accent) !important; color: #fff !important;
  border: none !important; border-radius: 10px !important;
  padding: 6px !important; box-shadow: 0 6px 18px rgba(0,0,0,.28);
  animation: beacon-ring 2.2s ease-out infinite;
}
[data-testid="stExpandSidebarButton"] svg {
  fill: #fff !important; color: #fff !important;
  width: 22px !important; height: 22px !important;
}
/* The native sidebar-open arrow, styled as an unmissable pill button.
   Streamlit renamed the test-id from "collapsedControl" to
   "stSidebarCollapsedControl" in newer releases — target BOTH, otherwise the
   toggle is invisible on phones and the sidebar can never be reopened. */
[data-testid="stSidebarCollapsedControl"], [data-testid="collapsedControl"] {
  display: flex !important; visibility: visible !important; opacity: 1 !important;
  background: var(--accent) !important; border-radius: 10px !important;
  /* box-shadow deliberately NOT !important: the beacon animation animates it,
     and animated keyframes cannot override an !important declaration */
  box-shadow: 0 6px 18px rgba(0,0,0,.28); z-index: 999999 !important;
  padding: 4px !important; margin-top: 4px !important;
  animation: beacon-ring 2.2s ease-out infinite;
}
/* Radiating "look here" beacon on the sidebar-open pill: an expanding ring +
   a gentle pulse, so nobody misses that the contents rail can be opened.
   (Globally disabled for prefers-reduced-motion further down.) */
@keyframes beacon-ring {
  0%   { box-shadow: 0 6px 18px rgba(0,0,0,.28), 0 0 0 0 rgba(217,83,105,.60); }
  60%  { box-shadow: 0 6px 18px rgba(0,0,0,.28), 0 0 0 13px rgba(217,83,105,0); }
  100% { box-shadow: 0 6px 18px rgba(0,0,0,.28), 0 0 0 0 rgba(217,83,105,0); }
}
[data-testid="stSidebarCollapsedControl"] button,
[data-testid="collapsedControl"] button {
  background: transparent !important; border: none !important; color: #fff !important;
}
[data-testid="stSidebarCollapsedControl"] svg, [data-testid="collapsedControl"] svg {
  fill: #fff !important; color: #fff !important;
  width: 22px !important; height: 22px !important;
}
/* The close («) control INSIDE the open sidebar: Streamlit only reveals it on
   hover, which does not exist on touch screens — keep it always visible so
   the drawer can be closed on mobile. */
[data-testid="stSidebarCollapseButton"] {
  display: flex !important; visibility: visible !important; opacity: 1 !important;
}
[data-testid="stSidebarCollapseButton"] button {
  background: var(--surface2) !important; border: 1px solid var(--border) !important;
  border-radius: 8px !important;
}
[data-testid="stSidebarCollapseButton"] svg { color: var(--text) !important; fill: var(--text) !important; }
.block-container, [data-testid="block-container"] {
  padding-top: 1rem; padding-bottom: 4rem; max-width: 1180px;
}

/* ---- Typography ---- */
html, body, [data-testid="stAppViewContainer"], .stMarkdown, p, li, span, div {
  color: var(--text); font-family: var(--serif);
}
[data-testid="stMarkdownContainer"] p {
  font-size: 1.04rem; line-height: 1.72; color: var(--text-body);
}
h1, h2, h3, h4 { font-family: var(--display); color: var(--text); letter-spacing: .2px; }
h1 { font-weight: 800; }
/* a hairline under second-level headings — classic journal typography */
h2 { font-weight: 700; font-size: 1.6rem; margin-top: .2rem;
     border-bottom: 1px solid var(--border); padding-bottom: .3rem; }
h3 { font-weight: 600; font-size: 1.24rem; }
a { color: var(--good); text-decoration: none; border-bottom: 1px solid var(--link-border); }
.measure { max-width: 760px; }

/* ---- Masthead / nameplate ---- */
.masthead {
  background: var(--masthead); color: var(--mast-title);
  border-radius: 10px; padding: 26px 32px 20px 32px; margin-bottom: 28px;
  box-shadow: 0 10px 30px rgba(10,31,56,.16); position: relative; overflow: hidden;
}
.masthead::before {
  content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 4px;
  background: linear-gradient(90deg, var(--mast-rule), var(--accent));
}
.masthead .eyebrow {
  font-family: var(--mono); font-size: .72rem; letter-spacing: .28em;
  text-transform: uppercase; color: var(--mast-eyebrow);
}
.masthead .title {
  font-family: var(--display); font-weight: 800; font-size: 2.15rem;
  line-height: 1.1; margin: 6px 0 8px 0; color: var(--mast-title);
}
.masthead .subtitle {
  font-family: var(--serif); font-style: italic; color: var(--mast-sub);
  font-size: 1.02rem; max-width: 720px;
}
.masthead .byline {
  font-family: var(--mono); font-size: .74rem; letter-spacing: .04em;
  color: var(--mast-sub); margin-top: 10px; display: flex; gap: 22px; flex-wrap: wrap;
}
.masthead .byline b { color: var(--mast-title); font-weight: 600; }
.masthead .byline .lab {
  color: var(--mast-eyebrow); text-transform: uppercase; letter-spacing: .14em;
  font-size: .64rem; margin-right: 6px;
}
.masthead .rule { border: none; border-top: 2px solid var(--mast-rule); margin: 14px 0 8px 0; opacity: .85; }
.masthead .rule-thin { border: none; border-top: 1px solid var(--mast-colophon); opacity: .5; margin: 0 0 12px 0; }
.masthead .colophon {
  font-family: var(--mono); font-size: .72rem; letter-spacing: .12em;
  color: var(--mast-colophon); display: flex; gap: 26px; flex-wrap: wrap;
}

/* ---- Theorem plates ---- */
[data-testid="stVerticalBlockBorderWrapper"] {
  background: var(--surface); border: 1px solid var(--border) !important;
  border-left: 3px solid var(--accent) !important; border-radius: 8px;
  box-shadow: 0 6px 22px rgba(12,35,64,.07); padding: 8px 6px;
  transition: box-shadow .2s ease;
}
[data-testid="stVerticalBlockBorderWrapper"]:hover {
  box-shadow: 0 10px 30px rgba(12,35,64,.10);
}
.plate-eyebrow {
  font-family: var(--mono); font-size: .70rem; letter-spacing: .22em;
  text-transform: uppercase; color: var(--muted); margin-bottom: 2px;
}
.plate-title {
  font-family: var(--display); font-weight: 700; font-size: 1.32rem;
  color: var(--text); margin: 0 0 .35rem 0;
}
.figure-caption {
  font-family: var(--mono); font-size: .76rem; color: var(--muted);
  letter-spacing: .04em; margin-top: 6px; border-top: 1px solid var(--border); padding-top: 6px;
}
.figure-caption b { color: var(--text); }

/* ---- Instrument readouts ---- */
.readout-strip { display: flex; flex-wrap: wrap; gap: 14px; margin: 6px 0 2px 0; }
.readout { flex: 1 1 140px; background: var(--surface2); border: 1px solid var(--border); border-radius: 4px; padding: 10px 12px; }
.readout .k { font-family: var(--mono); font-size: .66rem; letter-spacing: .16em; text-transform: uppercase; color: var(--muted); }
.readout .v { font-family: var(--mono); font-size: 1.5rem; font-weight: 600; color: var(--text); line-height: 1.2; margin-top: 2px; }
.readout .v.crimson { color: var(--accent); }
.readout .v.teal { color: var(--good); }
.readout .u { font-family: var(--mono); font-size: .72rem; color: var(--muted); }

.eyebrow { font-family: var(--mono); font-size: .72rem; letter-spacing: .26em; text-transform: uppercase; color: var(--accent); margin-bottom: 4px; }

.keyidea { border-left: 3px solid var(--good); background: var(--keyidea-bg); padding: 12px 16px; margin: 14px 0; font-style: italic; color: var(--keyidea-text); }
.keyidea ol, .keyidea li { color: var(--keyidea-text); }
.warn { border-left: 3px solid var(--accent); background: var(--warn-bg); padding: 12px 16px; margin: 14px 0; color: var(--warn-text); }

/* ---- Sidebar ---- */
[data-testid="stSidebar"] { background: var(--sidebar); border-right: 1px solid var(--border); }
[data-testid="stSidebar"] .sidebar-nameplate { font-family: var(--display); font-weight: 700; font-size: 1.05rem; color: var(--text); line-height: 1.2; }
[data-testid="stSidebar"] .sidebar-sub { font-family: var(--mono); font-size: .66rem; letter-spacing: .16em; text-transform: uppercase; color: var(--muted); margin-top: 2px; }
[data-testid="stSidebar"] hr { border-color: var(--border); }
/* Fixed width ONLY while the sidebar is open — an unconditional width kept
   the drawer visually stuck open after tapping close on mobile. */
[data-testid="stSidebar"][aria-expanded="true"] { min-width: 340px !important; width: 340px !important; }
[data-testid="stSidebar"][aria-expanded="true"] > div { width: 340px !important; }
[data-testid="stSidebar"] .rail-label { font-family: var(--mono); font-size: .66rem; letter-spacing: .2em; text-transform: uppercase; color: var(--muted); margin: 10px 0 4px 0; }
[data-testid="stSidebar"] [data-testid="stRadio"] label p {
  font-size: .92rem !important; line-height: 1.35 !important;
}
/* Contents-rail entries as quiet list rows with an accent bar on the active
   one — reads like a book's table of contents. */
[data-testid="stSidebar"] [data-testid="stRadio"] > div { gap: 2px; }
[data-testid="stSidebar"] [data-testid="stRadio"] label {
  width: 100%; margin: 0; padding: 6px 10px; border-radius: 8px;
  transition: background .12s ease;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover { background: var(--surface2); }
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {
  background: var(--surface2); box-shadow: inset 3px 0 0 var(--accent);
}
/* Sidebar language picker: three compact pills under the nameplate; the
   active language is rendered as a "primary" button (accent-filled). */
.st-key-sidebar-lang { margin: 4px 0 2px 0; }
.st-key-sidebar-lang [data-testid="stHorizontalBlock"] { gap: 6px !important; }
.st-key-sidebar-lang [data-testid="stButton"] > button {
  height: 34px !important; min-height: 34px !important; width: 100%;
  border-radius: 999px !important; font-size: .78rem !important;
  justify-content: center !important; text-align: center !important;
  padding: 0 6px !important; letter-spacing: 0 !important;
  border: 1px solid var(--border) !important; background: var(--surface2) !important;
  color: var(--text) !important; box-shadow: none !important;
}
.st-key-sidebar-lang [data-testid="stButton"] > button:hover {
  border-color: var(--accent) !important; color: var(--accent) !important;
}
.st-key-sidebar-lang button[kind="primary"],
.st-key-sidebar-lang [data-testid="stBaseButton-primary"] {
  background: var(--accent) !important; color: #fff !important;
  border-color: var(--accent) !important; font-weight: 700 !important;
}
.st-key-sidebar-lang button[kind="primary"] p,
.st-key-sidebar-lang [data-testid="stBaseButton-primary"] p { color: #fff !important; }
.st-key-sidebar-lang button[kind="primary"]:hover,
.st-key-sidebar-lang [data-testid="stBaseButton-primary"]:hover {
  color: #fff !important; filter: brightness(1.08);
}

/* Buttons */
.stButton > button { font-family: var(--mono); font-size: .82rem; letter-spacing: .02em; border: 1px solid var(--border); background: var(--btn); color: var(--text); border-radius: 6px; text-align: left; padding: 8px 12px; transition: none; }
.stButton > button:hover { border-color: var(--text); background: var(--btn-hover); color: var(--text); }
.stButton > button:focus { box-shadow: none; color: var(--text); }
/* Download button (PDF) -- must match the theme, never a dark box */
[data-testid="stDownloadButton"] > button,
.stDownloadButton > button {
  font-family: var(--mono); font-size: .82rem; letter-spacing: .02em;
  border: 1px solid var(--border); background: var(--btn); color: var(--text);
  border-radius: 4px; padding: 8px 12px; width: 100%; transition: none;
}
[data-testid="stDownloadButton"] > button:hover,
.stDownloadButton > button:hover { border-color: var(--accent); background: var(--btn-hover); color: var(--text); }
[data-testid="stDownloadButton"] > button:focus,
[data-testid="stDownloadButton"] > button:active { box-shadow: none; color: var(--text); background: var(--btn); }
[data-testid="stDownloadButton"] > button p { color: var(--text); }

/* Widget labels + inputs (kept legible in every theme) */
[data-testid="stWidgetLabel"] p { font-family: var(--mono); font-size: .74rem; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); }
[data-testid="stSidebar"] label, [data-testid="stRadio"] label, [data-testid="stCheckbox"] label { color: var(--text); }
[data-baseweb="select"] > div { background: var(--surface2); color: var(--text); border-color: var(--border); }
[data-testid="stSlider"] label, [data-testid="stSlider"] div { color: var(--text); }

/* Dropdown menu popover (rendered at body root) -- theme it so it is never a
   dark box on the light/colored themes. */
[data-baseweb="popover"] [role="listbox"],
[data-baseweb="popover"] ul,
[data-baseweb="menu"], ul[role="listbox"] {
  background: var(--surface) !important; border: 1px solid var(--border) !important;
}
[role="option"], li[role="option"] { background: var(--surface) !important; color: var(--text) !important; }
[role="option"]:hover, li[role="option"]:hover, [aria-selected="true"][role="option"] {
  background: var(--surface2) !important; color: var(--text) !important;
}

/* Tabs */
[data-testid="stTabs"] button[role="tab"] { font-family: var(--mono); letter-spacing: .08em; text-transform: uppercase; font-size: .78rem; color: var(--muted); }
[data-testid="stTabs"] button[role="tab"][aria-selected="true"] { color: var(--text); border-bottom-color: var(--accent); }

[data-testid="stTable"] table { font-family: var(--mono); font-size: .85rem; color: var(--text); }
[data-testid="stSlider"] [role="slider"] { background: var(--accent); }

/* ---- Floating "Ask me" assistant (bottom-right, pure CSS, no JS) ---- */
.assistant-fab { position: fixed; right: 26px; bottom: 26px; z-index: 99999; }
.assistant-fab > summary {
  list-style: none; cursor: pointer; display: inline-flex; align-items: center;
  gap: 9px; background: linear-gradient(135deg, #1B4E8C, #123152); color: #FFFFFF;
  font-family: var(--sans); font-weight: 700; font-size: .9rem; letter-spacing: .01em;
  padding: 13px 20px; border-radius: 999px;
  box-shadow: 0 8px 24px rgba(18,49,82,.35), 0 2px 6px rgba(0,0,0,.16);
  user-select: none; white-space: nowrap;
  transition: transform .15s ease, box-shadow .15s ease;
}
.assistant-fab > summary:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 30px rgba(18,49,82,.45), 0 3px 8px rgba(0,0,0,.20);
}
/* the label sits on a dark-blue gradient in EVERY theme; the global
   typography rule paints inner spans with var(--text), which is near-black
   in the light theme and made "Ask me" unreadable — force white */
.assistant-fab > summary, .assistant-fab > summary span,
.assistant-fab > summary .fab-label { color: #fff !important; }
.assistant-fab > summary::-webkit-details-marker { display: none; }
.assistant-fab > summary::marker { content: ""; }
.fab-icon { display: inline-flex; align-items: center; }
.assistant-fab[open] > summary { border-radius: 999px; }
.assistant-panel {
  position: absolute; bottom: 60px; right: 0; width: min(380px, 92vw);
  height: min(560px, 70vh); background: var(--surface); border: 1px solid var(--border);
  border-radius: 14px; overflow: hidden;
  box-shadow: 0 18px 50px rgba(0,0,0,.32); animation: fab-in .16s ease;
}
@keyframes fab-in { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }
.assistant-panel iframe { width: 100%; height: 100%; border: 0; display: block; }
.assistant-frame { border: 1px solid var(--border); border-radius: 6px; overflow: hidden; background: var(--surface); }

/* Demo explainer panel (above each practice demo) */
.demo-intro { border: 1px solid var(--border); border-left: 3px solid var(--accent);
  background: var(--surface2); border-radius: 6px; padding: 14px 16px; margin: 6px 0 18px 0; }
.demo-intro .di-row { display: flex; gap: 12px; padding: 3px 0; align-items: baseline; }
.demo-intro .di-k { flex: 0 0 148px; font-family: var(--mono); font-size: .68rem;
  letter-spacing: .07em; text-transform: uppercase; color: var(--accent); padding-top: 2px; }
.demo-intro .di-v { flex: 1; color: var(--text); font-size: .95rem; line-height: 1.5; }

/* ---- Mobile responsiveness (mobile-first refinements) ---- */
@media (max-width: 640px) {
  /* the open drawer takes ~88vw; width is scoped to the OPEN state so the
     close animation can still slide it away */
  [data-testid="stSidebar"][aria-expanded="true"],
  [data-testid="stSidebar"][aria-expanded="true"] > div {
    min-width: 88vw !important; width: 88vw !important; max-width: 360px !important;
  }
  .block-container, [data-testid="block-container"] { padding: 1.1rem .7rem 3rem .7rem; }
  .masthead { padding: 16px 16px 12px 16px; }
  .masthead .title { font-size: 1.5rem; }
  .masthead .subtitle { font-size: .92rem; }
  .masthead .colophon, .masthead .byline { gap: 10px; font-size: .62rem; }
  .readout .v { font-size: 1.15rem; }
  [data-testid="stMarkdownContainer"] p { font-size: .98rem; }
  .assistant-fab { right: 12px; bottom: 12px; }
  .assistant-fab > summary { padding: 10px 14px; font-size: .74rem; }
  /* section-card grid collapses to a single column on phones */
  .section-grid { grid-template-columns: 1fr !important; }
  .hero { padding: 24px 14px 20px 14px; }
  .hero .hero-title { font-size: 2.1rem !important; }
  .hero .hero-summary { font-size: 1rem !important; }
  .hero .hero-byline .cell { min-width: 100%; }
  /* stack Streamlit columns full-width on phones (both the old "column" and
     the new "stColumn" test-ids, so this works on every Streamlit release) */
  [data-testid="stHorizontalBlock"] { flex-direction: column !important; }
  [data-testid="column"], [data-testid="stColumn"] {
    width: 100% !important; flex: 1 1 100% !important;
  }
  /* ...EXCEPT the top toolbar: it wraps into a tidy 2-per-row grid, with the
     primary "Sections" button on its own full-width first row */
  .st-key-topbar [data-testid="stHorizontalBlock"] {
    flex-direction: row !important; flex-wrap: wrap !important; gap: 8px !important;
  }
  .st-key-topbar [data-testid="column"], .st-key-topbar [data-testid="stColumn"] {
    width: auto !important; flex: 1 1 44% !important; min-width: 44% !important;
  }
  .st-key-topbar [data-testid="column"]:first-child,
  .st-key-topbar [data-testid="stColumn"]:first-child {
    flex: 1 1 100% !important;
  }
  /* ...and the sidebar language pills stay in one row inside the drawer */
  .st-key-sidebar-lang [data-testid="stHorizontalBlock"] {
    flex-direction: row !important; gap: 6px !important;
  }
  .st-key-sidebar-lang [data-testid="column"],
  .st-key-sidebar-lang [data-testid="stColumn"] {
    /* basis 30% + grow leaves room for the 2×6px gaps, so all three pills
       share one row instead of wrapping */
    width: auto !important; flex: 1 1 30% !important; min-width: 0 !important;
  }
  .dedication { margin: 2px 4px 16px 4px; }
  .dedication .ded-text { font-size: .92rem; }
  /* ...and the Theory/Practice pair under each card stays side by side */
  [class*="st-key-modes-"] [data-testid="stHorizontalBlock"] {
    flex-direction: row !important;
  }
  [class*="st-key-modes-"] [data-testid="column"],
  [class*="st-key-modes-"] [data-testid="stColumn"] {
    /* min-width beats Streamlit's own calc(100% - 24px) column stacking */
    width: 50% !important; flex: 1 1 50% !important; min-width: 50% !important;
  }
}
@media (min-width: 641px) and (max-width: 1024px) {
  .section-grid { grid-template-columns: repeat(2, 1fr) !important; }
}

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }

/* ============================================================= */
/*  PRINT / PDF  —  clean, professional printout                 */
/*  Hides all chrome (sidebar, chatbot, buttons) and prints only */
/*  the article content in a legible, ink-friendly layout.       */
/* ============================================================= */
@media print {
  /* force a light, high-contrast, ink-saving palette */
  :root, [data-testid="stAppViewContainer"] {
    --text: #111 !important; --surface: #fff !important; --surface2: #fff !important;
    --border: #bbb !important; background: #fff !important;
  }
  html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    background: #fff !important; color: #111 !important;
  }
  /* hide everything that isn't the article */
  [data-testid="stSidebar"], [data-testid="collapsedControl"],
  [data-testid="stSidebarCollapsedControl"],
  .assistant-fab, .assistant-panel, header, footer,
  [data-testid="stToolbar"], [data-testid="stDecoration"],
  .stButton, [data-testid="stDownloadButton"], .site-nav, .view-toggle,
  .section-grid, .roadmap-panel,
  .st-key-topbar, .st-key-landing-grid, [class*="st-key-modes-"],
  [class*="st-key-nav-"] { display: none !important; }
  /* give the content the full page with sane margins */
  .block-container, [data-testid="block-container"] {
    max-width: 100% !important; padding: 0 !important; margin: 0 !important;
  }
  @page { margin: 1.6cm 1.4cm; }
  /* keep cards and figures from breaking awkwardly across pages */
  [data-testid="stVerticalBlockBorderWrapper"], .demo-intro, .keyidea, .warn,
  figure, .js-plotly-plot, [data-testid="stImage"] {
    break-inside: avoid; page-break-inside: avoid;
    box-shadow: none !important; border-color: #ccc !important;
  }
  h1, h2, h3, .plate-title { break-after: avoid; page-break-after: avoid; }
  a { color: #111 !important; text-decoration: none !important; }
  /* plotly/altair charts sometimes render dark controls — neutralise */
  .modebar { display: none !important; }
  .masthead { border: none !important; }
}

/* ============================================================= */
/*  HERO SECTION  —  blue band, course title, byline, summary    */
/* ============================================================= */
.hero {
  text-align: center; padding: 34px 22px 30px 22px; margin: 0 0 16px 0;
  border-radius: 16px; position: relative; overflow: hidden;
}
/* thin gold-to-crimson rule across the top — echoes the masthead ribbon */
.hero::before {
  content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 4px;
  background: linear-gradient(90deg, #E8B84B, #8A1C2B); z-index: 1;
}
.hero.hero-blue {
  background: linear-gradient(140deg, #0A1F38 0%, #123152 55%, #0C2340 100%);
  box-shadow: 0 14px 40px rgba(10,31,56,.28);
  --hero-art-node: #E8B84B; --hero-art-edge: #7F9BC0;
  --hero-art-shield: #8A1C2B; --hero-art-shieldline: #E8B84B;
}
.hero.hero-blue .hero-eyebrow { color: #E8B84B; }
.hero.hero-blue .hero-title { color: #FFFFFF; }
.hero.hero-blue .hero-summary {
  color: #E6ECF3; background: rgba(255,255,255,.06);
  border-left: 3px solid #E8B84B;
}
.hero.hero-blue .hero-byline .cell {
  background: rgba(255,255,255,.07); border: 1px solid rgba(255,255,255,.14);
}
.hero.hero-blue .hero-byline .lab { color: #E8B84B; }
.hero.hero-blue .hero-byline b { color: #FFFFFF; }
.hero-art-wrap { display: flex; justify-content: center; margin-bottom: 14px; }
.hero-art { width: 200px; height: auto; }
.hero .hero-eyebrow {
  font-family: var(--mono); font-size: .82rem; letter-spacing: .30em;
  text-transform: uppercase; margin-bottom: 12px;
}
.hero .hero-title {
  font-family: var(--serif); font-weight: 800; font-size: 3rem; line-height: 1.12;
  margin: 0 0 20px 0; letter-spacing: -.015em;
}
.hero .hero-byline {
  display: flex; gap: 18px; justify-content: center; flex-wrap: wrap;
  margin: 16px 0 18px 0;
}
.hero .hero-byline .cell {
  text-align: center; border-radius: 10px; padding: 12px 24px; min-width: 220px;
}
.hero .hero-byline .lab {
  display: block; font-family: var(--mono); font-size: .68rem; letter-spacing: .18em;
  text-transform: uppercase; margin-bottom: 6px;
}
.hero .hero-byline b { font-family: var(--serif); font-size: 1.2rem; font-weight: 700; }
.hero .hero-summary {
  max-width: 760px; margin: 18px auto 0 auto; font-family: var(--serif); font-size: 1.1rem;
  line-height: 1.65; border-radius: 8px; padding: 16px 22px; text-align: start;
}
.hero .hero-practice-note {
  max-width: 760px; margin: 12px auto 0 auto; font-family: var(--mono); font-size: .84rem;
  line-height: 1.6; color: #C9D6E5; padding: 0 22px; text-align: start;
}

/* ---- Footer ---- */
.site-footer {
  text-align: center; font-family: var(--mono); font-size: .72rem; letter-spacing: .06em;
  color: var(--muted); border-top: 1px solid var(--border);
  margin-top: 40px; padding: 22px 12px 8px 12px; line-height: 1.7;
}

/* ============================================================= */
/*  SECTION-CARD GRID  —  six course sections as elevated cards  */
/* ============================================================= */
.section-grid {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 22px 0;
}
/* clickable cards are real Streamlit buttons styled as cards (see below);
   this class is used for the static/roadmap grid. */
.section-card {
  background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
  padding: 20px 18px; transition: transform .15s ease, box-shadow .15s ease, border-color .15s ease;
  position: relative; overflow: hidden;
}
.section-card::before {
  content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 3px;
  background: var(--accent); opacity: .85;
}
.section-card:hover { transform: translateY(-3px); box-shadow: 0 10px 28px rgba(14,42,71,.14); border-color: var(--accent); }
.section-card .sc-icon { font-size: 1.6rem; line-height: 1; margin-bottom: 10px; display: block; }
.section-card .sc-num {
  font-family: var(--mono); font-size: .66rem; letter-spacing: .2em; text-transform: uppercase;
  color: var(--accent); margin-bottom: 6px;
}
.section-card .sc-title {
  font-family: var(--serif); font-weight: 700; font-size: 1.12rem; color: var(--text);
  margin-bottom: 6px; line-height: 1.25;
}
.section-card .sc-desc { font-size: .88rem; color: var(--muted); line-height: 1.5; }

/* ---- Clickable section cards: style Streamlit buttons in the landing grid.
   The wrapper class comes from st.container(key="landing-grid") in app.py. --- */
.st-key-landing-grid [data-testid="stButton"] > button,
.st-key-landing-grid .stButton > button {
  width: 100%; height: 188px; text-align: start; white-space: pre-line;
  background: var(--surface); border: 1px solid var(--border); border-bottom: none;
  border-radius: 12px 12px 0 0; border-top: 3px solid var(--accent);
  padding: 18px 18px; font-family: var(--serif); color: var(--text);
  box-shadow: 0 4px 14px rgba(14,42,71,.06);
  display: flex; flex-direction: column; align-items: flex-start; justify-content: flex-start;
  overflow: hidden; transition: box-shadow .15s ease, border-color .15s ease,
    transform .15s ease;
}
.st-key-landing-grid [data-testid="stButton"] > button:hover,
.st-key-landing-grid .stButton > button:hover {
  box-shadow: 0 10px 26px rgba(14,42,71,.14);
  border-color: var(--accent); color: var(--text); transform: translateY(-2px);
}
/* Mini Theory/Practice footer -- visually fused to the card above (no gap,
   matching border, rounded only on the two bottom outer corners). Each row is
   st.container(key="modes-<sec>") → class st-key-modes-<sec>. */
[class*="st-key-modes-"] { margin-top: 0; }
[class*="st-key-modes-"] [data-testid="stHorizontalBlock"] { gap: 0 !important; }
[class*="st-key-modes-"] [data-testid="stButton"] > button {
  height: 38px !important; width: 100% !important; font-size: .78rem !important;
  font-weight: 600 !important; border-radius: 0 !important;
  border: 1px solid var(--border) !important; border-top: 1px solid var(--border) !important;
  background: var(--surface2) !important; color: var(--text) !important;
  box-shadow: none !important; transform: none !important;
  align-items: center !important; justify-content: center !important;
  padding: 0 8px !important; text-align: center !important;
}
[class*="st-key-modes-"] [data-testid="stColumn"]:first-child [data-testid="stButton"] > button,
[class*="st-key-modes-"] [data-testid="column"]:first-child [data-testid="stButton"] > button {
  border-bottom-left-radius: 10px !important;
}
[class*="st-key-modes-"] [data-testid="stColumn"]:last-child [data-testid="stButton"] > button,
[class*="st-key-modes-"] [data-testid="column"]:last-child [data-testid="stButton"] > button {
  border-bottom-right-radius: 10px !important; border-left: none !important;
}
[class*="st-key-modes-"] [data-testid="stButton"] > button:hover {
  border-color: var(--accent) !important; background: var(--surface) !important;
  color: var(--accent) !important;
}

/* ---- Navigation button rows (quick section list, site-map jump list) ----
   Wrappers come from st.container(key="nav-sections"/"nav-map"). */
[class*="st-key-nav-"] [data-testid="stButton"] > button {
  font-family: var(--mono); font-size: .8rem; letter-spacing: .04em;
  border-radius: 8px; border: 1px solid var(--border); background: var(--surface2);
  color: var(--text); padding: 9px 14px; transition: all .15s ease; width: 100%;
}
[class*="st-key-nav-"] [data-testid="stButton"] > button:hover {
  border-color: var(--accent); background: var(--surface); color: var(--text);
}

/* ============================================================= */
/*  ROADMAP / SITE-MAP  —  as an SVG tree inside a panel          */
/* ============================================================= */
.roadmap-panel {
  background: var(--surface2); border: 1px solid var(--border); border-radius: 12px;
  padding: 18px 20px; margin: 8px 0 18px 0; overflow-x: auto;
}
.roadmap-panel svg { display: block; margin: 0 auto; max-width: 100%; height: auto; }
.rm-node-box { fill: var(--surface); stroke: var(--border); }
.rm-node-root { fill: var(--accent); }
.rm-node-sec { fill: var(--surface); stroke: var(--accent); }
.rm-node-accent { fill: var(--accent); }
.rm-edge { stroke: var(--border); stroke-width: 1.5; fill: none; }
.rm-txt { font-family: var(--mono); fill: var(--text); }
.rm-txt-leaf { font-family: var(--mono); fill: var(--text-body); opacity: 0.85; }
.rm-txt-root { font-family: var(--serif); fill: #fff; font-weight: 700; }
.rm-txt-accent { font-family: var(--mono); fill: var(--accent); }

/* ---- Top-bar mobile hint + About/Contact info panels ---- */
.topbar-hint {
  font-family: var(--mono); font-size: .68rem; letter-spacing: .12em;
  color: var(--muted); margin: 0 0 6px 2px; text-transform: uppercase;
}
/* The top bar is a real framed toolbar: one bordered strip that holds all
   seven controls at a uniform 44px height. The wrapping node carries the
   ``st-key-topbar`` class (from st.container(key="topbar") in app.py). */
.st-key-topbar {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 12px; padding: 10px 12px; margin: 2px 0 20px 0;
  box-shadow: 0 6px 20px rgba(12,35,64,.07);
}
.st-key-topbar [data-testid="stHorizontalBlock"] { gap: 8px; align-items: center; }
.st-key-topbar [data-baseweb="select"] > div {
  min-height: 44px !important; border-radius: 8px !important;
  border: 1px solid var(--border) !important; background: var(--surface2) !important;
  font-family: var(--serif) !important; font-size: .88rem !important;
}
.st-key-topbar [data-testid="stButton"] > button,
.st-key-topbar [data-testid="stDownloadButton"] > button {
  min-height: 44px !important; height: 44px !important; width: 100%;
  border-radius: 8px !important; border: 1px solid var(--border) !important;
  background: var(--surface2) !important; color: var(--text) !important;
  font-family: var(--serif) !important; font-weight: 600 !important; font-size: .88rem !important;
  box-shadow: none !important; margin: 0 !important;
  transition: all .15s ease !important; justify-content: center !important;
  white-space: nowrap !important; overflow: hidden !important; text-overflow: ellipsis !important;
  padding: 0 10px !important; text-align: center !important;
}
.st-key-topbar [data-testid="stButton"] > button p { font-size: .88rem !important; }
.st-key-topbar [data-testid="stButton"] > button:hover,
.st-key-topbar [data-testid="stDownloadButton"] > button:hover {
  border-color: var(--accent) !important; background: var(--surface) !important;
  box-shadow: 0 6px 16px rgba(12,35,64,.12) !important;
  transform: translateY(-1px);
}
/* The "Sections" control is the odd one out on purpose: same size as the
   other six, distinct accent color so it reads as the primary action. */
.st-key-topbar .st-key-btn_open_sections [data-testid="stButton"] > button,
.st-key-topbar .st-key-btn_open_sections button {
  background: var(--accent) !important; color: #fff !important;
  border-color: var(--accent) !important; font-weight: 700 !important;
}
.st-key-topbar .st-key-btn_open_sections button p { color: #fff !important; }
.st-key-topbar .st-key-btn_open_sections button:hover {
  filter: brightness(1.08);
  box-shadow: 0 8px 22px rgba(138,28,43,.35) !important;
}
.info-panel {
  background: var(--surface); border: 1px solid var(--border);
  border-left: 3px solid var(--accent); border-radius: 10px;
  padding: 18px 22px; margin: 6px 0 16px 0; box-shadow: 0 6px 22px rgba(12,35,64,.07);
}
.info-panel .ip-title {
  font-family: var(--display); font-weight: 700; font-size: 1.2rem;
  color: var(--text); margin-bottom: 8px;
}
.info-panel .ip-body { font-family: var(--serif); font-size: 1.02rem; line-height: 1.65; color: var(--text-body); }
.info-panel .ip-rows { margin-top: 14px; display: flex; flex-direction: column; gap: 6px; }
.info-panel .ip-row { display: flex; gap: 12px; align-items: baseline; }
.info-panel .ip-k {
  flex: 0 0 130px; font-family: var(--mono); font-size: .68rem; letter-spacing: .1em;
  text-transform: uppercase; color: var(--accent);
}
.info-panel .ip-v { flex: 1; font-family: var(--serif); color: var(--text); font-weight: 600; }
.info-panel .ip-links { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 16px; }
.info-panel .ip-link {
  display: inline-flex; align-items: center; font-family: var(--mono);
  font-size: .8rem; padding: 9px 18px; border-radius: 999px;
  border: 1px solid var(--border); background: var(--surface2);
  color: var(--text); border-bottom: 1px solid var(--border);
  text-decoration: none !important; transition: all .15s ease;
}
.info-panel .ip-link:hover {
  border-color: var(--good); color: var(--good);
  box-shadow: 0 5px 14px rgba(12,35,64,.12); transform: translateY(-1px);
}
.info-panel .ip-note {
  margin-top: 14px; padding-top: 10px; border-top: 1px dashed var(--border);
  font-family: var(--serif); font-style: italic; font-size: .94rem;
  color: var(--muted); line-height: 1.6;
}

/* ---- Dedication strip (acknowledgment under the hero) ---- */
.dedication {
  max-width: 820px; margin: 4px auto 22px auto; padding: 14px 18px 16px 18px;
  text-align: center; border-top: 1px solid var(--gold);
  border-bottom: 1px solid var(--gold); position: relative;
}
.dedication .ded-eyebrow {
  font-family: var(--mono); font-size: .66rem; letter-spacing: .3em;
  text-transform: uppercase; color: var(--gold); margin-bottom: 2px;
}
.dedication .ded-ornament { color: var(--gold); font-size: 1.05rem; line-height: 1.4; }
.dedication .ded-text {
  font-family: var(--serif); font-style: italic; font-size: 1rem;
  line-height: 1.75; color: var(--text-body); margin-top: 4px; text-align: center;
}
"""


def _rtl_css() -> str:
    return """
[data-testid="stAppViewContainer"] { direction: rtl; }
[data-testid="stMain"] { direction: rtl; text-align: right; }
[data-testid="stSidebar"] { direction: rtl; border-right: none; border-left: 1px solid var(--border); }
.assistant-fab { right: auto; left: 26px; }
.assistant-panel { right: auto; left: 0; }
[data-testid="stMarkdownContainer"], .stMarkdown, p, li, h1, h2, h3, h4 { text-align: right; }
html, body, [data-testid="stAppViewContainer"], .stMarkdown,
[data-testid="stMarkdownContainer"] p, p, li, span, div { font-family: var(--rtl-body); }
h1, h2, h3, h4, .masthead .title, .plate-title { font-family: var(--rtl-display); }
.masthead { text-align: right; }
.masthead .colophon, .masthead .byline { flex-direction: row-reverse; }
[data-testid="stVerticalBlockBorderWrapper"] { border-left: 1px solid var(--border) !important; border-right: 3px solid var(--text) !important; }
.keyidea { border-left: none; border-right: 3px solid var(--good); }
.demo-intro { border-left: 1px solid var(--border); border-right: 3px solid var(--accent); }
.warn { border-left: none; border-right: 3px solid var(--accent); }
.figure-caption { text-align: right; }
.stButton > button { text-align: right; }
.section-card::before { left: auto; right: 0; }
.section-card { text-align: right; }
.st-key-landing-grid [data-testid="stButton"] > button { text-align: right; }
/* fused Theory/Practice footer: swap the outer rounded corners + shared edge */
[class*="st-key-modes-"] [data-testid="stColumn"]:first-child [data-testid="stButton"] > button,
[class*="st-key-modes-"] [data-testid="column"]:first-child [data-testid="stButton"] > button {
  border-bottom-left-radius: 0 !important; border-bottom-right-radius: 10px !important;
}
[class*="st-key-modes-"] [data-testid="stColumn"]:last-child [data-testid="stButton"] > button,
[class*="st-key-modes-"] [data-testid="column"]:last-child [data-testid="stButton"] > button {
  border-bottom-right-radius: 0 !important; border-bottom-left-radius: 10px !important;
  border-left: 1px solid var(--border) !important; border-right: none !important;
}
/* active contents-rail entry: accent bar sits on the right in RTL */
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {
  box-shadow: inset -3px 0 0 var(--accent);
}
.info-panel { border-left: 1px solid var(--border); border-right: 3px solid var(--accent); }
/* Numerals and mono readouts stay LTR for legibility */
.readout, .colophon, .figure-caption { direction: ltr; }
.measure { margin-right: 0; }
"""


def inject_theme(theme: str = "light", direction: str = "ltr", lang: str = "en") -> None:
    """Inject the full stylesheet for the chosen ``theme``/``direction``/``lang``."""
    css = _FONTS + _root(theme, lang) + _base_css()
    if direction == "rtl":
        css += _rtl_css()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
