"""
components.py -- small, composable UI helpers built on top of theme.py.

These wrap the raw HTML/CSS classes defined in theme.py so the page modules can
say ``readout_strip([...])`` instead of hand-writing markup. Everything emits
through ``st.markdown(..., unsafe_allow_html=True)`` and stays purely
presentational; no compute lives here.
"""
from __future__ import annotations

import html as _html

import streamlit as st


def _esc(text) -> str:
    return _html.escape(str(text), quote=True)


# --------------------------------------------------------------------------- #
# Masthead (journal nameplate)                                                 #
# --------------------------------------------------------------------------- #
def masthead(eyebrow: str, title: str, subtitle: str, colophon: list[str],
             byline: list[dict] | None = None) -> None:
    """Render the top nameplate: mono eyebrow, display title, italic subtitle,
    an optional byline (e.g. supervisor / author), a gold double-rule, and a
    mono colophon row. ``byline`` is a list of {"label": ..., "name": ...}."""
    items = "".join(f"<span>{_esc(c)}</span>" for c in colophon)
    byline_html = ""
    if byline:
        cells = "".join(
            f'<span><span class="lab">{_esc(b.get("label", ""))}</span>'
            f'<b>{_esc(b.get("name", ""))}</b></span>'
            for b in byline
        )
        byline_html = f'<div class="byline">{cells}</div>'
    st.markdown(
        f"""
        <div class="masthead">
          <div class="eyebrow">{_esc(eyebrow)}</div>
          <div class="title">{_esc(title)}</div>
          <div class="subtitle">{_esc(subtitle)}</div>
          {byline_html}
          <hr class="rule"/>
          <hr class="rule-thin"/>
          <div class="colophon">{items}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def chatbot(url: str, label: str = "Ask me", height: int = 520) -> None:
    """Floating bottom-right assistant. A pure-CSS <details> bubble labelled
    "Ask me" that expands to an iframe of the web-chat -- no JavaScript needed,
    so it works inside Streamlit's markdown sandbox."""
    st.markdown(
        f"""
        <details class="assistant-fab">
          <summary>{_esc(label)}</summary>
          <div class="assistant-panel">
            <iframe src="{_esc(url)}" title="assistant"></iframe>
          </div>
        </details>
        """,
        unsafe_allow_html=True,
    )


# --------------------------------------------------------------------------- #
# Sidebar pieces                                                               #
# --------------------------------------------------------------------------- #
def sidebar_nameplate(name: str, sub: str) -> None:
    st.markdown(
        f'<div class="sidebar-nameplate">{_esc(name)}</div>'
        f'<div class="sidebar-sub">{_esc(sub)}</div>',
        unsafe_allow_html=True,
    )


def rail_label(text: str) -> None:
    st.markdown(f'<div class="rail-label">{_esc(text)}</div>', unsafe_allow_html=True)


# --------------------------------------------------------------------------- #
# Section + plate headers                                                      #
# --------------------------------------------------------------------------- #
def eyebrow(text: str) -> None:
    st.markdown(f'<div class="eyebrow">{_esc(text)}</div>', unsafe_allow_html=True)


def section_title(text: str) -> None:
    st.markdown(f"## {text}")


def plate_header(number: str, title: str) -> None:
    """Mono plate-number eyebrow + display plate title. Call inside a
    ``with st.container(border=True):`` block."""
    st.markdown(
        f'<div class="plate-eyebrow">{_esc(number)}</div>'
        f'<div class="plate-title">{_esc(title)}</div>',
        unsafe_allow_html=True,
    )


def figure_caption(html_text: str) -> None:
    """Mono 'Figure N.' style caption. ``html_text`` may contain <b>...</b>."""
    st.markdown(f'<div class="figure-caption">{html_text}</div>',
                unsafe_allow_html=True)


# --------------------------------------------------------------------------- #
# Prose with a comfortable reading measure                                     #
# --------------------------------------------------------------------------- #
def measure(html_text: str) -> None:
    """Render a block of (already-HTML) prose constrained to ~760px."""
    st.markdown(f'<div class="measure">{html_text}</div>', unsafe_allow_html=True)


# --------------------------------------------------------------------------- #
# Callouts                                                                     #
# --------------------------------------------------------------------------- #
def key_idea(html_text: str) -> None:
    st.markdown(f'<div class="keyidea">{html_text}</div>', unsafe_allow_html=True)


def warn(html_text: str) -> None:
    st.markdown(f'<div class="warn">{html_text}</div>', unsafe_allow_html=True)


# --------------------------------------------------------------------------- #
# Instrument readout strip                                                     #
# --------------------------------------------------------------------------- #
def readout_strip(items: list[dict]) -> None:
    """
    Render a row of mono "instrument readouts". Each item is a dict:
        {"k": label, "v": value, "u": unit (optional), "color": "crimson"|"teal"|None}
    Values and labels are shown verbatim (already formatted by the caller).
    """
    cells = []
    for it in items:
        color = it.get("color")
        vclass = f"v {color}" if color in ("crimson", "teal") else "v"
        unit = it.get("u")
        unit_html = f'<span class="u">{_esc(unit)}</span>' if unit else ""
        cells.append(
            '<div class="readout">'
            f'<div class="k">{_esc(it.get("k", ""))}</div>'
            f'<div class="{vclass}">{_esc(it.get("v", ""))} {unit_html}</div>'
            "</div>"
        )
    st.markdown(f'<div class="readout-strip">{"".join(cells)}</div>',
                unsafe_allow_html=True)


def spacer(px: int = 8) -> None:
    st.markdown(f'<div style="height:{int(px)}px"></div>', unsafe_allow_html=True)
