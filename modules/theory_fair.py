"""
modules/theory_fair.py -- the six theory plates of Section III (Fairness).

The metrics and mitigation plates show *real* computation on the synthetic
fairness dataset (the impossibility gaps; the MMD between two groups' score
distributions). The remaining plates use clearly-labelled schematic diagrams.
"""
from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import fairness_core as F
from i18n import t


def _p(text):
    return f"<p>{text}</p>"


@st.cache_data(show_spinner=False)
def _data():
    return F.make_fairness_dataset(seed=0)


# 1) sources of bias -- redundant-encoding diagram
def intro(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "fair_intro_eyebrow"), t(lang, "fair_intro"))
        C.measure(_p(t(lang, "fair_intro_p1")) + _p(t(lang, "fair_intro_p2")))
        st.latex(r"S \;\approx\; g(f_1, f_2, \ldots, f_k)\qquad\text{(redundant encoding)}")
        nodes = {"f1": (0.0, 1.0), "f2": (0.0, 0.5), "f3": (0.0, 0.0),
                 "S": (1.0, 0.5)}
        fig = P.causal_dag_figure(
            nodes, [("f1", "S"), ("f2", "S"), ("f3", "S")],
            labels={"f1": "zip code", "f2": "purchases", "f3": "name",
                    "S": "protected trait"},
            node_colors={"f1": P.SLATE, "f2": P.SLATE, "f3": P.SLATE,
                         "S": P.CRIMSON},
            edge_colors={("f1", "S"): P.CRIMSON, ("f2", "S"): P.CRIMSON,
                         ("f3", "S"): P.CRIMSON}, height=220)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "fair_intro_eqcap"))
        C.measure(_p(t(lang, "fair_intro_p3")))
        C.key_idea(t(lang, "fair_intro_call"))


# 2) metrics -- REAL impossibility gaps under demographic-parity enforcement
def metrics(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "fair_metrics_eyebrow"), t(lang, "fair_metrics"))
        C.measure(_p(t(lang, "fair_metrics_p1")) + _p(t(lang, "fair_metrics_p2")))
        st.latex(
            r"\text{DP}:\;P(\hat Y{=}1\mid a)=P(\hat Y{=}1\mid b)\qquad"
            r"\text{EOpp}:\;\mathrm{TPR}_a=\mathrm{TPR}_b\qquad"
            r"\text{EOdds}:\;\mathrm{TPR},\mathrm{FPR}\ \text{equal}")
        d = _data()
        ta, tb = F.thresholds_for_demographic_parity(d, 0.5)
        m = F.fairness_metrics(d, ta, tb)
        gaps = [m["demographic_parity_gap"], m["equal_opportunity_gap"],
                m["equalized_odds_gap"]]
        fig = go.Figure(go.Bar(
            x=["DP gap", "Equal-opp gap", "Equalized-odds gap"], y=gaps,
            marker_color=[P.TEAL, P.GOLD, P.CRIMSON]))
        P.style_2d(fig, x_title="", y_title="gap (0 = fair)", height=240,
                   legend=False)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "fair_metrics_eqcap"))
        C.measure(_p(t(lang, "fair_metrics_p3")))
        C.key_idea(t(lang, "fair_metrics_call"))


# 3) LLM bias -- three-stage flow diagram
def llm(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "fair_llm_eyebrow"), t(lang, "fair_llm"))
        C.measure(_p(t(lang, "fair_llm_p1")) + _p(t(lang, "fair_llm_p2")))
        st.latex(r"\text{embeddings} \;\to\; P(\text{next token}) \;\to\; \text{generated text}")
        nodes = {"emb": (0.0, 0.5), "prob": (0.5, 0.5), "text": (1.0, 0.5)}
        fig = P.causal_dag_figure(
            nodes, [("emb", "prob"), ("prob", "text")],
            labels={"emb": "embeddings", "prob": "probabilities",
                    "text": "generated text"},
            node_colors={"emb": P.INK, "prob": P.GOLD, "text": P.CRIMSON},
            height=180)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "fair_llm_eqcap"))
        C.measure(_p(t(lang, "fair_llm_p3")))
        C.key_idea(t(lang, "fair_llm_call"))


