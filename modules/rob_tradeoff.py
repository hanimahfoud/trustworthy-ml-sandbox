"""
modules/rob_tradeoff.py -- Practice demo: the accuracy/robustness trade-off.

Compare a standard CNN with an adversarially-trained one, on clean data and
under a live PGD attack. All four accuracies are measured, not scripted; the
hardened model trades clean accuracy for real resistance.
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
def _standard():
    net, acc = V.train_cnn(spurious=False, seed=0)
    return net


@st.cache_resource(show_spinner=False)
def _hardened():
    net, acc = R.adversarial_train(seed=0, epochs=10, n_train=400,
                                   epsilon=0.15, pgd_steps=4)
    return net


@st.cache_data(show_spinner=False)
def _testset():
    X, y, _ = V.make_shapes_dataset(60, spurious=False, seed=99)
    return X, y


@st.cache_data(show_spinner=False)
def _scores(use_adv, eps=0.20):
    X, y = _testset()
    net = _hardened() if use_adv else _standard()
    clean = R.clean_accuracy(net, X, y)
    attacked = 1.0 - R.attack_success_rate(net, X, y, eps, "pgd", 10)
    return clean, attacked


def render(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "prb_tradeoff_eyebrow"), t(lang, "prb_tradeoff"))
        C.measure(f"<p>{t(lang, 'prb_tradeoff_intro')}</p>")

        use_adv = st.checkbox(t(lang, "prb_tradeoff_adv"), value=False)

        with st.spinner(""):
            clean, attacked = _scores(use_adv)

        fig = go.Figure(go.Bar(
            x=[t(lang, "prb_tradeoff_clean"), t(lang, "prb_tradeoff_attacked")],
            y=[clean, attacked], marker_color=[P.TEAL, P.CRIMSON],
            text=[f"{clean:.0%}", f"{attacked:.0%}"], textposition="outside"))
        P.style_2d(fig, x_title="", y_title="accuracy", height=340, legend=False)
        fig.update_yaxes(range=[0, 1.05])
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "prb_tradeoff_cap_bars"))

        C.readout_strip([
            {"k": "model", "v": "adversarial" if use_adv else "standard"},
            {"k": t(lang, "prb_tradeoff_clean"), "v": f"{clean:.2f}",
             "color": "teal"},
            {"k": t(lang, "prb_tradeoff_attacked"), "v": f"{attacked:.2f}",
             "color": "teal" if attacked > 0.4 else "crimson"},
        ])
        C.key_idea(t(lang, "prb_tradeoff_note"))
