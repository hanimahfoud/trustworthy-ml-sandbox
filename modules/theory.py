"""
modules/theory.py -- the six theory plates of Section I.

Each plate is a white "theorem plate" (st.container(border=True)) holding
localized prose, one typeset equation rendered with st.latex (notation is
language independent, so the LaTeX lives here, not in i18n), a mono figure
caption, and a key-idea or caution callout.
"""
from __future__ import annotations

import streamlit as st

import components as C
from i18n import t


def _p(text: str) -> str:
    return f"<p>{text}</p>"


# --------------------------------------------------------------------------- #
# 1) Bias–Variance                                                             #
# --------------------------------------------------------------------------- #
def bias_variance(lang: str) -> None:
    with st.container(border=True):
        C.plate_header(t(lang, "th_bv_eyebrow"), t(lang, "th_bv"))
        C.measure(_p(t(lang, "th_bv_p1")) + _p(t(lang, "th_bv_p2")))
        st.latex(
            r"\mathbb{E}_{\mathcal{D}}\big[(y-\hat f(x))^2\big]="
            r"\underbrace{\big(\mathbb{E}_{\mathcal{D}}[\hat f(x)]-f(x)\big)^2}_{\text{Bias}^2}"
            r"+\underbrace{\mathbb{E}_{\mathcal{D}}\big[(\hat f(x)-\mathbb{E}_{\mathcal{D}}[\hat f(x)])^2\big]}_{\text{Variance}}"
            r"+\underbrace{\sigma^2}_{\text{Noise}}"
        )
        C.figure_caption(t(lang, "th_bv_eqcap"))
        C.measure(_p(t(lang, "th_bv_p3")))
        C.key_idea(t(lang, "th_bv_call"))


# --------------------------------------------------------------------------- #
# 2) VC dimension & complexity                                                 #
# --------------------------------------------------------------------------- #
def vc_dimension(lang: str) -> None:
    with st.container(border=True):
        C.plate_header(t(lang, "th_vc_eyebrow"), t(lang, "th_vc"))
        C.measure(_p(t(lang, "th_vc_p1")) + _p(t(lang, "th_vc_p2")))
        st.latex(
            r"\underbrace{R(h)}_{\text{test risk}}\;\le\;"
            r"\underbrace{\hat R(h)}_{\text{train risk}}\;+\;"
            r"\mathcal{O}\!\left(\sqrt{\dfrac{D_{\mathrm{VC}}}{N}}\right)"
        )
        C.figure_caption(t(lang, "th_vc_eqcap"))
        C.measure(_p(t(lang, "th_vc_p3")))
        C.warn(t(lang, "th_vc_call"))


# --------------------------------------------------------------------------- #
# 3) Inductive bias                                                            #
# --------------------------------------------------------------------------- #
def inductive_bias(lang: str) -> None:
    with st.container(border=True):
        C.plate_header(t(lang, "th_ib_eyebrow"), t(lang, "th_ib"))
        C.measure(_p(t(lang, "th_ib_p1")) + _p(t(lang, "th_ib_p2")))
        st.latex(
            r"\min_{w}\;\mathcal{L}(w)+\lambda\lVert w\rVert_2^{2}\quad(\text{L2})"
            r"\qquad\text{vs.}\qquad"
            r"\min_{w}\;\mathcal{L}(w)+\lambda\lVert w\rVert_1\quad(\text{L1})"
        )
        C.figure_caption(t(lang, "th_ib_eqcap"))
        C.measure(_p(t(lang, "th_ib_p3")))
        C.key_idea(t(lang, "th_ib_call"))


# --------------------------------------------------------------------------- #
# 4) Transfer & domain adaptation                                              #
# --------------------------------------------------------------------------- #
def transfer(lang: str) -> None:
    with st.container(border=True):
        C.plate_header(t(lang, "th_tl_eyebrow"), t(lang, "th_tl"))
        C.measure(_p(t(lang, "th_tl_p1")) + _p(t(lang, "th_tl_p2")))
        st.latex(
            r"\mathrm{MMD}^2(P,Q)=\Big\lVert\,"
            r"\mathbb{E}_{x\sim P}[\phi(x)]-\mathbb{E}_{x\sim Q}[\phi(x)]"
            r"\,\Big\rVert_{\mathcal{H}}^{2}"
        )
        C.figure_caption(t(lang, "th_tl_eqcap"))
        C.measure(_p(t(lang, "th_tl_p3")))
        C.key_idea(t(lang, "th_tl_call"))


# --------------------------------------------------------------------------- #
# 5) Sharpness-Aware Minimization                                              #
# --------------------------------------------------------------------------- #
def sam(lang: str) -> None:
    with st.container(border=True):
        C.plate_header(t(lang, "th_sam_eyebrow"), t(lang, "th_sam"))
        C.measure(_p(t(lang, "th_sam_p1")) + _p(t(lang, "th_sam_p2")))
        st.latex(
            r"\min_{w}\;\max_{\lVert\epsilon\rVert_2\le\rho}\;\mathcal{L}(w+\epsilon)"
        )
        C.figure_caption(t(lang, "th_sam_eqcap"))
        C.measure(_p(t(lang, "th_sam_p3")))
        C.key_idea(t(lang, "th_sam_call"))


# --------------------------------------------------------------------------- #
# 6) Causal foundations                                                        #
# --------------------------------------------------------------------------- #
def causality(lang: str) -> None:
    with st.container(border=True):
        C.plate_header(t(lang, "th_cz_eyebrow"), t(lang, "th_cz"))
        C.measure(_p(t(lang, "th_cz_p1")) + _p(t(lang, "th_cz_p2")))
        st.latex(
            r"P\big(Y\mid \mathrm{do}(X{=}x)\big)\;\neq\;P\big(Y\mid X{=}x\big)"
        )
        C.figure_caption(t(lang, "th_cz_eqcap"))
        C.measure(_p(t(lang, "th_cz_p3")))
        C.warn(t(lang, "th_cz_call"))


# Registry consumed by app.py (key -> render function).
SECTIONS = {
    "th_bv": bias_variance,
    "th_vc": vc_dimension,
    "th_ib": inductive_bias,
    "th_tl": transfer,
    "th_sam": sam,
    "th_cz": causality,
}
