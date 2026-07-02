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
    "page": "#F7F5EF", "surface": "#FFFFFF", "surface2": "#FBFAF6",
    "sidebar": "#FCFBF7",
    "text": "#0E2A47", "text_body": "#20303F", "muted": "#5A6B7B",
    "border": "#D9D4C7",
    "accent": "#8A1C2B", "good": "#0F6E66", "gold": "#A8842C",
    "masthead": "#0A1F38", "mast_title": "#FBF9F3", "mast_sub": "#C7D0DA",
    "mast_eyebrow": "#C9B98B", "mast_colophon": "#9FB0C0", "mast_rule": "#A8842C",
    "keyidea_bg": "#F2F6F5", "keyidea_text": "#1D3A36",
    "warn_bg": "#F8F0F0", "warn_text": "#4A1820",
    "btn": "#FFFFFF", "btn_hover": "#FBFAF6",
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
[data-testid="stHeader"], [data-testid="stToolbar"],
#MainMenu, footer, [data-testid="stDecoration"] {
  display: none !important; height: 0 !important;
}
.block-container, [data-testid="block-container"] {
  padding-top: 2.2rem; padding-bottom: 4rem; max-width: 1180px;
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
h2 { font-weight: 700; font-size: 1.6rem; margin-top: .2rem; }
h3 { font-weight: 600; font-size: 1.24rem; }
a { color: var(--good); text-decoration: none; border-bottom: 1px solid var(--link-border); }
.measure { max-width: 760px; }

/* ---- Masthead / nameplate ---- */
.masthead {
  background: var(--masthead); color: var(--mast-title);
  border-radius: 6px; padding: 22px 28px 18px 28px; margin-bottom: 26px;
  box-shadow: 0 1px 0 rgba(0,0,0,.04);
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
  border-left: 3px solid var(--text) !important; border-radius: 4px;
  box-shadow: 0 1px 2px rgba(0,0,0,.06); padding: 6px 4px;
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
[data-testid="stSidebar"] .rail-label { font-family: var(--mono); font-size: .66rem; letter-spacing: .2em; text-transform: uppercase; color: var(--muted); margin: 10px 0 4px 0; }

/* Buttons */
.stButton > button { font-family: var(--mono); font-size: .82rem; letter-spacing: .02em; border: 1px solid var(--border); background: var(--btn); color: var(--text); border-radius: 4px; text-align: left; padding: 8px 12px; transition: none; }
.stButton > button:hover { border-color: var(--text); background: var(--btn-hover); color: var(--text); }
.stButton > button:focus { box-shadow: none; color: var(--text); }

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
.assistant-fab { position: fixed; right: 22px; bottom: 22px; z-index: 9999; }
.assistant-fab > summary {
  list-style: none; cursor: pointer; display: inline-flex; align-items: center;
  gap: 8px; background: var(--accent); color: #fff; font-family: var(--mono);
  font-size: .8rem; letter-spacing: .06em; padding: 12px 18px; border-radius: 999px;
  box-shadow: 0 6px 20px rgba(0,0,0,.28); user-select: none; white-space: nowrap;
}
.assistant-fab > summary::-webkit-details-marker { display: none; }
.assistant-fab > summary::before { content: "\1F4AC"; font-size: 1rem; }
.assistant-fab[open] > summary { border-radius: 12px 12px 0 0; }
.assistant-panel {
  position: absolute; bottom: 52px; right: 0; width: min(380px, 92vw);
  height: min(560px, 70vh); background: var(--surface); border: 1px solid var(--border);
  border-radius: 12px; overflow: hidden; box-shadow: 0 12px 40px rgba(0,0,0,.35);
}
.assistant-panel iframe { width: 100%; height: 100%; border: 0; display: block; }
.assistant-frame { border: 1px solid var(--border); border-radius: 6px; overflow: hidden; background: var(--surface); }

/* ---- Mobile responsiveness ---- */
@media (max-width: 640px) {
  .block-container, [data-testid="block-container"] { padding: 1.1rem .7rem 3rem .7rem; }
  .masthead { padding: 16px 16px 12px 16px; }
  .masthead .title { font-size: 1.5rem; }
  .masthead .subtitle { font-size: .92rem; }
  .masthead .colophon, .masthead .byline { gap: 10px; font-size: .62rem; }
  .readout .v { font-size: 1.15rem; }
  [data-testid="stMarkdownContainer"] p { font-size: .98rem; }
  .assistant-fab { right: 12px; bottom: 12px; }
  .assistant-fab > summary { padding: 10px 14px; font-size: .74rem; }
}

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
"""


def _rtl_css() -> str:
    return """
[data-testid="stAppViewContainer"] { direction: rtl; }
[data-testid="stMain"] { direction: rtl; text-align: right; }
[data-testid="stSidebar"] { direction: rtl; border-right: none; border-left: 1px solid var(--border); }
[data-testid="stMarkdownContainer"], .stMarkdown, p, li, h1, h2, h3, h4 { text-align: right; }
html, body, [data-testid="stAppViewContainer"], .stMarkdown,
[data-testid="stMarkdownContainer"] p, p, li, span, div { font-family: var(--rtl-body); }
h1, h2, h3, h4, .masthead .title, .plate-title { font-family: var(--rtl-display); }
.masthead { text-align: right; }
.masthead .colophon, .masthead .byline { flex-direction: row-reverse; }
[data-testid="stVerticalBlockBorderWrapper"] { border-left: 1px solid var(--border) !important; border-right: 3px solid var(--text) !important; }
.keyidea { border-left: none; border-right: 3px solid var(--good); }
.warn { border-left: none; border-right: 3px solid var(--accent); }
.figure-caption { text-align: right; }
.stButton > button { text-align: right; }
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
