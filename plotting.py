"""
plotting.py -- a single, consistent visual grammar for every figure.

All charts in the sandbox are drawn with Plotly and share one typeset
"academic" look: white plate background, hairline grid, Merriweather for prose
labels and IBM Plex Mono for numbers and axis titles, and a restrained
navy / crimson / teal palette that matches the page theme. Keeping this in one
place is what makes a dozen different demos look like figures from the same
monograph rather than a pile of dashboards.

Nothing here imports Streamlit, so the module stays light and the styling can be
reasoned about (and unit-checked) on its own.
"""
from __future__ import annotations

import plotly.graph_objects as go

# --- Palette (kept in sync with theme.py by hand; small + stable) ----------- #
INK = "#0E2A47"
DEEP = "#0A1F38"
SLATE = "#5A6B7B"
PARCHMENT = "#F7F5EF"
CARD = "#FFFFFF"
CRIMSON = "#8A1C2B"
TEAL = "#0F6E66"
HAIRLINE = "#D9D4C7"
GOLD = "#A8842C"

SERIF = "Merriweather, Georgia, 'Times New Roman', serif"
MONO = "IBM Plex Mono, 'SFMono-Regular', Menlo, monospace"

# Categorical order used across the app: ink, then the two accents, then golds.
COLORWAY = [INK, CRIMSON, TEAL, GOLD, SLATE, "#3C5A78"]

# Monochrome navy ramp for the "true" loss surface; warm teal ramp for the
# worst-case (effective) surface so the two 3-D plots never get confused.
NAVY_SCALE = [[0.0, "#0A1F38"], [0.45, "#3C5A78"], [0.8, "#9FB0C0"], [1.0, "#ECE7DA"]]
TEAL_SCALE = [[0.0, "#0C4F49"], [0.45, "#2C7E76"], [0.8, "#9AC3BD"], [1.0, "#EFE9DB"]]

# Passed straight to st.plotly_chart(config=...).
PLOTLY_CONFIG = {
    "displayModeBar": False,
    "scrollZoom": False,
    "doubleClick": "reset",
    "displaylogo": False,
}


def _axis(title: str | None = None):
    """Common 2-D axis styling: hairline grid, mono ticks, no zero-line clutter."""
    return dict(
        title=dict(text=title or "", font=dict(family=MONO, size=12, color=INK)),
        showgrid=True, gridcolor=HAIRLINE, gridwidth=1,
        zeroline=False, showline=True, linecolor="#C4BFB1", linewidth=1,
        ticks="outside", ticklen=4, tickcolor="#C4BFB1",
        tickfont=dict(family=MONO, size=11, color=SLATE),
    )


def style_2d(fig: go.Figure, *, x_title: str = "", y_title: str = "",
             height: int = 360, y_log: bool = False, legend: bool = True,
             margin_t: int = 28) -> go.Figure:
    """Apply the house style to any 2-D Plotly figure, in place."""
    fig.update_layout(
        template="simple_white",
        paper_bgcolor=CARD, plot_bgcolor=CARD,
        colorway=COLORWAY,
        font=dict(family=SERIF, size=13, color=INK),
        height=height,
        margin=dict(l=58, r=22, t=margin_t, b=48),
        xaxis=_axis(x_title),
        yaxis=_axis(y_title),
        hoverlabel=dict(font=dict(family=MONO, size=12), bgcolor="#FFFFFF",
                        bordercolor=HAIRLINE),
        showlegend=legend,
        legend=dict(
            font=dict(family=MONO, size=11, color=INK),
            bgcolor="rgba(255,255,255,0.65)", bordercolor=HAIRLINE, borderwidth=1,
            orientation="h", yanchor="bottom", y=1.0, xanchor="right", x=1.0,
        ),
        bargap=0.18,
    )
    if y_log:
        fig.update_yaxes(type="log")
    return fig


def style_3d(fig: go.Figure, *, height: int = 460,
             z_title: str = "Loss", eye=(1.5, 1.4, 0.9)) -> go.Figure:
    """House style for 3-D surface plots (the SAM landscapes)."""
    _tfont = dict(family=MONO, size=11, color=SLATE)
    axis = dict(
        showbackground=True, backgroundcolor="#FCFBF7",
        gridcolor=HAIRLINE, zeroline=False,
        tickfont=dict(family=MONO, size=9, color=SLATE),
    )

    def _ax(text):
        return dict(title=dict(text=text, font=_tfont), **axis)

    fig.update_layout(
        paper_bgcolor=CARD,
        font=dict(family=SERIF, size=12, color=INK),
        height=height,
        margin=dict(l=2, r=2, t=24, b=2),
        showlegend=True,
        legend=dict(font=dict(family=MONO, size=11), bgcolor="rgba(255,255,255,0.7)",
                    bordercolor=HAIRLINE, borderwidth=1, x=0.0, y=1.0),
        scene=dict(
            xaxis=_ax("w₁"),
            yaxis=_ax("w₂"),
            zaxis=_ax(z_title),
            camera=dict(eye=dict(x=eye[0], y=eye[1], z=eye[2])),
            aspectmode="cube",
        ),
    )
    return fig


