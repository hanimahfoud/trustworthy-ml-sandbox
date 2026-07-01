"""
modules/counterfactual.py -- Pearl's three-step counterfactual, computed exactly.

A structural model with three latent customer types (responder, dog-hater,
always-sad) answers: given an observed (T, Y), what is P(Y=happy | do(T'))? The
abduction → action → prediction steps are run on the exact discrete model, so
the canonical query (prior .7/.1/.2, observe T=1,Y=0, do T=0) returns exactly
1/3. Prior-vs-posterior, the structural response table and the SCM diagram all
update from the controls.
"""
from __future__ import annotations

import streamlit as st
import plotly.graph_objects as go

import components as C
import plotting as P
from core import counterfactual_core as CF
from i18n import t

DEFAULT_PHATER = 0.10
DEFAULT_PSAD = 0.20


def render(lang: str) -> None:
    C.eyebrow(t(lang, "pr_cf_eyebrow"))
    C.section_title(t(lang, "pr_cf"))
    C.measure(f"<p>{t(lang, 'pr_cf_intro')}</p>")

    with st.container(border=True):
        c1, c2, c3, c4, c5 = st.columns(5)
        with c1:
            p_hater = st.slider(t(lang, "pr_cf_ctrl_phater"), 0.0, 0.6,
                                DEFAULT_PHATER, 0.05)
        with c2:
            p_sad = st.slider(t(lang, "pr_cf_ctrl_psad"), 0.0, 0.6,
                              DEFAULT_PSAD, 0.05)
        with c3:
            t_obs = st.selectbox(t(lang, "pr_cf_ctrl_tobs"), [0, 1], index=1)
        with c4:
            y_obs = st.selectbox(t(lang, "pr_cf_ctrl_yobs"), [0, 1], index=0)
        with c5:
            t_do = st.selectbox(t(lang, "pr_cf_ctrl_tdo"), [0, 1], index=0)

    prior = CF.make_prior(p_hater=float(p_hater), p_always_sad=float(p_sad))

    try:
        res = CF.counterfactual(prior, int(t_obs), int(y_obs), int(t_do))
    except ValueError:
        C.warn(t(lang, "pr_cf_impossible"))
        return

    order = list(CF.TYPES)
    labels = {
        "responder": t(lang, "pr_cf_responder"),
        "hater": t(lang, "pr_cf_hater"),
        "always_sad": t(lang, "pr_cf_always_sad"),
    }
    posterior = res["posterior"]
    rt = res["response_table"]

    # ---- headline ----
    C.readout_strip([
        {"k": "P(HAPPY | do)", "v": f"{res['fraction']}  =  {res['p_happy']:.3f}",
         "color": "teal"},
        {"k": "P(SAD | do)", "v": f"{res['p_sad']:.3f}", "color": "crimson"},
    ])

    # ---- Figures 1 & 3 side by side ----
    g_left, g_right = st.columns(2)
    with g_left:
        with st.container(border=True):
            f1 = go.Figure()
            f1.add_trace(go.Bar(
                x=[labels[k] for k in order], y=[prior[k] for k in order],
                name="Prior", marker_color=P.SLATE))
            f1.add_trace(go.Bar(
                x=[labels[k] for k in order], y=[posterior[k] for k in order],
                name="Posterior", marker_color=P.CRIMSON))
            P.style_2d(f1, x_title="Latent type", y_title="Probability",
                       height=360)
            f1.update_layout(barmode="group")
            f1.update_yaxes(range=[0, 1])
            st.plotly_chart(f1, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "pr_cf_cap_post"))

    with g_right:
        with st.container(border=True):
            nodes = {"U": (0.5, 1.0), "T": (0.0, 0.0), "Y": (1.0, 0.0)}
            edges = [("U", "Y"), ("T", "Y")]
            f3 = P.causal_dag_figure(
                nodes, edges,
                labels={"U": "U (type)", "T": "T", "Y": "Y"},
                node_colors={"U": P.CRIMSON, "T": P.INK, "Y": P.INK},
                edge_colors={("T", "Y"): P.TEAL},
                label_positions={"U": "top center", "T": "bottom center",
                                 "Y": "bottom center"},
                height=360)
            st.plotly_chart(f3, use_container_width=True, config=P.PLOTLY_CONFIG)
            C.figure_caption(t(lang, "pr_cf_cap_scm"))

    # ---- Figure 2: structural response table ----
    with st.container(border=True):
        f2 = go.Figure()
        f2.add_trace(go.Bar(
            x=[labels[k] for k in order], y=[rt[k]["T0"] for k in order],
            name="do(T=0)", marker_color=P.INK))
        f2.add_trace(go.Bar(
            x=[labels[k] for k in order], y=[rt[k]["T1"] for k in order],
            name="do(T=1)", marker_color=P.GOLD))
        P.style_2d(f2, x_title="Latent type", y_title="Outcome", height=320)
        f2.update_layout(barmode="group")
        f2.update_yaxes(range=[0, 1.15], tickvals=[0, 1],
                        ticktext=["Sad (0)", "Happy (1)"])
        st.plotly_chart(f2, use_container_width=True, config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "pr_cf_cap_table"))

    # ---- three-step trace ----
    post_pct = {k: f"{100.0 * posterior[k]:.0f}%" for k in order}
    consistent = ", ".join(labels[k] for k in res["steps"][0]["consistent_types"])
    trace_html = (
        "<ol>"
        f"<li><strong>{t(lang, 'pr_cf_step_abduction')}</strong><br>"
        f"<span style='font-family:{P.MONO};font-size:0.85em'>"
        f"consistent: {consistent} &nbsp;·&nbsp; "
        f"posterior = "
        + ", ".join(f"{labels[k]} {post_pct[k]}" for k in order)
        + "</span></li>"
        f"<li><strong>{t(lang, 'pr_cf_step_action')}</strong><br>"
        f"<span style='font-family:{P.MONO};font-size:0.85em'>do(T={int(t_do)})"
        "</span></li>"
        f"<li><strong>{t(lang, 'pr_cf_step_prediction')}</strong><br>"
        f"<span style='font-family:{P.MONO};font-size:0.85em'>"
        f"P(happy | do) = {res['fraction']} = {res['p_happy']:.3f}"
        "</span></li>"
        "</ol>"
    )
    C.key_idea(trace_html)
