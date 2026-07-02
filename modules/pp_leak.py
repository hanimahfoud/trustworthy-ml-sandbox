"""
modules/pp_leak.py -- Practice demo: Federated gradient-leakage simulator.

A client shares only the gradient of a linear model for one private image.
Press the button and the server reconstructs the image from the gradient alone,
showing that federated learning by itself is not private.
"""
from __future__ import annotations

import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import vision_core as V
from core import privacy_core as PV
from i18n import t


@st.cache_data(show_spinner=False)
def _samples():
    X, y, _ = V.make_shapes_dataset(6, spurious=False, seed=31)
    return X, y


def _img_fig(z, height=300):
    fig = go.Figure(go.Heatmap(z=z, colorscale="gray", showscale=False,
                               zmin=0, zmax=1))
    fig.update_layout(height=height, margin=dict(l=4, r=4, t=6, b=4),
                      paper_bgcolor=P.CARD, plot_bgcolor=P.CARD,
                      xaxis=dict(visible=False),
                      yaxis=dict(visible=False, scaleanchor="x",
                                 autorange="reversed"))
    return fig


def _noise_fig(dW, height=300):
    fig = go.Figure(go.Heatmap(z=dW, colorscale="RdBu", showscale=False))
    fig.update_layout(height=height, margin=dict(l=4, r=4, t=6, b=4),
                      paper_bgcolor=P.CARD, plot_bgcolor=P.CARD,
                      xaxis=dict(visible=False),
                      yaxis=dict(visible=False, autorange="reversed"))
    return fig


def render(lang):
    X, y = _samples()

    with st.container(border=True):
        C.plate_header(t(lang, "pp_leak_eyebrow"), t(lang, "pp_leak"))
        C.demo_intro(t(lang, "pp_leak_what"), t(lang, "pp_leak_why"),
                     t(lang, "pp_leak_expect"),
                     labels=(t(lang, "di_what"), t(lang, "di_why"),
                             t(lang, "di_expect")))

        c1, c2 = st.columns(2)
        with c1:
            idx = st.selectbox(t(lang, "pp_leak_sample"), list(range(6)),
                               format_func=lambda i: f"#{i + 1}")
        with c2:
            run = st.checkbox(t(lang, "pp_leak_run"), value=False)

        x = X[idx, 0]
        r = PV.gradient_leakage_linear(x.ravel(), int(y[idx]), n_classes=2, seed=0)

        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(_img_fig(x), use_container_width=True,
                            config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "pp_leak_cap_true"))
        with col2:
            if run:
                st.plotly_chart(_img_fig(r["x_rec"].reshape(V.H, V.W)),
                                use_container_width=True, config=P.PLOTLY_CONFIG)
                C.figure_caption(t(lang, "pp_leak_cap_rec"))
            else:
                # show the "obfuscated" shared gradient before the attack runs
                st.plotly_chart(_noise_fig(r["dW"]), use_container_width=True,
                                config=P.PLOTLY_CONFIG)
                C.figure_caption("shared gradient dW (obfuscated)")

        if run:
            C.readout_strip([
                {"k": t(lang, "pp_leak_err"), "v": f"{r['rel_error']:.1e}",
                 "color": "crimson"},
                {"k": "status", "v": "reconstructed", "color": "crimson"},
            ])
            C.warn(t(lang, "pp_leak_note"))
        else:
            C.key_idea(t(lang, "pp_leak_note"))
