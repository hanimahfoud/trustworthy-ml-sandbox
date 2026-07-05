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


class _Doc(FPDF):
    def __init__(self, lang):
        super().__init__(format="A4")
        self.lang = lang
        self.rtl = is_rtl(lang)
        self.set_auto_page_break(True, margin=18)
        self.add_font("Vazir", "", _REG)
        self.add_font("Vazir", "B", _BOLD)
        self.set_margins(18, 18, 18)

    def _wrap_logical(self, text: str, width: float) -> list[str]:
        """Word-wrap ``text`` to fit ``width`` mm, measuring in LOGICAL
        (reading) order -- i.e. *before* any bidi reshaping. This must happen
        first: reshaping/reversing the whole paragraph and then handing it to
        fpdf2's own multi_cell wrapper (as the previous version did) breaks
        word boundaries, because multi_cell splits on spaces in the already
        visually-reversed string, which is not where the real word breaks
        are. Wrapping on the logical string, then reshaping each finished
        line on its own, keeps both the wrapping and the visual order
        correct for Arabic and Persian."""
        words = text.split(" ")
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if not cur or self.get_string_width(trial) <= width:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines or [""]

    def _line(self, text, size=11, style="", gap=1.4, color=(32, 48, 63)):
        self.set_font("Vazir", style, size)
        self.set_text_color(*color)
        cleaned = _clean(text)
        line_h = size * 0.62
        if self.rtl:
            avail = self.w - self.l_margin - self.r_margin
            for ln in self._wrap_logical(cleaned, avail):
                shaped = get_display(arabic_reshaper.reshape(ln))
                self.cell(0, line_h, shaped, align="R", new_x="LMARGIN", new_y="NEXT")
        else:
            self.multi_cell(0, line_h, cleaned, align="L")
        self.ln(gap)


def build_pdf(lang: str, section: str) -> bytes:
    _ensure_fonts()
    doc = _Doc(lang)
    doc.add_page()

    doc._line(t(lang, "masthead_title"), size=20, style="B", gap=2,
              color=(14, 42, 71))
    # BUGFIX: the section subtitle used to be hardcoded to sec1/sec2 only,
    # so sections III-VI always printed "II - Explainability" in the header.
    # t(lang, section + "_title") works generically for every section.
    doc._line(t(lang, section + "_title"), size=13, style="B", gap=1,
              color=(138, 28, 43))
    doc._line(f'{t(lang, "byline_supervisor")}: {t(lang, "name_supervisor")}  ·  '
              f'{t(lang, "byline_author")}: {t(lang, "name_author")}',
              size=9, gap=4, color=(90, 107, 123))

    # Theory -- BUGFIX: loop ALL paragraph suffixes present (_p1.._p9), not a
    # hardcoded _p1.._p3; Section V topics have 4 paragraphs and were being
    # silently truncated.
    doc._line(t(lang, "pdf_theory_heading"), size=15, style="B", gap=2,
              color=(14, 42, 71))
    for key in nav.THEORY[section]:
        doc._line(t(lang, key), size=12, style="B", gap=1, color=(15, 110, 102))
        for i in range(1, 10):
            val = t(lang, f"{key}_p{i}")
            if not val or val == f"{key}_p{i}":
                break
            doc._line(val, size=10.5)
        call = t(lang, key + "_call")
        if call and call != key + "_call":
            doc._line(call, size=10.5, style="B", gap=3, color=(60, 90, 120))

    # Practice -- BUGFIX: sections I-IV use the "<key>_intro" convention, but
    # sections V-VI (and the retrofitted demo_intro standard) use
    # "<key>_what" / "_why" / "_expect" / "_note" instead; the old code only
    # ever looked for "_intro", so V/VI practice pages printed nothing.
    # We now support both conventions and include the full explainer.
    doc._line(t(lang, "pdf_practice_heading"), size=15, style="B", gap=2,
              color=(14, 42, 71))
    for key in nav.PRACTICE[section]:
        doc._line(t(lang, key), size=12, style="B", gap=1, color=(15, 110, 102))
        intro = t(lang, key + "_intro")
        if intro and intro != key + "_intro":
            doc._line(intro, size=10.5, gap=2)
        else:
            for suf, label_color in (("_what", (15, 110, 102)),
                                     ("_why", (15, 110, 102)),
                                     ("_expect", (15, 110, 102))):
                val = t(lang, key + suf)
                if val and val != key + suf:
                    doc._line(val, size=10.5, gap=2)
        note = t(lang, key + "_note")
        if note and note != key + "_note":
            doc._line(note, size=10.5, style="B", gap=3, color=(60, 90, 120))

    doc._line(t(lang, "pdf_generated"), size=8, gap=0, color=(150, 150, 150))

    out = doc.output()
    return bytes(out)
