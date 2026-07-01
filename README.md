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

## What makes it rigorous
- **No fake UI.** Every slider triggers genuine `numpy`/`scipy`/`scikit-learn`
  compute. The CNN is a real conv-net with im2col forward/backward.
- **Verified.** 57 unit tests: exact SHAP additivity (residual ≈ 0), causal
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
tests/            57 unit tests
assets/           bundled Vazirmatn TTF (Arabic+Persian+Latin) for the PDF
```
