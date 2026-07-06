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


def hero_art() -> str:
    """Return an inline SVG that evokes Trustworthy ML: a small neural network
    whose output is guarded by a shield bearing a checkmark. Uses currentColor
    and theme vars so it adapts to light/dark. Returned as a string to embed."""
    return (
        '<svg class="hero-art" viewBox="0 0 240 150" xmlns="http://www.w3.org/2000/svg" '
        'role="img" aria-label="trustworthy machine learning">'
        # edges (network)
        '<g stroke="var(--hero-art-edge)" stroke-width="1.4" opacity="0.55">'
        '<line x1="34" y1="40" x2="96" y2="30"/><line x1="34" y1="40" x2="96" y2="75"/>'
        '<line x1="34" y1="110" x2="96" y2="75"/><line x1="34" y1="110" x2="96" y2="120"/>'
        '<line x1="34" y1="75" x2="96" y2="30"/><line x1="34" y1="75" x2="96" y2="120"/>'
        '<line x1="96" y1="30" x2="150" y2="52"/><line x1="96" y1="75" x2="150" y2="52"/>'
        '<line x1="96" y1="120" x2="150" y2="98"/><line x1="96" y1="75" x2="150" y2="98"/>'
        '</g>'
        # nodes
        '<g fill="var(--hero-art-node)">'
        '<circle cx="34" cy="40" r="7"/><circle cx="34" cy="75" r="7"/>'
        '<circle cx="34" cy="110" r="7"/><circle cx="96" cy="30" r="7"/>'
        '<circle cx="96" cy="75" r="7"/><circle cx="96" cy="120" r="7"/>'
        '<circle cx="150" cy="52" r="7"/><circle cx="150" cy="98" r="7"/>'
        '</g>'
        # shield (trust) with checkmark
        '<path d="M198 34 L226 44 L226 78 C226 100 212 112 198 120 '
        'C184 112 170 100 170 78 L170 44 Z" '
        'fill="var(--hero-art-shield)" stroke="var(--hero-art-shieldline)" stroke-width="2"/>'
        '<path d="M186 76 L195 86 L212 62" fill="none" stroke="#fff" '
        'stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>'
        # connector from network to shield
        '<line x1="150" y1="52" x2="172" y2="60" stroke="var(--hero-art-edge)" '
        'stroke-width="1.4" opacity="0.55"/>'
        '<line x1="150" y1="98" x2="172" y2="92" stroke="var(--hero-art-edge)" '
        'stroke-width="1.4" opacity="0.55"/>'
        '</svg>'
    )


def footer(text: str) -> None:
    """A simple, elegant copyright footer."""
    st.markdown(f'<div class="site-footer">{_esc(text)}</div>',
                unsafe_allow_html=True)


def hero(eyebrow: str, title: str, summary: str, practice_note: str = "",
         byline: list[dict] | None = None) -> None:
    """A centered hero band under the navbar: course name, byline
    (supervisor / author), course summary, and a short note on what choosing
    Theory vs Practice means."""
    byline_html = ""
    if byline:
        cells = "".join(
            f'<div class="cell"><span class="lab">{_esc(b.get("label", ""))}</span>'
            f'<b>{_esc(b.get("name", ""))}</b></div>'
            for b in byline
        )
        byline_html = f'<div class="hero-byline">{cells}</div>'
    note_html = (f'<div class="hero-practice-note">{_esc(practice_note)}</div>'
                if practice_note else "")
    st.markdown(
        f"""
        <div class="hero hero-blue">
          <div class="hero-art-wrap">{hero_art()}</div>
          <div class="hero-eyebrow">{_esc(eyebrow)}</div>
          <div class="hero-title">{_esc(title)}</div>
          {byline_html}
          <div class="hero-summary">{_esc(summary)}</div>
          {note_html}
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


def info_panel(title: str, body: str, rows: list | None = None,
               links: list | None = None, note: str | None = None) -> None:
    """A framed information panel (used for About / Contact overlays).

    ``rows``  -- list of (label, value) tuples rendered as a definition list;
                 values get dir="auto" so phone numbers / emails stay LTR in RTL.
    ``links`` -- list of (label, url) tuples rendered as pill link-buttons.
    ``note``  -- an italic footnote under a hairline (e.g. support notice).
    """
    rows_html = ""
    if rows:
        cells = "".join(
            f'<div class="ip-row"><span class="ip-k">{_esc(k)}</span>'
            f'<span class="ip-v" dir="auto">{_esc(v)}</span></div>' for k, v in rows)
        rows_html = f'<div class="ip-rows">{cells}</div>'
    links_html = ""
    if links:
        anchors = "".join(
            f'<a class="ip-link" href="{_esc(u)}" target="_blank" '
            f'rel="noopener noreferrer">{_esc(lbl)}</a>' for lbl, u in links)
        links_html = f'<div class="ip-links">{anchors}</div>'
    note_html = f'<div class="ip-note">{_esc(note)}</div>' if note else ""
    st.markdown(
        f'<div class="info-panel"><div class="ip-title">{_esc(title)}</div>'
        f'<div class="ip-body">{_esc(body)}</div>{rows_html}{links_html}{note_html}</div>',
        unsafe_allow_html=True,
    )


def dedication(eyebrow: str, text: str) -> None:
    """A book-style dedication strip: a small mono eyebrow, a fleuron ornament,
    and a centered italic sentence between gold hairlines. Used under the hero
    for the acknowledgment to the course supervisor."""
    st.markdown(
        f'<div class="dedication">'
        f'<div class="ded-eyebrow">{_esc(eyebrow)}</div>'
        f'<div class="ded-ornament" aria-hidden="true">❦</div>'
        f'<div class="ded-text">{_esc(text)}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


def sitemap_head(eyebrow: str, root_label: str) -> None:
    """The glowing head of the interactive site-map tree: a mono eyebrow, the
    pulsing root node, a vertical stem and a shimmering rail from which the
    six section branch-cards (real Streamlit buttons) hang."""
    st.markdown(
        f'<div class="rm-head">'
        f'<div class="rm-eyebrow">{_esc(eyebrow)}</div>'
        f'<div class="rm-root">✦ {_esc(root_label)}</div>'
        f'<div class="rm-stem"></div>'
        f'<div class="rm-rail"></div>'
        f'</div>',
        unsafe_allow_html=True,
    )


def sitemap_group(label: str) -> None:
    """A small 'Theory' / 'Practice' branch label inside a site-map card."""
    st.markdown(f'<div class="rm-group">{_esc(label)}</div>',
                unsafe_allow_html=True)


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
