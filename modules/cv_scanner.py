"""
modules/cv_scanner.py -- Practice demo: attribution maps for the NumPy CNN.

The convolutional network (core.vision_core) is trained once and cached. The
reader chooses a sample, an attribution method and a target class, and sees the
real gradient-based explanation overlaid on the image.
"""
from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import vision_core as V
from i18n import t


@st.cache_resource(show_spinner=False)
def _net():
    net, acc = V.train_cnn(spurious=False, seed=0)
    return net, acc


@st.cache_data(show_spinner=False)
def _samples():
    X, y, bb = V.make_shapes_dataset(8, spurious=False, seed=123)
    return X, y, bb


def _img_fig(z, scale, height=300, overlay=None):
    fig = go.Figure(go.Heatmap(z=z, colorscale=scale, showscale=False,
                               zmin=0, zmax=1))
    if overlay is not None:
        fig.add_trace(go.Heatmap(z=overlay, colorscale=P.TEAL_SCALE,
                                 showscale=False, opacity=0.55, zmin=0, zmax=1))
    fig.update_layout(
        height=height, margin=dict(l=4, r=4, t=6, b=4),
        paper_bgcolor=P.CARD, plot_bgcolor=P.CARD,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False, scaleanchor="x", autorange="reversed"))
    return fig


def render(lang):
    net, acc = _net()
    X, y, bb = _samples()

    with st.container(border=True):
        C.plate_header(t(lang, "px_cv_eyebrow"), t(lang, "px_cv"))
        C.demo_intro(t(lang, "px_cv_what"), t(lang, "px_cv_why"),
                 t(lang, "px_cv_expect"),
                 labels=(t(lang, "di_what"), t(lang, "di_why"),
                         t(lang, "di_expect")))

        c1, c2, c3 = st.columns(3)
        with c1:
            idx = st.selectbox(t(lang, "px_cv_sample"), list(range(8)),
                               format_func=lambda i: f"#{i + 1}")
        with c2:
            methods = ["px_cv_m_gradcam", "px_cv_m_saliency", "px_cv_m_guided"]
            method = st.selectbox(t(lang, "px_cv_method"), methods,
                                  format_func=lambda k: t(lang, k))
        with c3:
            target = st.selectbox(t(lang, "px_cv_target"), [0, 1],
                                  format_func=lambda v: t(lang, f"px_cv_class{v}"))

        x = X[idx:idx + 1]
        pred = int(net.predict(x)[0])
        prob = float(net.probs(x)[0, pred])

        if method == "px_cv_m_gradcam":
            cam = net.grad_cam(x, target)
        elif method == "px_cv_m_saliency":
            cam = net.saliency(x, target)
        else:
            cam = net.guided_grad_cam(x, target)

        C.readout_strip([
            {"k": t(lang, "px_cv_pred"),
             "v": t(lang, f"px_cv_class{pred}"),
             "color": "teal" if pred == int(y[idx]) else "crimson"},
            {"k": "confidence", "v": f"{prob:.3f}"},
            {"k": "model train acc", "v": f"{acc:.3f}"},
        ])

        col_a, col_b = st.columns(2)
        with col_a:
            st.plotly_chart(_img_fig(X[idx, 0], "gray"),
                            use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "px_cv_cap_input"))
        with col_b:
            st.plotly_chart(_img_fig(X[idx, 0], "gray", overlay=cam),
                            use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "px_cv_cap_map").format(
                method=t(lang, method)))
