"""
modules/spurious.py -- Practice demo: exposing a shortcut with Grad-CAM.

Two networks are trained: one on clean shapes, one on data where a bright
bottom band is perfectly correlated with class 0. On the same class-0 image,
the clean model's Grad-CAM lands on the object while the shortcut model's lands
on the band -- a black box that is right for the wrong reason.
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
def _nets():
    clean, acc_c = V.train_cnn(spurious=False, seed=0)
    short, acc_s = V.train_cnn(spurious=True, seed=0)
    return clean, acc_c, short, acc_s


@st.cache_data(show_spinner=False)
def _sample():
    # a class-0 image that carries the shortcut band
    X, y, bb = V.make_shapes_dataset(40, spurious=True, seed=7)
    i = int(np.where(y == 0)[0][0])
    return X[i:i + 1], bb[i]


def _overlay(img, cam, height=300):
    fig = go.Figure(go.Heatmap(z=img, colorscale="gray", showscale=False,
                               zmin=0, zmax=1))
    fig.add_trace(go.Heatmap(z=cam, colorscale=P.TEAL_SCALE, showscale=False,
                             opacity=0.55, zmin=0, zmax=1))
    fig.update_layout(height=height, margin=dict(l=4, r=4, t=6, b=4),
                      paper_bgcolor=P.CARD, plot_bgcolor=P.CARD,
                      xaxis=dict(visible=False),
                      yaxis=dict(visible=False, scaleanchor="x",
                                 autorange="reversed"))
    return fig


def render(lang):
    clean, acc_c, short, acc_s = _nets()
    x, bb = _sample()

    cam_clean = clean.grad_cam(x, 0)
    cam_short = short.grad_cam(x, 0)

    cue = np.zeros((V.H, V.W), bool); cue[V.CUE_ROWS, :] = True
    y0, y1, x0, x1 = bb
    shape_mask = np.zeros((V.H, V.W), bool); shape_mask[y0:y1, x0:x1] = True
    obj_energy = V.cam_energy_in_region(cam_clean, shape_mask)
    band_energy = V.cam_energy_in_region(cam_short, cue)

    with st.container(border=True):
        C.plate_header(t(lang, "px_spurious_eyebrow"), t(lang, "px_spurious"))
        C.demo_intro(t(lang, "px_spurious_what"), t(lang, "px_spurious_why"),
                 t(lang, "px_spurious_expect"),
                 labels=(t(lang, "di_what"), t(lang, "di_why"),
                         t(lang, "di_expect")))

        col_a, col_b = st.columns(2)
        with col_a:
            st.plotly_chart(_overlay(x[0, 0], cam_clean),
                            use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "px_spurious_cap_clean"))
        with col_b:
            st.plotly_chart(_overlay(x[0, 0], cam_short),
                            use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "px_spurious_cap_short"))

        C.readout_strip([
            {"k": t(lang, "px_spurious_energy_clean"), "v": f"{obj_energy:.2f}",
             "color": "teal"},
            {"k": t(lang, "px_spurious_energy_short"), "v": f"{band_energy:.2f}",
             "color": "crimson"},
            {"k": "clean acc", "v": f"{acc_c:.2f}"},
            {"k": "shortcut acc", "v": f"{acc_s:.2f}"},
        ])
        C.warn(t(lang, "px_spurious_warn"))