# 4) mitigation -- REAL MMD between the two groups' score distributions
def mitig(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "fair_mitig_eyebrow"), t(lang, "fair_mitig"))
        C.measure(_p(t(lang, "fair_mitig_p1")) + _p(t(lang, "fair_mitig_p2")))
        st.latex(r"\mathrm{MMD}^2=\big\|\,\mathbb{E}[\phi(s_a)]-\mathbb{E}[\phi(s_b)]\,\big\|_{\mathcal H}^2")
        d = _data()
        sa = d["score"][d["group"] == "A"]
        sb = d["score"][d["group"] == "B"]
        mmd = F.mmd_rbf(sa, sb)
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=sa, name="group A", opacity=0.6,
                                   marker_color=P.TEAL, nbinsx=30))
        fig.add_trace(go.Histogram(x=sb, name="group B", opacity=0.6,
                                   marker_color=P.CRIMSON, nbinsx=30))
        fig.update_layout(barmode="overlay")
        P.style_2d(fig, x_title="model score", y_title="count", height=240)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "fair_mitig_eqcap") +
                         f" &nbsp; MMD² = {mmd:.3f}")
        C.measure(_p(t(lang, "fair_mitig_p3")))
        C.key_idea(t(lang, "fair_mitig_call"))


# 5) FAP -- adversarial de-biasing diagram
def fap(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "fair_fap_eyebrow"), t(lang, "fair_fap"))
        C.measure(_p(t(lang, "fair_fap_p1")) + _p(t(lang, "fair_fap_p2")))
        st.latex(r"\min_{\delta}\;\mathcal{L}_{\text{cls}}(x+\delta)\;-\;\lambda\,\mathcal{L}_{\text{disc}}(x+\delta)")
        nodes = {"x": (0.0, 0.5), "z": (0.45, 0.5),
                 "cls": (1.0, 1.0), "disc": (1.0, 0.0)}
        fig = P.causal_dag_figure(
            nodes, [("x", "z"), ("z", "cls"), ("z", "disc")],
            labels={"x": "input + δ", "z": "latent", "cls": "classifier ✓",
                    "disc": "discriminator ✗"},
            node_colors={"x": P.SLATE, "z": P.INK, "cls": P.TEAL,
                         "disc": P.CRIMSON},
            edge_colors={("z", "cls"): P.TEAL, ("z", "disc"): P.CRIMSON},
            height=220)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "fair_fap_eqcap"))
        C.measure(_p(t(lang, "fair_fap_p3")))
        C.key_idea(t(lang, "fair_fap_call"))


# 6) alignment -- critique/revise diagram
def align(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "fair_align_eyebrow"), t(lang, "fair_align"))
        C.measure(_p(t(lang, "fair_align_p1")) + _p(t(lang, "fair_align_p2")))
        st.latex(r"\text{revise}(a)=a'\quad\text{s.t.}\quad a'\models \text{Constitution}")
        nodes = {"a": (0.0, 0.5), "crit": (0.5, 0.5), "rev": (1.0, 0.5)}
        fig = P.causal_dag_figure(
            nodes, [("a", "crit"), ("crit", "rev")],
            labels={"a": "answer", "crit": "self-critique", "rev": "revision"},
            node_colors={"a": P.CRIMSON, "crit": P.GOLD, "rev": P.TEAL},
            height=180)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "fair_align_eqcap"))
        C.measure(_p(t(lang, "fair_align_p3")))
        C.key_idea(t(lang, "fair_align_call"))


SECTIONS_FAIR = {
    "fair_intro": intro,
    "fair_metrics": metrics,
    "fair_llm": llm,
    "fair_mitig": mitig,
    "fair_fap": fap,
    "fair_align": align,
}
