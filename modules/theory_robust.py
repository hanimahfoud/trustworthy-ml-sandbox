"""
modules/theory_robust.py -- the six theory plates of Section IV (Robustness).

The attacks plate shows a *real* FGSM adversarial example produced from the
trained CNN's own gradients; the certified plate shows a real randomized-
smoothing vote. The rest use clearly-labelled schematic diagrams.
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


def _p(text):
    return f"<p>{text}</p>"


@st.cache_resource(show_spinner=False)
def _net():
    net, acc = V.train_cnn(spurious=False, seed=0)
    return net


@st.cache_data(show_spinner=False)
def _sample():
    X, y, _ = V.make_shapes_dataset(6, spurious=False, seed=21)
    return X, y


def _img_fig(z, scale="gray", height=200, overlay=None):
    fig = go.Figure(go.Heatmap(z=z, colorscale=scale, showscale=False,
                               zmin=0, zmax=1))
    fig.update_layout(height=height, margin=dict(l=4, r=4, t=6, b=4),
                      paper_bgcolor=P.CARD, plot_bgcolor=P.CARD,
                      xaxis=dict(visible=False),
                      yaxis=dict(visible=False, scaleanchor="x",
                                 autorange="reversed"))
    return fig


# 1) intro -- boundary-crossing schematic
def intro(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "rob_intro_eyebrow"), t(lang, "rob_intro"))
        C.measure(_p(t(lang, "rob_intro_p1")) + _p(t(lang, "rob_intro_p2")))
        st.latex(r"\min_{x'}\;\|x'-x\|\quad\text{s.t.}\quad f(x')\neq f(x)")
        nodes = {"x": (0.2, 0.5), "xp": (0.8, 0.5)}
        fig = P.causal_dag_figure(
            nodes, [("x", "xp")],
            labels={"x": "x (panda)", "xp": "x' (gibbon)"},
            node_colors={"x": P.TEAL, "xp": P.CRIMSON},
            edge_colors={("x", "xp"): P.INK}, height=170)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "rob_intro_eqcap"))
        C.measure(_p(t(lang, "rob_intro_p3")))
        C.key_idea(t(lang, "rob_intro_call"))


# 2) formulation -- the three norm balls
def formulation(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "rob_formulation_eyebrow"),
                       t(lang, "rob_formulation"))
        C.measure(_p(t(lang, "rob_formulation_p1")) +
                  _p(t(lang, "rob_formulation_p2")))
        st.latex(r"\|x'-x\|_\infty \le \epsilon \qquad \|x'-x\|_2 \le \epsilon "
                 r"\qquad \|x'-x\|_1 \le \epsilon")
        th = np.linspace(0, 2 * np.pi, 200)
        fig = go.Figure()
        # L-inf square
        fig.add_trace(go.Scatter(x=[-1, 1, 1, -1, -1], y=[-1, -1, 1, 1, -1],
                                 mode="lines", name="L∞ (box)",
                                 line=dict(color=P.CRIMSON, width=2)))
        # L2 circle
        fig.add_trace(go.Scatter(x=np.cos(th), y=np.sin(th), mode="lines",
                                 name="L2 (sphere)",
                                 line=dict(color=P.TEAL, width=2)))
        # L1 diamond
        fig.add_trace(go.Scatter(x=[1, 0, -1, 0, 1], y=[0, 1, 0, -1, 0],
                                 mode="lines", name="L1 (diamond)",
                                 line=dict(color=P.GOLD, width=2)))
        fig.add_trace(go.Scatter(x=[0], y=[0], mode="markers", name="x",
                                 marker=dict(color=P.INK, size=8)))
        P.style_2d(fig, x_title="", y_title="", height=320)
        fig.update_yaxes(scaleanchor="x", scaleratio=1)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "rob_formulation_eqcap"))
        C.measure(_p(t(lang, "rob_formulation_p3")))
        C.key_idea(t(lang, "rob_formulation_call"))


# 3) attacks -- REAL FGSM adversarial example from the CNN
def attacks(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "rob_attacks_eyebrow"), t(lang, "rob_attacks"))
        C.measure(_p(t(lang, "rob_attacks_p1")) + _p(t(lang, "rob_attacks_p2")))
        st.latex(r"x' = x + \epsilon \cdot \mathrm{sign}\!\big(\nabla_x \mathcal{L}(x,y)\big)")
        net = _net(); X, y = _sample()
        x = X[0:1]
        x_adv = R.fgsm(net, x, int(y[0]), 0.25)
        p_clean = int(net.predict(x)[0]); p_adv = int(net.predict(x_adv)[0])
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(_img_fig(x[0, 0]), use_container_width=True,
                            config=P.PLOTLY_CONFIG)
            C.figure_caption(f"clean → <b>{t(lang, 'px_cv_class'+str(p_clean))}</b>")
        with col2:
            st.plotly_chart(_img_fig(x_adv[0, 0]), use_container_width=True,
                            config=P.PLOTLY_CONFIG)
            C.figure_caption(f"FGSM ε=0.25 → <b>{t(lang, 'px_cv_class'+str(p_adv))}</b>")
        C.measure(_p(t(lang, "rob_attacks_p3")))
        C.key_idea(t(lang, "rob_attacks_call"))


# 4) defense -- min-max schematic
def defense(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "rob_defense_eyebrow"), t(lang, "rob_defense"))
        C.measure(_p(t(lang, "rob_defense_p1")) + _p(t(lang, "rob_defense_p2")))
        st.latex(r"\min_{\theta}\;\mathbb{E}\Big[\max_{\|\delta\|\le\epsilon}"
                 r"\mathcal{L}\big(f_\theta(x+\delta),\,y\big)\Big]")
        nodes = {"inner": (0.25, 0.5), "outer": (0.75, 0.5)}
        fig = P.causal_dag_figure(
            nodes, [("inner", "outer")],
            labels={"inner": "max: PGD attack", "outer": "min: update weights"},
            node_colors={"inner": P.CRIMSON, "outer": P.TEAL},
            edge_colors={("inner", "outer"): P.INK}, height=170)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "rob_defense_eqcap"))
        C.measure(_p(t(lang, "rob_defense_p3")))
        C.warn(t(lang, "rob_defense_call"))


# 5) certified -- REAL randomized-smoothing vote
def certified(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "rob_certified_eyebrow"), t(lang, "rob_certified"))
        C.measure(_p(t(lang, "rob_certified_p1")) + _p(t(lang, "rob_certified_p2")))
        st.latex(r"R = \sigma \cdot \Phi^{-1}(\underline{p_A})")
        net = _net(); X, y = _sample()
        cert = R.randomized_smoothing(net, X[0:1], sigma=0.25, n=200, seed=0)
        fig = go.Figure(go.Bar(
            x=[t(lang, "px_cv_class0"), t(lang, "px_cv_class1")],
            y=cert["votes"], marker_color=[P.TEAL, P.CRIMSON]))
        P.style_2d(fig, x_title="", y_title="votes", height=240, legend=False)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "rob_certified_eqcap") +
                         f" &nbsp; R = {cert['radius']:.3f}")
        C.measure(_p(t(lang, "rob_certified_p3")))
        C.key_idea(t(lang, "rob_certified_call"))


# 6) LLM -- injection schematic
def llm(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "rob_llm_eyebrow"), t(lang, "rob_llm"))
        C.measure(_p(t(lang, "rob_llm_p1")) + _p(t(lang, "rob_llm_p2")))
        st.latex(r"\text{prompt} = [\;\text{system guardrail}\;\|\;"
                 r"\underbrace{\text{user input}}_{\text{hidden instruction}}\;]")
        nodes = {"inp": (0.15, 0.5), "guard": (0.55, 0.5), "out": (0.9, 0.5)}
        fig = P.causal_dag_figure(
            nodes, [("inp", "guard"), ("guard", "out")],
            labels={"inp": "injected input", "guard": "guardrail",
                    "out": "leaked output"},
            node_colors={"inp": P.CRIMSON, "guard": P.GOLD, "out": P.CRIMSON},
            edge_colors={("inp", "guard"): P.CRIMSON,
                         ("guard", "out"): P.CRIMSON}, height=170)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "rob_llm_eqcap"))
        C.measure(_p(t(lang, "rob_llm_p3")))
        C.key_idea(t(lang, "rob_llm_call"))


SECTIONS_ROBUST = {
    "rob_intro": intro,
    "rob_formulation": formulation,
    "rob_attacks": attacks,
    "rob_defense": defense,
    "rob_certified": certified,
    "rob_llm": llm,
}
