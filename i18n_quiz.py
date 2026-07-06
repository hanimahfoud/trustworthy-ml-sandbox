"""
i18n_quiz.py -- strings for Exam mode: the quiz chrome (labels, verdicts,
review panel) and the per-section question banks, in English, Persian and
Arabic. Merged into LANG_DICT like every other i18n module.

Key conventions (consumed by modules/quiz.py):
  qz_<id>        question text (numeric questions carry {} placeholders)
  qz_<id>_a.._d  the four choices of an MCQ (index 0 == "_a" is NOT always
                 the correct one -- the answer index lives in the bank)
  qz_<id>_x      the one-sentence explanation shown after grading
"""
from __future__ import annotations

EN_QUIZ = {
    # ---- exam chrome ----
    "mode_quiz": "Exam",
    "quiz_page": "Section Exam",
    "choose_quiz": "📝 Exam",
    "quiz_eyebrow": "Assessment",
    "quiz_title": "Section Exam",
    "quiz_intro": "Twelve questions drawn from this section's theory and "
        "practice. Choices and numbers are reshuffled on every attempt. "
        "Answer everything, then press “Submit the exam”.",
    "quiz_q": "Question",
    "quiz_true": "True",
    "quiz_false": "False",
    "quiz_num_hint": "Enter a number (3 decimals).",
    "quiz_submit": "Submit the exam",
    "quiz_score": "Score",
    "quiz_correct_n": "Correct answers",
    "quiz_time": "Time taken",
    "quiz_time_fmt": "{m} min {s} s",
    "quiz_v_excellent": "Excellent — you have mastered this section.",
    "quiz_v_vgood": "Very good — a quick review will make it perfect.",
    "quiz_v_good": "Good — revisit the lessons flagged below.",
    "quiz_v_weak": "Needs review — reread the section, then try again.",
    "quiz_review": "Answer review",
    "quiz_your_answer": "Your answer",
    "quiz_no_answer": "— unanswered —",
    "quiz_right_answer": "Correct answer",
    "quiz_explain": "Why",
    "quiz_open_lesson": "Open the lesson →",
    "quiz_retry": "⟳ Retake with fresh questions",
    "quiz_badge_note": "Score {p}% or higher to earn this section's badge 🏅.",
    "quiz_passed": "Badge earned 🏅",
    "quiz_soon_title": "Exam under preparation",
    "quiz_soon_body": "The exam for this section is being written. Sections I "
        "and II already have exams — try one of them meanwhile.",

    # =================== Section I — Generalization ===================== #
    "qz_s1q1": "Into which three components does the expected test error of a "
        "supervised model decompose?",
    "qz_s1q1_a": "Squared bias, variance, and irreducible noise",
    "qz_s1q1_b": "Training error, validation error, and test error",
    "qz_s1q1_c": "Underfitting, overfitting, and regularization",
    "qz_s1q1_d": "Optimization error, learning rate, and batch size",
    "qz_s1q1_x": "E[(y−f̂(x))²] = Bias² + Variance + σ²: being too simple, being "
        "too sensitive, and the noise floor no model can remove.",

    "qz_s1q2": "Increasing a model's capacity typically…",
    "qz_s1q2_a": "lowers bias and raises variance",
    "qz_s1q2_b": "raises bias and lowers variance",
    "qz_s1q2_c": "lowers both bias and variance",
    "qz_s1q2_d": "raises both bias and variance",
    "qz_s1q2_x": "Flexibility buys a smaller systematic error but makes the fit "
        "more sensitive to the particular training sample.",

    "qz_s1q3": "The “double descent” phenomenon shows that…",
    "qz_s1q3_a": "test error can fall again once capacity grows far past the "
        "interpolation point",
    "qz_s1q3_b": "training error always rises twice during training",
    "qz_s1q3_c": "the classical U-shaped curve is exact for all models",
    "qz_s1q3_d": "variance grows monotonically with capacity, without exception",
    "qz_s1q3_x": "Heavily over-parameterized networks can generalize again beyond "
        "interpolation — the U-curve is a first intuition, not the whole story.",

    "qz_s1q4": "The VC dimension of a linear classifier (with bias term) in ℝᵈ is…",
    "qz_s1q4_a": "d + 1",
    "qz_s1q4_b": "d",
    "qz_s1q4_c": "2d + 1",
    "qz_s1q4_d": "d²",
    "qz_s1q4_x": "A hyperplane with an intercept can shatter at most d+1 points "
        "in general position in ℝᵈ.",

    "qz_s1q5": "“Inductive bias” refers to…",
    "qz_s1q5_a": "the set of assumptions a learner uses to generalize beyond "
        "the training data",
    "qz_s1q5_b": "the systematic error caused by a model that is too simple",
    "qz_s1q5_c": "social bias present in the labels of a dataset",
    "qz_s1q5_d": "the preference of optimizers for small learning rates",
    "qz_s1q5_x": "Without assumptions there is no generalization (no-free-lunch): "
        "convolutions assume locality, linear models assume linearity.",

    "qz_s1q6": "DANN (domain-adversarial training) aligns two domains by…",
    "qz_s1q6_a": "learning features that predict labels while fooling a domain "
        "discriminator",
    "qz_s1q6_b": "re-weighting the classes of the source domain",
    "qz_s1q6_c": "raising the learning rate on the target domain",
    "qz_s1q6_d": "training one separate model per domain",
    "qz_s1q6_x": "The gradient-reversal layer pushes the encoder toward features "
        "the domain discriminator cannot tell apart — domain-invariant features.",

    "qz_s1q7": "Sharpness-Aware Minimization (SAM) seeks parameters that…",
    "qz_s1q7_a": "keep the loss low across a whole neighborhood (flat minima)",
    "qz_s1q7_b": "reach the lowest possible training loss, however sharp",
    "qz_s1q7_c": "are as sparse as possible",
    "qz_s1q7_d": "make training converge in the fewest steps",
    "qz_s1q7_x": "SAM minimizes the worst-case loss in an ε-ball around the "
        "weights; flat minima tend to generalize better than sharp ones.",

    "qz_s1q8": "Simpson's paradox warns that a trend seen in aggregated data…",
    "qz_s1q8_a": "can reverse when the data are split by a confounding variable",
    "qz_s1q8_b": "always matches the trend inside every subgroup",
    "qz_s1q8_c": "is sufficient proof of a causal relationship",
    "qz_s1q8_d": "only appears when the sample is very small",
    "qz_s1q8_x": "Association is not causation: conditioning on the confounder "
        "can flip the sign of the apparent effect.",

    "qz_s1t1": "A sufficiently large model can eliminate the irreducible noise "
        "term σ² of the error decomposition.",
    "qz_s1t1_x": "False: σ² comes from the data-generating process itself; no "
        "model, however large, can remove it.",

    "qz_s1t2": "Under covariate shift, the input distribution p(x) changes while "
        "the conditional p(y|x) stays the same.",
    "qz_s1t2_x": "True: that is the definition of covariate shift, and it is why "
        "importance weighting / domain adaptation can work at all.",

    "qz_s1n1": "In the bias–variance decomposition, suppose Bias = {b}, "
        "Variance = {v} and noise σ² = {n}. Compute the expected squared error "
        "Bias² + Variance + σ².",
    "qz_s1n1_x": "Bias² = {b}² = {b2}; adding Variance {v} and noise {n} gives "
        "{ans}.",

    "qz_s1n2": "Averaging {k} models with independent errors leaves bias "
        "unchanged and divides variance by {k}. If a single model has "
        "Variance = {v}, what is the ensemble's variance?",
    "qz_s1n2_x": "{v} / {k} = {ans} — this is exactly why bagging tames "
        "high-variance learners.",

    # =================== Section II — Explainability ==================== #
    "qz_s2q1": "What distinguishes interpretability from explainability?",
    "qz_s2q1_a": "An interpretable model is transparent by design; explainability "
        "adds post-hoc explanations to a black box",
    "qz_s2q1_b": "They are exact synonyms in the literature",
    "qz_s2q1_c": "Explainability applies only to linear models",
    "qz_s2q1_d": "Interpretability is another name for accuracy",
    "qz_s2q1_x": "A shallow decision tree is interpretable in itself; SHAP or "
        "LIME explain a black box after the fact.",

    "qz_s2q2": "Which property do SHAP values satisfy for a single prediction?",
    "qz_s2q2_a": "They sum exactly to f(x) − E[f] (efficiency / additivity)",
    "qz_s2q2_b": "They are always positive",
    "qz_s2q2_c": "They are identical for every input",
    "qz_s2q2_d": "They exist only for tree ensembles",
    "qz_s2q2_x": "Efficiency is the Shapley axiom that makes the attribution "
        "complete: the contributions account for the whole gap from the base value.",

    "qz_s2q3": "LIME explains one prediction by…",
    "qz_s2q3_a": "fitting a simple weighted surrogate on perturbed samples "
        "around the instance",
    "qz_s2q3_b": "reading the network's weights directly",
    "qz_s2q3_c": "retraining the full model without each feature",
    "qz_s2q3_d": "computing exact Shapley values in closed form",
    "qz_s2q3_x": "Locally, even a black box is approximately linear — LIME fits "
        "that local surrogate and reports its coefficients.",

    "qz_s2q4": "A counterfactual explanation answers the question…",
    "qz_s2q4_a": "“what minimal change to the inputs would flip the decision?”",
    "qz_s2q4_b": "“which feature is globally most important?”",
    "qz_s2q4_c": "“how accurate is the model on the test set?”",
    "qz_s2q4_d": "“which samples were mislabeled during training?”",
    "qz_s2q4_x": "Counterfactuals are instance-level: the smallest movement across "
        "the decision boundary, e.g. “+$4k income would approve the loan”.",

    "qz_s2q5": "For recourse to be actionable, the recommended change must…",
    "qz_s2q5_a": "involve features the person can actually change — never "
        "immutable ones",
    "qz_s2q5_b": "maximize the model's confidence at any cost",
    "qz_s2q5_c": "alter as many features as possible at once",
    "qz_s2q5_d": "be applied to the training data as well",
    "qz_s2q5_x": "“Lower your age by five years” is not recourse; actionability "
        "constrains counterfactual search to mutable features.",

    "qz_s2q6": "Grad-CAM produces…",
    "qz_s2q6_a": "a class-specific heatmap from the gradients flowing into the "
        "last convolutional layer",
    "qz_s2q6_b": "a decision tree that mimics the CNN",
    "qz_s2q6_c": "a permutation ranking of tabular features",
    "qz_s2q6_d": "an adversarial example for the target class",
    "qz_s2q6_x": "The class score's gradients weight the conv feature maps, "
        "highlighting where the network looked for that class.",

    "qz_s2q7": "A vision model that detects “wolf” by looking at snowy "
        "backgrounds is an example of…",
    "qz_s2q7_a": "spurious correlation (shortcut learning)",
    "qz_s2q7_b": "double descent",
    "qz_s2q7_c": "differential privacy",
    "qz_s2q7_d": "reward hacking",
    "qz_s2q7_x": "The background co-occurs with the label in training data, so the "
        "shortcut works — until a wolf appears on grass.",

    "qz_s2q8": "The black-box problem matters most because…",
    "qz_s2q8_a": "high-stakes decisions (credit, medicine, justice) demand "
        "justification and auditability",
    "qz_s2q8_b": "black-box models are always less accurate",
    "qz_s2q8_c": "regulators forbid using neural networks anywhere",
    "qz_s2q8_d": "explanations make training substantially faster",
    "qz_s2q8_x": "Accuracy alone is not enough when a decision must be contested, "
        "audited or trusted by the person it affects.",

    "qz_s2t1": "KernelSHAP is model-agnostic: it only needs query access to the "
        "model's predictions.",
    "qz_s2t1_x": "True: it estimates Shapley values from input–output behavior "
        "alone, so it works for any classifier.",

    "qz_s2t2": "A deep neural network is inherently interpretable, so no "
        "explanation method is ever needed.",
    "qz_s2t2_x": "False: millions of entangled weights are exactly the black-box "
        "problem that motivates XAI.",

    "qz_s2n1": "For one prediction, f(x) = {fx} and the base value E[f] = {base}. "
        "Three of the four SHAP values are φ₁ = {p1}, φ₂ = {p2}, φ₃ = {p3}. "
        "Use additivity to compute φ₄.",
    "qz_s2n1_x": "φ₄ = f(x) − E[f] − φ₁ − φ₂ − φ₃ = {ans}.",

    "qz_s2n2": "A LIME local surrogate is g(z) = {w1}·z₁ + {w2}·z₂ + {b}. "
        "For z₁ = {z1} and z₂ = {z2}, compute g(z).",
    "qz_s2n2_x": "g = {w1}·{z1} + {w2}·{z2} + {b} = {ans} — the surrogate's "
        "coefficients are the explanation.",

    # ===================== Section III — Fairness ======================== #
    "qz_s3q1": "The primary source of unfairness in ML systems is usually…",
    "qz_s3q1_a": "historical and societal bias baked into the training data",
    "qz_s3q1_b": "floating-point rounding errors on the GPU",
    "qz_s3q1_c": "using a learning rate that is too small",
    "qz_s3q1_d": "applying too much L2 regularization",
    "qz_s3q1_x": "Models faithfully learn the patterns of their data — including "
        "discriminatory patterns of past decisions.",

    "qz_s3q2": "Demographic parity requires that…",
    "qz_s3q2_a": "the positive-prediction rate is equal across protected groups",
    "qz_s3q2_b": "the accuracy is equal across protected groups",
    "qz_s3q2_c": "every individual receives the same prediction",
    "qz_s3q2_d": "the training set contains equal group counts",
    "qz_s3q2_x": "P(ŷ=1 | A=a) must match across groups — it ignores the true "
        "labels entirely, which is both its strength and its weakness.",

    "qz_s3q3": "Equalized odds requires that…",
    "qz_s3q3_a": "true-positive AND false-positive rates match across groups",
    "qz_s3q3_b": "only the overall error rate matches across groups",
    "qz_s3q3_c": "the model never uses the protected attribute as input",
    "qz_s3q3_d": "predictions are calibrated within each group",
    "qz_s3q3_x": "Conditioning on the true label separates it from demographic "
        "parity: qualified and unqualified people are each treated equally.",

    "qz_s3q4": "The fairness impossibility theorem states that…",
    "qz_s3q4_a": "calibration and the equal error-rate criteria cannot all hold "
        "simultaneously when base rates differ",
    "qz_s3q4_b": "no model can ever be fair in any sense",
    "qz_s3q4_c": "fairness always reduces accuracy to chance level",
    "qz_s3q4_d": "only linear models can satisfy fairness constraints",
    "qz_s3q4_x": "With different base rates, the definitions mathematically "
        "conflict (Kleinberg et al.; COMPAS debate) — you must choose.",

    "qz_s3q5": "Bias in large language models typically surfaces as…",
    "qz_s3q5_a": "stereotyped associations and completions that differ by group",
    "qz_s3q5_b": "slower token generation for some topics",
    "qz_s3q5_c": "higher perplexity on all minority dialects, always",
    "qz_s3q5_d": "refusal to answer any demographic question",
    "qz_s3q5_x": "Co-occurrence statistics of the web corpus become model "
        "associations — probed with templates and counterfactual pairs.",

    "qz_s3q6": "Reweighing, as a pre-processing mitigation, works by…",
    "qz_s3q6_a": "adjusting instance weights before training so groups and "
        "labels are statistically balanced",
    "qz_s3q6_b": "changing the decision threshold after training",
    "qz_s3q6_c": "adding an adversary to the training loop",
    "qz_s3q6_d": "removing the protected attribute column only",
    "qz_s3q6_x": "It fixes the data distribution the model sees; dropping the "
        "column alone fails because of correlated proxy features.",

    "qz_s3q7": "Adversarial de-biasing trains…",
    "qz_s3q7_a": "a predictor whose representation an adversary cannot use to "
        "recover the protected attribute",
    "qz_s3q7_b": "two models that compete to maximize accuracy",
    "qz_s3q7_c": "a model on adversarial image perturbations",
    "qz_s3q7_d": "a reward model from human preferences",
    "qz_s3q7_x": "Same gradient-reversal idea as DANN, aimed at fairness: purge "
        "group information from the learned representation.",

    "qz_s3q8": "Threshold post-processing achieves fairness by…",
    "qz_s3q8_a": "choosing per-group decision thresholds that equalize the "
        "chosen error rates",
    "qz_s3q8_b": "retraining the model from scratch with more data",
    "qz_s3q8_c": "deleting misclassified samples",
    "qz_s3q8_d": "averaging predictions across groups",
    "qz_s3q8_x": "It leaves the scores untouched and repairs the decision rule — "
        "cheap, auditable, applied after training.",

    "qz_s3t1": "Demographic parity and equalized odds are the same criterion "
        "under a different name.",
    "qz_s3t1_x": "False: parity constrains predictions only; equalized odds also "
        "conditions on the true label — they generally conflict.",

    "qz_s3t2": "A model that never sees the protected attribute can still "
        "discriminate through correlated proxy features.",
    "qz_s3t2_x": "True: postcode, names or shopping history can encode group "
        "membership — “fairness through unawareness” fails.",

    "qz_s3n1": "Group A receives positive decisions at rate {a} and group B at "
        "rate {b}. Compute the demographic-parity gap |{a} − {b}|.",
    "qz_s3n1_x": "|{a} − {b}| = {ans}; a gap of 0 would mean parity is satisfied.",

    "qz_s3n2": "For one group, the classifier produced {tp} true positives and "
        "{fn} false negatives. Compute its true-positive rate TP∕(TP+FN).",
    "qz_s3n2_x": "TPR = {tp}/({tp}+{fn}) = {ans} — comparing this rate across "
        "groups is the heart of equal-opportunity checks.",

    # ==================== Section IV — Robustness ======================== #
    "qz_s4q1": "An adversarial example is…",
    "qz_s4q1_a": "an input with a tiny, human-imperceptible perturbation that "
        "flips the model's prediction",
    "qz_s4q1_b": "a training sample with a wrong label",
    "qz_s4q1_c": "any image the model classifies with low confidence",
    "qz_s4q1_d": "a sample generated by a GAN",
    "qz_s4q1_x": "The perturbation is optimized against the model's own "
        "gradients — invisible to us, decisive for it.",

    "qz_s4q2": "FGSM computes its perturbation as…",
    "qz_s4q2_a": "ε · sign(∇ₓ loss) — one step in the gradient's sign direction",
    "qz_s4q2_b": "random uniform noise of size ε",
    "qz_s4q2_c": "the gradient of the weights, clipped to ε",
    "qz_s4q2_d": "a rotation and crop of the input",
    "qz_s4q2_x": "One cheap step: perturb every pixel by ±ε in whichever "
        "direction increases the loss.",

    "qz_s4q3": "How does PGD differ from FGSM?",
    "qz_s4q3_a": "it iterates several smaller steps, projecting back into the "
        "ε-ball after each",
    "qz_s4q3_b": "it perturbs the labels instead of the inputs",
    "qz_s4q3_c": "it requires no access to gradients at all",
    "qz_s4q3_d": "it only works on linear models",
    "qz_s4q3_x": "Iteration + projection makes PGD the standard strong "
        "first-order attack; FGSM is its single-step special case.",

    "qz_s4q4": "An ℓ∞ threat model with budget ε means the attacker may…",
    "qz_s4q4_a": "change each input coordinate by at most ε",
    "qz_s4q4_b": "change at most ε coordinates in total",
    "qz_s4q4_c": "scale the whole image by ε",
    "qz_s4q4_d": "query the model at most ε times",
    "qz_s4q4_x": "ℓ∞ bounds the largest single-coordinate change — the usual "
        "“imperceptible perturbation” formalization.",

    "qz_s4q5": "Adversarial training improves robustness by…",
    "qz_s4q5_a": "generating adversarial examples on the fly and training on "
        "them — usually at some cost in clean accuracy",
    "qz_s4q5_b": "adding dropout to every layer",
    "qz_s4q5_c": "training only on correctly classified samples",
    "qz_s4q5_d": "freezing the first layers of the network",
    "qz_s4q5_x": "Min–max training bakes the attack into the objective; the "
        "robustness/accuracy trade-off is the price.",

    "qz_s4q6": "Randomized smoothing certifies robustness by…",
    "qz_s4q6_a": "voting over many Gaussian-noised copies of the input, which "
        "yields a provable radius",
    "qz_s4q6_b": "smoothing the loss landscape with SAM",
    "qz_s4q6_c": "blurring the input image before classification",
    "qz_s4q6_d": "adding noise to the labels during training",
    "qz_s4q6_x": "If the majority vote is stable under noise, a certified ℓ₂ "
        "radius follows — a guarantee, not an empirical claim.",

    "qz_s4q7": "A “jailbreak” of an LLM is…",
    "qz_s4q7_a": "a prompt crafted to bypass the model's safety guardrails",
    "qz_s4q7_b": "extracting the model's weights from its outputs",
    "qz_s4q7_c": "running the model outside its licensed hardware",
    "qz_s4q7_d": "fine-tuning the model on private data",
    "qz_s4q7_x": "Role-play, obfuscation or competing instructions can push the "
        "model to produce what its safety training should refuse.",

    "qz_s4q8": "“Obfuscated gradients” are a warning sign because…",
    "qz_s4q8_a": "defenses that merely break gradient flow give a false sense "
        "of security and fall to adaptive attacks",
    "qz_s4q8_b": "they slow down training too much",
    "qz_s4q8_c": "they make the model impossible to save to disk",
    "qz_s4q8_d": "they increase the model's file size",
    "qz_s4q8_x": "Athalye et al. broke most such defenses: evaluate against "
        "adaptive attacks, not only off-the-shelf ones.",

    "qz_s4t1": "Adversarial examples often transfer: a perturbation crafted "
        "against one model can fool a different model.",
    "qz_s4t1_x": "True: transferability enables black-box attacks without any "
        "gradient access to the target.",

    "qz_s4t2": "A certified-robustness guarantee only holds against the "
        "specific attack algorithm used during evaluation.",
    "qz_s4t2_x": "False: certification bounds EVERY perturbation within the "
        "radius — that is exactly what distinguishes it from empirical robustness.",

    "qz_s4n1": "FGSM with budget ε = {eps} pushes a pixel of value {x} in the "
        "positive gradient direction. Compute the perturbed value x + ε.",
    "qz_s4n1_x": "{x} + {eps} = {ans}; every coordinate moves by exactly ±ε "
        "under the ℓ∞ budget.",

    "qz_s4n2": "A model scores {a} clean accuracy but {r} accuracy under PGD. "
        "Compute the robustness gap (clean − robust).",
    "qz_s4n2_x": "{a} − {r} = {ans} — this gap is the empirical price the "
        "attack extracts.",

    # ===================== Section V — Privacy =========================== #
    "qz_s5q1": "A backdoor (trojan) attack on a model…",
    "qz_s5q1_a": "implants a trigger during training so the model misbehaves "
        "only when the trigger appears",
    "qz_s5q1_b": "steals the model weights through an API",
    "qz_s5q1_c": "floods the model with queries to slow it down",
    "qz_s5q1_d": "perturbs inputs at test time only",
    "qz_s5q1_x": "Clean accuracy stays normal, so the backdoor passes standard "
        "evaluation — that is what makes poisoning insidious.",

    "qz_s5q2": "A membership-inference attack tries to determine…",
    "qz_s5q2_a": "whether a specific example was part of the training set",
    "qz_s5q2_b": "the architecture of the model",
    "qz_s5q2_c": "the learning rate used in training",
    "qz_s5q2_d": "how many GPUs trained the model",
    "qz_s5q2_x": "Models are typically more confident on training members; that "
        "confidence gap leaks membership — a direct privacy harm.",

    "qz_s5q3": "A mechanism is ε-differentially private if…",
    "qz_s5q3_a": "changing one record changes any output's probability by at "
        "most a factor e^ε",
    "qz_s5q3_b": "it never outputs an individual's exact record",
    "qz_s5q3_c": "the data are encrypted at rest",
    "qz_s5q3_d": "the model's accuracy drops by at most ε",
    "qz_s5q3_x": "DP bounds the influence of any single person on the output "
        "distribution — a worst-case, composable guarantee.",

    "qz_s5q4": "A smaller privacy budget ε means…",
    "qz_s5q4_a": "stronger privacy, more noise, and typically lower utility",
    "qz_s5q4_b": "weaker privacy but faster training",
    "qz_s5q4_c": "no change in the privacy guarantee",
    "qz_s5q4_d": "the mechanism becomes deterministic",
    "qz_s5q4_x": "ε is the privacy dial: small ε = outputs nearly independent of "
        "any individual = more noise injected.",

    "qz_s5q5": "The Laplace mechanism adds noise with scale…",
    "qz_s5q5_a": "sensitivity ∕ ε",
    "qz_s5q5_b": "ε ∕ sensitivity",
    "qz_s5q5_c": "ε² ∕ 2",
    "qz_s5q5_d": "always exactly 1",
    "qz_s5q5_x": "b = Δf/ε: the more one person can move the query (Δf) and the "
        "stronger the guarantee (small ε), the more noise is needed.",

    "qz_s5q6": "Federated learning protects data by…",
    "qz_s5q6_a": "training locally on each device and sharing only model "
        "updates, never raw data",
    "qz_s5q6_b": "encrypting the dataset with a public key",
    "qz_s5q6_c": "storing all data in one secure datacenter",
    "qz_s5q6_d": "deleting the data after one epoch",
    "qz_s5q6_x": "The data never leave the device — but the shared gradients "
        "still leak, which motivates DP and secure aggregation on top.",

    "qz_s5q7": "Gradient-leakage attacks show that…",
    "qz_s5q7_a": "raw training samples can be reconstructed from shared "
        "gradients",
    "qz_s5q7_b": "gradients always vanish in deep networks",
    "qz_s5q7_c": "federated learning cannot converge",
    "qz_s5q7_d": "gradient clipping breaks model accuracy",
    "qz_s5q7_x": "“Deep Leakage from Gradients”: matching gradients recovers "
        "pixels and tokens — updates are data in disguise.",

    "qz_s5q8": "Randomized response gives plausible deniability by…",
    "qz_s5q8_a": "having each person answer truthfully only with a known "
        "probability, e.g. based on a coin flip",
    "qz_s5q8_b": "letting people skip any question",
    "qz_s5q8_c": "encrypting each answer with a random key",
    "qz_s5q8_d": "shuffling the order of the survey questions",
    "qz_s5q8_x": "The analyst can de-bias the aggregate while no single answer "
        "proves anything about one person — DP's oldest ancestor.",

    "qz_s5t1": "Federated learning by itself already guarantees differential "
        "privacy.",
    "qz_s5t1_x": "False: without added noise, shared updates can leak the data "
        "(gradient inversion); FL needs DP or secure aggregation on top.",

    "qz_s5t2": "DP guarantees compose: running several ε₀-DP queries adds their "
        "budgets together.",
    "qz_s5t2_x": "True: basic composition sums the epsilons — the reason a total "
        "privacy budget must be managed.",

    "qz_s5n1": "A query has sensitivity Δf = {d} and we want ε = {eps}. Compute "
        "the Laplace noise scale b = Δf ∕ ε.",
    "qz_s5n1_x": "b = {d}/{eps} = {ans}; the noise grows as the budget shrinks.",

    "qz_s5n2": "You run {k} queries, each ε₀ = {e0}-DP. By basic composition, "
        "compute the total privacy budget ε = k · ε₀.",
    "qz_s5n2_x": "{k} × {e0} = {ans} — every query spends budget; it never "
        "comes back.",

    # ==================== Section VI — Alignment ========================= #
    "qz_s6q1": "The “alignment gap” is the difference between…",
    "qz_s6q1_a": "the proxy objective we optimize and the behavior we actually "
        "intend",
    "qz_s6q1_b": "training accuracy and test accuracy",
    "qz_s6q1_c": "model size and dataset size",
    "qz_s6q1_d": "the loss of two random seeds",
    "qz_s6q1_x": "Optimization pressure aims at the measurable proxy; whatever "
        "the proxy misses, the model will happily ignore or exploit.",

    "qz_s6q2": "The standard RLHF pipeline order is…",
    "qz_s6q2_a": "supervised fine-tuning → reward model from human preferences "
        "→ RL against the reward model",
    "qz_s6q2_b": "RL first, then supervised fine-tuning, then a reward model",
    "qz_s6q2_c": "train the reward model and the policy on the same labels at "
        "once",
    "qz_s6q2_d": "pre-training only, with a filtered dataset",
    "qz_s6q2_x": "SFT teaches the format, the reward model encodes preferences, "
        "and PPO pushes the policy toward them.",

    "qz_s6q3": "“Reward hacking” happens when…",
    "qz_s6q3_a": "the policy exploits flaws of the reward model to score high "
        "without the intended behavior",
    "qz_s6q3_b": "someone steals the reward model's weights",
    "qz_s6q3_c": "the reward is accidentally negated",
    "qz_s6q3_d": "training runs out of human labels",
    "qz_s6q3_x": "Goodhart's law in action: the measure becomes the target and "
        "stops measuring what you meant.",

    "qz_s6q4": "DPO (Direct Preference Optimization) differs from RLHF by…",
    "qz_s6q4_a": "optimizing preferences directly with a classification-style "
        "loss — no explicit reward model, no RL loop",
    "qz_s6q4_b": "using twice as many reward models",
    "qz_s6q4_c": "requiring online human feedback at every step",
    "qz_s6q4_d": "only working for vision models",
    "qz_s6q4_x": "DPO folds the reward into the policy ratio against a reference "
        "model — the preference data trains the policy directly.",

    "qz_s6q5": "GRPO's key idea is to…",
    "qz_s6q5_a": "compare a GROUP of sampled answers and use each one's "
        "advantage over the group mean — no value network",
    "qz_s6q5_b": "grow the model gradually layer by layer",
    "qz_s6q5_c": "replace rewards with random noise",
    "qz_s6q5_d": "train only on the single best answer",
    "qz_s6q5_x": "Group-relative advantages plus rule-based rewards made "
        "reasoning training (à la DeepSeek-R1) simple and stable.",

    "qz_s6q6": "Prompt injection (OWASP LLM Top-10 #1) is when…",
    "qz_s6q6_a": "malicious instructions smuggled into the input or retrieved "
        "context override the developer's intent",
    "qz_s6q6_b": "the prompt is too long for the context window",
    "qz_s6q6_c": "SQL is inserted into a database query",
    "qz_s6q6_d": "the user asks the model to translate a prompt",
    "qz_s6q6_x": "The model cannot firmly distinguish instructions from data — "
        "any text it reads can try to steer it.",

    "qz_s6q7": "“Excessive agency” is the risk that…",
    "qz_s6q7_a": "an LLM given too many tools and permissions takes impactful "
        "actions beyond the user's intent",
    "qz_s6q7_b": "the model becomes too intelligent to run on a GPU",
    "qz_s6q7_c": "agents refuse to ever call a tool",
    "qz_s6q7_d": "users delegate too little to the model",
    "qz_s6q7_x": "Mitigation is least privilege + human oversight of "
        "consequential actions — agency should be earned, not default.",

    "qz_s6q8": "The KL penalty in RLHF exists to…",
    "qz_s6q8_a": "keep the policy close to the reference model so it does not "
        "degenerate while chasing reward",
    "qz_s6q8_b": "make the reward model train faster",
    "qz_s6q8_c": "compress the model after training",
    "qz_s6q8_d": "increase the entropy of the dataset",
    "qz_s6q8_x": "Unconstrained reward maximization drifts into gibberish that "
        "games the reward — the KL term anchors the language model.",

    "qz_s6t1": "DPO requires training a separate explicit reward model before "
        "the policy can be optimized.",
    "qz_s6t1_x": "False: eliminating the separate reward model is precisely "
        "DPO's contribution.",

    "qz_s6t2": "Treating LLM output as trusted code or commands without checks "
        "is a security risk (insecure output handling).",
    "qz_s6t2_x": "True: model output is attacker-influenceable input to your "
        "system — validate and sandbox it like any untrusted data.",

    "qz_s6n1": "A policy produces the aligned answer with probability {p}, "
        "earning reward {ra}; otherwise it earns {rb}. Compute the expected "
        "reward p·rₐ + (1−p)·r_b.",
    "qz_s6n1_x": "{p}·{ra} + (1−{p})·{rb} = {ans} — the quantity RL pushes "
        "upward.",

    "qz_s6n2": "GRPO samples a group of four answers with rewards {r1}, {r2}, "
        "{r3}, {r4} (mean = {mean}). Compute the advantage of the FIRST "
        "answer: r₁ − mean.",
    "qz_s6n2_x": "{r1} − {mean} = {ans}; answers above the group mean are "
        "reinforced, those below are suppressed.",
}

