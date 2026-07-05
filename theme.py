"""
theme.py -- visual identity for the Trustworthy ML sandbox.
Completely revamped for professional academic aesthetic, perfectly responsive 
buttons, and fully functional mobile sidebar.
"""
from __future__ import annotations
import streamlit as st

# Academic Palettes
LIGHT = {
    "page": "#F9F8F6", "surface": "#FFFFFF", "surface2": "#F3F1EC",
    "sidebar": "#FFFFFF",
    "text": "#111827", "text_body": "#374151", "muted": "#6B7280",
    "border": "#E5E7EB",
    "accent": "#8A1C2B", "good": "#0F766E", "gold": "#B45309",
    "masthead": "#111827", "mast_title": "#F9FAFB", "mast_sub": "#9CA3AF",
    "mast_eyebrow": "#D97706", "mast_colophon": "#6B7280", "mast_rule": "#8A1C2B",
    "keyidea_bg": "#F0FDF4", "keyidea_text": "#14532D",
    "warn_bg": "#FEF2F2", "warn_text": "#7F1D1D",
    "btn": "#FFFFFF", "btn_hover": "#F9FAFB",
    "link_border": "rgba(15,118,110,.35)",
}

DARK = {
    "page": "#0F172A", "surface": "#1E293B", "surface2": "#334155",
    "sidebar": "#0F172A",
    "text": "#F8FAFC", "text_body": "#E2E8F0", "muted": "#94A3B8",
    "border": "#334155",
    "accent": "#E11D48", "good": "#14B8A6", "gold": "#F59E0B",
    "masthead": "#020617", "mast_title": "#F8FAFC", "mast_sub": "#94A3B8",
    "mast_eyebrow": "#F59E0B", "mast_colophon": "#64748B", "mast_rule": "#F59E0B",
    "keyidea_bg": "#064E3B", "keyidea_text": "#A7F3D0",
    "warn_bg": "#4C0519", "warn_text": "#FECDD3",
    "btn": "#1E293B", "btn_hover": "#334155",
    "link_border": "rgba(20,184,166,.4)",
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
    rtl_font = "'Cairo', 'Segoe UI', Tahoma, sans-serif" if lang == "ar" else "'Vazirmatn', 'Segoe UI', Tahoma, sans-serif"
    vars_ = "".join(f"--{k.replace('_','-')}: {v};" for k, v in p.items())
    return (
        ":root {" + vars_ +
        "--serif: 'Merriweather', Georgia, 'Times New Roman', serif;" +
        "--display: 'Playfair Display', Georgia, serif;" +
        "--mono: 'IBM Plex Mono', 'SFMono-Regular', Menlo, monospace;" +
        f"--rtl-body: {rtl_font}; --rtl-display: {rtl_font};" + "}"
    )

def _base_css() -> str:
    return """
/* Base Layout & Responsive Fixes */
[data-testid="stAppViewContainer"] { background: var(--page); }
.block-container { padding-top: 2rem; max-width: 1180px; }

/* FIX 1: SIDEBAR ON MOBILE - ensure toggle is fully visible & clickable */
[data-testid="stHeader"] {
  background-color: transparent !important;
  box-shadow: none !important;
}
[data-testid="collapsedControl"] {
  display: flex !important; visibility: visible !important; opacity: 1 !important;
  background: var(--surface) !important;
  border-radius: 8px !important;
  border: 1px solid var(--border) !important;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
  padding: 8px !important; margin: 12px !important;
  z-index: 999999 !important;
}
[data-testid="collapsedControl"] svg {
  fill: var(--accent) !important; width: 24px !important; height: 24px !important;
}

/* Typography */
html, body, .stMarkdown, p, li, span, div { color: var(--text); font-family: var(--serif); line-height: 1.7; }
h1, h2, h3, h4 { font-family: var(--display); color: var(--text); }
h1 { font-weight: 800; } h2 { font-weight: 700; margin-top: 1rem; }
a { color: var(--good); text-decoration: none; border-bottom: 1px solid var(--link-border); }

/* Buttons & Interactive Elements (FIX 2: Ensure buttons are flawless) */
[data-testid="stButton"] button, [data-testid="stDownloadButton"] button {
  font-family: var(--mono) !important; font-size: 0.85rem !important; font-weight: 600 !important;
  border: 1px solid var(--border) !important; background: var(--btn) !important; color: var(--text) !important;
  border-radius: 8px !important; padding: 10px 16px !important; transition: all 0.2s ease !important;
  box-shadow: 0 2px 4px rgba(0,0,0,0.02) !important;
}
[data-testid="stButton"] button:hover, [data-testid="stDownloadButton"] button:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 16px rgba(0,0,0,0.08) !important;
  border-color: var(--accent) !important; color: var(--accent) !important;
}

/* Landing Grid Cards (Buttons styled as big cards) */
.landing-grid [data-testid="stButton"] button {
  min-height: 140px; text-align: left; padding: 24px;
  border-top: 4px solid var(--accent) !important; border-radius: 12px !important;
  background: var(--surface) !important; white-space: pre-line;
}
.landing-prompt {
  text-align: center; font-family: var(--mono); color: var(--muted); font-size: 0.85rem; letter-spacing: 0.05em; margin-bottom: 20px;
}

/* Top Control Bar Grid for Mobile (FIX 3) */
.topbar-container > [data-testid="stHorizontalBlock"] { gap: 12px !important; }
.topbar-hint { font-family: var(--mono); font-size: 0.7rem; color: var(--muted); text-transform: uppercase; margin-bottom: 6px; }

/* Hero Box */
.hero { text-align: center; padding: 40px 24px; border-radius: 16px; margin-bottom: 24px; position: relative; overflow: hidden; }
.hero.hero-blue {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  box-shadow: 0 20px 40px rgba(0,0,0,0.15);
  --hero-art-node: #F59E0B; --hero-art-edge: #94A3B8; --hero-art-shield: #E11D48; --hero-art-shieldline: #F59E0B;
}
.hero-eyebrow { font-family: var(--mono); font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: #F59E0B; margin-bottom: 12px; }
.hero-title { font-family: var(--display); font-weight: 800; font-size: 3.2rem; color: #FFFFFF; line-height: 1.1; margin-bottom: 24px; }
.hero-byline { display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-bottom: 24px; }
.hero-byline .cell { background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.1); padding: 12px 24px; border-radius: 12px; }
.hero-byline .lab { display: block; font-family: var(--mono); font-size: 0.7rem; letter-spacing: 0.15em; text-transform: uppercase; color: #F59E0B; margin-bottom: 4px; }
.hero-byline b { font-family: var(--serif); font-size: 1.2rem; color: #FFFFFF; font-weight: 700; }
.hero-summary { max-width: 800px; margin: 0 auto; font-family: var(--serif); font-size: 1.15rem; line-height: 1.6; color: #E2E8F0; text-align: start; }
.hero-practice-note { max-width: 800px; margin: 16px auto 0; font-family: var(--mono); font-size: 0.85rem; color: #94A3B8; text-align: start; }

/* Masthead */
.masthead {
  background: var(--masthead); color: var(--mast-title); border-radius: 12px;
  padding: 32px; margin-bottom: 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.1); position: relative;
}
.masthead::before { content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 5px; background: linear-gradient(90deg, var(--mast-rule), var(--accent)); }
.masthead .eyebrow { font-family: var(--mono); font-size: 0.75rem; letter-spacing: 0.25em; text-transform: uppercase; color: var(--mast-eyebrow); }
.masthead .title { font-family: var(--display); font-weight: 800; font-size: 2.4rem; color: var(--mast-title); margin: 8px 0; }
.masthead .subtitle { font-family: var(--serif); font-style: italic; font-size: 1.1rem; color: var(--mast-sub); }
.masthead .colophon { display: flex; gap: 24px; font-family: var(--mono); font-size: 0.75rem; color: var(--mast-colophon); margin-top: 16px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 16px; }

/* Readouts */
.readout-strip { display: flex; flex-wrap: wrap; gap: 16px; margin: 12px 0; }
.readout { flex: 1 1 150px; background: var(--surface2); border: 1px solid var(--border); border-radius: 8px; padding: 14px; }
.readout .k { font-family: var(--mono); font-size: 0.7rem; text-transform: uppercase; color: var(--muted); letter-spacing: 0.1em; }
.readout .v { font-family: var(--mono); font-size: 1.6rem; font-weight: 700; color: var(--text); margin-top: 4px; }

/* Sidebar Rail styling */
[data-testid="stSidebar"] { background: var(--sidebar); border-right: 1px solid var(--border); }
.sidebar-nameplate { font-family: var(--display); font-weight: 700; font-size: 1.15rem; color: var(--text); }
.sidebar-sub { font-family: var(--mono); font-size: 0.7rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--muted); margin-bottom: 20px; }
.rail-label { font-family: var(--mono); font-size: 0.7rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--muted); margin: 24px 0 8px 0; border-bottom: 1px solid var(--border); padding-bottom: 4px; }

/* Callouts */
.keyidea { border-left: 4px solid var(--good); background: var(--keyidea-bg); padding: 16px 20px; border-radius: 0 8px 8px 0; color: var(--keyidea-text); font-size: 1.05rem; }
.warn { border-left: 4px solid var(--accent); background: var(--warn-bg); padding: 16px 20px; border-radius: 0 8px 8px 0; color: var(--warn-text); }

/* Chatbot Float */
.assistant-fab { position: fixed; right: 24px; bottom: 24px; z-index: 99999; }
.assistant-fab summary {
  list-style: none; cursor: pointer; display: flex; align-items: center; gap: 10px;
  background: var(--accent); color: #fff; font-family: var(--mono); font-weight: 700;
  padding: 14px 24px; border-radius: 99px; box-shadow: 0 8px 24px rgba(0,0,0,0.2); transition: all 0.2s ease;
}
.assistant-fab summary:hover { transform: translateY(-3px); box-shadow: 0 12px 32px rgba(0,0,0,0.25); }
.assistant-panel {
  position: absolute; bottom: 70px; right: 0; width: min(400px, 90vw); height: min(600px, 75vh);
  background: var(--surface); border: 1px solid var(--border); border-radius: 16px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.2); overflow: hidden;
}
.assistant-panel iframe { width: 100%; height: 100%; border: none; }

/* Roadmap Tree */
.roadmap-panel { background: var(--surface2); border: 1px solid var(--border); border-radius: 16px; padding: 24px; overflow-x: auto; margin-bottom: 24px; }

/* ==== MOBILE RESPONSIVENESS ==== */
@media (max-width: 768px) {
  .block-container { padding: 1.5rem 1rem; }
  .hero-title { font-size: 2.2rem; }
  .masthead { padding: 24px; }
  .masthead .title { font-size: 1.8rem; }
  
  /* Top Bar Grid: 3x2 */
  .topbar-container > [data-testid="stHorizontalBlock"] {
    display: grid !important; grid-template-columns: repeat(3, 1fr) !important; gap: 8px !important;
  }
  .topbar-container > [data-testid="stHorizontalBlock"] > [data-testid="column"] {
    width: 100% !important; min-width: 100% !important;
  }

  /* Landing Cards: Stack vertically */
  .landing-grid [data-testid="stHorizontalBlock"] { flex-direction: column !important; }
  .landing-grid [data-testid="column"] { width: 100% !important; margin-bottom: 12px; }
  
  .assistant-fab { right: 16px; bottom: 16px; }
  .assistant-fab summary { padding: 12px 20px; font-size: 0.8rem; }
}
"""

def _rtl_css() -> str:
    return """
/* RTL Optimizations for Arabic/Persian */
.block-container, [data-testid="stSidebar"] > div { direction: rtl; text-align: right; }
html, body, .stMarkdown, p, li, span, div, h1, h2, h3, h4 { font-family: var(--rtl-body); text-align: right; }
h1, h2, h3, h4, .masthead .title, .plate-title { font-family: var(--rtl-display); }
.assistant-fab { right: auto; left: 24px; }
.assistant-panel { right: auto; left: 0; }
.masthead, .hero, .landing-grid [data-testid="stButton"] button { text-align: right; }
.masthead .colophon { flex-direction: row-reverse; }
.keyidea { border-left: none; border-right: 4px solid var(--good); border-radius: 8px 0 0 8px; }
.warn { border-left: none; border-right: 4px solid var(--accent); border-radius: 8px 0 0 8px; }
/* Keep numbers LTR */
.readout, .colophon, .figure-caption { direction: ltr; }
"""

def inject_theme(theme: str = "light", direction: str = "ltr", lang: str = "en") -> None:
    css = _FONTS + _root(theme, lang) + _base_css()
    if direction == "rtl":
        css += _rtl_css()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
