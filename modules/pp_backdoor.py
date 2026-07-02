"""
modules/pp_backdoor.py -- Practice demo: Backdoor Injection Lab.

A real CNN poisoned with a corner trigger. Toggle the trigger on a test image
and watch the prediction jump to the attacker's target class, even though the
model is highly accurate on clean data.
"""
from __future__ import annotations

import plotly.graph_objects as go
import streamlit as st

import components as C
import plotting as P
from core import vision_core as V
from core import privacy_core as PV
from i18n import t


@st.cache_resource(show_spinner=False)
def _backdoored():
    net, clean_acc, target = PV.make_backdoored_cnn(target=1, seed=0)
    return net, clean_acc, target


@st.cache_data(show_spinner=False)
def _samples():
    X, y, _ = V.make_shapes_dataset(8, spurious=False, seed=123)
    return X, y


@st.cache_data(show_spinner=False)
def _asr():
    net, _, target = _backdoored()
    Xc, yc, _ = V.make_shapes_dataset(60, spurious=False, seed=77)
    return PV.backdoor_success_rate(net, Xc, target)


def _img_fig(z, height=300):
    fig = go.Figure(go.Heatmap(z=z, colorscale="gray", showscale=False,
                               zmin=0, zmax=1))
    fig.update_layout(height=height, margin=dict(l=4, r=4, t=6, b=4),
                      paper_bgcolor=P.CARD, plot_bgcolor=P.CARD,
                      xaxis=dict(visible=False),
                      yaxis=dict(visible=False, scaleanchor="x",
                                 autorange="reversed"))
    return fig


def render(lang):
    net, clean_acc, target = _backdoored()
    X, y = _samples()

    with st.container(border=True):
        C.plate_header(t(lang, "pp_backdoor_eyebrow"), t(lang, "pp_backdoor"))
        C.demo_intro(t(lang, "pp_backdoor_what"), t(lang, "pp_backdoor_why"),
                     t(lang, "pp_backdoor_expect"),
                     labels=(t(lang, "di_what"), t(lang, "di_why"),
                             t(lang, "di_expect")))

        c1, c2 = st.columns(2)
        with c1:
            idx = st.selectbox(t(lang, "pp_backdoor_sample"), list(range(8)),
                               format_func=lambda i: f"#{i + 1}")
        with c2:
            triggered = st.checkbox(t(lang, "pp_backdoor_trigger"), value=False)

        x = X[idx:idx + 1]
        if triggered:
            x = PV.stamp_trigger(x)
        pred = int(net.predict(x)[0])
        conf = float(net.probs(x)[0, pred])

        st.plotly_chart(_img_fig(x[0, 0]), use_container_width=True,
                        config=P.PLOTLY_CONFIG)
        C.figure_caption(t(lang, "pp_backdoor_cap_clean"))

        is_target = pred == target
        C.readout_strip([
            {"k": t(lang, "pp_backdoor_cap_pred"),
             "v": t(lang, "px_cv_class" + str(pred)),
             "color": "crimson" if (triggered and is_target) else "teal"},
            {"k": "confidence", "v": f"{conf:.3f}"},
            {"k": t(lang, "pp_backdoor_clean_acc"), "v": f"{clean_acc:.2f}",
             "color": "teal"},
            {"k": t(lang, "pp_backdoor_asr"), "v": f"{_asr():.2f}",
             "color": "crimson"},
        ])
        if triggered:
            C.warn(t(lang, "pp_backdoor_note"))
        else:
            C.key_idea(t(lang, "pp_backdoor_note"))
