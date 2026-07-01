"""
modules/pdf_export.py -- build a printable PDF of a section's theory and
practice text in the current language.

Text is pulled from the i18n dictionary via the shared nav registry, HTML tags
are stripped, and Arabic/Persian is shaped (arabic_reshaper + python-bidi) and
right-aligned so it renders correctly. A single Unicode font (Vazirmatn) covers
Arabic, Persian and Latin.
"""
from __future__ import annotations

import html
import os
import re
import urllib.request

import arabic_reshaper
from bidi.algorithm import get_display
from fpdf import FPDF

import nav
from i18n import is_rtl, t

_HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_ASSETS = os.path.join(_HERE, "assets")
_REG = os.path.join(_ASSETS, "Vazirmatn-Regular.ttf")
_BOLD = os.path.join(_ASSETS, "Vazirmatn-Bold.ttf")

# The .ttf fonts are binary, which Hugging Face's plain-git push rejects, so
# they are not stored in the repo. On first use we fetch them once from the
# official Vazirmatn release and cache them locally. (Runs on the server, not
# in the browser; the download host is reachable from Spaces.)
_FONT_URLS = {
    _REG: "https://raw.githubusercontent.com/rastikerdar/vazirmatn/master/"
          "fonts/ttf/Vazirmatn-Regular.ttf",
    _BOLD: "https://raw.githubusercontent.com/rastikerdar/vazirmatn/master/"
           "fonts/ttf/Vazirmatn-Bold.ttf",
}


def _ensure_fonts():
    os.makedirs(_ASSETS, exist_ok=True)
    for path, url in _FONT_URLS.items():
        if not os.path.exists(path) or os.path.getsize(path) < 50000:
            urllib.request.urlretrieve(url, path)

_TAG = re.compile(r"<[^>]+>")

# Vazirmatn lacks a few Greek/math glyphs used in some captions; transliterate
# them so the PDF never shows empty boxes.
_TRANSLIT = {
    "λ": "lambda", "ρ": "rho", "α": "alpha", "β": "beta", "σ": "sigma",
    "μ": "mu", "ε": "epsilon", "φ": "phi", "∣": "|", "≈": "~=", "→": "->",
    "∈": "in", "×": "x", "²": "2",
}


def _clean(text: str) -> str:
    """Strip HTML tags, unescape entities, transliterate unsupported glyphs."""
    text = html.unescape(_TAG.sub("", text))
    for k, v in _TRANSLIT.items():
        text = text.replace(k, v)
    return text.replace("  ", " ").strip()


def _shape(text: str, lang: str) -> str:
    if is_rtl(lang):
        return get_display(arabic_reshaper.reshape(text))
    return text


class _Doc(FPDF):
    def __init__(self, lang):
        super().__init__(format="A4")
        self.lang = lang
        self.rtl = is_rtl(lang)
        self.set_auto_page_break(True, margin=18)
        self.add_font("Vazir", "", _REG)
        self.add_font("Vazir", "B", _BOLD)
        self.set_margins(18, 18, 18)

    def _line(self, text, size=11, style="", gap=1.4, color=(32, 48, 63)):
        self.set_font("Vazir", style, size)
        self.set_text_color(*color)
        align = "R" if self.rtl else "L"
        self.multi_cell(0, size * 0.62, _shape(_clean(text), self.lang),
                        align=align)
        self.ln(gap)


def build_pdf(lang: str, section: str) -> bytes:
    _ensure_fonts()
    doc = _Doc(lang)
    doc.add_page()

    doc._line(t(lang, "masthead_title"), size=20, style="B", gap=2,
              color=(14, 42, 71))
    sub = "sec1_title" if section == "sec1" else "sec2_title"
    doc._line(t(lang, sub), size=13, style="B", gap=1, color=(138, 28, 43))
    doc._line(f'{t(lang, "byline_supervisor")}: {t(lang, "name_supervisor")}  ·  '
              f'{t(lang, "byline_author")}: {t(lang, "name_author")}',
              size=9, gap=4, color=(90, 107, 123))

    # Theory
    doc._line(t(lang, "pdf_theory_heading"), size=15, style="B", gap=2,
              color=(14, 42, 71))
    for key in nav.THEORY[section]:
        doc._line(t(lang, key), size=12, style="B", gap=1, color=(15, 110, 102))
        for suf in ("_p1", "_p2", "_p3"):
            val = t(lang, key + suf)
            if val and val != key + suf:
                doc._line(val, size=10.5)
        call = t(lang, key + "_call")
        if call and call != key + "_call":
            doc._line(call, size=10.5, style="B", gap=3, color=(60, 90, 120))

    # Practice
    doc._line(t(lang, "pdf_practice_heading"), size=15, style="B", gap=2,
              color=(14, 42, 71))
    for key in nav.PRACTICE[section]:
        doc._line(t(lang, key), size=12, style="B", gap=1, color=(15, 110, 102))
        intro = t(lang, key + "_intro")
        if intro and intro != key + "_intro":
            doc._line(intro, size=10.5, gap=3)

    doc._line(t(lang, "pdf_generated"), size=8, gap=0, color=(150, 150, 150))

    out = doc.output()
    return bytes(out)