def empty_note(message: str, height: int = 320) -> go.Figure:
    """A blank styled canvas carrying a single centered note (e.g. error states)."""
    fig = go.Figure()
    fig.add_annotation(text=message, x=0.5, y=0.5, xref="paper", yref="paper",
                       showarrow=False,
                       font=dict(family=MONO, size=13, color=CRIMSON))
    fig.update_layout(paper_bgcolor=CARD, plot_bgcolor=CARD, height=height,
                      xaxis=dict(visible=False), yaxis=dict(visible=False),
                      margin=dict(l=10, r=10, t=10, b=10))
    return fig


# --------------------------------------------------------------------------- #
# Reusable directed-acyclic-graph figure (Simpson confounder + SCM diagrams)   #
# --------------------------------------------------------------------------- #
def causal_dag_figure(nodes: dict, edges: list, *,
                      labels: dict | None = None,
                      node_colors: dict | None = None,
                      edge_colors: dict | None = None,
                      label_positions: dict | None = None,
                      height: int = 340, title: str | None = None,
                      footnotes: list | None = None) -> go.Figure:
    """
    Draw a small causal graph: nodes as ringed dots with outside labels and
    directed edges as trimmed arrow annotations. Reused by the Simpson and
    counterfactual demos so every diagram in the app is visually identical.

    nodes           : {key: (x, y)}
    edges           : [(src_key, dst_key), ...]
    labels          : {key: display_text}  (defaults to the key)
    node_colors     : {key: hex}            (ring + dot tint; defaults to INK)
    edge_colors     : {(src,dst): hex}      (defaults to SLATE)
    label_positions : {key: plotly textposition}  (defaults chosen by geometry)
    footnotes       : list of small mono captions placed under the graph
    """
    labels = labels or {}
    node_colors = node_colors or {}
    edge_colors = edge_colors or {}
    label_positions = label_positions or {}

    xs = [p[0] for p in nodes.values()]
    ys = [p[1] for p in nodes.values()]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    span_x = max(x_max - x_min, 1e-6)
    span_y = max(y_max - y_min, 1e-6)
    pad_x = 0.35 * span_x + 0.15
    pad_y = 0.45 * span_y + 0.20

    fig = go.Figure()

    # ---- edges as arrows, trimmed so the head rests just off the node dot ----
    for (s, d) in edges:
        x0, y0 = nodes[s]
        x1, y1 = nodes[d]
        dx, dy = x1 - x0, y1 - y0
        dist = (dx * dx + dy * dy) ** 0.5 or 1.0
        ux, uy = dx / dist, dy / dist
        gap0, gap1 = 0.12 * dist + 0.03, 0.16 * dist + 0.05
        color = edge_colors.get((s, d), SLATE)
        fig.add_annotation(
            x=x1 - ux * gap1, y=y1 - uy * gap1,
            ax=x0 + ux * gap0, ay=y0 + uy * gap0,
            xref="x", yref="y", axref="x", ayref="y",
            showarrow=True, arrowhead=3, arrowsize=1.2, arrowwidth=1.7,
            arrowcolor=color, standoff=0, startstandoff=0,
        )

    # ---- nodes as ringed dots with labels just outside ----
    def default_pos(key):
        x, y = nodes[key]
        if y >= (y_min + y_max) / 2 + 1e-9:      # upper node -> label above
            return "top center"
        return "bottom center"

    nx, ny, ntext, tpos, fills, lines = [], [], [], [], [], []
    for key, (x, y) in nodes.items():
        nx.append(x); ny.append(y)
        ntext.append(labels.get(key, key))
        tpos.append(label_positions.get(key, default_pos(key)))
        col = node_colors.get(key, INK)
        fills.append(_tint(col, 0.10))
        lines.append(col)

    fig.add_trace(go.Scatter(
        x=nx, y=ny, mode="markers+text",
        text=ntext, textposition=tpos,
        textfont=dict(family=MONO, size=12, color=INK),
        marker=dict(size=22, color=fills,
                    line=dict(color=lines, width=2.2)),
        hoverinfo="skip", showlegend=False,
    ))

    fig.update_layout(
        paper_bgcolor=CARD, plot_bgcolor=CARD,
        height=height, margin=dict(l=10, r=10, t=30 if title else 12, b=10),
        title=dict(text=title or "", font=dict(family=MONO, size=12, color=SLATE),
                   x=0.02, xanchor="left"),
        xaxis=dict(visible=False, range=[x_min - pad_x, x_max + pad_x]),
        yaxis=dict(visible=False, range=[y_min - pad_y, y_max + pad_y],
                   scaleanchor="x", scaleratio=1),
        showlegend=False,
    )

    if footnotes:
        for i, note in enumerate(footnotes):
            fig.add_annotation(
                x=0.0, y=-0.02 - 0.07 * i, xref="paper", yref="paper",
                xanchor="left", yanchor="top", showarrow=False, text=note,
                font=dict(family=MONO, size=10.5, color=SLATE),
            )
    return fig


def _tint(hex_color: str, alpha: float) -> str:
    """Return an rgba() string of ``hex_color`` over white at the given alpha."""
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    r = int(r * alpha + 255 * (1 - alpha))
    g = int(g * alpha + 255 * (1 - alpha))
    b = int(b * alpha + 255 * (1 - alpha))
    return f"rgb({r},{g},{b})"
