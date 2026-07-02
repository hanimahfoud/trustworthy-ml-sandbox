"""
modules/pp_laplace.py -- Practice demo: Laplace privacy dashboard.

Publish a salary histogram under the Laplace mechanism. Move the privacy budget
epsilon and watch the noise (and distortion) grow as privacy increases.
"""
from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import privacy_core as PV
from i18n import t


@st.cache_data(show_spinner=False)
def _salaries():
    rng = np.random.default_rng(0)
    return rng.normal(5000, 1300, 1500)


def render(lang):
    salaries = _salaries()
    bins = np.linspace(salaries.min(), salaries.max(), 14)

    with st.container(border=True):
        C.plate_header(t(lang, "pp_laplace_eyebrow"), t(lang, "pp_laplace"))
        C.demo_intro(t(lang, "pp_laplace_what"), t(lang, "pp_laplace_why"),
                     t(lang, "pp_laplace_expect"),
                     labels=(t(lang, "di_what"), t(lang, "di_why"),
                             t(lang, "di_expect")))

        eps = st.slider(t(lang, "pp_laplace_eps"), 0.01, 10.0, 1.0, 0.01)
        true_c, noisy_c, edges = PV.dp_histogram(salaries, bins, epsilon=eps, seed=0)
        centers = 0.5 * (edges[:-1] + edges[1:])

        fig = go.Figure()
        fig.add_trace(go.Bar(x=centers, y=true_c, name="true",
                             marker_color=P.TEAL, opacity=0.55))
        fig.add_trace(go.Bar(x=centers, y=noisy_c, name="private (DP)",
                             marker_color=P.CRIMSON, opacity=0.75))
        fig.update_layout(barmode="overlay")
        P.style_2d(fig, x_title="salary", y_title="count", height=320)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "pp_laplace_cap"))

        distortion = float(np.mean(np.abs(noisy_c - true_c)))
        scale = 1.0 / max(eps, 1e-6)
        C.readout_strip([
            {"k": "ε", "v": f"{eps:.2f}"},
            {"k": t(lang, "pp_laplace_scale"), "v": f"{scale:.2f}"},
            {"k": t(lang, "pp_laplace_err"), "v": f"{distortion:.2f}",
             "color": "crimson" if distortion > 5 else "teal"},
        ])
        C.key_idea(t(lang, "pp_laplace_note"))
