"""
modules/quiz.py -- Exam mode: per-section comprehensive exams.

Question banks reference i18n keys (see i18n_quiz.py for the key convention);
all randomness (question order, choice order, numeric parameters) is derived
from a per-attempt seed kept in session state, so the exam is stable across
Streamlit reruns within one attempt and fresh on every retake.

Question kinds
  mcq  four choices; the correct one is ALWAYS the "_a" i18n key (index 0);
       the displayed order is a per-attempt permutation, so position varies.
  tf   True/False.
  num  numeric answer computed from generated parameters (1% tolerance).
"""
from __future__ import annotations

import random
import time

import streamlit as st

import components as C
from i18n import t

PASS = 70          # % needed to earn the section badge
_LETTERS = "abcd"

# --------------------------------------------------------------------------- #
# Question banks. "page" = (mode, page_idx) of the lesson to review.           #
# --------------------------------------------------------------------------- #
BANK = {
    "sec1": [
        {"id": "s1q1", "type": "mcq", "page": ("mode_theory", 0)},
        {"id": "s1q2", "type": "mcq", "page": ("mode_theory", 0)},
        {"id": "s1q3", "type": "mcq", "page": ("mode_theory", 0)},
        {"id": "s1q4", "type": "mcq", "page": ("mode_theory", 1)},
        {"id": "s1q5", "type": "mcq", "page": ("mode_theory", 2)},
        {"id": "s1q6", "type": "mcq", "page": ("mode_theory", 3)},
        {"id": "s1q7", "type": "mcq", "page": ("mode_theory", 4)},
        {"id": "s1q8", "type": "mcq", "page": ("mode_theory", 5)},
        {"id": "s1t1", "type": "tf", "ans": False, "page": ("mode_theory", 0)},
        {"id": "s1t2", "type": "tf", "ans": True, "page": ("mode_theory", 3)},
        {"id": "s1n1", "type": "num", "gen": "bv_total", "page": ("mode_theory", 0)},
        {"id": "s1n2", "type": "num", "gen": "var_ensemble", "page": ("mode_theory", 0)},
    ],
    "sec2": [
        {"id": "s2q1", "type": "mcq", "page": ("mode_theory", 0)},
        {"id": "s2q2", "type": "mcq", "page": ("mode_theory", 2)},
        {"id": "s2q3", "type": "mcq", "page": ("mode_theory", 2)},
        {"id": "s2q4", "type": "mcq", "page": ("mode_theory", 3)},
        {"id": "s2q5", "type": "mcq", "page": ("mode_theory", 3)},
        {"id": "s2q6", "type": "mcq", "page": ("mode_theory", 4)},
        {"id": "s2q7", "type": "mcq", "page": ("mode_theory", 4)},
        {"id": "s2q8", "type": "mcq", "page": ("mode_theory", 1)},
        {"id": "s2t1", "type": "tf", "ans": True, "page": ("mode_theory", 2)},
        {"id": "s2t2", "type": "tf", "ans": False, "page": ("mode_theory", 0)},
        {"id": "s2n1", "type": "num", "gen": "shap_missing", "page": ("mode_theory", 2)},
        {"id": "s2n2", "type": "num", "gen": "lime_local", "page": ("mode_theory", 2)},
    ],
}


# --------------------------------------------------------------------------- #
# Numeric-question generators: rng -> (format params, float answer).           #
# Params are pre-formatted strings so they slot into every language's text.    #
# --------------------------------------------------------------------------- #
def _gen_bv_total(rng: random.Random):
    b = rng.choice([0.1, 0.2, 0.3, 0.4, 0.5])
    v = rng.choice([0.05, 0.10, 0.15, 0.20])
    n = rng.choice([0.05, 0.10, 0.15])
    ans = b * b + v + n
    return {"b": f"{b:.2f}", "v": f"{v:.2f}", "n": f"{n:.2f}",
            "b2": f"{b * b:.3f}"}, ans


def _gen_var_ensemble(rng: random.Random):
    k = rng.choice([2, 4, 5, 8, 10])
    v = rng.choice([0.2, 0.4, 0.5, 0.8, 1.0])
    return {"k": str(k), "v": f"{v:.2f}"}, v / k


