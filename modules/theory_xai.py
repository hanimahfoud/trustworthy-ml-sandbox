"""
modules/theory_xai.py -- the six theory plates of Section II (XAI).

Each plate mirrors the Section I grammar (plate, prose, equation, figure,
callout) but adds a small live figure beside the text so the reader sees the
idea while reading. Several figures are real computations on the shared loan
model (glass-box logistic weights, exact SHAP contributions, the causal graph);
the vision/VLM plates use clearly-labelled schematic diagrams.
"""
from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
import streamlit as st
from sklearn.linear_model import LogisticRegression

import components as C
import plotting as P
from core import loan_model_core as L
from core import shap_core as SH
from i18n import t


def _p(text: str) -> str:
    return f"<p>{text}</p>"


# ---- cached shared compute ----
@st.cache_resource(show_spinner=False)
def _loan():
    model, X, y, std = L.train_model(0)
    return model, X, y, std


@st.cache_data(show_spinner=False)
def _glass_weights():
    _, X, y, std = _loan()
    Xs = (X - X.mean(0)) / np.where(std < 1e-8, 1, std)
    lr = LogisticRegression(max_iter=500).fit(Xs, y)
    return L.FEATURES, lr.coef_[0]


@st.cache_data(show_spinner=False)
def _shap_default():
    model, X, _, _ = _loan()
    return SH.shapley_values(model, L.to_vector(L.DEFAULT_APPLICANT), X[:120])


def _heatmap(z, height=190, scale=None):
    fig = go.Figure(go.Heatmap(z=z, colorscale=scale or P.NAVY_SCALE,
                               showscale=False))
    fig.update_layout(
        height=height, margin=dict(l=4, r=4, t=6, b=4),
        paper_bgcolor=P.CARD, plot_bgcolor=P.CARD,
        xaxis=dict(visible=False), yaxis=dict(visible=False,
                                              scaleanchor="x", autorange="reversed"),
    )
    return fig


# --------------------------------------------------------------------------- #
# 1) Interpretability vs Explainability -- glass-box weights                   #
# --------------------------------------------------------------------------- #
def interp(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "xai_interp_eyebrow"), t(lang, "xai_interp"))
        C.measure(_p(t(lang, "xai_interp_p1")) + _p(t(lang, "xai_interp_p2")))
        st.latex(r"\hat y = w_0 + \sum_{i} w_i\,x_i \qquad\text{(glass box)}")
        feats, w = _glass_weights()
        fig = go.Figure(go.Bar(
            x=w, y=feats, orientation="h",
            marker_color=[P.TEAL if v >= 0 else P.CRIMSON for v in w]))
        P.style_2d(fig, x_title="Logistic weight (standardized)", y_title="",
                   height=230, legend=False)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "xai_interp_eqcap"))
        C.measure(_p(t(lang, "xai_interp_p3")))
        C.measure(_p(t(lang, "xai_interp_p4")))
        C.key_idea(t(lang, "xai_interp_call"))


# --------------------------------------------------------------------------- #
# 2) The black-box problem -- shortcut diagram                                 #
# --------------------------------------------------------------------------- #
def blackbox(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "xai_black_eyebrow"), t(lang, "xai_black"))
        C.measure(_p(t(lang, "xai_black_p1")) + _p(t(lang, "xai_black_p2")))
        st.latex(r"P(\hat y \mid \text{background cue}) \approx "
                 r"P(\hat y \mid \text{object}) \;\Rightarrow\; \text{shortcut}")
        nodes = {"cue": (0.0, 1.0), "object": (0.0, 0.0), "pred": (1.0, 0.5)}
        fig = P.causal_dag_figure(
            nodes, [("cue", "pred"), ("object", "pred")],
            labels={"cue": "background cue", "object": "object", "pred": "prediction"},
            node_colors={"cue": P.CRIMSON, "object": P.SLATE, "pred": P.INK},
            edge_colors={("cue", "pred"): P.CRIMSON, ("object", "pred"): P.SLATE},
            height=210)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "xai_black_eqcap"))
        C.measure(_p(t(lang, "xai_black_p3")))
        C.measure(_p(t(lang, "xai_black_p4")))
        C.warn(t(lang, "xai_black_call"))


