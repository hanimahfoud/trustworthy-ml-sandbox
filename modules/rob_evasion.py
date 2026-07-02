"""
modules/rob_evasion.py -- Practice demo: live evasion attack on our CNN.

Pick a sample and an attack (FGSM or PGD), move the epsilon slider, and watch
the trained network's prediction flip. The perturbation is a real
gradient-based attack (core.robustness_core) on the from-scratch NumPy CNN.
"""
from __future__ import annotations

import numpy as np
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
    X, y, _ = V.make_shapes_dataset(8, spurious=False, seed=123)
    return X, y


def _img_fig(z, scale="gray", height=280):
    fig = go.Figure(go.Heatmap(z=z, colorscale=scale, showscale=False,
                               zmin=0, zmax=1))
    fig.update_layout(height=height, margin=dict(l=4, r=4, t=6, b=4),
                      paper_bgcolor=P.CARD, plot_bgcolor=P.CARD,
                      xaxis=dict(visible=False),
                      yaxis=dict(visible=False, scaleanchor="x",
                                 autorange="reversed"))
    return fig


def render(lang):
    net = _net()
    X, y = _samples()

    with st.container(border=True):
        C.plate_header(t(lang, "prb_evasion_eyebrow"), t(lang, "prb_evasion"))
        C.measure(f"<p>{t(lang, 'prb_evasion_intro')}</p>")

        c1, c2, c3 = st.columns(3)
        with c1:
            idx = st.selectbox(t(lang, "prb_evasion_sample"), list(range(8)),
                               format_func=lambda i: f"#{i + 1}")
        with c2:
            methods = ["prb_evasion_m_fgsm", "prb_evasion_m_pgd"]
            method = st.selectbox(t(lang, "prb_evasion_method"), methods,
                                  format_func=lambda k: t(lang, k))
        with c3:
            eps = st.slider(t(lang, "prb_evasion_eps"), 0.0, 0.5, 0.20, 0.01)

        x = X[idx:idx + 1]
        m = "fgsm" if method == "prb_evasion_m_fgsm" else "pgd"
        x_adv = R.attack(net, x, int(y[idx]), eps, method=m, steps=12)

        p_clean = int(net.predict(x)[0])
        p_adv = int(net.predict(x_adv)[0])
        conf_clean = float(net.probs(x)[0, p_clean])
        conf_adv = float(net.probs(x_adv)[0, p_adv])

        # amplified perturbation for display
        pert = np.clip(0.5 + 5.0 * (x_adv[0, 0] - x[0, 0]), 0, 1)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.plotly_chart(_img_fig(x[0, 0]), use_container_width=True,
                            config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "prb_evasion_cap_orig"))
        with col2:
            st.plotly_chart(_img_fig(pert, scale="RdBu"),
                            use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "prb_evasion_cap_noise"))
        with col3:
            st.plotly_chart(_img_fig(x_adv[0, 0]), use_container_width=True,
                            config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "prb_evasion_cap_adv"))

        flipped = p_adv != p_clean
        C.readout_strip([
            {"k": t(lang, "prb_evasion_pred_clean"),
             "v": f"{t(lang, 'px_cv_class'+str(p_clean))} ({conf_clean:.2f})",
             "color": "teal"},
            {"k": t(lang, "prb_evasion_pred_adv"),
             "v": f"{t(lang, 'px_cv_class'+str(p_adv))} ({conf_adv:.2f})",
             "color": "crimson" if flipped else "teal"},
            {"k": "L∞ perturbation", "v": f"{np.abs(x_adv-x).max():.3f}"},
        ])
        C.key_idea(t(lang, "prb_evasion_note"))
