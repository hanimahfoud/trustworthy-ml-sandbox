"""
modules/domain_adaptation.py -- live domain-adversarial training (DANN).

Two-moons source and a rotated/shifted target (covariate shift). A from-scratch
NumPy network with a true Gradient Reversal Layer is trained for the chosen λ
and seed; the input-space decision boundary, the 2-D PCA of the learned
features, and target/source accuracy plus feature-space MMD are all recomputed.
λ = 0 reproduces the source-only baseline.
"""
from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import dann_core as D
from i18n import t

DEFAULT_LAMBDA = 1.0
DEFAULT_SEED = 1
EPOCHS = 700


@st.cache_data(show_spinner=False)
def _train(lam: float, seed: int):
    Xs, ys, Xt, yt = D.make_domain_data(seed=seed)
    params, _hist = D.train_dann(Xs, ys, Xt, yt, lam=lam, epochs=EPOCHS, seed=seed)
    res = D.analyse(params, Xs, ys, Xt, yt, seed=seed)
    res["Xs"], res["ys"], res["Xt"], res["yt"] = Xs, ys, Xt, yt
    return res


def _pct(v: float) -> str:
    return f"{100.0 * v:.1f}%"


def render(lang: str) -> None:
    C.eyebrow(t(lang, "pr_dann_eyebrow"))
    C.section_title(t(lang, "pr_dann"))
    C.demo_intro(t(lang, "pr_dann_what"), t(lang, "pr_dann_why"),
                 t(lang, "pr_dann_expect"),
                 labels=(t(lang, "di_what"), t(lang, "di_why"),
                         t(lang, "di_expect")))

    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            lam = st.slider(t(lang, "pr_dann_ctrl_lambda"), 0.0, 2.5,
                            DEFAULT_LAMBDA, 0.1)
        with c2:
            seed = st.slider(t(lang, "pr_dann_ctrl_seed"), 0, 20, DEFAULT_SEED, 1)

    with st.spinner(t(lang, "pr_dann_training")):
        r = _train(float(lam), int(seed))

    cls0, cls1 = P.INK, P.CRIMSON

    # ---- Figure 1: input space + decision boundary ----
    g_left, g_right = st.columns(2)
    with g_left:
        with st.container(border=True):
            f1 = go.Figure()
            # faint class-probability fill, then the 0.5 boundary line
            f1.add_trace(go.Contour(
                x=r["grid_x"], y=r["grid_y"], z=r["grid_prob"],
                showscale=False, opacity=0.18,
                colorscale=[[0.0, P.INK], [0.5, P.PARCHMENT], [1.0, P.CRIMSON]],
                contours=dict(showlines=False),
                hoverinfo="skip",
            ))
            f1.add_trace(go.Contour(
                x=r["grid_x"], y=r["grid_y"], z=r["grid_prob"],
                showscale=False,
                contours=dict(start=0.5, end=0.5, size=1, coloring="lines"),
                line=dict(color=P.GOLD, width=2),
                hoverinfo="skip", name="Boundary",
            ))
            Xs, ys, Xt, yt = r["Xs"], r["ys"], r["Xt"], r["yt"]
            for cls, color, label in [(0, cls0, "Source y=0"), (1, cls1, "Source y=1")]:
                m = ys == cls
                f1.add_trace(go.Scatter(
                    x=Xs[m, 0], y=Xs[m, 1], mode="markers", name=label,
                    marker=dict(size=6, color=color, opacity=0.75,
                                line=dict(width=0)),
                ))
            for cls, color, label in [(0, cls0, "Target y=0"), (1, cls1, "Target y=1")]:
                m = yt == cls
                f1.add_trace(go.Scatter(
                    x=Xt[m, 0], y=Xt[m, 1], mode="markers", name=label,
                    marker=dict(size=7, color="rgba(0,0,0,0)",
                                line=dict(width=1.6, color=color)),
                ))
            P.style_2d(f1, x_title="x₁", y_title="x₂", height=400)
            st.plotly_chart(f1, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "pr_dann_cap_space"))

    # ---- Figure 2: learned-feature PCA ----
    with g_right:
        with st.container(border=True):
            f2 = go.Figure()
            f2.add_trace(go.Scatter(
                x=r["feat_src"][:, 0], y=r["feat_src"][:, 1], mode="markers",
                name="Source",
                marker=dict(size=6, color=P.INK, opacity=0.6, line=dict(width=0)),
            ))
            f2.add_trace(go.Scatter(
                x=r["feat_tgt"][:, 0], y=r["feat_tgt"][:, 1], mode="markers",
                name="Target",
                marker=dict(size=7, color="rgba(0,0,0,0)",
                            line=dict(width=1.6, color=P.CRIMSON)),
            ))
            P.style_2d(f2, x_title="PC 1", y_title="PC 2", height=400)
            st.plotly_chart(f2, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "pr_dann_cap_feat"))

    # ---- readouts ----
    tgt_color = "teal" if r["tgt_acc"] >= 0.80 else "crimson"
    C.readout_strip([
        {"k": "TARGET ACC", "v": _pct(r["tgt_acc"]), "color": tgt_color},
        {"k": "SOURCE ACC", "v": _pct(r["src_acc"]), "color": "teal"},
        {"k": "FEATURE MMD", "v": f"{r['feat_mmd']:.4f}"},
        {"k": "DOMAIN ACC", "v": _pct(r["domain_acc"])},
    ])

    # ---- status ----
    if lam < 0.05:
        C.warn(t(lang, "pr_dann_baseline"))
    else:
        C.key_idea(t(lang, "pr_dann_adapt"))