# --------------------------------------------------------------------------- #
# 3) LIME & SHAP -- real Shapley contributions on the default applicant        #
# --------------------------------------------------------------------------- #
def tabular(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "xai_tab_eyebrow"), t(lang, "xai_tab"))
        C.measure(_p(t(lang, "xai_tab_p1")) + _p(t(lang, "xai_tab_p2")))
        st.latex(
            r"\xi(x)=\arg\min_{g\in G}\;\mathcal{L}(f,g,\pi_x)+\Omega(g)"
            r"\qquad\phi_i=\!\!\sum_{S\subseteq N\setminus\{i\}}\!\!"
            r"\frac{|S|!\,(M-|S|-1)!}{M!}\,[\,f(S\cup\{i\})-f(S)\,]"
        )
        r = _shap_default()
        fig = go.Figure(go.Bar(
            x=r["phi"], y=r["features"], orientation="h",
            marker_color=[P.TEAL if v >= 0 else P.CRIMSON for v in r["phi"]]))
        P.style_2d(fig, x_title="Shapley contribution φ", y_title="",
                   height=230, legend=False)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "xai_tab_eqcap"))
        C.measure(_p(t(lang, "xai_tab_p3")))
        C.measure(_p(t(lang, "xai_tab_p4")))
        C.key_idea(t(lang, "xai_tab_call"))


# --------------------------------------------------------------------------- #
# 4) Recourse -- the real causal edge                                          #
# --------------------------------------------------------------------------- #
def recourse(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "xai_recourse_eyebrow"), t(lang, "xai_recourse"))
        C.measure(_p(t(lang, "xai_recourse_p1")) + _p(t(lang, "xai_recourse_p2")))
        st.latex(
            r"\min_{x'}\;\mathrm{cost}(x,x')\quad\text{s.t.}\quad "
            r"f(x')=1,\;\; x'\in\mathcal{A},\;\; x'=\mathrm{SCM}\big(x,\mathrm{do}(\cdot)\big)"
        )
        g = L.causal_graph()
        fig = P.causal_dag_figure(
            g["nodes"], g["edges"],
            labels={"income": "income", "savings": "savings"},
            node_colors={"income": P.INK, "savings": P.TEAL},
            edge_colors={("income", "savings"): P.TEAL},
            height=200)
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "xai_recourse_eqcap"))
        C.measure(_p(t(lang, "xai_recourse_p3")))
        C.measure(_p(t(lang, "xai_recourse_p4")))
        C.key_idea(t(lang, "xai_recourse_call"))


# --------------------------------------------------------------------------- #
# 5) Vision XAI -- schematic Grad-CAM heatmap                                  #
# --------------------------------------------------------------------------- #
def vision(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "xai_cv_eyebrow"), t(lang, "xai_cv"))
        C.measure(_p(t(lang, "xai_cv_p1")) + _p(t(lang, "xai_cv_p2")))
        st.latex(
            r"\alpha_k^{c}=\frac{1}{Z}\sum_{i,j}\frac{\partial y^{c}}{\partial A^{k}_{ij}}"
            r"\qquad L^{c}_{\text{Grad-CAM}}=\mathrm{ReLU}\!\Big(\textstyle\sum_k \alpha_k^{c}A^{k}\Big)"
        )
        # illustrative heatmap: class evidence concentrated on a central region
        yy, xx = np.mgrid[0:24, 0:24]
        z = np.exp(-(((xx - 11) ** 2 + (yy - 10) ** 2) / 40.0))
        st.plotly_chart(_heatmap(z, scale=P.TEAL_SCALE),
                        use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "xai_cv_eqcap"))
        C.measure(_p(t(lang, "xai_cv_p3")))
        C.measure(_p(t(lang, "xai_cv_p4")))
        C.key_idea(t(lang, "xai_cv_call"))


# --------------------------------------------------------------------------- #
# 6) Vision-Language Models -- schematic cross-attention                       #
# --------------------------------------------------------------------------- #
def vlm(lang):
    with st.container(border=True):
        C.plate_header(t(lang, "xai_vlm_eyebrow"), t(lang, "xai_vlm"))
        C.measure(_p(t(lang, "xai_vlm_p1")) + _p(t(lang, "xai_vlm_p2")))
        st.latex(r"\tilde{A}=\prod_{l}\big(A^{(l)}+I\big)\qquad\text{(attention rollout)}")
        tokens = ["a", "dog", "runs"]
        att = np.array([[0.05, 0.05, 0.05, 0.05, 0.05, 0.05],
                        [0.02, 0.05, 0.35, 0.40, 0.10, 0.03],
                        [0.10, 0.08, 0.05, 0.06, 0.20, 0.30]])
        fig = go.Figure(go.Heatmap(z=att, x=[f"patch {i+1}" for i in range(6)],
                                   y=tokens, colorscale=P.NAVY_SCALE, showscale=False))
        P.style_2d(fig, x_title="image patches", y_title="text tokens",
                   height=210, legend=False)
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "xai_vlm_eqcap"))
        C.measure(_p(t(lang, "xai_vlm_p3")))
        C.measure(_p(t(lang, "xai_vlm_p4")))
        C.key_idea(t(lang, "xai_vlm_call"))


SECTIONS_XAI = {
    "xai_interp": interp,
    "xai_black": blackbox,
    "xai_tab": tabular,
    "xai_recourse": recourse,
    "xai_cv": vision,
    "xai_vlm": vlm,
}
