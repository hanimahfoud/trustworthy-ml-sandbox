"""
modules/theory_privacy.py -- the six theory plates of Section V (Privacy,
Poisoning & Federated Learning). Prose is full and explanatory; the poisoning,
privacy, DP and leakage plates carry real computed figures.
"""
from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import vision_core as V
from core import privacy_core as PV
from i18n import t


def _p(text):
    return f"<p>{text}</p>"


@st.cache_resource(show_spinner=False)
def _backdoored():
    net, clean_acc, target = PV.make_backdoored_cnn(target=1, seed=0)
    return net, clean_acc, target


@st.cache_data(show_spinner=False)
def _mi():
    return PV.membership_inference_demo(seed=0)


def _img_fig(z, scale="gray", height=200):
    fig = go.Figure(go.Heatmap(z=z, colorscale=scale, showscale=False,
                               zmin=0, zmax=1))
    fig.update_layout(height=height, margin=dict(l=4, r=4, t=6, b=4),
                      paper_bgcolor=P.CARD, plot_bgcolor=P.CARD,
                      xaxis=dict(visible=False),
                      yaxis=dict(visible=False, scaleanchor="x",
                                 autorange="reversed"))
    return fig


# 1) poisoning & backdoors -- REAL backdoored CNN
def poison(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "prv_poison_eyebrow"), t(lang, "prv_poison"))
        C.measure(_p(t(lang, "prv_poison_p1")) + _p(t(lang, "prv_poison_p2")))
        net, clean_acc, target = _backdoored()
        X, y, _ = V.make_shapes_dataset(4, spurious=False, seed=55)
        x = X[0:1]
        xt = PV.stamp_trigger(x)
        pc = int(net.predict(x)[0]); pt = int(net.predict(xt)[0])
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(_img_fig(x[0, 0]), use_container_width=True,
                            config=P.PLOTLY_CONFIG)
            C.figure_caption(f"clean → <b>{t(lang, 'px_cv_class'+str(pc))}</b>")
        with col2:
            st.plotly_chart(_img_fig(xt[0, 0]), use_container_width=True,
                            config=P.PLOTLY_CONFIG)
            C.figure_caption(f"triggered → <b>{t(lang, 'px_cv_class'+str(pt))}</b>")
        C.figure_caption(t(lang, "prv_poison_eqcap"))
        C.measure(_p(t(lang, "prv_poison_p3")) + _p(t(lang, "prv_poison_p4")))
        C.key_idea(t(lang, "prv_poison_call"))


# 2) privacy attacks -- REAL membership-inference confidence gap
def privacy(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "prv_privacy_eyebrow"), t(lang, "prv_privacy"))
        C.measure(_p(t(lang, "prv_privacy_p1")) + _p(t(lang, "prv_privacy_p2")))
        r = _mi()
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=r["conf_members"], name="members",
                                   marker_color=P.CRIMSON, opacity=0.6, nbinsx=25))
        fig.add_trace(go.Histogram(x=r["conf_nonmembers"], name="non-members",
                                   marker_color=P.TEAL, opacity=0.6, nbinsx=25))
        fig.update_layout(barmode="overlay")
        P.style_2d(fig, x_title="confidence on true label", y_title="count",
                   height=260)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "prv_privacy_eqcap") +
                         f" &nbsp; attack acc = {r['attack_accuracy']:.2f}")
        C.measure(_p(t(lang, "prv_privacy_p3")))
        C.measure(_p(t(lang, "prv_privacy_p4")))
        C.key_idea(t(lang, "prv_privacy_call"))


# 3) differential privacy -- epsilon trade-off curve
def dp(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "prv_dp_eyebrow"), t(lang, "prv_dp"))
        C.measure(_p(t(lang, "prv_dp_p1")) + _p(t(lang, "prv_dp_p2")))
        st.latex(r"P\big(M(D_1)=y\big)\;\le\;e^{\epsilon}\,\cdot\,P\big(M(D_2)=y\big)")
        eps = np.linspace(0.01, 5, 120)
        privacy_level = np.exp(-eps)          # schematic: privacy decays with eps
        utility = 1 - np.exp(-eps)            # utility rises with eps
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=eps, y=privacy_level, mode="lines",
                                 name="privacy", line=dict(color=P.TEAL, width=2)))
        fig.add_trace(go.Scatter(x=eps, y=utility, mode="lines",
                                 name="utility", line=dict(color=P.CRIMSON, width=2)))
        P.style_2d(fig, x_title="privacy budget ε", y_title="", height=260)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "prv_dp_eqcap"))
        C.measure(_p(t(lang, "prv_dp_p3")))
        C.measure(_p(t(lang, "prv_dp_p4")))
        C.key_idea(t(lang, "prv_dp_call"))