def _gen_shap_missing(rng: random.Random):
    base = rng.choice([0.30, 0.35, 0.40])
    p1, p2, p3 = (rng.choice([-0.10, -0.05, 0.05, 0.10, 0.15, 0.20])
                  for _ in range(3))
    p4 = rng.choice([0.05, 0.08, 0.10, 0.12, 0.15])
    fx = base + p1 + p2 + p3 + p4
    return {"fx": f"{fx:.2f}", "base": f"{base:.2f}", "p1": f"{p1:.2f}",
            "p2": f"{p2:.2f}", "p3": f"{p3:.2f}"}, p4


def _gen_lime_local(rng: random.Random):
    w1 = rng.choice([0.2, 0.3, 0.4, 0.5])
    w2 = rng.choice([-0.3, -0.2, -0.1, 0.1])
    b = rng.choice([0.0, 0.1, 0.2])
    z1 = rng.choice([1, 2, 3])
    z2 = rng.choice([1, 2])
    ans = w1 * z1 + w2 * z2 + b
    return {"w1": f"{w1:.1f}", "w2": f"{w2:.1f}", "b": f"{b:.1f}",
            "z1": str(z1), "z2": str(z2)}, ans


GENS = {"bv_total": _gen_bv_total, "var_ensemble": _gen_var_ensemble,
        "shap_missing": _gen_shap_missing, "lime_local": _gen_lime_local}


# --------------------------------------------------------------------------- #
# Attempt materialization: one deterministic pass, seeded per (section,        #
# attempt), yields question order, choice permutations and numeric params.     #
# --------------------------------------------------------------------------- #
def _materialize(sec: str, attempt: int):
    rng = random.Random(f"{sec}-{attempt}")
    qs = []
    for q in BANK[sec]:
        item = dict(q)
        if q["type"] == "mcq":
            item["perm"] = rng.sample(range(4), 4)
        elif q["type"] == "num":
            params, ans = GENS[q["gen"]](rng)
            params["ans"] = f"{ans:.3f}"
            item["params"], item["ans"] = params, ans
        qs.append(item)
    rng.shuffle(qs)
    return qs


def _goto(sec: str, mode: str, idx: int):
    """Jump to a lesson page from the review panel (same contract as
    app._go_page, incl. updating the _prev_* trackers so the sidebar's
    change-detection guard does not reset page_idx back to 0)."""
    ss = st.session_state
    ss["section"] = sec
    ss["mode"] = mode
    ss["page_idx"] = idx
    ss["_prev_section"] = sec
    ss["_prev_mode"] = mode
    ss["overlay"] = None


def _retry(sec: str):
    ss = st.session_state
    ss[f"qz_attempt_{sec}"] = ss.get(f"qz_attempt_{sec}", 1) + 1
    ss.pop(f"qz_result_{sec}", None)


def _fmt_ans(lang: str, q: dict, value) -> str:
    """Human-readable form of an answer (the user's or the correct one)."""
    if value is None:
        return t(lang, "quiz_no_answer")
    if q["type"] == "mcq":
        return t(lang, f"qz_{q['id']}_{_LETTERS[value]}")
    if q["type"] == "tf":
        return t(lang, "quiz_true" if value else "quiz_false")
    return f"{value:.3f}"


def _grade_one(q: dict, user):
    if user is None:
        return False
    if q["type"] == "mcq":
        return user == 0                       # "_a" is always correct
    if q["type"] == "tf":
        return user == q["ans"]
    tol = max(0.005, 0.01 * abs(q["ans"]))
    return abs(float(user) - q["ans"]) <= tol


