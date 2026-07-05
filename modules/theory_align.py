"""
modules/theory_align.py -- the six theory plates of Section VI (Generative AI
Safety & Alignment). The RLHF, DPO and GRPO plates carry real computed figures;
the rest use clearly-labelled schematics.
"""
from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import alignment_core as A
from i18n import t


def _p(text):
    return f"<p>{text}</p>"


# 1) alignment gap -- schematic
def gap(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "aln_gap_eyebrow"), t(lang, "aln_gap"))
        C.measure(_p(t(lang, "aln_gap_p1")) + _p(t(lang, "aln_gap_p2")))
        nodes = {"pt": (0.2, 0.5), "al": (0.8, 0.5)}
        fig = P.causal_dag_figure(
            nodes, [("pt", "al")],
            labels={"pt": "pre-training (fluent)", "al": "alignment (HHH)"},
            node_colors={"pt": P.SLATE, "al": P.TEAL},
            edge_colors={("pt", "al"): P.INK}, height=170)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "aln_gap_eqcap"))
        C.measure(_p(t(lang, "aln_gap_p3")))
        C.measure(_p(t(lang, "aln_gap_p4")))
        C.key_idea(t(lang, "aln_gap_call"))


# 2) RLHF -- real reward-model training curve + Bradley-Terry
def rlhf(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "aln_rlhf_eyebrow"), t(lang, "aln_rlhf"))
        C.measure(_p(t(lang, "aln_rlhf_p1")) + _p(t(lang, "aln_rlhf_p2")))
        st.latex(r"\mathcal{L}_{RM} = -\log \sigma\big(r(x,y_w) - r(x,y_l)\big)")
        # real Bradley-Terry reward-model training
        rng = np.random.default_rng(0)
        Xw = rng.normal(0, 1, (150, 3)); Xw[:, 0] += 1.4
        Xl = rng.normal(0, 1, (150, 3)); Xl[:, 0] -= 1.4
        out = A.train_reward_model(Xw, Xl, epochs=250, lr=0.2, seed=0)
        fig = go.Figure(go.Scatter(y=out["losses"], mode="lines",
                                   line=dict(color=P.CRIMSON, width=2),
                                   name="RM loss"))
        P.style_2d(fig, x_title="training step", y_title="Bradley–Terry loss",
                   height=240, legend=False)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "aln_rlhf_eqcap"))
        C.measure(_p(t(lang, "aln_rlhf_p3")))
        st.latex(r"\max_\pi\; \mathbb{E}_{\pi}[r(x,y)] \;-\; "
                 r"\beta\,\mathrm{KL}\big(\pi \,\|\, \pi_{ref}\big)")
        C.measure(_p(t(lang, "aln_rlhf_p4")))
        C.warn(t(lang, "aln_rlhf_call"))


# 3) DPO -- real implicit-reward margin vs beta
def dpo(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "aln_dpo_eyebrow"), t(lang, "aln_dpo"))
        C.measure(_p(t(lang, "aln_dpo_p1")) + _p(t(lang, "aln_dpo_p2")))
        st.latex(r"\mathcal{L}_{DPO} = -\log \sigma\Big(\beta \log "
                 r"\frac{\pi(y_w)}{\pi_{ref}(y_w)} - \beta \log "
                 r"\frac{\pi(y_l)}{\pi_{ref}(y_l)}\Big)")
        # real DPO loss as the policy increasingly prefers the winner
        gaps = np.linspace(-2, 3, 60)
        losses = []
        for g in gaps:
            lw_pi = np.array([-1.0 + g]); ll_pi = np.array([-1.0])
            lw_ref = np.array([-1.0]); ll_ref = np.array([-1.0])
            loss, _ = A.dpo_loss(lw_pi, ll_pi, lw_ref, ll_ref, beta=0.5)
            losses.append(loss)
        fig = go.Figure(go.Scatter(x=gaps, y=losses, mode="lines",
                                   line=dict(color=P.TEAL, width=2)))
        P.style_2d(fig, x_title="policy log-prob advantage for y_w",
                   y_title="DPO loss", height=240, legend=False)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "aln_dpo_eqcap"))
        C.measure(_p(t(lang, "aln_dpo_p3")))
        C.measure(_p(t(lang, "aln_dpo_p4")))
        C.key_idea(t(lang, "aln_dpo_call"))


