"""
modules/rob_smoothing.py -- Practice demo: randomized smoothing certificate.

Add Gaussian noise N times to a sample, take the majority vote, and compute the
provable Cohen et al. L2 radius R = sigma * Phi^{-1}(pA). Every number is
measured live on the trained CNN.
"""
from __future__ import annotations

import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import vision_core as V
from core import robustness_core as R
from i18n import t


@st.cache_resource(show_spinner=False)
def _net():
    net, acc = V.train_cnn(spurious=False, seed=0)
    return net


@st.cache_data(show_spinner=False)
def _samples():
    X, y, _ = V.make_shapes_dataset(6, spurious=False, seed=42)
    return X, y


@st.cache_data(show_spinner=False)
def _certify(idx, sigma, n):
    net = _net()
    X, y = _samples()
    return R.randomized_smoothing(net, X[idx:idx + 1], sigma=sigma, n=n, seed=0)


def render(lang):
    X, y = _samples()

    with st.container(border=True):
        C.plate_header(t(lang, "prb_smoothing_eyebrow"), t(lang, "prb_smoothing"))
        C.measure(f"<p>{t(lang, 'prb_smoothing_intro')}</p>")

        c1, c2, c3 = st.columns(3)
        with c1:
            idx = st.selectbox(t(lang, "prb_smoothing_sample"), list(range(6)),
                               format_func=lambda i: f"#{i + 1}")
        with c2:
            sigma = st.slider(t(lang, "prb_smoothing_sigma"), 0.05, 0.60, 0.25, 0.05)
        with c3:
            n = st.slider(t(lang, "prb_smoothing_n"), 100, 800, 300, 100)

        cert = _certify(idx, sigma, n)
        cls = t(lang, "px_cv_class" + str(cert["prediction"]))

        fig = go.Figure(go.Bar(
            x=[t(lang, "px_cv_class0"), t(lang, "px_cv_class1")],
            y=cert["votes"], marker_color=[P.TEAL, P.CRIMSON]))
        P.style_2d(fig, x_title="", y_title="votes", height=300, legend=False)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "prb_smoothing_cap_votes"))

        C.readout_strip([
            {"k": "prediction", "v": cls, "color": "teal"},
            {"k": "pA (lower)", "v": f"{cert['p_a_lower']:.3f}"},
            {"k": "L2 radius R", "v": f"{cert['radius']:.3f}",
             "color": "teal" if cert["certified"] else "crimson"},
            {"k": "σ", "v": f"{sigma:.2f}"},
            {"k": "N", "v": str(n)},
        ])
        if cert["certified"]:
            C.key_idea(t(lang, "prb_smoothing_cert").format(
                cls=cls, r=cert["radius"], p=cert["p_a_lower"]))
        else:
            C.warn(t(lang, "prb_smoothing_uncert"))
        C.measure(f"<p>{t(lang, 'prb_smoothing_note')}</p>")
