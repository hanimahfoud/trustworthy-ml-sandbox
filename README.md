---
title: Trustworthy Machine Learning
emoji: "⚖️"
colorFrom: indigo
colorTo: gray
sdk: docker
app_port: 8501
pinned: false
license: mit
---


# Trustworthy Machine Learning — an interactive sandbox

A trilingual (English · فارسی · العربية), journal-styled Streamlit application
that teaches trustworthy ML through **live, mathematically real** computation —
every figure is produced from actual models and gradients, never mocked.

**Prepared by** Hani Akram Mahfoudh · **Supervisor** Dr. Behrouz Minaei-Bidgoli

## Sections

**I · Generalization & Causal Foundations** — bias–variance, VC dimension,
inductive bias, transfer/DANN, SAM (sharpness-aware minimization), Simpson's
paradox and counterfactuals. Five interactive demos, all real compute.

**II · Explainability (XAI)** — interpretability vs explainability, the
black-box problem, LIME & SHAP, causal recourse, Grad-CAM/Saliency, and
vision–language attention. Four interactive demos:
- **LIME vs SHAP** on a real RandomForest loan model (exact Shapley values).
- **Causal recourse** — least-cost, causally-consistent counterfactuals.
- **Vision XAI scanner** — Grad-CAM / Saliency / Guided Grad-CAM from a CNN
  **built and trained from scratch in NumPy** (no PyTorch), with **real
  gradients** verified against finite differences.
- **Spurious-correlation detector** — Grad-CAM exposes a model that learned a
  background shortcut instead of the object.

**III · Fairness & Bias** — sources of bias, the fairness metrics and their
impossibility, mitigation (CDA, CLP, MinDiff/MMD, thresholding), adversarial
de-biasing (FAP), and LLM alignment (instruction tuning, RLHF, Constitutional
AI). Four interactive demos:
- **Fairness Scales** — move per-group thresholds and watch demographic parity,
  equal opportunity and equalized odds trade off live (the impossibility
  theorem, computed).
- **Counterfactual augmentation** — deterministic gender-swap of a sentence.
- **Implicit-bias simulator** and **Constitutional AI lab** — transparent,
  rule-based educational simulations (explicitly not live LLMs).

**IV · Robustness & Security** — adversarial attacks (poisoning vs evasion),
attack formulation and norms, evasion algorithms (FGSM, PGD, DeepFool, C&W),
defenses and the accuracy/robustness trade-off, certified robustness by
randomized smoothing, and LLM prompt injection. Four interactive demos:
- **Evasion simulator** — real FGSM/PGD attacks on the NumPy CNN; raise epsilon
  and watch the prediction flip while the image looks unchanged.
- **Accuracy vs robustness** — standard vs adversarially-trained model, measured
  live on clean data and under PGD.
- **Randomized smoothing** — a real Cohen et al. certified L2 radius.
- **LLM jailbreak game** — a transparent, rule-based prompt-injection simulation
  (explicitly not a live LLM).

**V · Privacy, Poisoning & Federated Learning** — data-poisoning and backdoor
trojans, privacy attacks (de-anonymization, membership inference), differential
privacy (ε-DP), noise mechanisms (randomized response, Laplace), federated
learning, and the gradient-leakage flaw. Four interactive demos:
- **Backdoor Injection Lab** — a real poisoned CNN; toggle the trigger and watch
  the prediction flip to the attacker's target while clean accuracy stays high.
- **Randomized-Response Simulator** — the coin-flip DP protocol; individual
  answers stay deniable while the aggregate rate is recovered.
- **Laplace Privacy Dashboard** — a differentially-private salary histogram with
  a live ε privacy-budget dial.
- **Gradient-Leakage Simulator** — reconstruct a client's private image from the
  shared gradient alone (DP-FL motivation).

Every practice demo now opens with a plain-language explainer (what it does, why
it matters, what to look for), and the theory plates are written as full
explanations with diagrams rather than bullet points.

**VI · Generative AI Safety & Alignment** — the alignment gap, RLHF (SFT +
Bradley–Terry reward model + PPO) and reward hacking, DPO's implicit reward,
the SimPO/RDPO/GRPO family, the OWASP LLM Top 10, and excessive agency. Four
interactive demos:
- **Reward-Hacking Simulator** — the closed-form KL-regularized policy; shrink β
  and watch the policy game an over-valued reward model.
- **GRPO Reasoning Visualizer** — K candidates scored by a real rule-based
  arithmetic verifier plus majority voting; no human labels.
- **Jailbreak Challenge** — a rule-based Gandalf-style guardrail; indirect
  framings defeat a naive refusal.
- **Excessive-Agency Sandbox** — an inbox with a hidden instruction; identical
  injection is inert under read-only, catastrophic under delete access.

## What makes it rigorous
- **No fake UI.** Every slider triggers genuine `numpy`/`scipy`/`scikit-learn`
  compute. The CNN is a real conv-net with im2col forward/backward.
- **Verified.** 79 unit tests: exact SHAP additivity (residual ≈ 0), causal
  recourse strictly cheaper, CNN gradients correct to ~1e-10 vs finite
  differences, Grad-CAM localizes the object, and the shortcut model's Grad-CAM
  provably lands on the spurious band.
- **Three themes** (Light / Dark / Colored), full RTL for Arabic & Persian,
  Cairo (Arabic) and Vazirmatn (Persian) typography.
- **Printable PDF** of any section's theory + practice text, in any language.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Hugging Face Spaces
1. Create a new Space → SDK: **Streamlit**.
2. Push this repository (the YAML header above sets `app_file: app.py`).
3. The Space installs `requirements.txt` and launches automatically. CPU
   Basic is sufficient; the NumPy CNN trains once (~10–30 s) and is cached.

## Tests
```bash
PYTHONPATH=. python -m pytest tests/     # or the bundled lightweight runner
```

## Layout
```
app.py            entry point (nav, theming, routing, PDF button)
nav.py            section / theory / practice key registry
i18n.py           English base + Persian + Arabic (Section I)
i18n_xai.py       Section II strings, merged into i18n
theme.py          3-theme, palette-driven CSS (LTR/RTL, per-language fonts)
components.py     masthead, plates, readouts, chatbot embed
plotting.py       one consistent academic Plotly grammar
core/             all compute engines (+ from-scratch NumPy CNN)
modules/          theory plates + interactive demos + pdf_export
tests/            79 unit tests
assets/           bundled Vazirmatn TTF (Arabic+Persian+Latin) for the PDF
```
