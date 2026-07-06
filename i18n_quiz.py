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
}
