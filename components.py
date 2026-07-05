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


def hero(eyebrow: str, title: str, summary: str,
         byline: list[dict] | None = None) -> None:
    """A centered hero band under the navbar: course name, byline
    (supervisor / author), and a concise course summary."""
    byline_html = ""
    if byline:
        cells = "".join(
            f'<div class="cell"><span class="lab">{_esc(b.get("label", ""))}</span>'
            f'<b>{_esc(b.get("name", ""))}</b></div>'
            for b in byline
        )
        byline_html = f'<div class="hero-byline">{cells}</div>'
    st.markdown(
        f"""
        <div class="hero">
          <div class="hero-eyebrow">{_esc(eyebrow)}</div>
          <div class="hero-title">{_esc(title)}</div>
          {byline_html}
          <div class="hero-summary">{_esc(summary)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_grid(cards: list[dict]) -> None:
    """A responsive grid of section cards. Each card is a dict with keys
    ``icon``, ``num``, ``title``, ``desc``. Purely visual overview; navigation
    stays in the sidebar/toggles."""
    cells = "".join(
        f'<div class="section-card">'
        f'<span class="sc-icon">{_esc(c.get("icon", "◆"))}</span>'
        f'<div class="sc-num">{_esc(c.get("num", ""))}</div>'
        f'<div class="sc-title">{_esc(c.get("title", ""))}</div>'
        f'<div class="sc-desc">{_esc(c.get("desc", ""))}</div>'
        f'</div>'
        for c in cards
    )
    st.markdown(f'<div class="section-grid">{cells}</div>', unsafe_allow_html=True)


def roadmap_tree(root_label: str, sections: list[dict], is_rtl: bool = False) -> None:
    """Render the site map as a clean SVG tree: a root node branching to the six
    section nodes, each listing its theory + practice page count. Scales
    horizontally and respects the theme via CSS classes."""
    n = len(sections)
    col_w = 190
    width = max(760, n * col_w)
    root_x = width / 2
    top_y = 40
    sec_y = 150
    box_w, box_h = 168, 96
    gap = width / n

    parts = [f'<svg viewBox="0 0 {width} 300" xmlns="http://www.w3.org/2000/svg" '
             f'role="img" aria-label="site map">']

    # root node
    parts.append(
        f'<rect class="rm-node-root" x="{root_x-110}" y="{top_y}" width="220" '
        f'height="46" rx="10"/>'
        f'<text class="rm-txt-root" x="{root_x}" y="{top_y+29}" '
        f'text-anchor="middle" font-size="16">{_esc(root_label)}</text>')

    for i, sec in enumerate(sections):
        cx = gap * (i + 0.5)
        bx = cx - box_w / 2
        # edge from root to this section (smooth curve)
        parts.append(
            f'<path class="rm-edge" d="M {root_x} {top_y+46} '
            f'C {root_x} {sec_y-30}, {cx} {top_y+70}, {cx} {sec_y}"/>')
        # section box
        parts.append(
            f'<rect class="rm-node-sec" x="{bx}" y="{sec_y}" width="{box_w}" '
            f'height="{box_h}" rx="10" stroke-width="1.5"/>')
        # section title
        title = sec.get("title", "")
        parts.append(
            f'<text class="rm-txt" x="{cx}" y="{sec_y+26}" text-anchor="middle" '
            f'font-size="12.5" font-weight="700">{_esc(title)}</text>')
        # counts line
        parts.append(
            f'<text class="rm-txt-accent" x="{cx}" y="{sec_y+50}" '
            f'text-anchor="middle" font-size="10.5" letter-spacing="1">'
            f'{sec.get("n_theory",0)} theory · {sec.get("n_practice",0)} practice</text>')
        # a couple of sample leaf titles
        leaves = sec.get("leaves", [])[:2]
        for j, lf in enumerate(leaves):
            parts.append(
                f'<text class="rm-txt" x="{cx}" y="{sec_y+68+j*15}" '
                f'text-anchor="middle" font-size="9.5" opacity="0.7">'
                f'{_esc(lf[:22])}</text>')

    parts.append('</svg>')
    svg = "".join(parts)
    st.markdown(f'<div class="roadmap-panel">{svg}</div>', unsafe_allow_html=True)


def chatbot(url: str, label: str = "Ask me", height: int = 520) -> None:
    """Floating bottom-right assistant. A pure-CSS <details> bubble labelled
    "Ask me" that expands to an iframe of the web-chat -- no JavaScript needed,
    so it works inside Streamlit's markdown sandbox."""
    st.markdown(
        f"""
        <details class="assistant-fab">
          <summary>
            <span class="fab-icon" aria-hidden="true">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none"
                   stroke="currentColor" stroke-width="2" stroke-linecap="round"
                   stroke-linejoin="round">
                <path d="M21 11.5a8.38 8.38 0 0 1-8.5 8.5 8.5 8.5 0 0 1-3.8-.9L3 21l1.9-5.7A8.5 8.5 0 1 1 21 11.5z"/>
              </svg>
            </span>
            <span class="fab-label">{_esc(label)}</span>
          </summary>
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


def demo_intro(what: str, why: str, expect: str,
               labels=("What this does", "Why it matters",
                       "What to look for")) -> None:
    """An explainer panel shown above a practice demo: what it does, why it
    matters, and what the reader should watch for. All strings are plain text."""
    l1, l2, l3 = labels
    st.markdown(
        '<div class="demo-intro">'
        f'<div class="di-row"><span class="di-k">{_esc(l1)}</span>'
        f'<span class="di-v">{_esc(what)}</span></div>'
        f'<div class="di-row"><span class="di-k">{_esc(l2)}</span>'
        f'<span class="di-v">{_esc(why)}</span></div>'
        f'<div class="di-row"><span class="di-k">{_esc(l3)}</span>'
        f'<span class="di-v">{_esc(expect)}</span></div>'
        '</div>',
        unsafe_allow_html=True,
    )


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
