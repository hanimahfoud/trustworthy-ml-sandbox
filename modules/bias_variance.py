"""
modules/bias_variance.py -- live bias–variance trade-off simulator.

A polynomial of the chosen degree is fit to fresh noisy samples of sin(2πx);
three figures (the fit, the train/test error curve, the bias²/variance/noise
composition) and a readout strip are all recomputed from the controls. The
decomposition is the Monte-Carlo estimate verified in the unit tests, so the
displayed bias² + variance + noise reconstructs the measured error.
"""
from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import bias_variance_core as BV
from i18n import t

MAX_DEGREE = 14
DEFAULT_N = 40
DEFAULT_NOISE = 0.22
DEFAULT_SEED = 0

# Composition colors: muted navy / crimson / gold for bias² / variance / noise.
_BIAS_C = "#3C5A78"
_VAR_C = P.CRIMSON
_NOISE_C = P.GOLD


@st.cache_data(show_spinner=False)
def _err_curve(max_degree, n_train, noise, seed):
    d, tr, te = BV.error_vs_degree(max_degree, n_train, noise, seed, n_repeats=40)
    return np.asarray(d), np.asarray(tr), np.asarray(te)


@st.cache_data(show_spinner=False)
def _composition(max_degree, n_train, noise, seed):
    return BV.composition_vs_degree(max_degree, n_train, noise, seed)


@st.cache_data(show_spinner=False)
def _decomp(degree, n_train, noise, seed):
    return BV.bias_variance_decomposition(degree, n_train, noise, seed,
                                          n_datasets=200, n_eval=200)


def _fmt(v: float) -> str:
    if not np.isfinite(v):
        return "—"
    if abs(v) >= 1000:
        return f"{v:.2e}"
    return f"{v:.3f}"


def render(lang: str) -> None:
    C.eyebrow(t(lang, "pr_bv_eyebrow"))
    C.section_title(t(lang, "pr_bv"))
    C.measure(f"<p>{t(lang, 'pr_bv_intro')}</p>")

    # ---- controls ----
    with st.container(border=True):
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            degree = st.slider(t(lang, "pr_bv_ctrl_degree"), 1, MAX_DEGREE, 3, 1)
        with c2:
            n_train = st.slider(t(lang, "pr_bv_ctrl_n"), 15, 120, DEFAULT_N, 5)
        with c3:
            noise = st.slider(t(lang, "pr_bv_ctrl_noise"), 0.0, 0.6,
                              DEFAULT_NOISE, 0.02)
        with c4:
            seed = st.slider(t(lang, "pr_bv_ctrl_seed"), 0, 50, DEFAULT_SEED, 1)

    # ---- compute ----
    fit = BV.fit_and_score(degree, n_train, noise, seed)
    degs, tr, te = _err_curve(MAX_DEGREE, n_train, noise, seed)
    comp = _composition(MAX_DEGREE, n_train, noise, seed)
    dec = _decomp(degree, n_train, noise, seed)
    best_deg = int(degs[int(np.argmin(te))])

    # ---- Figure 1: single fit ----
    with st.container(border=True):
        f1 = go.Figure()
        f1.add_trace(go.Scatter(
            x=fit["x_train"], y=fit["y_train"], mode="markers",
            name="Training data",
            marker=dict(size=7, color=P.SLATE, opacity=0.55,
                        line=dict(width=0)),
        ))
        f1.add_trace(go.Scatter(
            x=fit["grid"], y=fit["truth"], mode="lines", name="True f(x)",
            line=dict(color=P.TEAL, width=2.5),
        ))
        f1.add_trace(go.Scatter(
            x=fit["grid"], y=fit["curve"], mode="lines",
            name=f"Fitted (deg {degree})",
            line=dict(color=P.CRIMSON, width=2.5),
        ))
        P.style_2d(f1, x_title="x", y_title="y", height=380)
        f1.update_yaxes(range=[-2.4, 2.4])
        f1.update_xaxes(range=[0, 1])
        st.plotly_chart(f1, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "pr_bv_cap_fit"))

    # ---- Figures 2 & 3 side by side ----
    g_left, g_right = st.columns(2)
    with g_left:
        with st.container(border=True):
            f2 = go.Figure()
            f2.add_trace(go.Scatter(x=degs, y=tr, mode="lines+markers",
                                    name="Train", line=dict(color=P.INK, width=2),
                                    marker=dict(size=6)))
            f2.add_trace(go.Scatter(x=degs, y=te, mode="lines+markers",
                                    name="Test", line=dict(color=P.CRIMSON, width=2),
                                    marker=dict(size=6)))
            P.style_2d(f2, x_title="Polynomial degree",
                       y_title="Mean squared error (log)", height=360, y_log=True)
            f2.add_vline(x=best_deg, line=dict(color=P.GOLD, width=1.5, dash="dash"))
            f2.add_annotation(x=best_deg, y=1.0, yref="paper", yanchor="bottom",
                              showarrow=False, text=f"best = {best_deg}",
                              font=dict(family=P.MONO, size=10, color=P.GOLD))
            st.plotly_chart(f2, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "pr_bv_cap_err"))

    with g_right:
        with st.container(border=True):
            f3 = go.Figure()
            f3.add_trace(go.Bar(x=comp["degrees"], y=comp["bias2_pct"],
                                name="Bias²", marker_color=_BIAS_C))
            f3.add_trace(go.Bar(x=comp["degrees"], y=comp["variance_pct"],
                                name="Variance", marker_color=_VAR_C))
            f3.add_trace(go.Bar(x=comp["degrees"], y=comp["noise_pct"],
                                name="Noise", marker_color=_NOISE_C))
            P.style_2d(f3, x_title="Polynomial degree",
                       y_title="Share of expected error (%)", height=360)
            f3.update_layout(barmode="stack")
            f3.update_yaxes(range=[0, 100])
            f3.add_vline(x=degree, line=dict(color=P.INK, width=1.2, dash="dot"))
            st.plotly_chart(f3, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "pr_bv_cap_comp"))

    # ---- readouts ----
    test_color = "crimson" if fit["test_mse"] > 1.6 * fit["train_mse"] + 0.02 else None
    C.readout_strip([
        {"k": "TRAIN MSE", "v": _fmt(fit["train_mse"])},
        {"k": "TEST MSE", "v": _fmt(fit["test_mse"]), "color": test_color},
        {"k": "BIAS²", "v": _fmt(dec["bias2"]), "color": "teal"},
        {"k": "VARIANCE", "v": _fmt(dec["variance"]), "color": "crimson"},
        {"k": "BEST DEGREE", "v": str(best_deg)},
    ])

    # ---- status ----
    if degree <= best_deg - 2:
        C.warn(t(lang, "pr_bv_underfit"))
    elif degree >= best_deg + 2:
        C.warn(t(lang, "pr_bv_overfit"))
    else:
        C.key_idea(t(lang, "pr_bv_balanced"))