# 4) variants -- real GRPO group scoring
def variants(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "aln_variants_eyebrow"), t(lang, "aln_variants"))
        C.measure(_p(t(lang, "aln_variants_p1")) + _p(t(lang, "aln_variants_p2")))
        st.latex(r"A_i = \frac{r_i - \mathrm{mean}(r)}{\mathrm{std}(r)}"
                 r"\qquad r_i \in \{0,1\}\ \text{(verifier)}")
        cands = ["6*7", "42", "6*7+1", "40", "(6*7)", "42", "7*6", "6*8"]
        r = A.grpo_group_score(cands, target=42)
        colors = [P.TEAL if rr == 1 else P.CRIMSON for rr in r["rewards"]]
        fig = go.Figure(go.Bar(x=[f"y{i+1}" for i in range(len(cands))],
                               y=r["advantages"], marker_color=colors))
        P.style_2d(fig, x_title="candidate", y_title="group-relative advantage",
                   height=240, legend=False)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "aln_variants_eqcap") +
                         f" &nbsp; {r['n_correct']}/{len(cands)} correct")
        C.measure(_p(t(lang, "aln_variants_p3")))
        C.measure(_p(t(lang, "aln_variants_p4")))
        C.key_idea(t(lang, "aln_variants_call"))


# 5) OWASP -- schematic map
def owasp(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "aln_owasp_eyebrow"), t(lang, "aln_owasp"))
        C.measure(_p(t(lang, "aln_owasp_p1")) + _p(t(lang, "aln_owasp_p2")))
        nodes = {"llm": (0.5, 0.5), "inj": (0.1, 0.85), "dis": (0.9, 0.85),
                 "rel": (0.1, 0.15), "sup": (0.9, 0.15)}
        fig = P.causal_dag_figure(
            nodes,
            [("inj", "llm"), ("dis", "llm"), ("rel", "llm"), ("sup", "llm")],
            labels={"llm": "LLM", "inj": "injection", "dis": "disclosure",
                    "rel": "overreliance", "sup": "supply chain"},
            node_colors={"llm": P.INK, "inj": P.CRIMSON, "dis": P.CRIMSON,
                         "rel": P.GOLD, "sup": P.CRIMSON},
            edge_colors={k: P.CRIMSON for k in
                         [("inj", "llm"), ("dis", "llm"), ("rel", "llm"),
                          ("sup", "llm")]}, height=280)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "aln_owasp_eqcap"))
        C.measure(_p(t(lang, "aln_owasp_p3")))
        C.measure(_p(t(lang, "aln_owasp_p4")))
        C.key_idea(t(lang, "aln_owasp_call"))


# 6) agency -- schematic two-outcome
def agency(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "aln_agency_eyebrow"), t(lang, "aln_agency"))
        C.measure(_p(t(lang, "aln_agency_p1")) + _p(t(lang, "aln_agency_p2")))
        nodes = {"inj": (0.15, 0.5), "ro": (0.7, 0.8), "wd": (0.7, 0.2)}
        fig = P.causal_dag_figure(
            nodes, [("inj", "ro"), ("inj", "wd")],
            labels={"inj": "hidden instruction", "ro": "read-only: safe",
                    "wd": "delete access: wiped"},
            node_colors={"inj": P.SLATE, "ro": P.TEAL, "wd": P.CRIMSON},
            edge_colors={("inj", "ro"): P.TEAL, ("inj", "wd"): P.CRIMSON},
            height=220)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "aln_agency_eqcap"))
        C.measure(_p(t(lang, "aln_agency_p3")))
        C.measure(_p(t(lang, "aln_agency_p4")))
        C.warn(t(lang, "aln_agency_call"))


SECTIONS_ALIGN = {
    "aln_gap": gap,
    "aln_rlhf": rlhf,
    "aln_dpo": dpo,
    "aln_variants": variants,
    "aln_owasp": owasp,
    "aln_agency": agency,
}