def render(lang: str, sec: str) -> None:
    if sec not in BANK:
        C.info_panel(t(lang, "quiz_soon_title"), t(lang, "quiz_soon_body"))
        return

    ss = st.session_state
    attempt = ss.setdefault(f"qz_attempt_{sec}", 1)
    qs = _materialize(sec, attempt)
    ss.setdefault(f"qz_start_{sec}_{attempt}", time.time())

    C.info_panel(f"📝 {t(lang, 'quiz_title')}", t(lang, "quiz_intro"),
                 note=t(lang, "quiz_badge_note").format(p=PASS))

    # ---- the exam form -------------------------------------------------- #
    def _wkey(qid: str) -> str:
        return f"qzw_{sec}_{attempt}_{qid}"

    def _qtext(q: dict) -> str:
        raw = t(lang, f"qz_{q['id']}")
        return raw.format(**q["params"]) if q["type"] == "num" else raw

    with st.form(f"qzf_{sec}_{attempt}"):
        for i, q in enumerate(qs):
            with st.container(border=True):
                st.markdown(f'<div class="plate-eyebrow">'
                            f'{t(lang, "quiz_q")} {i + 1:02d} / {len(qs)}</div>',
                            unsafe_allow_html=True)
                st.markdown(f"**{_qtext(q)}**")
                if q["type"] == "mcq":
                    st.radio(q["id"], q["perm"], index=None, key=_wkey(q["id"]),
                             format_func=lambda j, qk=q["id"]:
                                 t(lang, f"qz_{qk}_{_LETTERS[j]}"),
                             label_visibility="collapsed")
                elif q["type"] == "tf":
                    st.radio(q["id"], [True, False], index=None,
                             key=_wkey(q["id"]), horizontal=True,
                             format_func=lambda v:
                                 t(lang, "quiz_true" if v else "quiz_false"),
                             label_visibility="collapsed")
                else:
                    st.number_input(t(lang, "quiz_num_hint"), value=None,
                                    step=0.001, format="%.3f",
                                    key=_wkey(q["id"]))
        submitted = st.form_submit_button(f"✓ {t(lang, 'quiz_submit')}",
                                          use_container_width=True)

    # ---- grading --------------------------------------------------------- #
    if submitted:
        correct = sum(_grade_one(q, ss.get(_wkey(q["id"]))) for q in qs)
        pct = round(100 * correct / len(qs))
        elapsed = int(time.time() - ss[f"qz_start_{sec}_{attempt}"])
        ss[f"qz_result_{sec}"] = {"attempt": attempt, "pct": pct,
                                  "correct": correct, "total": len(qs),
                                  "elapsed": elapsed}
        best = ss.setdefault("qz_best", {})
        best[sec] = max(best.get(sec, 0), pct)

    # ---- results + review ------------------------------------------------ #
    res = ss.get(f"qz_result_{sec}")
    if not res or res["attempt"] != attempt:
        return

    pct, correct, total = res["pct"], res["correct"], res["total"]
    color = "teal" if pct >= PASS else "crimson"
    C.readout_strip([
        {"k": t(lang, "quiz_score"), "v": f"{pct}", "u": "%", "color": color},
        {"k": t(lang, "quiz_correct_n"), "v": f"{correct} / {total}"},
        {"k": t(lang, "quiz_time"),
         "v": t(lang, "quiz_time_fmt").format(m=res["elapsed"] // 60,
                                              s=res["elapsed"] % 60)},
    ])
    if pct >= 90:
        C.key_idea(f"🏅 {t(lang, 'quiz_v_excellent')}")
    elif pct >= 75:
        C.key_idea(f"🏅 {t(lang, 'quiz_v_vgood')}")
    elif pct >= 60:
        C.warn(t(lang, "quiz_v_good"))
    else:
        C.warn(t(lang, "quiz_v_weak"))
    if pct >= PASS:
        st.markdown(f'<div class="rail-label">{t(lang, "quiz_passed")}</div>',
                    unsafe_allow_html=True)

    st.button(t(lang, "quiz_retry"), key=f"qz_retry_{sec}",
              use_container_width=True, on_click=_retry, args=(sec,))

    st.markdown(f"### {t(lang, 'quiz_review')}")
    for i, q in enumerate(qs):
        user = ss.get(_wkey(q["id"]))
        ok = _grade_one(q, user)
        correct_val = (0 if q["type"] == "mcq"
                       else q["ans"] if q["type"] == "tf" else q["ans"])
        explain = t(lang, f"qz_{q['id']}_x")
        if q["type"] == "num":
            explain = explain.format(**q["params"])
        with st.container(border=True):
            st.markdown(f"{'✅' if ok else '❌'} **{i + 1}. {_qtext(q)}**")
            st.markdown(
                f"- **{t(lang, 'quiz_your_answer')}:** {_fmt_ans(lang, q, user)}\n"
                f"- **{t(lang, 'quiz_right_answer')}:** "
                f"{_fmt_ans(lang, q, correct_val)}\n"
                f"- **{t(lang, 'quiz_explain')}:** {explain}")
            if not ok:
                mode, idx = q["page"]
                st.button(t(lang, "quiz_open_lesson"),
                          key=f"qzgo_{sec}_{attempt}_{q['id']}",
                          on_click=_goto, args=(sec, mode, idx))