FA_QUIZ = {
    "mode_quiz": "آزمون",
    "quiz_page": "آزمونِ بخش",
    "choose_quiz": "📝 آزمون",
    "quiz_eyebrow": "ارزیابی",
    "quiz_title": "آزمونِ بخش",
    "quiz_intro": "دوازده پرسش از نظری و عملیِ این بخش. گزینه‌ها و اعداد در هر "
        "تلاش دوباره چیده می‌شوند. به همه پاسخ دهید و سپس «تحویل آزمون» را بزنید.",
    "quiz_q": "پرسش",
    "quiz_true": "درست",
    "quiz_false": "نادرست",
    "quiz_num_hint": "عددی وارد کنید (۳ رقم اعشار).",
    "quiz_submit": "تحویل آزمون",
    "quiz_score": "نمره",
    "quiz_correct_n": "پاسخ‌های درست",
    "quiz_time": "زمانِ صرف‌شده",
    "quiz_time_fmt": "{m} دقیقه و {s} ثانیه",
    "quiz_v_excellent": "عالی — بر این بخش مسلّط شده‌اید.",
    "quiz_v_vgood": "خیلی خوب — با یک مرورِ کوتاه کامل می‌شود.",
    "quiz_v_good": "خوب — درس‌های نشان‌شده در پایین را دوباره بخوانید.",
    "quiz_v_weak": "نیازمندِ مرور — بخش را دوباره بخوانید و بازآزمایی کنید.",
    "quiz_review": "مرورِ پاسخ‌ها",
    "quiz_your_answer": "پاسخ شما",
    "quiz_no_answer": "— بی‌پاسخ —",
    "quiz_right_answer": "پاسخ درست",
    "quiz_explain": "چرا",
    "quiz_open_lesson": "بازکردنِ درس ←",
    "quiz_retry": "⟳ بازآزمایی با پرسش‌های تازه",
    "quiz_badge_note": "برای نشانِ این بخش {p}٪ یا بیشتر بگیرید 🏅.",
    "quiz_passed": "نشان گرفته شد 🏅",
    "quiz_soon_title": "آزمون در دستِ آماده‌سازی",
    "quiz_soon_body": "آزمونِ این بخش در حال نوشته‌شدن است. بخش‌های یکم و دوم "
        "هم‌اکنون آزمون دارند — فعلاً یکی از آن‌ها را امتحان کنید.",

    # ---------------- بخش یکم — تعمیم ---------------- #
    "qz_s1q1": "خطای موردانتظارِ آزمونِ یک مدلِ بانظارت به کدام سه مؤلفه تجزیه می‌شود؟",
    "qz_s1q1_a": "مجذورِ بایاس، واریانس، و نوفهٔ حذف‌نشدنی",
    "qz_s1q1_b": "خطای آموزش، خطای اعتبارسنجی، و خطای آزمون",
    "qz_s1q1_c": "کم‌برازش، بیش‌برازش، و منظم‌سازی",
    "qz_s1q1_d": "خطای بهینه‌سازی، نرخ یادگیری، و اندازهٔ دسته",
    "qz_s1q1_x": "E[(y−f̂)²] = بایاس² + واریانس + σ²: زیادی‌ساده‌بودن، "
        "زیادی‌حساس‌بودن، و کفِ نوفه‌ای که هیچ مدلی نمی‌تواند بردارد.",

    "qz_s1q2": "افزایشِ ظرفیتِ مدل معمولاً…",
    "qz_s1q2_a": "بایاس را کم و واریانس را زیاد می‌کند",
    "qz_s1q2_b": "بایاس را زیاد و واریانس را کم می‌کند",
    "qz_s1q2_c": "هر دو را کم می‌کند",
    "qz_s1q2_d": "هر دو را زیاد می‌کند",
    "qz_s1q2_x": "انعطاف، خطای سیستماتیک را می‌کاهد اما برازش را به نمونهٔ "
        "آموزشیِ خاص حساس‌تر می‌کند.",

    "qz_s1q3": "پدیدهٔ «نزولِ دوگانه» نشان می‌دهد که…",
    "qz_s1q3_a": "خطای آزمون پس از گذر از نقطهٔ درون‌یابی می‌تواند دوباره کم شود",
    "qz_s1q3_b": "خطای آموزش همیشه دو بار بالا می‌رود",
    "qz_s1q3_c": "منحنیِ U شکلِ کلاسیک برای همهٔ مدل‌ها دقیق است",
    "qz_s1q3_d": "واریانس بی‌استثنا با ظرفیت یکنواخت زیاد می‌شود",
    "qz_s1q3_x": "شبکه‌های به‌شدت فرا-پارامتری پس از درون‌یابی می‌توانند دوباره "
        "تعمیم دهند — منحنیِ U شهودِ نخست است، نه همهٔ ماجرا.",

    "qz_s1q4": "بُعدِ VC یک دسته‌بندِ خطی (با جملهٔ بایاس) در ℝᵈ برابر است با…",
    "qz_s1q4_a": "d + 1",
    "qz_s1q4_b": "d",
    "qz_s1q4_c": "2d + 1",
    "qz_s1q4_d": "d²",
    "qz_s1q4_x": "ابرصفحه‌ای با عرض از مبدأ در ℝᵈ حداکثر d+1 نقطهٔ در وضعیتِ "
        "عمومی را خُرد می‌کند.",

    "qz_s1q5": "«سوگیریِ استقرایی» یعنی…",
    "qz_s1q5_a": "مجموعه‌فرض‌هایی که یادگیرنده برای تعمیم فراتر از داده به کار می‌برد",
    "qz_s1q5_b": "خطای سیستماتیکِ ناشی از مدلِ زیادی‌ساده",
    "qz_s1q5_c": "سوگیریِ اجتماعیِ موجود در برچسب‌های داده",
    "qz_s1q5_d": "ترجیحِ بهینه‌سازها برای نرخ‌های یادگیریِ کوچک",
    "qz_s1q5_x": "بدونِ فرض، تعمیمی در کار نیست (ناهار مجانی نداریم): کانولوشن "
        "محلی‌بودن را فرض می‌گیرد و مدلِ خطی خطی‌بودن را.",

    "qz_s1q6": "DANN (آموزشِ تخاصمیِ دامنه) دو دامنه را هم‌تراز می‌کند از راهِ…",
    "qz_s1q6_a": "یادگیریِ ویژگی‌هایی که برچسب را پیش‌بینی می‌کنند و هم‌زمان "
        "تشخیص‌دهندهٔ دامنه را می‌فریبند",
    "qz_s1q6_b": "بازوزن‌دهیِ کلاس‌های دامنهٔ مبدأ",
    "qz_s1q6_c": "بالابردنِ نرخ یادگیری روی دامنهٔ هدف",
    "qz_s1q6_d": "آموزشِ مدلی جداگانه برای هر دامنه",
    "qz_s1q6_x": "لایهٔ وارونگیِ گرادیان، رمزگذار را به‌سوی ویژگی‌هایی می‌راند که "
        "تشخیص‌دهندهٔ دامنه نمی‌تواند از هم جدا کند — ویژگی‌های دامنه‌ناوردا.",

    "qz_s1q7": "کمینه‌سازیِ آگاه از تیزی (SAM) پارامترهایی می‌جوید که…",
    "qz_s1q7_a": "در کلِّ یک همسایگی، تابع هزینه را پایین نگه دارند (کمینهٔ تخت)",
    "qz_s1q7_b": "به کمترین هزینهٔ آموزش برسند، هرچند تیز",
    "qz_s1q7_c": "تا حدِ ممکن تُنُک باشند",
    "qz_s1q7_d": "آموزش را در کمترین گام همگرا کنند",
    "qz_s1q7_x": "SAM بدترین هزینه در گویِ ε-شعاعیِ اطرافِ وزن‌ها را کمینه می‌کند؛ "
        "کمینه‌های تخت معمولاً بهتر تعمیم می‌دهند.",

    "qz_s1q8": "پارادوکسِ سیمپسون هشدار می‌دهد که روندِ دیده‌شده در دادهٔ تجمیع‌شده…",
    "qz_s1q8_a": "با شکستنِ داده برحسبِ متغیرِ مخدوش‌گر می‌تواند وارونه شود",
    "qz_s1q8_b": "همیشه با روندِ درونِ هر زیرگروه یکی است",
    "qz_s1q8_c": "اثباتِ کافیِ رابطهٔ علّی است",
    "qz_s1q8_d": "فقط در نمونه‌های خیلی کوچک رخ می‌دهد",
    "qz_s1q8_x": "همبستگی علّیت نیست: شرطی‌شدن بر مخدوش‌گر می‌تواند علامتِ اثرِ "
        "ظاهری را برگرداند.",

    "qz_s1t1": "مدلی به‌قدرِ کافی بزرگ می‌تواند جملهٔ نوفهٔ حذف‌نشدنیِ σ² را از "
        "تجزیهٔ خطا حذف کند.",
    "qz_s1t1_x": "نادرست: σ² از خودِ فرایندِ تولیدِ داده می‌آید؛ هیچ مدلی، هرچه "
        "بزرگ، نمی‌تواند آن را بردارد.",

    "qz_s1t2": "در جابه‌جاییِ متغیّرِ کمکی، توزیعِ ورودی p(x) عوض می‌شود ولی "
        "شرطیِ p(y|x) ثابت می‌ماند.",
    "qz_s1t2_x": "درست: این تعریفِ covariate shift است و همین است که وزن‌دهیِ "
        "اهمیت و انطباقِ دامنه را اصلاً ممکن می‌کند.",

    "qz_s1n1": "در تجزیهٔ بایاس–واریانس فرض کنید بایاس = {b}، واریانس = {v} و "
        "نوفه σ² = {n}. خطای مجذورِ موردانتظار یعنی بایاس² + واریانس + σ² را "
        "حساب کنید.",
    "qz_s1n1_x": "بایاس² = {b}² = {b2}؛ با افزودنِ واریانسِ {v} و نوفهٔ {n} "
        "می‌شود {ans}.",

    "qz_s1n2": "میانگین‌گیری از {k} مدل با خطاهای مستقل، بایاس را ثابت نگه "
        "می‌دارد و واریانس را بر {k} تقسیم می‌کند. اگر واریانسِ یک مدلِ تنها "
        "{v} باشد، واریانسِ گروه چند است؟",
    "qz_s1n2_x": "{v} ÷ {k} = {ans} — دقیقاً به همین دلیل bagging یادگیرنده‌های "
        "پُرواریانس را رام می‌کند.",

    # ---------------- بخش دوم — تفسیرپذیری ---------------- #
    "qz_s2q1": "تفاوتِ تفسیرپذیری با تبیین‌پذیری چیست؟",
    "qz_s2q1_a": "مدلِ تفسیرپذیر ذاتاً شفاف است؛ تبیین‌پذیری توضیحِ پسینی به "
        "جعبه‌سیاه می‌افزاید",
    "qz_s2q1_b": "در ادبیاتِ حوزه دقیقاً مترادف‌اند",
    "qz_s2q1_c": "تبیین‌پذیری فقط برای مدل‌های خطی است",
    "qz_s2q1_d": "تفسیرپذیری نامِ دیگرِ دقّت است",
    "qz_s2q1_x": "درختِ تصمیمِ کم‌عمق خودش فهمیدنی است؛ SHAP یا LIME جعبه‌سیاه "
        "را پس از وقوع توضیح می‌دهند.",

    "qz_s2q2": "مقادیرِ SHAP برای یک پیش‌بینیِ واحد کدام ویژگی را برآورده می‌کنند؟",
    "qz_s2q2_a": "جمعشان دقیقاً برابر است با f(x) − E[f] (کارایی/جمع‌پذیری)",
    "qz_s2q2_b": "همیشه مثبت‌اند",
    "qz_s2q2_c": "برای هر ورودی یکسان‌اند",
    "qz_s2q2_d": "فقط برای گروه‌درخت‌ها تعریف می‌شوند",
    "qz_s2q2_x": "کارایی همان اصلِ شپلی است که اسناد را کامل می‌کند: سهم‌ها همهٔ "
        "فاصله از مقدارِ پایه را پوشش می‌دهند.",

    "qz_s2q3": "LIME یک پیش‌بینی را توضیح می‌دهد با…",
    "qz_s2q3_a": "برازشِ جانشینی سادهٔ وزن‌دار بر نمونه‌های اغتشاش‌یافتهٔ اطرافِ "
        "همان نمونه",
    "qz_s2q3_b": "خواندنِ مستقیمِ وزن‌های شبکه",
    "qz_s2q3_c": "بازآموزیِ کاملِ مدل بدونِ هر ویژگی",
    "qz_s2q3_d": "محاسبهٔ دقیقِ مقادیرِ شپلی به‌صورت بسته",
    "qz_s2q3_x": "به‌طورِ محلی حتی جعبه‌سیاه هم تقریباً خطی است — LIME همان "
        "جانشینِ محلی را می‌برازد و ضرایبش را گزارش می‌کند.",

    "qz_s2q4": "توضیحِ خلافِ واقع به کدام پرسش پاسخ می‌دهد؟",
    "qz_s2q4_a": "«کمینه‌تغییرِ ورودی که تصمیم را برمی‌گرداند چیست؟»",
    "qz_s2q4_b": "«کدام ویژگی در کل مهم‌ترین است؟»",
    "qz_s2q4_c": "«دقتِ مدل روی مجموعهٔ آزمون چقدر است؟»",
    "qz_s2q4_d": "«کدام نمونه‌ها هنگام آموزش بدبرچسب خورده‌اند؟»",
    "qz_s2q4_x": "خلافِ واقع در سطحِ نمونه است: کوچک‌ترین حرکت از مرزِ تصمیم، "
        "مثلاً «۴هزار دلار درآمدِ بیشتر، وام را تأیید می‌کرد».",

    "qz_s2q5": "برای آنکه جبران عملی باشد، تغییرِ پیشنهادی باید…",
    "qz_s2q5_a": "روی ویژگی‌هایی باشد که فرد واقعاً می‌تواند عوض کند — نه "
        "ویژگی‌های تغییرناپذیر",
    "qz_s2q5_b": "اطمینانِ مدل را به هر قیمتی بیشینه کند",
    "qz_s2q5_c": "هم‌زمان بیشترین شمارِ ویژگی‌ها را عوض کند",
    "qz_s2q5_d": "روی دادهٔ آموزش هم اعمال شود",
    "qz_s2q5_x": "«سنّت را پنج سال کم کن» جبران نیست؛ عملی‌بودن جست‌وجوی خلافِ "
        "واقع را به ویژگی‌های تغییرپذیر محدود می‌کند.",

    "qz_s2q6": "Grad-CAM چه تولید می‌کند؟",
    "qz_s2q6_a": "نقشهٔ گرمایی مخصوصِ هر کلاس از گرادیان‌های آخرین لایهٔ کانولوشنی",
    "qz_s2q6_b": "درختِ تصمیمی که از CNN تقلید می‌کند",
    "qz_s2q6_c": "رتبه‌بندیِ جایگشتیِ ویژگی‌های جدولی",
    "qz_s2q6_d": "نمونهٔ تخاصمی برای کلاسِ هدف",
    "qz_s2q6_x": "گرادیان‌های نمرهٔ کلاس، نقشه‌های ویژگیِ کانولوشنی را وزن می‌دهند "
        "و نشان می‌دهند شبکه برای آن کلاس کجا را نگاه کرده است.",

    "qz_s2q7": "مدلِ بینایی‌ای که «گرگ» را از پس‌زمینهٔ برفی تشخیص می‌دهد "
        "نمونه‌ای است از…",
    "qz_s2q7_a": "همبستگیِ کاذب (یادگیریِ میان‌بر)",
    "qz_s2q7_b": "نزولِ دوگانه",
    "qz_s2q7_c": "حریمِ تفاضلی",
    "qz_s2q7_d": "هکِ پاداش",
    "qz_s2q7_x": "پس‌زمینه در دادهٔ آموزش با برچسب هم‌رخداد است؛ میان‌بر جواب "
        "می‌دهد — تا وقتی گرگی روی چمن ظاهر شود.",

    "qz_s2q8": "مسئلهٔ جعبه‌سیاه بیش از همه از آن رو مهم است که…",
    "qz_s2q8_a": "تصمیم‌های پُرریسک (اعتبار، پزشکی، قضاوت) توجیه و "
        "حسابرسی‌پذیری می‌خواهند",
    "qz_s2q8_b": "مدل‌های جعبه‌سیاه همیشه کم‌دقت‌ترند",
    "qz_s2q8_c": "قانون‌گذاران استفاده از شبکهٔ عصبی را همه‌جا ممنوع کرده‌اند",
    "qz_s2q8_d": "توضیح‌ها آموزش را بسیار سریع‌تر می‌کنند",
    "qz_s2q8_x": "وقتی تصمیمی باید قابلِ اعتراض و حسابرسی باشد، دقتِ تنها "
        "کافی نیست.",

    "qz_s2t1": "KernelSHAP مدل‌ناوابسته است: تنها به دسترسیِ پرسشی به "
        "پیش‌بینی‌های مدل نیاز دارد.",
    "qz_s2t1_x": "درست: مقادیرِ شپلی را فقط از رفتارِ ورودی–خروجی برآورد می‌کند، "
        "پس با هر دسته‌بندی کار می‌کند.",

    "qz_s2t2": "شبکهٔ عصبیِ عمیق ذاتاً تفسیرپذیر است و هیچ روشِ توضیحی لازم ندارد.",
    "qz_s2t2_x": "نادرست: میلیون‌ها وزنِ درهم‌تنیده دقیقاً همان مسئلهٔ جعبه‌سیاه "
        "است که XAI را ایجاب می‌کند.",

    "qz_s2n1": "برای یک پیش‌بینی، f(x) = {fx} و مقدارِ پایه E[f] = {base}. سه "
        "مقدار از چهار مقدارِ SHAP چنین‌اند: φ₁ = {p1}، φ₂ = {p2}، φ₃ = {p3}. "
        "با جمع‌پذیری φ₄ را حساب کنید.",
    "qz_s2n1_x": "φ₄ = f(x) − E[f] − φ₁ − φ₂ − φ₃ = {ans}.",

    "qz_s2n2": "جانشینِ محلیِ LIME چنین است: g(z) = {w1}·z₁ + {w2}·z₂ + {b}. "
        "برای z₁ = {z1} و z₂ = {z2} مقدارِ g(z) را حساب کنید.",
    "qz_s2n2_x": "g = {w1}·{z1} + {w2}·{z2} + {b} = {ans} — ضرایبِ جانشین همان "
        "توضیح‌اند.",

    # ---------------- بخش سوم — انصاف ---------------- #
    "qz_s3q1": "سرچشمهٔ اصلیِ بی‌انصافی در سامانه‌های یادگیری ماشین معمولاً…",
    "qz_s3q1_a": "سوگیریِ تاریخی و اجتماعیِ نهفته در دادهٔ آموزش است",
    "qz_s3q1_b": "خطاهای گردکردنِ اعشاری روی GPU است",
    "qz_s3q1_c": "نرخِ یادگیریِ زیادی کوچک است",
    "qz_s3q1_d": "منظم‌سازیِ L2 بیش از اندازه است",
    "qz_s3q1_x": "مدل الگوهای داده‌اش را وفادارانه می‌آموزد — از جمله الگوهای "
        "تبعیض‌آمیزِ تصمیم‌های گذشته.",

    "qz_s3q2": "برابریِ جمعیت‌شناختی می‌خواهد که…",
    "qz_s3q2_a": "نرخِ پیش‌بینیِ مثبت میان گروه‌های محافظت‌شده برابر باشد",
    "qz_s3q2_b": "دقّت میان گروه‌ها برابر باشد",
    "qz_s3q2_c": "هر فرد همان پیش‌بینیِ یکسان را بگیرد",
    "qz_s3q2_d": "شمارِ گروه‌ها در دادهٔ آموزش برابر باشد",
    "qz_s3q2_x": "P(ŷ=1|A=a) باید میان گروه‌ها یکی باشد — برچسبِ واقعی را "
        "یکسره نادیده می‌گیرد؛ هم قوّتش همین است هم ضعفش.",

    "qz_s3q3": "شانس‌های برابرشده می‌خواهد که…",
    "qz_s3q3_a": "نرخِ مثبتِ درست و نرخِ مثبتِ کاذب هر دو میان گروه‌ها برابر باشند",
    "qz_s3q3_b": "فقط نرخِ خطای کلی میان گروه‌ها برابر باشد",
    "qz_s3q3_c": "مدل هرگز ویژگیِ محافظت‌شده را ورودی نگیرد",
    "qz_s3q3_d": "پیش‌بینی‌ها درونِ هر گروه کالیبره باشند",
    "qz_s3q3_x": "شرطی‌شدن بر برچسبِ واقعی آن را از برابریِ جمعیت‌شناختی جدا "
        "می‌کند: با شایسته و ناشایسته در هر گروه یکسان رفتار می‌شود.",

    "qz_s3q4": "قضیهٔ ناممکنیِ انصاف می‌گوید…",
    "qz_s3q4_a": "کالیبراسیون و معیارهای برابریِ نرخِ خطا وقتی نرخ‌های پایه "
        "متفاوت‌اند نمی‌توانند هم‌زمان برقرار باشند",
    "qz_s3q4_b": "هیچ مدلی به هیچ معنایی نمی‌تواند منصف باشد",
    "qz_s3q4_c": "انصاف همیشه دقّت را تا حدِّ شانس پایین می‌آورد",
    "qz_s3q4_d": "فقط مدل‌های خطی می‌توانند قیدهای انصاف را برآورده کنند",
    "qz_s3q4_x": "با نرخ‌های پایهٔ متفاوت، تعریف‌ها ریاضیاتی ناسازگارند "
        "(کلاینبرگ و همکاران؛ مناقشهٔ COMPAS) — باید انتخاب کرد.",

    "qz_s3q5": "سوگیری در مدل‌های زبانیِ بزرگ معمولاً چگونه رخ می‌نماید؟",
    "qz_s3q5_a": "تداعی‌ها و تکمیل‌های کلیشه‌ای که بسته به گروه فرق می‌کنند",
    "qz_s3q5_b": "کندشدنِ تولیدِ توکن برای برخی موضوع‌ها",
    "qz_s3q5_c": "سرگشتگیِ بالاتر روی همهٔ گویش‌های اقلیت، همیشه",
    "qz_s3q5_d": "خودداری از پاسخ به هر پرسشِ جمعیت‌شناختی",
    "qz_s3q5_x": "آمارِ هم‌رخدادیِ پیکرهٔ وب به تداعی‌های مدل بدل می‌شود — با "
        "الگوها و جفت‌های خلافِ واقع می‌سنجندش.",

    "qz_s3q6": "بازوزن‌دهی، به‌عنوان کاهشِ پیش‌پردازشی، چنین کار می‌کند…",
    "qz_s3q6_a": "پیش از آموزش، وزنِ نمونه‌ها را طوری تنظیم می‌کند که گروه‌ها و "
        "برچسب‌ها آماریاً متوازن شوند",
    "qz_s3q6_b": "آستانهٔ تصمیم را پس از آموزش عوض می‌کند",
    "qz_s3q6_c": "حریفی به حلقهٔ آموزش می‌افزاید",
    "qz_s3q6_d": "فقط ستونِ ویژگیِ محافظت‌شده را حذف می‌کند",
    "qz_s3q6_x": "توزیعِ داده‌ای را که مدل می‌بیند اصلاح می‌کند؛ حذفِ ستون "
        "به‌تنهایی به‌خاطرِ ویژگی‌های نیابتیِ همبسته شکست می‌خورد.",

    "qz_s3q7": "حذفِ سوگیریِ تخاصمی چه چیزی آموزش می‌دهد؟",
    "qz_s3q7_a": "پیش‌بینی‌گری که از بازنمایی‌اش هیچ حریفی نتواند ویژگیِ "
        "محافظت‌شده را بازیابد",
    "qz_s3q7_b": "دو مدل که برای بیشینه‌کردنِ دقّت رقابت می‌کنند",
    "qz_s3q7_c": "مدلی روی اغتشاش‌های تخاصمیِ تصویر",
    "qz_s3q7_d": "مدلِ پاداشی از ترجیحاتِ انسانی",
    "qz_s3q7_x": "همان ایدهٔ وارونگیِ گرادیانِ DANN، این‌بار برای انصاف: "
        "اطلاعاتِ گروه را از بازنمایی بروب.",

    "qz_s3q8": "پس‌پردازشِ آستانه‌ای انصاف را چگونه برقرار می‌کند؟",
    "qz_s3q8_a": "برای هر گروه آستانهٔ تصمیمی برمی‌گزیند که نرخ‌های خطای "
        "منظور را برابر کند",
    "qz_s3q8_b": "مدل را از نو با دادهٔ بیشتر آموزش می‌دهد",
    "qz_s3q8_c": "نمونه‌های بدطبقه‌بندی‌شده را حذف می‌کند",
    "qz_s3q8_d": "پیش‌بینی‌ها را میان گروه‌ها میانگین می‌گیرد",
    "qz_s3q8_x": "نمره‌ها دست‌نخورده می‌مانند و قاعدهٔ تصمیم ترمیم می‌شود — "
        "ارزان، حسابرسی‌پذیر، و پس از آموزش.",

    "qz_s3t1": "برابریِ جمعیت‌شناختی و شانس‌های برابرشده یک معیارند با دو نام.",
    "qz_s3t1_x": "نادرست: برابری فقط پیش‌بینی‌ها را قید می‌زند؛ شانس‌های "
        "برابرشده بر برچسبِ واقعی هم شرطی می‌شود — عموماً ناسازگارند.",

    "qz_s3t2": "مدلی که ویژگیِ محافظت‌شده را هرگز نمی‌بیند باز هم می‌تواند از "
        "راهِ ویژگی‌های نیابتیِ همبسته تبعیض بورزد.",
    "qz_s3t2_x": "درست: کدپستی، نام یا تاریخچهٔ خرید می‌توانند عضویتِ گروه را "
        "رمز کنند — «انصاف از راهِ بی‌خبری» شکست می‌خورد.",

    "qz_s3n1": "گروه A با نرخ {a} و گروه B با نرخ {b} تصمیمِ مثبت می‌گیرند. "
        "شکافِ برابریِ جمعیت‌شناختی یعنی |{a} − {b}| را حساب کنید.",
    "qz_s3n1_x": "|{a} − {b}| = {ans}؛ شکافِ صفر یعنی برابری برقرار است.",

    "qz_s3n2": "برای یک گروه، دسته‌بند {tp} مثبتِ درست و {fn} منفیِ کاذب داده "
        "است. نرخِ مثبتِ درست یعنی TP∕(TP+FN) را حساب کنید.",
    "qz_s3n2_x": "TPR = {tp}/({tp}+{fn}) = {ans} — مقایسهٔ همین نرخ میان "
        "گروه‌ها هستهٔ آزمونِ فرصتِ برابر است.",

    # ---------------- بخش چهارم — استواری ---------------- #
    "qz_s4q1": "نمونهٔ تخاصمی چیست؟",
    "qz_s4q1_a": "ورودی‌ای با اغتشاشی ریز و نامحسوس برای انسان که پیش‌بینیِ "
        "مدل را برمی‌گرداند",
    "qz_s4q1_b": "نمونهٔ آموزشی با برچسبِ غلط",
    "qz_s4q1_c": "هر تصویری که مدل با اطمینانِ کم دسته‌بندی کند",
    "qz_s4q1_d": "نمونه‌ای که یک GAN تولید کرده باشد",
    "qz_s4q1_x": "اغتشاش علیه گرادیان‌های خودِ مدل بهینه می‌شود — برای ما "
        "نادیدنی، برای مدل تعیین‌کننده.",

    "qz_s4q2": "FGSM اغتشاشش را چگونه می‌سازد؟",
    "qz_s4q2_a": "ε · sign(∇ₓ loss) — یک گام در جهتِ علامتِ گرادیان",
    "qz_s4q2_b": "نوفهٔ یکنواختِ تصادفی به اندازهٔ ε",
    "qz_s4q2_c": "گرادیانِ وزن‌ها، بریده‌شده به ε",
    "qz_s4q2_d": "چرخش و برشِ ورودی",
    "qz_s4q2_x": "یک گامِ ارزان: هر پیکسل را ±ε در جهتی جابه‌جا کن که هزینه "
        "را بالا ببرد.",

    "qz_s4q3": "PGD چه فرقی با FGSM دارد؟",
    "qz_s4q3_a": "چند گامِ کوچک‌تر برمی‌دارد و پس از هر گام به درونِ گویِ ε "
        "بازمی‌تاباند",
    "qz_s4q3_b": "به‌جای ورودی، برچسب‌ها را می‌آشوبد",
    "qz_s4q3_c": "به هیچ گرادیانی نیاز ندارد",
    "qz_s4q3_d": "فقط روی مدل‌های خطی کار می‌کند",
    "qz_s4q3_x": "تکرار + بازتاباندن، PGD را حملهٔ مرتبهٔ اولِ استانداردِ قوی "
        "می‌کند؛ FGSM حالتِ تک‌گامِ آن است.",

    "qz_s4q4": "مدلِ تهدیدِ ℓ∞ با بودجهٔ ε یعنی مهاجم می‌تواند…",
    "qz_s4q4_a": "هر مختصهٔ ورودی را حداکثر ε تغییر دهد",
    "qz_s4q4_b": "حداکثر ε مختصه را در مجموع تغییر دهد",
    "qz_s4q4_c": "کلِّ تصویر را با ضریبِ ε مقیاس کند",
    "qz_s4q4_d": "حداکثر ε بار از مدل پرس‌وجو کند",
    "qz_s4q4_x": "ℓ∞ بزرگ‌ترین تغییرِ تک‌مختصه را می‌بندد — صورت‌بندیِ رایجِ "
        "«اغتشاشِ نامحسوس».",

    "qz_s4q5": "آموزشِ تخاصمی استواری را چگونه بالا می‌برد؟",
    "qz_s4q5_a": "نمونه‌های تخاصمی را حین آموزش می‌سازد و روی آن‌ها آموزش "
        "می‌دهد — معمولاً به بهای اندکی دقّتِ تمیز",
    "qz_s4q5_b": "به هر لایه dropout می‌افزاید",
    "qz_s4q5_c": "فقط روی نمونه‌های درست‌دسته‌بندی‌شده آموزش می‌دهد",
    "qz_s4q5_d": "لایه‌های نخستِ شبکه را منجمد می‌کند",
    "qz_s4q5_x": "آموزشِ کمینه–بیشینه حمله را در خودِ هدف می‌گنجاند؛ بده‌بستانِ "
        "استواری/دقّت بهای آن است.",

    "qz_s4q6": "هموارسازیِ تصادفی استواری را چگونه گواهی می‌کند؟",
    "qz_s4q6_a": "با رأی‌گیری روی نسخه‌های نوفه‌خوردهٔ گاوسیِ ورودی، که شعاعی "
        "اثبات‌پذیر می‌دهد",
    "qz_s4q6_b": "با هموارکردنِ چشم‌اندازِ هزینه به کمکِ SAM",
    "qz_s4q6_c": "با تارکردنِ تصویر پیش از دسته‌بندی",
    "qz_s4q6_d": "با نوفه‌افزودن به برچسب‌ها هنگام آموزش",
    "qz_s4q6_x": "اگر رأیِ اکثریت زیرِ نوفه پایدار بماند، شعاعِ ℓ₂ گواهی‌شده "
        "به دست می‌آید — تضمین، نه ادّعای تجربی.",

    "qz_s4q7": "«شکستنِ حفاظ» (jailbreak) در LLM یعنی…",
    "qz_s4q7_a": "پرامپتی که برای دورزدنِ حفاظ‌های ایمنیِ مدل ساخته شده است",
    "qz_s4q7_b": "استخراجِ وزن‌های مدل از خروجی‌هایش",
    "qz_s4q7_c": "اجرای مدل بیرون از سخت‌افزارِ مجاز",
    "qz_s4q7_d": "ریزتنظیمِ مدل روی دادهٔ خصوصی",
    "qz_s4q7_x": "نقش‌بازی، رمزگذاری یا دستورهای رقیب می‌توانند مدل را به "
        "تولیدِ چیزی برانند که آموزشِ ایمنی باید رد می‌کرد.",

    "qz_s4q8": "«گرادیان‌های مبهم‌شده» چرا زنگِ خطرند؟",
    "qz_s4q8_a": "دفاع‌هایی که فقط جریانِ گرادیان را می‌شکنند ایمنیِ کاذب "
        "می‌دهند و در برابرِ حمله‌های تطبیقی فرو می‌ریزند",
    "qz_s4q8_b": "آموزش را زیادی کند می‌کنند",
    "qz_s4q8_c": "ذخیرهٔ مدل روی دیسک را ناممکن می‌کنند",
    "qz_s4q8_d": "حجمِ فایلِ مدل را بالا می‌برند",
    "qz_s4q8_x": "آتالی و همکاران بیشترِ این دفاع‌ها را شکستند: با حملهٔ "
        "تطبیقی بسنجید، نه فقط حمله‌های آماده.",

    "qz_s4t1": "نمونه‌های تخاصمی اغلب منتقل می‌شوند: اغتشاشی که علیه یک مدل "
        "ساخته شده می‌تواند مدلِ دیگری را هم بفریبد.",
    "qz_s4t1_x": "درست: انتقال‌پذیری حمله‌های جعبه‌سیاه را بی‌نیاز از گرادیانِ "
        "هدف ممکن می‌کند.",

    "qz_s4t2": "تضمینِ استواریِ گواهی‌شده فقط در برابرِ همان الگوریتمِ حمله‌ای "
        "برقرار است که در ارزیابی به کار رفته.",
    "qz_s4t2_x": "نادرست: گواهی «هر» اغتشاشِ درونِ شعاع را می‌بندد — فرقِ "
        "اصلی‌اش با استواریِ تجربی همین است.",

    "qz_s4n1": "FGSM با بودجهٔ ε = {eps} پیکسلی با مقدارِ {x} را در جهتِ مثبتِ "
        "گرادیان می‌راند. مقدارِ آشفته یعنی x + ε را حساب کنید.",
    "qz_s4n1_x": "{x} + {eps} = {ans}؛ زیرِ بودجهٔ ℓ∞ هر مختصه دقیقاً ±ε جابه‌جا "
        "می‌شود.",

    "qz_s4n2": "مدلی دقّتِ تمیزِ {a} دارد ولی زیرِ PGD به {r} می‌رسد. شکافِ "
        "استواری یعنی (تمیز − استوار) را حساب کنید.",
    "qz_s4n2_x": "{a} − {r} = {ans} — این شکاف بهایی است که حمله می‌ستاند.",

    # ---------------- بخش پنجم — حریم خصوصی ---------------- #
    "qz_s5q1": "حملهٔ درِ پشتی (تروجان) به مدل…",
    "qz_s5q1_a": "حین آموزش ماشه‌ای می‌کارد تا مدل فقط با دیدنِ ماشه بدرفتاری کند",
    "qz_s5q1_b": "وزن‌های مدل را از راهِ API می‌دزدد",
    "qz_s5q1_c": "مدل را با سیلِ پرس‌وجو کند می‌کند",
    "qz_s5q1_d": "فقط در زمانِ آزمون ورودی را می‌آشوبد",
    "qz_s5q1_x": "دقّتِ تمیز عادی می‌ماند و درِ پشتی از ارزیابیِ استاندارد "
        "می‌گذرد — خطرناکیِ مسموم‌سازی همین است.",

    "qz_s5q2": "حملهٔ استنتاجِ عضویت می‌خواهد بفهمد…",
    "qz_s5q2_a": "آیا نمونه‌ای مشخص در مجموعهٔ آموزش بوده است یا نه",
    "qz_s5q2_b": "معماریِ مدل چیست",
    "qz_s5q2_c": "نرخِ یادگیریِ آموزش چقدر بوده",
    "qz_s5q2_d": "چند GPU مدل را آموزش داده‌اند",
    "qz_s5q2_x": "مدل روی اعضای آموزش معمولاً مطمئن‌تر است؛ همین شکافِ اطمینان "
        "عضویت را لو می‌دهد — آسیبِ مستقیمِ حریم خصوصی.",

    "qz_s5q3": "سازوکاری ε-تفاضلی-خصوصی است اگر…",
    "qz_s5q3_a": "تغییرِ یک رکورد احتمالِ هر خروجی را حداکثر به ضریبِ e^ε "
        "تغییر دهد",
    "qz_s5q3_b": "هرگز رکوردِ دقیقِ یک فرد را خروجی ندهد",
    "qz_s5q3_c": "داده‌ها در حالِ سکون رمز شده باشند",
    "qz_s5q3_d": "دقّتِ مدل حداکثر ε افت کند",
    "qz_s5q3_x": "DP اثرِ هر فردِ واحد را بر توزیعِ خروجی می‌بندد — تضمینی "
        "بدترین-حالتی و ترکیب‌پذیر.",

    "qz_s5q4": "بودجهٔ حریمِ کوچک‌تر یعنی…",
    "qz_s5q4_a": "حریمِ قوی‌تر، نوفهٔ بیشتر، و معمولاً سودمندیِ کمتر",
    "qz_s5q4_b": "حریمِ ضعیف‌تر ولی آموزشِ سریع‌تر",
    "qz_s5q4_c": "هیچ تغییری در تضمین",
    "qz_s5q4_d": "قطعی‌شدنِ سازوکار",
    "qz_s5q4_x": "ε پیچِ حریم است: ε کوچک = خروجی تقریباً مستقل از هر فرد = "
        "نوفهٔ تزریقیِ بیشتر.",

    "qz_s5q5": "سازوکارِ لاپلاس نوفه‌ای با چه مقیاسی می‌افزاید؟",
    "qz_s5q5_a": "حساسیت ∕ ε",
    "qz_s5q5_b": "ε ∕ حساسیت",
    "qz_s5q5_c": "ε² ∕ 2",
    "qz_s5q5_d": "همیشه دقیقاً ۱",
    "qz_s5q5_x": "b = Δf/ε: هرچه یک نفر بتواند پرس‌وجو را بیشتر جابه‌جا کند و "
        "تضمین قوی‌تر باشد، نوفهٔ بیشتری لازم است.",

    "qz_s5q6": "یادگیریِ فدرال داده را چگونه محافظت می‌کند؟",
    "qz_s5q6_a": "روی هر دستگاه محلی آموزش می‌دهد و فقط به‌روزرسانیِ مدل را "
        "می‌فرستد، نه دادهٔ خام را",
    "qz_s5q6_b": "دادگان را با کلیدِ عمومی رمز می‌کند",
    "qz_s5q6_c": "همهٔ داده را در یک مرکزِ امن نگه می‌دارد",
    "qz_s5q6_d": "داده را پس از یک epoch پاک می‌کند",
    "qz_s5q6_x": "داده از دستگاه بیرون نمی‌رود — ولی گرادیان‌های مشترک هنوز "
        "نشت می‌کنند؛ برای همین DP و تجمیعِ امن لازم می‌شود.",

    "qz_s5q7": "حمله‌های نشتِ گرادیان نشان می‌دهند که…",
    "qz_s5q7_a": "نمونه‌های خامِ آموزش را می‌توان از گرادیان‌های مشترک بازسازی کرد",
    "qz_s5q7_b": "گرادیان‌ها در شبکه‌های عمیق همیشه محو می‌شوند",
    "qz_s5q7_c": "یادگیریِ فدرال نمی‌تواند همگرا شود",
    "qz_s5q7_d": "برشِ گرادیان دقّت را می‌شکند",
    "qz_s5q7_x": "«نشتِ عمیق از گرادیان‌ها»: هم‌ارزکردنِ گرادیان‌ها پیکسل‌ها و "
        "توکن‌ها را بازمی‌گرداند — به‌روزرسانی همان داده است در لباسِ مبدّل.",

    "qz_s5q8": "پاسخِ تصادفی‌شده انکارپذیری می‌دهد چون…",
    "qz_s5q8_a": "هر فرد فقط با احتمالی معلوم — مثلاً بر پایهٔ سکه — راست "
        "می‌گوید",
    "qz_s5q8_b": "افراد می‌توانند هر پرسشی را رد کنند",
    "qz_s5q8_c": "هر پاسخ با کلیدی تصادفی رمز می‌شود",
    "qz_s5q8_d": "ترتیبِ پرسش‌های نظرسنجی بُر می‌خورد",
    "qz_s5q8_x": "تحلیل‌گر می‌تواند جمع را بی‌سوگیری کند در حالی که هیچ پاسخِ "
        "منفردی چیزی را دربارهٔ یک نفر ثابت نمی‌کند — نیای کهنِ DP.",

    "qz_s5t1": "یادگیریِ فدرال به‌خودی‌خود حریمِ تفاضلی را تضمین می‌کند.",
    "qz_s5t1_x": "نادرست: بی‌نوفه، به‌روزرسانی‌های مشترک می‌توانند داده را لو "
        "بدهند (وارونگیِ گرادیان)؛ FL به DP یا تجمیعِ امن نیاز دارد.",

    "qz_s5t2": "تضمین‌های DP ترکیب می‌شوند: چند پرس‌وجوی ε₀ بودجه‌هایشان جمع "
        "می‌شود.",
    "qz_s5t2_x": "درست: ترکیبِ پایه اپسیلون‌ها را جمع می‌زند — برای همین باید "
        "بودجهٔ کل مدیریت شود.",

    "qz_s5n1": "پرس‌وجویی حساسیتِ Δf = {d} دارد و ε = {eps} می‌خواهیم. مقیاسِ "
        "نوفهٔ لاپلاس یعنی b = Δf ∕ ε را حساب کنید.",
    "qz_s5n1_x": "b = {d}/{eps} = {ans}؛ هرچه بودجه کوچک‌تر، نوفه بزرگ‌تر.",

    "qz_s5n2": "{k} پرس‌وجو اجرا می‌کنید، هر یک ε₀ = {e0}. با ترکیبِ پایه، "
        "بودجهٔ کل یعنی ε = k · ε₀ را حساب کنید.",
    "qz_s5n2_x": "{k} × {e0} = {ans} — هر پرس‌وجو بودجه می‌خرجد و هرگز "
        "برنمی‌گردد.",

    # ---------------- بخش ششم — هم‌ترازی ---------------- #
    "qz_s6q1": "«شکافِ هم‌ترازی» تفاوتِ میانِ چیست؟",
    "qz_s6q1_a": "هدفِ نیابتی‌ای که بهینه می‌کنیم و رفتاری که واقعاً می‌خواهیم",
    "qz_s6q1_b": "دقّتِ آموزش و دقّتِ آزمون",
    "qz_s6q1_c": "اندازهٔ مدل و اندازهٔ دادگان",
    "qz_s6q1_d": "هزینهٔ دو بذرِ تصادفیِ متفاوت",
    "qz_s6q1_x": "فشارِ بهینه‌سازی به نیابتیِ اندازه‌پذیر می‌خورد؛ هرچه نیابتی "
        "جا بیندازد، مدل با خیالِ راحت نادیده می‌گیرد یا سوءاستفاده می‌کند.",

    "qz_s6q2": "ترتیبِ استانداردِ خطِ لولهٔ RLHF چیست؟",
    "qz_s6q2_a": "ریزتنظیمِ بانظارت ← مدلِ پاداش از ترجیحاتِ انسانی ← RL علیه "
        "مدلِ پاداش",
    "qz_s6q2_b": "اول RL، بعد ریزتنظیمِ بانظارت، بعد مدلِ پاداش",
    "qz_s6q2_c": "مدلِ پاداش و سیاست هم‌زمان روی همان برچسب‌ها",
    "qz_s6q2_d": "فقط پیش‌آموزش با دادگانِ پالوده",
    "qz_s6q2_x": "SFT قالب را می‌آموزد، مدلِ پاداش ترجیحات را رمز می‌کند، و "
        "PPO سیاست را به‌سویشان می‌راند.",

    "qz_s6q3": "«هکِ پاداش» کی رخ می‌دهد؟",
    "qz_s6q3_a": "وقتی سیاست از کاستی‌های مدلِ پاداش بهره می‌گیرد تا بی‌رفتارِ "
        "مطلوب نمرهٔ بالا بگیرد",
    "qz_s6q3_b": "وقتی کسی وزن‌های مدلِ پاداش را می‌دزدد",
    "qz_s6q3_c": "وقتی پاداش تصادفاً وارونه می‌شود",
    "qz_s6q3_d": "وقتی برچسبِ انسانی تمام می‌شود",
    "qz_s6q3_x": "قانونِ گودهارت در عمل: سنجه هدف می‌شود و از سنجیدنِ آنچه "
        "می‌خواستید بازمی‌ماند.",

    "qz_s6q4": "DPO چه فرقی با RLHF دارد؟",
    "qz_s6q4_a": "ترجیحات را مستقیم با تابعی از جنسِ دسته‌بندی بهینه می‌کند — "
        "بی‌مدلِ پاداشِ صریح و بی‌حلقهٔ RL",
    "qz_s6q4_b": "دو برابر مدلِ پاداش به کار می‌برد",
    "qz_s6q4_c": "در هر گام بازخوردِ انسانیِ برخط می‌خواهد",
    "qz_s6q4_d": "فقط برای مدل‌های بینایی کار می‌کند",
    "qz_s6q4_x": "DPO پاداش را در نسبتِ سیاست به مدلِ مرجع می‌گنجاند — دادهٔ "
        "ترجیح مستقیماً سیاست را آموزش می‌دهد.",

    "qz_s6q5": "ایدهٔ کلیدیِ GRPO چیست؟",
    "qz_s6q5_a": "مقایسهٔ گروهی از پاسخ‌های نمونه‌گیری‌شده و استفاده از مزیتِ "
        "هر یک نسبت به میانگینِ گروه — بدونِ شبکهٔ ارزش",
    "qz_s6q5_b": "رشدِ تدریجیِ مدل لایه‌به‌لایه",
    "qz_s6q5_c": "جایگزینیِ پاداش با نوفهٔ تصادفی",
    "qz_s6q5_d": "آموزش فقط روی بهترین پاسخِ واحد",
    "qz_s6q5_x": "مزیتِ گروه-نسبی + پاداشِ قاعده‌مند، آموزشِ استدلال (به سبکِ "
        "DeepSeek-R1) را ساده و پایدار کرد.",

    "qz_s6q6": "تزریقِ پرامپت (ردیفِ یکمِ OWASP برای LLM) یعنی…",
    "qz_s6q6_a": "دستورهای بدخواهانهٔ پنهان در ورودی یا بافتارِ بازیابی‌شده، "
        "قصدِ توسعه‌دهنده را زیر می‌گیرند",
    "qz_s6q6_b": "پرامپت برای پنجرهٔ بافتار زیادی بلند است",
    "qz_s6q6_c": "SQL در پرس‌وجوی پایگاهِ داده تزریق می‌شود",
    "qz_s6q6_d": "کاربر از مدل ترجمهٔ پرامپت می‌خواهد",
    "qz_s6q6_x": "مدل نمی‌تواند دستور را از داده قاطعانه جدا کند — هر متنی که "
        "می‌خواند می‌تواند بکوشد فرمانش را برگرداند.",

    "qz_s6q7": "خطرِ «عاملیتِ بیش‌ازحد» چیست؟",
    "qz_s6q7_a": "مدلی با ابزار و مجوزِ زیاد، کارهایی اثرگذار فراتر از قصدِ "
        "کاربر انجام دهد",
    "qz_s6q7_b": "مدل زیادی هوشمند شود و روی GPU نگنجد",
    "qz_s6q7_c": "عامل‌ها هرگز حاضر به فراخوانیِ ابزار نشوند",
    "qz_s6q7_d": "کاربران زیادی کم به مدل واگذار کنند",
    "qz_s6q7_x": "چاره: کمینه‌امتیاز + نظارتِ انسانی بر کنش‌های پیامددار — "
        "عاملیت باید کسب شود، نه پیش‌فرض باشد.",

    "qz_s6q8": "جریمهٔ KL در RLHF برای چیست؟",
    "qz_s6q8_a": "سیاست را نزدیکِ مدلِ مرجع نگه می‌دارد تا در تعقیبِ پاداش "
        "تباهی نگیرد",
    "qz_s6q8_b": "آموزشِ مدلِ پاداش را سریع‌تر می‌کند",
    "qz_s6q8_c": "مدل را پس از آموزش فشرده می‌کند",
    "qz_s6q8_d": "آنتروپیِ دادگان را بالا می‌برد",
    "qz_s6q8_x": "بیشینه‌سازیِ بی‌قیدِ پاداش به یاوه‌هایی می‌لغزد که پاداش را "
        "بازی می‌دهند — جملهٔ KL مدلِ زبانی را لنگر می‌کند.",

    "qz_s6t1": "DPO پیش از بهینه‌سازیِ سیاست به آموزشِ مدلِ پاداشِ جداگانه "
        "نیاز دارد.",
    "qz_s6t1_x": "نادرست: حذفِ مدلِ پاداشِ جداگانه دقیقاً همان سهمِ DPO است.",

    "qz_s6t2": "اعتماد به خروجیِ LLM به‌مثابهٔ کد یا فرمان، بدونِ بررسی، خطری "
        "امنیتی است (پردازشِ ناامنِ خروجی).",
    "qz_s6t2_x": "درست: خروجیِ مدل ورودی‌ایست که مهاجم می‌تواند بر آن اثر "
        "بگذارد — مثل هر دادهٔ نامطمئن اعتبارسنجی و قرنطینه‌اش کنید.",

    "qz_s6n1": "سیاستی با احتمالِ {p} پاسخِ هم‌تراز می‌دهد و پاداشِ {ra} "
        "می‌گیرد؛ وگرنه {rb}. پاداشِ موردانتظار یعنی p·rₐ + (1−p)·r_b را حساب "
        "کنید.",
    "qz_s6n1_x": "{p}·{ra} + (1−{p})·{rb} = {ans} — همان کمیتی که RL بالا "
        "می‌بَرد.",

    "qz_s6n2": "GRPO گروهی چهارتایی با پاداش‌های {r1}، {r2}، {r3}، {r4} "
        "می‌گیرد (میانگین = {mean}). مزیتِ پاسخِ نخست یعنی r₁ − میانگین را "
        "حساب کنید.",
    "qz_s6n2_x": "{r1} − {mean} = {ans}؛ پاسخ‌های بالای میانگین تقویت و "
        "پایینی‌ها سرکوب می‌شوند.",
}