# 4) noise mechanisms -- Laplace distribution at two scales
def noise(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "prv_noise_eyebrow"), t(lang, "prv_noise"))
        C.measure(_p(t(lang, "prv_noise_p1")) + _p(t(lang, "prv_noise_p2")))
        st.latex(r"\text{Laplace noise scale} = \frac{\Delta}{\epsilon}")
        xs = np.linspace(-6, 6, 400)
        def lap(b): return np.exp(-np.abs(xs) / b) / (2 * b)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=xs, y=lap(0.5), mode="lines",
                                 name="ε large (b=0.5)", line=dict(color=P.TEAL, width=2)))
        fig.add_trace(go.Scatter(x=xs, y=lap(2.0), mode="lines",
                                 name="ε small (b=2.0)", line=dict(color=P.CRIMSON, width=2)))
        P.style_2d(fig, x_title="noise added", y_title="density", height=260)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "prv_noise_eqcap"))
        C.measure(_p(t(lang, "prv_noise_p3")))
        C.measure(_p(t(lang, "prv_noise_p4")))
        C.key_idea(t(lang, "prv_noise_call"))


# 5) federated learning -- topology diagram
def fl(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "prv_fl_eyebrow"), t(lang, "prv_fl"))
        C.measure(_p(t(lang, "prv_fl_p1")) + _p(t(lang, "prv_fl_p2")))
        nodes = {"server": (0.5, 1.0), "c1": (0.1, 0.0), "c2": (0.5, 0.0),
                 "c3": (0.9, 0.0)}
        fig = P.causal_dag_figure(
            nodes, [("c1", "server"), ("c2", "server"), ("c3", "server")],
            labels={"server": "server (aggregate)", "c1": "client 1",
                    "c2": "client 2", "c3": "client 3"},
            node_colors={"server": P.INK, "c1": P.TEAL, "c2": P.TEAL,
                         "c3": P.TEAL},
            edge_colors={("c1", "server"): P.GOLD, ("c2", "server"): P.GOLD,
                         ("c3", "server"): P.GOLD}, height=240)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "prv_fl_eqcap"))
        C.measure(_p(t(lang, "prv_fl_p3")))
        C.measure(_p(t(lang, "prv_fl_p4")))
        C.key_idea(t(lang, "prv_fl_call"))


# 6) gradient leakage -- REAL reconstruction from a linear gradient
def leak(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "prv_leak_eyebrow"), t(lang, "prv_leak"))
        C.measure(_p(t(lang, "prv_leak_p1")) + _p(t(lang, "prv_leak_p2")))
        X, y, _ = V.make_shapes_dataset(3, spurious=False, seed=8)
        x = X[0, 0]
        r = PV.gradient_leakage_linear(x.ravel(), int(y[0]), n_classes=2, seed=0)
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(_img_fig(x), use_container_width=True,
                            config=P.PLOTLY_CONFIG)
            C.figure_caption("true input")
        with col2:
            st.plotly_chart(_img_fig(r["x_rec"].reshape(V.H, V.W)),
                            use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(f"reconstructed (err {r['rel_error']:.1e})")
        C.figure_caption(t(lang, "prv_leak_eqcap"))
        C.measure(_p(t(lang, "prv_leak_p3")))
        C.measure(_p(t(lang, "prv_leak_p4")))
        C.warn(t(lang, "prv_leak_call"))


SECTIONS_PRIVACY = {
    "prv_poison": poison,
    "prv_privacy": privacy,
    "prv_dp": dp,
    "prv_noise": noise,
    "prv_fl": fl,
    "prv_leak": leak,
}
