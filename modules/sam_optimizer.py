"""
modules/sam_optimizer.py -- SAM vs SGD on a sharp-vs-flat landscape.

The true loss L(w) has a narrow deep local minimum and a wide global one. SGD
descends L; SAM descends the worst-case surface E(w)=max_{‖ε‖≤ρ} L(w+ε). As ρ
grows the sharp well fills in on E, so SAM stops settling in the trap and moves
to the flat basin. Both 3-D surfaces, both descent paths, and the sharpness
readouts are recomputed from ρ.
"""
from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import sam_core as S
from i18n import t

DEFAULT_RHO = 0.55


@st.cache_data(show_spinner=False)
def _demo(rho: float):
    return S.compute_demo(rho=rho)


def render(lang: str) -> None:
    C.eyebrow(t(lang, "pr_sam_eyebrow"))
    C.section_title(t(lang, "pr_sam"))
    C.measure(f"<p>{t(lang, 'pr_sam_intro')}</p>")

    with st.container(border=True):
        rho = st.slider(t(lang, "pr_sam_ctrl_rho"), 0.0, 1.2, DEFAULT_RHO, 0.05)

    d = _demo(float(rho))
    Xt, Yt, Zt = d["true_surface"]
    Xe, Ye, Ze = d["eff_surface"]
    sgd, sam = d["sgd_traj"], d["sam_traj"]
    sgd_z, sam_z = d["sgd_loss_curve"], d["sam_loss_curve"]

    # ---- Figures 1 & 2: the two 3-D surfaces ----
    g_left, g_right = st.columns(2)
    with g_left:
        with st.container(border=True):
            f1 = go.Figure()
            f1.add_trace(go.Surface(x=Xt, y=Yt, z=Zt, colorscale=P.NAVY_SCALE,
                                    showscale=False, opacity=0.92))
            f1.add_trace(go.Scatter3d(
                x=sgd[:, 0], y=sgd[:, 1], z=np.asarray(sgd_z) + 0.04,
                mode="lines", name="SGD",
                line=dict(color=P.CRIMSON, width=5)))
            f1.add_trace(go.Scatter3d(
                x=sam[:, 0], y=sam[:, 1], z=np.asarray(sam_z) + 0.04,
                mode="lines", name="SAM",
                line=dict(color=P.TEAL, width=5)))
            P.style_3d(f1, z_title="Loss", height=440)
            st.plotly_chart(f1, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "pr_sam_cap_true"))

    with g_right:
        with st.container(border=True):
            f2 = go.Figure()
            f2.add_trace(go.Surface(x=Xe, y=Ye, z=Ze, colorscale=P.TEAL_SCALE,
                                    showscale=False, opacity=0.92))
            f2.add_trace(go.Scatter3d(
                x=[S.SHARP_C[0]], y=[S.SHARP_C[1]], z=[d["sharp_eff"] + 0.05],
                mode="markers", name="sharp",
                marker=dict(size=4, color=P.CRIMSON)))
            f2.add_trace(go.Scatter3d(
                x=[S.FLAT_C[0]], y=[S.FLAT_C[1]], z=[d["flat_eff"] + 0.05],
                mode="markers", name="flat",
                marker=dict(size=4, color=P.INK)))
            P.style_3d(f2, z_title="E(w)", height=440)
            st.plotly_chart(f2, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "pr_sam_cap_eff"))

    # ---- Figure 3: descent paths on the true-loss contour ----
    with st.container(border=True):
        f3 = go.Figure()
        f3.add_trace(go.Contour(
            x=Xt[0], y=Yt[:, 0], z=Zt, showscale=False,
            colorscale=P.NAVY_SCALE, opacity=0.55,
            contours=dict(coloring="heatmap"), hoverinfo="skip"))
        f3.add_trace(go.Scatter(x=sgd[:, 0], y=sgd[:, 1], mode="lines",
                                name="SGD", line=dict(color=P.CRIMSON, width=3)))
        f3.add_trace(go.Scatter(x=sam[:, 0], y=sam[:, 1], mode="lines",
                                name="SAM", line=dict(color=P.TEAL, width=3)))
        f3.add_trace(go.Scatter(x=[sgd[0, 0]], y=[sgd[0, 1]], mode="markers",
                                name="start",
                                marker=dict(size=10, color=P.INK, symbol="circle")))
        f3.add_trace(go.Scatter(x=[sgd[-1, 0]], y=[sgd[-1, 1]], mode="markers",
                                name="SGD end",
                                marker=dict(size=11, color=P.CRIMSON, symbol="x")))
        f3.add_trace(go.Scatter(x=[sam[-1, 0]], y=[sam[-1, 1]], mode="markers",
                                name="SAM end",
                                marker=dict(size=11, color=P.TEAL, symbol="star")))
        P.style_2d(f3, x_title="w₁", y_title="w₂", height=380)
        st.plotly_chart(f3, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "pr_sam_cap_traj"))

    # ---- readouts ----
    sam_basin = d["sam_basin"]
    C.readout_strip([
        {"k": "SHARP SHARPNESS", "v": f"{d['sharp_sharpness']:.2f}", "color": "crimson"},
        {"k": "FLAT SHARPNESS", "v": f"{d['flat_sharpness']:.2f}", "color": "teal"},
        {"k": "SGD BASIN", "v": d["sgd_basin"].upper(),
         "color": "teal" if d["sgd_basin"] == "flat" else "crimson"},
        {"k": "SAM BASIN", "v": sam_basin.upper(),
         "color": "teal" if sam_basin == "flat" else "crimson"},
    ])

    # ---- status ----
    if sam_basin == "flat":
        C.key_idea(t(lang, "pr_sam_flat"))
    else:
        C.warn(t(lang, "pr_sam_sharp"))