AR_QUIZ = {
    "mode_quiz": "الامتحان",
    "quiz_page": "امتحان القسم",
    "choose_quiz": "📝 امتحان",
    "quiz_eyebrow": "تقييم",
    "quiz_title": "امتحان القسم",
    "quiz_intro": "اثنا عشر سؤالًا من نظريّ هذا القسم وعمليِّه. تُخلَط الخيارات "
        "والأرقام في كلّ محاولة. أجب عن الكلّ ثم اضغط «سلّم الامتحان».",
    "quiz_q": "السؤال",
    "quiz_true": "صحيح",
    "quiz_false": "خطأ",
    "quiz_num_hint": "أدخل عددًا (٣ منازل عشريّة).",
    "quiz_submit": "سلّم الامتحان",
    "quiz_score": "النتيجة",
    "quiz_correct_n": "الإجابات الصحيحة",
    "quiz_time": "الزمن المستغرَق",
    "quiz_time_fmt": "{m} دقيقة و{s} ثانية",
    "quiz_v_excellent": "ممتاز — لقد أتقنتَ هذا القسم.",
    "quiz_v_vgood": "جيّد جدًّا — مراجعةٌ سريعة تجعله كاملًا.",
    "quiz_v_good": "جيّد — راجع الدروس المُشار إليها أدناه.",
    "quiz_v_weak": "يحتاج مراجعة — أعد قراءة القسم ثم حاول مجدّدًا.",
    "quiz_review": "مراجعة الإجابات",
    "quiz_your_answer": "إجابتك",
    "quiz_no_answer": "— بلا إجابة —",
    "quiz_right_answer": "الإجابة الصحيحة",
    "quiz_explain": "لماذا",
    "quiz_open_lesson": "افتح الدرس ←",
    "quiz_retry": "⟳ أعد الامتحان بأسئلة جديدة",
    "quiz_badge_note": "احصل على {p}٪ أو أكثر لتنال شارة هذا القسم 🏅.",
    "quiz_passed": "نلتَ الشارة 🏅",
    "quiz_soon_title": "الامتحان قيد الإعداد",
    "quiz_soon_body": "امتحان هذا القسم يُكتَب حاليًّا. القسمان الأوّل والثاني "
        "جاهزان — جرّب أحدهما ريثما يكتمل.",

    # ---------------- القسم الأوّل — التعميم ---------------- #
    "qz_s1q1": "إلى أيّ ثلاث مكوّناتٍ يتفكّك خطأ الاختبار المتوقَّع لنموذجٍ مُشرَف؟",
    "qz_s1q1_a": "مربّع الانحياز، والتباين، والضجيج غير القابل للإزالة",
    "qz_s1q1_b": "خطأ التدريب، وخطأ التحقّق، وخطأ الاختبار",
    "qz_s1q1_c": "قصور التمثيل، وفرط التمثيل، والتنظيم",
    "qz_s1q1_d": "خطأ الأمثَلة، ومعدّل التعلّم، وحجم الدفعة",
    "qz_s1q1_x": "E[(y−f̂)²] = انحياز² + تباين + σ²: فرطُ البساطة، وفرطُ "
        "الحساسيّة، وأرضيّةُ ضجيجٍ لا يستطيع أيُّ نموذجٍ إزالتها.",

    "qz_s1q2": "زيادة سعة النموذج عادةً…",
    "qz_s1q2_a": "تُخفِّض الانحياز وترفع التباين",
    "qz_s1q2_b": "ترفع الانحياز وتُخفِّض التباين",
    "qz_s1q2_c": "تُخفِّض الاثنين معًا",
    "qz_s1q2_d": "ترفع الاثنين معًا",
    "qz_s1q2_x": "المرونة تشتري خطأً منهجيًّا أصغر، لكنّها تجعل الملاءمة أكثر "
        "حساسيّةً لعيّنة التدريب بعينها.",

    "qz_s1q3": "ظاهرة «النزول المزدوج» تُظهر أنّ…",
    "qz_s1q3_a": "خطأ الاختبار قد ينخفض مجدّدًا بعد تجاوز السعة نقطةَ الاستيفاء بكثير",
    "qz_s1q3_b": "خطأ التدريب يرتفع دائمًا مرّتين أثناء التدريب",
    "qz_s1q3_c": "منحنى U الكلاسيكيّ دقيقٌ لكلّ النماذج",
    "qz_s1q3_d": "التباين يتزايد مع السعة رتيبًا دون استثناء",
    "qz_s1q3_x": "الشبكات المفرطة المعاملات قد تعمّم من جديد بعد الاستيفاء — "
        "منحنى U حدسٌ أوّل، لا القصّة كلّها.",

    "qz_s1q4": "بُعد VC لمصنِّفٍ خطّيٍّ (مع حدّ الانحياز) في ℝᵈ يساوي…",
    "qz_s1q4_a": "d + 1",
    "qz_s1q4_b": "d",
    "qz_s1q4_c": "2d + 1",
    "qz_s1q4_d": "d²",
    "qz_s1q4_x": "المستوى الفائق مع تقاطعٍ يستطيع تحطيم d+1 نقطةً على الأكثر في "
        "الوضع العامّ في ℝᵈ.",

    "qz_s1q5": "«التحيُّز الاستقرائيّ» يعني…",
    "qz_s1q5_a": "مجموعة الافتراضات التي يعتمدها المتعلِّم ليعمِّم خارج بيانات التدريب",
    "qz_s1q5_b": "الخطأ المنهجيّ الناجم عن نموذجٍ مفرطِ البساطة",
    "qz_s1q5_c": "الانحياز الاجتماعيّ الموجود في وسوم البيانات",
    "qz_s1q5_d": "تفضيل المُحسِّنات لمعدّلات تعلُّمٍ صغيرة",
    "qz_s1q5_x": "لا تعميمَ بلا افتراضات (لا غداء مجّانيًّا): الالتفاف يفترض "
        "المحليّة، والنموذج الخطّيّ يفترض الخطّيّة.",

    "qz_s1q6": "يُحاذي DANN (التدريب التخاصميّ للمجال) مجالين عبر…",
    "qz_s1q6_a": "تعلُّم سماتٍ تتنبّأ بالوسوم وتخدع مميِّزَ المجال في آنٍ واحد",
    "qz_s1q6_b": "إعادة وزن أصناف المجال المصدر",
    "qz_s1q6_c": "رفع معدّل التعلّم على المجال الهدف",
    "qz_s1q6_d": "تدريب نموذجٍ منفصلٍ لكلّ مجال",
    "qz_s1q6_x": "طبقة عكس التدرّج تدفع المُرمِّز نحو سماتٍ لا يستطيع مميِّزُ "
        "المجال التفريق بينها — سماتٌ ثابتة عبر المجالات.",

    "qz_s1q7": "التحسين الواعي بالحِدّة (SAM) يبحث عن معاملات…",
    "qz_s1q7_a": "تُبقي الخسارة منخفضةً في جوارٍ كامل (قيعان مسطّحة)",
    "qz_s1q7_b": "تبلغ أدنى خسارة تدريبٍ ممكنة مهما كانت حادّة",
    "qz_s1q7_c": "تكون متفرّقةً قدر الإمكان",
    "qz_s1q7_d": "تجعل التدريب يتقارب بأقلّ عدد خطوات",
    "qz_s1q7_x": "يُصغِّر SAM أسوأ خسارةٍ داخل كرةِ ε حول الأوزان؛ القيعان "
        "المسطّحة تميل إلى تعميمٍ أفضل من الحادّة.",

    "qz_s1q8": "مفارقة سيمبسون تُحذِّر من أنّ الاتجاه الظاهر في البيانات المجمَّعة…",
    "qz_s1q8_a": "قد ينعكس عند تقسيم البيانات وفق متغيّرٍ مُربِك",
    "qz_s1q8_b": "يطابق دائمًا الاتجاه داخل كلّ مجموعةٍ فرعيّة",
    "qz_s1q8_c": "برهانٌ كافٍ على علاقةٍ سببيّة",
    "qz_s1q8_d": "لا يظهر إلا حين تكون العيّنة صغيرةً جدًّا",
    "qz_s1q8_x": "الارتباط ليس سببيّةً: الاشتراط على المتغيّر المُربِك قد يقلب "
        "إشارةَ الأثر الظاهر.",

    "qz_s1t1": "يستطيع نموذجٌ كبيرٌ بما يكفي إزالةَ حدِّ الضجيج σ² من تفكيك الخطأ.",
    "qz_s1t1_x": "خطأ: σ² ينبع من عمليّة توليد البيانات نفسها؛ لا يستطيع أيّ "
        "نموذجٍ، مهما كَبُر، إزالته.",

    "qz_s1t2": "في انزياح المتغيّرات المصاحبة يتغيّر توزيع الدخل p(x) بينما يبقى "
        "الشرطيّ p(y|x) ثابتًا.",
    "qz_s1t2_x": "صحيح: هذا هو تعريف covariate shift، وهو ما يجعل الترجيح "
        "بالأهمّيّة وتكييف المجال ممكنَين أصلًا.",

    "qz_s1n1": "في تفكيك الانحياز–التباين، افترض أنّ الانحياز = {b} والتباين = "
        "{v} والضجيج σ² = {n}. احسب الخطأ التربيعيّ المتوقَّع: انحياز² + تباين "
        "+ σ².",
    "qz_s1n1_x": "انحياز² = {b}² = {b2}؛ وبإضافة التباين {v} والضجيج {n} يكون "
        "الناتج {ans}.",

    "qz_s1n2": "أخذُ متوسّطِ {k} نماذجَ بأخطاءٍ مستقلّة يُبقي الانحيازَ ثابتًا "
        "ويقسم التباين على {k}. إذا كان تباين النموذج الواحد {v}، فما تباين "
        "المجموعة؟",
    "qz_s1n2_x": "{v} ÷ {k} = {ans} — ولهذا بالضبط يروِّض التجميع (bagging) "
        "المتعلّمين مرتفعي التباين.",

    # ---------------- القسم الثاني — التفسير ---------------- #
    "qz_s2q1": "ما الفرق بين قابليّة التفسير وقابليّة الشرح؟",
    "qz_s2q1_a": "النموذج القابل للتفسير شفّافٌ بتصميمه؛ أمّا قابليّة الشرح "
        "فتضيف تفسيراتٍ لاحقةً إلى صندوقٍ أسود",
    "qz_s2q1_b": "هما مترادفان تمامًا في الأدبيّات",
    "qz_s2q1_c": "قابليّة الشرح تخصّ النماذج الخطّيّة فقط",
    "qz_s2q1_d": "قابليّة التفسير اسمٌ آخر للدقّة",
    "qz_s2q1_x": "شجرة قرارٍ ضحلة مفهومةٌ بذاتها؛ بينما يشرح SHAP أو LIME "
        "الصندوقَ الأسود بعد وقوع التنبّؤ.",

    "qz_s2q2": "أيّ خاصيّةٍ تحقّقها قيم SHAP لتنبّؤٍ واحد؟",
    "qz_s2q2_a": "مجموعها يساوي بالضبط f(x) − E[f] (الكفاءة/الجمعيّة)",
    "qz_s2q2_b": "تكون موجبةً دائمًا",
    "qz_s2q2_c": "تتطابق لكلّ المدخلات",
    "qz_s2q2_d": "تُعرَّف لمجموعات الأشجار فقط",
    "qz_s2q2_x": "الكفاءة هي بديهيّة شابلي التي تجعل الإسناد كاملًا: تغطّي "
        "المساهماتُ الفجوةَ كلَّها عن القيمة الأساس.",

    "qz_s2q3": "يشرح LIME تنبّؤًا واحدًا عبر…",
    "qz_s2q3_a": "ملاءمة بديلٍ بسيطٍ موزونٍ على عيّناتٍ مضطربةٍ حول الحالة نفسها",
    "qz_s2q3_b": "قراءة أوزان الشبكة مباشرة",
    "qz_s2q3_c": "إعادة تدريب النموذج كاملًا دون كلّ سمة",
    "qz_s2q3_d": "حساب قيم شابلي الدقيقة بصيغةٍ مغلقة",
    "qz_s2q3_x": "محلّيًّا يكون حتى الصندوق الأسود خطّيًّا تقريبًا — يلائم LIME "
        "ذلك البديلَ المحلّيَّ ويقدّم معاملاته تفسيرًا.",

    "qz_s2q4": "التفسير المضادّ (counterfactual) يجيب عن السؤال…",
    "qz_s2q4_a": "«ما أصغرُ تغييرٍ في المدخلات يقلب قرار النموذج؟»",
    "qz_s2q4_b": "«أيّ سمةٍ هي الأهمّ إجمالًا؟»",
    "qz_s2q4_c": "«ما دقّة النموذج على مجموعة الاختبار؟»",
    "qz_s2q4_d": "«أيّ عيّناتٍ وُسمت خطأً أثناء التدريب؟»",
    "qz_s2q4_x": "التفسير المضادّ على مستوى الحالة: أقصر حركةٍ عبر حدّ القرار، "
        "مثل «زيادة الدخل ٤ آلافٍ كانت ستُقِرّ القرض».",

    "qz_s2q5": "كي يكون الجبرُ قابلًا للتنفيذ، يجب أن يكون التغيير المقترح…",
    "qz_s2q5_a": "في سماتٍ يستطيع الشخص فعلًا تغييرها — لا في الثوابت",
    "qz_s2q5_b": "مُعظِّمًا لثقة النموذج بأيّ ثمن",
    "qz_s2q5_c": "مغيِّرًا أكبرَ عددٍ من السمات دفعةً واحدة",
    "qz_s2q5_d": "مُطبَّقًا على بيانات التدريب أيضًا",
    "qz_s2q5_x": "«أنقِص عمرك خمس سنوات» ليس جبرًا؛ قابليّةُ التنفيذ تقصر البحث "
        "المضادّ على السمات القابلة للتغيير.",

    "qz_s2q6": "ماذا يُنتج Grad-CAM؟",
    "qz_s2q6_a": "خريطةً حراريّةً خاصّةً بالصنف من تدرّجات آخر طبقةٍ التفافيّة",
    "qz_s2q6_b": "شجرةَ قرارٍ تحاكي الشبكة الالتفافيّة",
    "qz_s2q6_c": "ترتيبًا تبديليًّا لسماتٍ جدوليّة",
    "qz_s2q6_d": "مثالًا تخاصميًّا للصنف الهدف",
    "qz_s2q6_x": "تدرّجاتُ درجةِ الصنف تُوزِّن خرائطَ السمات الالتفافيّة فتُبرز "
        "أين نظرت الشبكة لأجل ذلك الصنف.",

    "qz_s2q7": "نموذجُ رؤيةٍ يكشف «الذئب» من الخلفيّة الثلجيّة مثالٌ على…",
    "qz_s2q7_a": "الارتباط الزائف (تعلُّم الطريق المختصر)",
    "qz_s2q7_b": "النزول المزدوج",
    "qz_s2q7_c": "الخصوصيّة التفاضليّة",
    "qz_s2q7_d": "اختراق المكافأة",
    "qz_s2q7_x": "الخلفيّة تتلازم مع الوسم في بيانات التدريب فينجح المختصر — "
        "إلى أن يظهر ذئبٌ على العشب.",

    "qz_s2q8": "مشكلة الصندوق الأسود مهمّةٌ قبل كلّ شيء لأنّ…",
    "qz_s2q8_a": "القرارات عالية المخاطر (ائتمان، طبّ، قضاء) تستلزم تبريرًا "
        "وقابليّةً للتدقيق",
    "qz_s2q8_b": "نماذج الصندوق الأسود أقلّ دقّةً دائمًا",
    "qz_s2q8_c": "المنظِّمين يمنعون الشبكات العصبيّة في كلّ مكان",
    "qz_s2q8_d": "التفسيرات تجعل التدريب أسرع بكثير",
    "qz_s2q8_x": "حين يجب أن يكون القرار قابلًا للاعتراض والتدقيق والثقة، لا "
        "تكفي الدقّة وحدها.",

    "qz_s2t1": "KernelSHAP محايدٌ للنموذج: يكفيه الوصولُ الاستعلاميّ إلى تنبّؤات "
        "النموذج.",
    "qz_s2t1_x": "صحيح: يقدّر قيم شابلي من سلوك الدخل–الخرج وحده، فيعمل مع أيّ "
        "مصنِّف.",

    "qz_s2t2": "الشبكة العصبيّة العميقة قابلةٌ للتفسير بطبيعتها، فلا حاجة أبدًا "
        "إلى أساليب الشرح.",
    "qz_s2t2_x": "خطأ: ملايينُ الأوزان المتشابكة هي بالضبط مشكلةُ الصندوق الأسود "
        "التي تستدعي XAI.",

    "qz_s2n1": "لتنبّؤٍ واحد: f(x) = {fx} والقيمة الأساس E[f] = {base}. ثلاثٌ من "
        "قيم SHAP الأربع: φ₁ = {p1}، φ₂ = {p2}، φ₃ = {p3}. احسب φ₄ "
        "بالجمعيّة.",
    "qz_s2n1_x": "φ₄ = f(x) − E[f] − φ₁ − φ₂ − φ₃ = {ans}.",

    "qz_s2n2": "البديل المحلّيّ في LIME هو: g(z) = {w1}·z₁ + {w2}·z₂ + {b}. "
        "لأجل z₁ = {z1} وz₂ = {z2} احسب g(z).",
    "qz_s2n2_x": "g = {w1}·{z1} + {w2}·{z2} + {b} = {ans} — معاملات البديل هي "
        "التفسير نفسه.",

    # ---------------- القسم الثالث — العدالة ---------------- #
    "qz_s3q1": "المصدر الأوّل لانعدام العدالة في أنظمة تعلّم الآلة عادةً هو…",
    "qz_s3q1_a": "الانحياز التاريخيّ والمجتمعيّ الكامن في بيانات التدريب",
    "qz_s3q1_b": "أخطاء التقريب العشريّ على معالج الرسوميّات",
    "qz_s3q1_c": "معدّل تعلُّمٍ أصغر من اللازم",
    "qz_s3q1_d": "إفراطٌ في تنظيم L2",
    "qz_s3q1_x": "يتعلّم النموذج أنماطَ بياناته بأمانة — بما فيها الأنماط "
        "التمييزيّة لقرارات الماضي.",

    "qz_s3q2": "يشترط التكافؤ الديموغرافيّ أن…",
    "qz_s3q2_a": "يتساوى معدّل التنبّؤ الإيجابيّ بين الفئات المحميّة",
    "qz_s3q2_b": "تتساوى الدقّة بين الفئات المحميّة",
    "qz_s3q2_c": "يتلقّى كلّ فردٍ التنبّؤَ نفسه",
    "qz_s3q2_d": "تتساوى أعداد الفئات في بيانات التدريب",
    "qz_s3q2_x": "يجب أن يتطابق P(ŷ=1|A=a) بين الفئات — وهو يتجاهل الوسوم "
        "الحقيقيّة كلّيًّا؛ تلك قوّته وضعفه معًا.",

    "qz_s3q3": "تشترط الفرص المتكافئة (equalized odds) أن…",
    "qz_s3q3_a": "يتساوى معدّلا الإيجاب الصحيح والإيجاب الكاذب معًا بين الفئات",
    "qz_s3q3_b": "يتساوى معدّل الخطأ الإجماليّ فقط",
    "qz_s3q3_c": "لا يستقبل النموذج السمة المحميّة مدخلًا أبدًا",
    "qz_s3q3_d": "تكون التنبّؤات معايَرةً داخل كلّ فئة",
    "qz_s3q3_x": "الاشتراط على الوسم الحقيقيّ يفصلها عن التكافؤ الديموغرافيّ: "
        "يُعامَل المؤهَّلون وغير المؤهَّلين في كلّ فئةٍ سواء.",

    "qz_s3q4": "تنصّ مبرهنة استحالة العدالة على أنّ…",
    "qz_s3q4_a": "المعايرة ومعياري تساوي معدّلات الخطأ لا يمكن أن تتحقّق معًا "
        "حين تختلف المعدّلات الأساسيّة",
    "qz_s3q4_b": "لا نموذج يمكن أن يكون عادلًا بأيّ معنى",
    "qz_s3q4_c": "العدالة تهبط بالدقّة دائمًا إلى مستوى الصدفة",
    "qz_s3q4_d": "النماذج الخطّيّة وحدها تحقّق قيود العدالة",
    "qz_s3q4_x": "مع اختلاف المعدّلات الأساسيّة تتعارض التعاريف رياضيًّا "
        "(كلاينبرغ وآخرون؛ سجال COMPAS) — لا بدّ من الاختيار.",

    "qz_s3q5": "يظهر الانحياز في النماذج اللغويّة الكبيرة عادةً في صورة…",
    "qz_s3q5_a": "تداعياتٍ وإكمالاتٍ نمطيّةٍ تختلف باختلاف الفئة",
    "qz_s3q5_b": "توليدِ رموزٍ أبطأ لبعض المواضيع",
    "qz_s3q5_c": "حيرةٍ أعلى على كلّ لهجات الأقلّيّات دائمًا",
    "qz_s3q5_d": "رفضِ أيّ سؤالٍ ديموغرافيّ",
    "qz_s3q5_x": "إحصاءات التلازم في متن الويب تصير تداعياتٍ في النموذج — "
        "تُسبَر بالقوالب والأزواج المضادّة.",

    "qz_s3q6": "إعادة الوزن، كتخفيفٍ قبل التدريب، تعمل عبر…",
    "qz_s3q6_a": "ضبط أوزان الأمثلة قبل التدريب حتى تتوازن الفئات والوسوم "
        "إحصائيًّا",
    "qz_s3q6_b": "تغيير عتبة القرار بعد التدريب",
    "qz_s3q6_c": "إضافة خصمٍ إلى حلقة التدريب",
    "qz_s3q6_d": "حذف عمود السمة المحميّة فحسب",
    "qz_s3q6_x": "تُصلح توزيعَ البيانات الذي يراه النموذج؛ وحذف العمود وحده "
        "يفشل بسبب السمات الوكيلة المرتبطة.",

    "qz_s3q7": "إزالة الانحياز التخاصميّة تدرِّب…",
    "qz_s3q7_a": "متنبّئًا لا يستطيع خصمٌ أن يستردّ من تمثيله السمةَ المحميّة",
    "qz_s3q7_b": "نموذجين يتنافسان على أعلى دقّة",
    "qz_s3q7_c": "نموذجًا على اضطرابات الصور التخاصميّة",
    "qz_s3q7_d": "نموذجَ مكافأةٍ من التفضيلات البشريّة",
    "qz_s3q7_x": "فكرة عكس التدرّج ذاتها من DANN لكن لأجل العدالة: طهِّر "
        "التمثيل من معلومات الفئة.",

    "qz_s3q8": "المعالجة اللاحقة بالعتبات تحقّق العدالة عبر…",
    "qz_s3q8_a": "اختيار عتبة قرارٍ لكلّ فئةٍ تُساوي معدّلات الخطأ المقصودة",
    "qz_s3q8_b": "إعادة تدريب النموذج من الصفر ببياناتٍ أكثر",
    "qz_s3q8_c": "حذف العيّنات المُخطأ تصنيفها",
    "qz_s3q8_d": "أخذ متوسّط التنبّؤات بين الفئات",
    "qz_s3q8_x": "تُبقي الدرجات كما هي وتُرمّم قاعدةَ القرار — رخيصةٌ وقابلة "
        "للتدقيق وتُطبَّق بعد التدريب.",

    "qz_s3t1": "التكافؤ الديموغرافيّ والفرص المتكافئة معيارٌ واحد باسمين.",
    "qz_s3t1_x": "خطأ: التكافؤ يقيّد التنبّؤات فقط؛ أمّا الفرص المتكافئة "
        "فتشترط على الوسم الحقيقيّ أيضًا — وهما يتعارضان غالبًا.",

    "qz_s3t2": "نموذجٌ لا يرى السمة المحميّة أبدًا يظلّ قادرًا على التمييز عبر "
        "سماتٍ وكيلةٍ مرتبطةٍ بها.",
    "qz_s3t2_x": "صحيح: الرمز البريديّ أو الأسماء أو تاريخ الشراء قد تُشفِّر "
        "الانتماء — «العدالة بالتجاهل» تفشل.",

    "qz_s3n1": "تتلقّى الفئة A قراراتٍ إيجابيّةً بمعدّل {a} والفئة B بمعدّل "
        "{b}. احسب فجوة التكافؤ الديموغرافيّ |{a} − {b}|.",
    "qz_s3n1_x": "|{a} − {b}| = {ans}؛ فجوةُ صفرٍ تعني تحقُّقَ التكافؤ.",

    "qz_s3n2": "أنتج المصنِّف لإحدى الفئات {tp} إيجابًا صحيحًا و{fn} سلبًا "
        "كاذبًا. احسب معدّل الإيجاب الصحيح TP∕(TP+FN).",
    "qz_s3n2_x": "TPR = {tp}/({tp}+{fn}) = {ans} — مقارنة هذا المعدّل بين "
        "الفئات هي جوهر فحص تكافؤ الفرص.",

    # ---------------- القسم الرابع — المتانة ---------------- #
    "qz_s4q1": "المثال التخاصميّ هو…",
    "qz_s4q1_a": "مُدخَلٌ باضطرابٍ ضئيلٍ لا تدركه العين يقلب تنبّؤ النموذج",
    "qz_s4q1_b": "عيّنة تدريبٍ بوسمٍ خاطئ",
    "qz_s4q1_c": "أيّ صورةٍ يصنّفها النموذج بثقةٍ منخفضة",
    "qz_s4q1_d": "عيّنة ولّدتها شبكة GAN",
    "qz_s4q1_x": "يُحسَّن الاضطراب ضدّ تدرّجات النموذج نفسها — غير مرئيٍّ "
        "لنا، حاسمٌ للنموذج.",

    "qz_s4q2": "يحسب FGSM اضطرابه هكذا…",
    "qz_s4q2_a": "ε · sign(∇ₓ الخسارة) — خطوةٌ واحدة باتجاه إشارة التدرّج",
    "qz_s4q2_b": "ضجيجٌ منتظمٌ عشوائيّ بحجم ε",
    "qz_s4q2_c": "تدرّج الأوزان مقصوصًا إلى ε",
    "qz_s4q2_d": "تدويرٌ وقصٌّ للمُدخَل",
    "qz_s4q2_x": "خطوةٌ واحدة رخيصة: حرِّك كلّ بكسل ±ε في الاتجاه الذي يرفع "
        "الخسارة.",

    "qz_s4q3": "بمَ يختلف PGD عن FGSM؟",
    "qz_s4q3_a": "يكرّر خطواتٍ أصغر ويُسقِط بعد كلٍّ منها إلى داخل كرة ε",
    "qz_s4q3_b": "يضطرب الوسومَ بدل المدخلات",
    "qz_s4q3_c": "لا يحتاج إلى أيّ تدرّجات",
    "qz_s4q3_d": "يعمل على النماذج الخطّيّة فقط",
    "qz_s4q3_x": "التكرار + الإسقاط يجعلان PGD الهجومَ القياسيّ القويّ من "
        "الرتبة الأولى؛ وFGSM حالتُه ذات الخطوة الواحدة.",

    "qz_s4q4": "نموذج تهديد ℓ∞ بميزانيّة ε يعني أنّ المهاجم يستطيع…",
    "qz_s4q4_a": "تغيير كلّ إحداثيّةٍ من المُدخَل بمقدار ε على الأكثر",
    "qz_s4q4_b": "تغيير ε إحداثيّةً على الأكثر إجمالًا",
    "qz_s4q4_c": "تحجيم الصورة كلّها بمعامل ε",
    "qz_s4q4_d": "استعلام النموذج ε مرّةً على الأكثر",
    "qz_s4q4_x": "يقيّد ℓ∞ أكبرَ تغييرٍ في إحداثيّةٍ واحدة — الصياغة المعتادة "
        "لـ«اضطرابٍ غير محسوس».",

    "qz_s4q5": "يرفع التدريبُ التخاصميّ المتانةَ عبر…",
    "qz_s4q5_a": "توليد أمثلةٍ تخاصميّة أثناء التدريب والتعلّم عليها — عادةً "
        "بثمنٍ من الدقّة النظيفة",
    "qz_s4q5_b": "إضافة dropout إلى كلّ طبقة",
    "qz_s4q5_c": "التدريب على العيّنات الصحيحة التصنيف فقط",
    "qz_s4q5_d": "تجميد الطبقات الأولى من الشبكة",
    "qz_s4q5_x": "تدريبُ أدنى–أقصى يُدخل الهجومَ في الهدف نفسه؛ ومقايضةُ "
        "المتانة/الدقّة هي الثمن.",

    "qz_s4q6": "التنعيم العشوائيّ يعتمد المتانة عبر…",
    "qz_s4q6_a": "التصويت على نسخٍ كثيرة من المُدخَل مضافٍ إليها ضجيجٌ "
        "غاوسيّ، ممّا يعطي نصف قطرٍ مُبرهَنًا",
    "qz_s4q6_b": "تنعيم سطح الخسارة بـ SAM",
    "qz_s4q6_c": "تغبيش الصورة قبل التصنيف",
    "qz_s4q6_d": "إضافة ضجيجٍ إلى الوسوم أثناء التدريب",
    "qz_s4q6_x": "إن ظلّ تصويتُ الأغلبيّة ثابتًا تحت الضجيج نتج نصفُ قطر ℓ₂ "
        "معتمَد — ضمانةٌ لا ادّعاءٌ تجريبيّ.",

    "qz_s4q7": "«اختراق الحماية» (jailbreak) في النماذج اللغويّة هو…",
    "qz_s4q7_a": "مُوجّهٌ مصوغٌ لتجاوز حواجز الأمان في النموذج",
    "qz_s4q7_b": "استخراج أوزان النموذج من مخرجاته",
    "qz_s4q7_c": "تشغيل النموذج خارج العتاد المرخَّص",
    "qz_s4q7_d": "معايرة النموذج على بياناتٍ خاصّة",
    "qz_s4q7_x": "لعب الأدوار أو التمويه أو الأوامر المتنافسة قد تدفع النموذج "
        "إلى إنتاج ما كان على تدريب الأمان رفضُه.",

    "qz_s4q8": "«التدرّجات المُموَّهة» نذيرُ سوءٍ لأنّ…",
    "qz_s4q8_a": "الدفاعات التي تكتفي بكسر مسار التدرّج تمنح أمانًا زائفًا "
        "وتسقط أمام الهجمات المتكيّفة",
    "qz_s4q8_b": "تُبطئ التدريب كثيرًا",
    "qz_s4q8_c": "تمنع حفظ النموذج على القرص",
    "qz_s4q8_d": "تُضخّم حجم ملفّ النموذج",
    "qz_s4q8_x": "كسر أثالي وزملاؤه معظمَ تلك الدفاعات: قيِّم ضدّ هجومٍ "
        "متكيّف، لا ضدّ الجاهز فقط.",

    "qz_s4t1": "الأمثلة التخاصميّة كثيرًا ما تنتقل: اضطرابٌ صيغ ضدّ نموذجٍ قد "
        "يخدع نموذجًا آخر.",
    "qz_s4t1_x": "صحيح: قابليّة الانتقال تتيح هجمات الصندوق الأسود دون أيّ "
        "وصولٍ إلى تدرّجات الهدف.",

    "qz_s4t2": "ضمانة المتانة المعتمدة لا تصحّ إلا ضدّ خوارزميّة الهجوم "
        "المستعملة في التقييم بعينها.",
    "qz_s4t2_x": "خطأ: الاعتماد يقيّد «كلّ» اضطرابٍ داخل نصف القطر — وهذا "
        "بالضبط ما يميّزه عن المتانة التجريبيّة.",

    "qz_s4n1": "يدفع FGSM بميزانيّة ε = {eps} بكسلًا قيمتُه {x} في الاتجاه "
        "الموجب للتدرّج. احسب القيمة المضطربة x + ε.",
    "qz_s4n1_x": "{x} + {eps} = {ans}؛ تحت ميزانيّة ℓ∞ تتحرّك كلّ إحداثيّةٍ "
        "بمقدار ±ε بالضبط.",

    "qz_s4n2": "يحرز نموذجٌ دقّةً نظيفة {a} لكنّها تهبط تحت PGD إلى {r}. احسب "
        "فجوة المتانة (النظيفة − المتينة).",
    "qz_s4n2_x": "{a} − {r} = {ans} — هذه الفجوة هي الثمن الذي ينتزعه الهجوم.",

    # ---------------- القسم الخامس — الخصوصيّة ---------------- #
    "qz_s5q1": "هجوم الباب الخلفيّ (طروادة) على نموذج…",
    "qz_s5q1_a": "يزرع مُطلِقًا أثناء التدريب فلا يسيء النموذج التصرّف إلا "
        "عند ظهوره",
    "qz_s5q1_b": "يسرق أوزان النموذج عبر واجهة برمجيّة",
    "qz_s5q1_c": "يُغرق النموذج بالاستعلامات لإبطائه",
    "qz_s5q1_d": "يضطرب المدخلات وقت الاختبار فقط",
    "qz_s5q1_x": "تبقى الدقّة النظيفة طبيعيّة فيمرّ البابُ الخلفيّ من التقييم "
        "القياسيّ — وهنا خبثُ التسميم.",

    "qz_s5q2": "يحاول هجوم استنتاج العضويّة معرفة…",
    "qz_s5q2_a": "هل كانت عيّنةٌ بعينها ضمن مجموعة التدريب أم لا",
    "qz_s5q2_b": "معماريّة النموذج",
    "qz_s5q2_c": "معدّل التعلّم المستعمل في التدريب",
    "qz_s5q2_d": "عدد المعالجات التي درّبت النموذج",
    "qz_s5q2_x": "يكون النموذج عادةً أوثقَ على أعضاء تدريبه؛ وفجوة الثقة تلك "
        "تفضح العضويّة — ضررٌ مباشر بالخصوصيّة.",

    "qz_s5q3": "تكون الآليّة ε-تفاضليّةَ الخصوصيّة إذا…",
    "qz_s5q3_a": "غيّر تبديلُ سجلٍّ واحد احتمالَ أيّ خرجٍ بعاملٍ لا يتجاوز e^ε",
    "qz_s5q3_b": "لم تُخرج قطّ سجلَّ فردٍ بعينه",
    "qz_s5q3_c": "كانت البيانات مشفَّرةً وهي مخزَّنة",
    "qz_s5q3_d": "هبطت دقّة النموذج بمقدار ε على الأكثر",
    "qz_s5q3_x": "تقيّد DP أثرَ أيّ فردٍ واحد في توزيع الخرج — ضمانةُ أسوأ "
        "حالةٍ وقابلةٌ للتركيب.",

    "qz_s5q4": "ميزانيّة خصوصيّةٍ أصغر ε تعني…",
    "qz_s5q4_a": "خصوصيّةً أقوى وضجيجًا أكثر ونفعًا أقلّ عادةً",
    "qz_s5q4_b": "خصوصيّةً أضعف لكن تدريبًا أسرع",
    "qz_s5q4_c": "لا تغيير في الضمانة",
    "qz_s5q4_d": "صيرورةَ الآليّة حتميّةً",
    "qz_s5q4_x": "ε هو مقبض الخصوصيّة: ε صغير = خرجٌ شبه مستقلٍّ عن أيّ فرد = "
        "ضجيجٌ محقونٌ أكثر.",

    "qz_s5q5": "تضيف آليّة لابلاس ضجيجًا مقياسُه…",
    "qz_s5q5_a": "الحساسيّة ∕ ε",
    "qz_s5q5_b": "ε ∕ الحساسيّة",
    "qz_s5q5_c": "ε² ∕ 2",
    "qz_s5q5_d": "الواحد دائمًا",
    "qz_s5q5_x": "b = Δf/ε: كلّما استطاع فردٌ تحريكَ الاستعلام أكثر (Δf) "
        "وكانت الضمانة أقوى (ε صغير)، لزم ضجيجٌ أكبر.",

    "qz_s5q6": "يحمي التعلّم الموحَّد البيانات عبر…",
    "qz_s5q6_a": "التدريب محلّيًّا على كلّ جهاز ومشاركة تحديثات النموذج فقط، "
        "لا البيانات الخام أبدًا",
    "qz_s5q6_b": "تشفير مجموعة البيانات بمفتاحٍ عامّ",
    "qz_s5q6_c": "تخزين كلّ البيانات في مركزٍ آمنٍ واحد",
    "qz_s5q6_d": "حذف البيانات بعد حقبة تدريبٍ واحدة",
    "qz_s5q6_x": "لا تغادر البياناتُ الجهازَ — لكنّ التدرّجات المشتركة تظلّ "
        "تُسرِّب؛ لذا تلزم DP والتجميع الآمن فوقه.",

    "qz_s5q7": "تُبيّن هجمات تسريب التدرّج أنّ…",
    "qz_s5q7_a": "عيّنات التدريب الخام يمكن إعادة بنائها من التدرّجات المشتركة",
    "qz_s5q7_b": "التدرّجات تتلاشى دائمًا في الشبكات العميقة",
    "qz_s5q7_c": "التعلّم الموحَّد لا يستطيع التقارب",
    "qz_s5q7_d": "قصّ التدرّج يكسر دقّة النموذج",
    "qz_s5q7_x": "«التسريب العميق من التدرّجات»: مطابقة التدرّجات تستردّ "
        "البكسلات والرموز — التحديثات بياناتٌ متنكّرة.",

    "qz_s5q8": "يمنح الردُّ العشوائيّ إنكارًا مقبولًا لأنّ…",
    "qz_s5q8_a": "كلَّ شخصٍ يصدُق باحتمالٍ معلومٍ فقط — على قرعة عملةٍ مثلًا",
    "qz_s5q8_b": "الأشخاص يستطيعون تجاوز أيّ سؤال",
    "qz_s5q8_c": "كلَّ إجابةٍ تُشفَّر بمفتاحٍ عشوائيّ",
    "qz_s5q8_d": "ترتيبَ أسئلة الاستبيان يُخلَط",
    "qz_s5q8_x": "يستطيع المحلِّل إزالة انحياز المجموع بينما لا تُثبت أيّ "
        "إجابةٍ منفردة شيئًا عن شخصٍ واحد — الجدّ الأقدم لـ DP.",

    "qz_s5t1": "التعلّم الموحَّد يضمن بحدّ ذاته الخصوصيّةَ التفاضليّة.",
    "qz_s5t1_x": "خطأ: من دون ضجيجٍ مضاف قد تُسرِّب التحديثاتُ المشتركة "
        "البيانات (عكس التدرّج)؛ يحتاج التعلّم الموحَّد إلى DP أو تجميعٍ آمن "
        "فوقه.",

    "qz_s5t2": "ضمانات DP تتركّب: تنفيذُ عدّة استعلامات ε₀ يجمع ميزانيّاتها.",
    "qz_s5t2_x": "صحيح: التركيب الأساسيّ يجمع قيم إبسيلون — ولهذا تجب إدارةُ "
        "ميزانيّةٍ كلّيّة للخصوصيّة.",

    "qz_s5n1": "لاستعلامٍ حساسيّتُه Δf = {d} ونريد ε = {eps}. احسب مقياس ضجيج "
        "لابلاس b = Δf ∕ ε.",
    "qz_s5n1_x": "b = {d}/{eps} = {ans}؛ يكبر الضجيج كلّما صغُرت الميزانيّة.",

    "qz_s5n2": "تنفّذ {k} استعلامات، كلٌّ منها ε₀ = {e0}. بالتركيب الأساسيّ "
        "احسب الميزانيّة الكلّيّة ε = k · ε₀.",
    "qz_s5n2_x": "{k} × {e0} = {ans} — كلّ استعلامٍ يُنفق ميزانيّةً لا تعود "
        "أبدًا.",

    # ---------------- القسم السادس — المحاذاة ---------------- #
    "qz_s6q1": "«فجوة المحاذاة» هي الفرق بين…",
    "qz_s6q1_a": "الهدف الوكيل الذي نُحسِّنه والسلوك الذي نقصده فعلًا",
    "qz_s6q1_b": "دقّة التدريب ودقّة الاختبار",
    "qz_s6q1_c": "حجم النموذج وحجم البيانات",
    "qz_s6q1_d": "خسارة بذرتين عشوائيّتين",
    "qz_s6q1_x": "ضغط التحسين يستهدف الوكيلَ القابل للقياس؛ وكلُّ ما يفوته "
        "الوكيل سيتجاهله النموذج أو يستغلّه بلا تردّد.",

    "qz_s6q2": "الترتيب القياسيّ لخطّ أنابيب RLHF هو…",
    "qz_s6q2_a": "معايرةٌ بإشراف ← نموذجُ مكافأةٍ من التفضيلات البشريّة ← "
        "تعلُّمٌ معزَّز ضدّ نموذج المكافأة",
    "qz_s6q2_b": "التعلّم المعزَّز أوّلًا ثمّ المعايرة ثمّ نموذج المكافأة",
    "qz_s6q2_c": "تدريب نموذج المكافأة والسياسة معًا على الوسوم نفسها",
    "qz_s6q2_d": "اكتفاءٌ بالتدريب المسبق على بياناتٍ منقّحة",
    "qz_s6q2_x": "تعلّم المعايرةُ الشكلَ، ويُشفِّر نموذجُ المكافأة التفضيلات، "
        "ويدفع PPO السياسةَ نحوها.",

    "qz_s6q3": "يحدث «اختراق المكافأة» حين…",
    "qz_s6q3_a": "تستغلّ السياسةُ عيوبَ نموذج المكافأة لتحرز درجاتٍ عالية دون "
        "السلوك المقصود",
    "qz_s6q3_b": "يسرق أحدُهم أوزانَ نموذج المكافأة",
    "qz_s6q3_c": "تُعكَس المكافأة سهوًا",
    "qz_s6q3_d": "تنفد الوسوم البشريّة أثناء التدريب",
    "qz_s6q3_x": "قانون غودهارت عمليًّا: يصير المقياسُ هدفًا فيكفّ عن قياس ما "
        "أردتَه.",

    "qz_s6q4": "يختلف DPO عن RLHF في أنّه…",
    "qz_s6q4_a": "يُحسِّن التفضيلات مباشرةً بخسارةٍ من جنس التصنيف — بلا "
        "نموذج مكافأةٍ صريح ولا حلقة تعلُّمٍ معزَّز",
    "qz_s6q4_b": "يستعمل ضعف عدد نماذج المكافأة",
    "qz_s6q4_c": "يتطلّب تعقيبًا بشريًّا حيًّا في كلّ خطوة",
    "qz_s6q4_d": "يصلح لنماذج الرؤية فقط",
    "qz_s6q4_x": "يطوي DPO المكافأةَ في نسبة السياسة إلى نموذجٍ مرجعيّ — "
        "فتدرِّب بياناتُ التفضيل السياسةَ رأسًا.",

    "qz_s6q5": "الفكرة المفتاحيّة في GRPO هي…",
    "qz_s6q5_a": "مقارنة مجموعةٍ من الإجابات المعيَّنة واستعمال ميزة كلٍّ "
        "منها على متوسّط المجموعة — دون شبكة قيمة",
    "qz_s6q5_b": "تنمية النموذج طبقةً فطبقة",
    "qz_s6q5_c": "استبدال ضجيجٍ عشوائيٍّ بالمكافآت",
    "qz_s6q5_d": "التدريب على أفضل إجابةٍ واحدة فقط",
    "qz_s6q5_x": "الميزات النسبيّة للمجموعة + مكافآت قاعديّة جعلت تدريبَ "
        "الاستدلال (على طريقة DeepSeek-R1) بسيطًا مستقرًّا.",

    "qz_s6q6": "حقن الموجِّهات (الأوّل في OWASP للنماذج اللغويّة) هو أن…",
    "qz_s6q6_a": "تعليماتٍ خبيثةً مدسوسةً في المُدخَل أو السياق المسترجَع "
        "تتجاوز قصدَ المطوِّر",
    "qz_s6q6_b": "يطول الموجِّهُ عن نافذة السياق",
    "qz_s6q6_c": "يُدسّ SQL في استعلام قاعدة بيانات",
    "qz_s6q6_d": "يطلب المستخدم ترجمةَ موجِّه",
    "qz_s6q6_x": "لا يستطيع النموذج الفصلَ الحازم بين التعليمات والبيانات — "
        "كلُّ نصٍّ يقرؤه قد يحاول توجيهه.",

    "qz_s6q7": "خطر «الوكالة المفرطة» هو أن…",
    "qz_s6q7_a": "نموذجًا أُعطي أدواتٍ وصلاحيّاتٍ كثيرة يتّخذ أفعالًا مؤثّرةً "
        "تتجاوز قصد المستخدم",
    "qz_s6q7_b": "يصير النموذج أذكى من أن يعمل على معالج",
    "qz_s6q7_c": "يرفض الوكلاء استدعاءَ أيّ أداة",
    "qz_s6q7_d": "يفوّض المستخدمون القليلَ جدًّا للنموذج",
    "qz_s6q7_x": "العلاج: أدنى صلاحيّة + إشرافٌ بشريّ على الأفعال ذات "
        "العواقب — الوكالة تُكتسَب ولا تُمنح افتراضًا.",

    "qz_s6q8": "توجد عقوبة KL في RLHF لكي…",
    "qz_s6q8_a": "تُبقي السياسةَ قريبةً من النموذج المرجعيّ فلا تنحطّ وهي "
        "تلاحق المكافأة",
    "qz_s6q8_b": "تسرِّع تدريبَ نموذج المكافأة",
    "qz_s6q8_c": "تضغط النموذج بعد التدريب",
    "qz_s6q8_d": "ترفع إنتروبيا البيانات",
    "qz_s6q8_x": "تعظيمُ المكافأة بلا قيدٍ ينزلق إلى هذيانٍ يتلاعب بالمكافأة — "
        "حدُّ KL يُرسي النموذجَ اللغويّ.",

    "qz_s6t1": "يتطلّب DPO تدريبَ نموذج مكافأةٍ صريحٍ منفصلٍ قبل تحسين السياسة.",
    "qz_s6t1_x": "خطأ: إلغاءُ نموذج المكافأة المنفصل هو بالضبط إسهامُ DPO.",

    "qz_s6t2": "معاملة خرج النموذج اللغويّ كأنّه شيفرةٌ أو أوامر موثوقة دون "
        "فحصٍ خطرٌ أمنيّ (معالجة الخرج غير الآمنة).",
    "qz_s6t2_x": "صحيح: خرجُ النموذج مُدخَلٌ يمكن للمهاجم التأثيرُ فيه — "
        "تحقَّق منه واعزله كأيّ بياناتٍ غير موثوقة.",

    "qz_s6n1": "تنتج السياسةُ الإجابةَ المحاذاة باحتمال {p} فتكسب مكافأة "
        "{ra}، وإلا فتكسب {rb}. احسب المكافأة المتوقَّعة p·rₐ + (1−p)·r_b.",
    "qz_s6n1_x": "{p}·{ra} + (1−{p})·{rb} = {ans} — وهي الكمّيّة التي يرفعها "
        "التعلّم المعزَّز.",

    "qz_s6n2": "يعيّن GRPO مجموعةً من أربع إجاباتٍ مكافآتُها {r1} و{r2} و{r3} "
        "و{r4} (المتوسّط = {mean}). احسب ميزة الإجابة الأولى: r₁ − المتوسّط.",
    "qz_s6n2_x": "{r1} − {mean} = {ans}؛ ما فوق المتوسّط يُعزَّز وما دونه "
        "يُكبَح.",
}
