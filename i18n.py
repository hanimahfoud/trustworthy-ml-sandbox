"""
i18n.py -- the single source of every user-facing string, in English, Persian
and Arabic. UI code never hard-codes prose; it calls ``t(lang, key)``.

Design notes
------------
* English is the base. ``t`` falls back to English for any missing key, so a
  half-translated key can never crash the app.
* Mathematical equations are *not* stored here -- they live in ``modules`` as
  LaTeX, because notation is language independent and rendering RTL math is a
  trap. Likewise, chart axis titles, series names and the short mono "readout"
  tags are kept in English on purpose: in a real bilingual scientific tool the
  numerals and technical labels stay in one script while the prose localizes.
* Theory prose values are plain text with at most inline <em>/<strong>; the
  theory module wraps each paragraph in <p>...</p>.
"""
from __future__ import annotations

# Languages offered in the sidebar, and which ones are right-to-left.
LANGS = [("en", "English"), ("fa", "فارسی"), ("ar", "العربية")]
RTL = {"fa", "ar"}


def is_rtl(lang: str) -> bool:
    return lang in RTL


# =========================================================================== #
# ENGLISH (base)                                                              #
# =========================================================================== #
EN: dict[str, str] = {
    # ---- masthead / chrome ----
    "masthead_eyebrow": "Trustworthy Machine Learning Laboratory",
    "masthead_title": "Generalization & Causal Foundations",
    "masthead_subtitle": "An interactive companion to the bias–variance trade-off, "
        "distribution shift, the sharpness of minima, and causal inference — "
        "computed live.",
    "colophon_1": "Course · Trustworthy Machine Learning",
    "colophon_2": "Section I · Generalization & Causal Foundations",
    "colophon_3": "Build 2026.1",
    "lang_label": "Language",
    "sidebar_name": "Trustworthy ML Lab",
    "sidebar_sub": "Section I",
    "mode_label": "Part",
    "mode_theory": "Theory",
    "mode_practice": "Practice",
    "nav_label": "Page",
    "live_badge": "Live compute — every figure is recomputed from the controls.",

    # ---- theory nav titles ----
    "th_bv": "The Bias–Variance Trade-off",
    "th_vc": "VC Dimension & Complexity",
    "th_ib": "Inductive Bias",
    "th_tl": "Transfer & Domain Adaptation",
    "th_sam": "Sharpness-Aware Minimization",
    "th_cz": "Causal Foundations",

    # ---- practice nav titles ----
    "pr_bv": "Bias–Variance Simulator",
    "pr_dann": "Domain Adaptation (DANN)",
    "pr_sam": "SAM vs SGD Landscape",
    "pr_simpson": "Simpson's Paradox",
    "pr_cf": "Counterfactual Calculator",

    # ===================== THEORY PROSE =====================
    # 1) Bias–Variance
    "th_bv_eyebrow": "Generalization · Plate 01",
    "th_bv_p1": "Supervised learning seeks a function that is right not on the data "
        "we hold but on data we have not yet seen. Expected test error decomposes "
        "into three independent pieces: the square of the <em>bias</em>, the "
        "<em>variance</em>, and an irreducible <em>noise</em> floor set by the data "
        "themselves.",
    "th_bv_p2": "Bias measures how far the average model — across many hypothetical "
        "training sets — sits from the truth; it is the error of being too simple. "
        "Variance measures how much the fitted function jumps as the training set "
        "changes; it is the error of being too sensitive. The noise term can never "
        "be removed by any model.",
    "th_bv_p3": "Increasing capacity trades one for the other. Too little capacity "
        "underfits (high bias); too much overfits (high variance). The best "
        "generalization lives at the minimum of their sum, not at either extreme.",
    "th_bv_eqcap": "<b>Figure.</b> Expected squared error at a point, decomposed.",
    "th_bv_call": "Generalization is the art of spending capacity exactly where it "
        "lowers bias faster than it raises variance.",

    # 2) VC dimension
    "th_vc_eyebrow": "Generalization · Plate 02",
    "th_vc_p1": "How much can training performance promise about test performance? "
        "Statistical learning theory answers with a bound: test error is at most "
        "training error plus a complexity penalty that grows with the capacity of "
        "the hypothesis class and shrinks as the sample grows.",
    "th_vc_p2": "The Vapnik–Chervonenkis (VC) dimension formalizes capacity as the "
        "largest number of points the class can <em>shatter</em> — label in every "
        "possible way. A higher VC dimension means a looser guarantee for the same "
        "amount of data.",
    "th_vc_p3": "This is also the line between interpolation and extrapolation. "
        "Inside the support of the training data a flexible model can interpolate "
        "safely; outside it, no amount of fit on seen points constrains behavior, "
        "and confident error is the rule.",
    "th_vc_eqcap": "<b>Figure.</b> A capacity–sample generalization bound (schematic constants).",
    "th_vc_call": "A model that interpolates the training set perfectly has proven "
        "nothing about points beyond it — low training error is necessary, never "
        "sufficient.",

    # 3) Inductive bias
    "th_ib_eyebrow": "Generalization · Plate 03",
    "th_ib_p1": "No learner generalizes without assumptions. <em>Inductive bias</em> "
        "is the set of preferences — independent of the training data — that pick "
        "one hypothesis over another when both fit equally well. Without it, "
        "generalization is impossible in principle.",
    "th_ib_p2": "It enters through (i) architecture (e.g. convolution's translation "
        "equivariance), (ii) feature engineering, (iii) data augmentation, which "
        "encodes invariances by example, (iv) the optimizer, whose implicit "
        "regularization favors particular solutions, and (v) the loss/penalty — L2 "
        "prefers small, spread-out weights, L1 prefers sparse ones.",
    "th_ib_p3": "Choosing an inductive bias well matched to the problem is often "
        "worth more than raw capacity or data volume.",
    "th_ib_eqcap": "<b>Figure.</b> L1 vs L2 penalties seen as a prior over weights.",
    "th_ib_call": "The right inductive bias is a hypothesis about the world, paid "
        "for in advance and refunded as data efficiency.",

    # 4) Transfer / domain adaptation
    "th_tl_eyebrow": "Distribution Shift · Plate 04",
    "th_tl_p1": "Models are trained on one distribution and deployed on another. The "
        "shift comes in named forms: <em>covariate shift</em> (the inputs' "
        "distribution changes, the labeling rule does not), <em>concept shift</em> "
        "(the rule itself changes), and <em>prior shift</em> (the class balance "
        "changes).",
    "th_tl_p2": "Unsupervised domain adaptation seeks a representation in which "
        "source and target look the same. Distance between the two feature "
        "distributions is the Maximum Mean Discrepancy (MMD): the gap between their "
        "mean embeddings in a reproducing-kernel Hilbert space, which is zero "
        "exactly when the distributions match.",
    "th_tl_p3": "A domain-adversarial network (DANN) makes this learnable. A domain "
        "classifier tries to tell source from target features; a Gradient Reversal "
        "Layer multiplies its gradient by −λ on the way into the feature extractor, "
        "so the extractor is trained to defeat it — yielding features that carry "
        "the label signal but not the domain.",
    "th_tl_eqcap": "<b>Figure.</b> MMD between source and target embeddings.",
    "th_tl_call": "Adaptation succeeds when a classifier can still read the label "
        "but can no longer tell which domain it came from.",

    # 5) SAM
    "th_sam_eyebrow": "Optimization · Plate 05",
    "th_sam_p1": "Two sets of weights can reach the same training loss yet "
        "generalize very differently. A <em>sharp</em> minimum sits at the bottom "
        "of a narrow ravine: a small parameter perturbation sends the loss up "
        "steeply. A <em>flat</em> minimum sits in a wide basin and tolerates "
        "perturbation — and flat minima tend to transfer better to unseen data.",
    "th_sam_p2": "Sharpness-Aware Minimization (SAM) optimizes not the loss at the "
        "current point but the worst-case loss within a ρ-ball around it. It first "
        "takes an ascent step to the most damaging nearby point, then descends from "
        "there, explicitly seeking neighborhoods that are uniformly low.",
    "th_sam_p3": "The hyperparameter ρ sets the radius of that neighborhood — how "
        "much flatness the optimizer insists on.",
    "th_sam_eqcap": "<b>Figure.</b> The SAM min–max objective on a ρ-ball.",
    "th_sam_call": "SGD asks ‘is this point low?’; SAM asks ‘is this whole "
        "neighborhood low?’.",

    # 6) Causality
    "th_cz_eyebrow": "Causal Inference · Plate 06",
    "th_cz_p1": "Prediction asks what tends to occur together; causation asks what "
        "would happen if we intervened. <em>Simpson's paradox</em> is the warning "
        "shot: an association present in every subgroup can reverse once the "
        "subgroups are pooled, because a confounder drives both the treatment and "
        "the outcome.",
    "th_cz_p2": "The do-operator separates seeing from doing. P(Y∣X) conditions on "
        "<em>observing</em> X; P(Y∣do(X)) describes <em>setting</em> X by "
        "intervention, cutting the arrows that normally point into X. They coincide "
        "only when no confounding remains.",
    "th_cz_p3": "A counterfactual goes further — what would have happened to this "
        "unit, had things been different? Pearl's three steps answer it: "
        "<em>abduction</em> (update beliefs about the latent background from what "
        "was observed), <em>action</em> (apply the hypothetical intervention to the "
        "model), and <em>prediction</em> (read off the outcome). The Markov blanket "
        "— a node's parents, children, and children's other parents — is the set "
        "that renders it independent of all else.",
    "th_cz_eqcap": "<b>Figure.</b> Intervention severs the inbound arrows to X.",
    "th_cz_call": "Conditioning on a confounder is not adjusting for it; only an "
        "intervention — real or modeled — licenses a causal claim.",

    # ===================== PRACTICE =====================
    # 1) Bias–Variance simulator
    "pr_bv_eyebrow": "Practice · Demo 01",
    "pr_bv_intro": "Fit a polynomial of your chosen degree to noisy samples of a "
        "smooth target, and watch the bias–variance trade-off resolve in real "
        "time. Every number below is computed from fresh draws — nothing is "
        "pre-recorded.",
    "pr_bv_ctrl_degree": "Polynomial degree",
    "pr_bv_ctrl_n": "Training points",
    "pr_bv_ctrl_noise": "Noise level (σ)",
    "pr_bv_ctrl_seed": "Random seed",
    "pr_bv_cap_fit": "<b>Figure 1.</b> A single fit at the chosen degree. Dots are "
        "noisy training samples; the teal curve is the true function; crimson is "
        "the fitted polynomial.",
    "pr_bv_cap_err": "<b>Figure 2.</b> Train vs test error across degrees (log "
        "scale), averaged over many resamples. The valley marks the capacity that "
        "generalizes best.",
    "pr_bv_cap_comp": "<b>Figure 3.</b> The same error split into bias², variance "
        "and noise as a share of the total. Bias dominates on the left, variance "
        "on the right.",
    "pr_bv_underfit": "High bias — the model is too simple and underfits.",
    "pr_bv_overfit": "High variance — the model chases noise and overfits.",
    "pr_bv_balanced": "Near the sweet spot — bias and variance are balanced.",

    # 2) DANN
    "pr_dann_eyebrow": "Practice · Demo 02",
    "pr_dann_intro": "Source and target share the same labeling rule but the target "
        "is rotated and shifted — a covariate shift. Train a domain-adversarial "
        "network and watch target accuracy recover as the adversary forces "
        "domain-invariant features. λ is the strength of the Gradient Reversal "
        "Layer; λ = 0 is the source-only baseline.",
    "pr_dann_ctrl_lambda": "Adversary strength λ (GRL)",
    "pr_dann_ctrl_seed": "Random seed",
    "pr_dann_cap_space": "<b>Figure 1.</b> Input space: source (filled) and target "
        "(outlined) two-moons, with the learned decision boundary.",
    "pr_dann_cap_feat": "<b>Figure 2.</b> Learned features projected to 2-D (PCA). "
        "Adaptation pulls the two domain clouds together.",
    "pr_dann_baseline": "Adaptation disabled — this is the source-only baseline.",
    "pr_dann_adapt": "Adaptation active — the feature extractor is being pushed to "
        "confuse the domain classifier.",
    "pr_dann_training": "Training the domain-adversarial network…",

    # 3) SAM
    "pr_sam_eyebrow": "Practice · Demo 03",
    "pr_sam_intro": "A landscape with a narrow, deep local minimum and a wide global "
        "one. SGD descends the true loss; SAM descends the worst-case loss inside a "
        "ρ-ball. Increase ρ to see SAM stop preferring the sharp trap and settle in "
        "the flat, generalizing basin.",
    "pr_sam_ctrl_rho": "Neighborhood radius ρ",
    "pr_sam_cap_true": "<b>Figure 1.</b> The true loss surface L(w). The narrow well "
        "on the left is the sharp minimum; the wide well is flat.",
    "pr_sam_cap_eff": "<b>Figure 2.</b> The worst-case surface E(w) = "
        "max₍‖ε‖≤ρ₎ L(w+ε) that SAM actually minimizes. The sharp well fills in as "
        "ρ grows.",
    "pr_sam_cap_traj": "<b>Figure 3.</b> Descent paths from the same start. SGD "
        "follows L; SAM follows E.",
    "pr_sam_flat": "At this ρ, SAM reaches the flat (generalizing) basin.",
    "pr_sam_sharp": "At this ρ, SAM still settles in the sharp basin — raise ρ to "
        "escape it.",

    # 4) Simpson
    "pr_simpson_eyebrow": "Practice · Demo 04",
    "pr_simpson_intro": "A treatment that wins within every severity group can lose "
        "in the pooled totals if assignment is confounded with severity. Slide the "
        "allocation skew and watch the paradox switch on.",
    "pr_simpson_ctrl_skew": "Allocation skew (severity → treatment)",
    "pr_simpson_cap_groups": "<b>Figure 1.</b> Within-group recovery rates. B (teal) "
        "beats A (crimson) in both mild and severe cases.",
    "pr_simpson_cap_agg": "<b>Figure 2.</b> Pooled recovery rates. Past the onset "
        "skew, A overtakes B — the reversal.",
    "pr_simpson_cap_curve": "<b>Figure 3.</b> Pooled rates vs skew; the dashed line "
        "marks where the paradox appears.",
    "pr_simpson_cap_dag": "<b>Figure 4.</b> The confounding triangle. Severity "
        "causes both treatment assignment and outcome.",
    "pr_simpson_on": "Simpson's paradox present: B is better in every group, yet A "
        "is better overall.",
    "pr_simpson_off": "No paradox at this skew: the pooled comparison agrees with "
        "the subgroups.",

    # 5) Counterfactual
    "pr_cf_eyebrow": "Practice · Demo 05",
    "pr_cf_intro": "A structural model with three latent customer types answers a "
        "counterfactual: given that a customer who was shown the ad stayed unhappy, "
        "what is the probability they would have been happy had we not shown it? "
        "Set the prior, the observation and the intervention; the three steps are "
        "traced exactly.",
    "pr_cf_ctrl_phater": "P(dog-hater type)",
    "pr_cf_ctrl_psad": "P(always-sad type)",
    "pr_cf_ctrl_tobs": "Observed treatment T",
    "pr_cf_ctrl_yobs": "Observed outcome Y",
    "pr_cf_ctrl_tdo": "Counterfactual do(T)",
    "pr_cf_step_abduction": "Abduction — reweight the latent types to those that "
        "could have produced the observation.",
    "pr_cf_step_action": "Action — replace the treatment with the intervention, "
        "holding the latent type fixed.",
    "pr_cf_step_prediction": "Prediction — read off the outcome distribution under "
        "the intervention.",
    "pr_cf_cap_post": "<b>Figure 1.</b> Prior vs posterior over latent types after "
        "abduction.",
    "pr_cf_cap_table": "<b>Figure 2.</b> Structural response of each type to T = 0 "
        "and T = 1.",
    "pr_cf_cap_scm": "<b>Figure 3.</b> The structural model: the latent type U and "
        "the treatment T jointly determine the outcome Y.",
    "pr_cf_impossible": "This observation is impossible under the current model — no "
        "latent type produces it. Adjust the observation or the prior.",
    "pr_cf_headline": "Counterfactual probability of a happy outcome",
    "pr_cf_responder": "Responder",
    "pr_cf_hater": "Dog-hater",
    "pr_cf_always_sad": "Always-sad",

    # ---- theme + byline + assistant (Section II chrome) ----
    "theme_label": "Theme",
    "theme_light": "Light",
    "theme_dark": "Dark",
    "theme_colored": "Colored",
    "byline_supervisor": "Supervisor",
    "byline_author": "Prepared by",
    "name_supervisor": "Dr. Behrouz Minaei-Bidgoli",
    "name_author": "Hani Akram Mahfoud",
    "assistant_label": "Ask me",
}


# =========================================================================== #
# PERSIAN                                                                      #
# =========================================================================== #
FA: dict[str, str] = {
    "masthead_eyebrow": "آزمایشگاهِ یادگیریِ ماشینِ قابلِ‌اعتماد",
    "masthead_title": "تعمیم‌پذیری و بنیادهای علّی",
    "masthead_subtitle": "همراهی تعاملی برای مفاضلهٔ سوگیری–واریانس، انزیاحِ توزیع، "
        "تیزیِ کمینه‌ها، و استنتاجِ علّی — که زنده محاسبه می‌کند.",
    "colophon_1": "درس · یادگیریِ ماشینِ قابلِ‌اعتماد",
    "colophon_2": "بخشِ یکم · تعمیم‌پذیری و بنیادهای علّی",
    "colophon_3": "نسخهٔ ۲۰۲۶٫۱",
    "lang_label": "زبان",
    "sidebar_name": "آزمایشگاهِ یادگیریِ قابلِ‌اعتماد",
    "sidebar_sub": "بخشِ یکم",
    "mode_label": "بخش",
    "mode_theory": "نظریه",
    "mode_practice": "تمرین",
    "nav_label": "صفحه",
    "live_badge": "محاسبهٔ زنده — هر نمودار از روی کنترل‌ها بازمحاسبه می‌شود.",

    "th_bv": "مفاضلهٔ سوگیری–واریانس",
    "th_vc": "بُعد VC و پیچیدگی",
    "th_ib": "سوگیریِ استقرایی",
    "th_tl": "انتقال و تطبیقِ دامنه",
    "th_sam": "کمینه‌سازیِ آگاه‌به‌تیزی",
    "th_cz": "بنیادهای علّی",

    "pr_bv": "شبیه‌سازِ سوگیری–واریانس",
    "pr_dann": "تطبیقِ دامنه (DANN)",
    "pr_sam": "سیمای SAM در برابر SGD",
    "pr_simpson": "پارادوکسِ سیمپسون",
    "pr_cf": "ماشین‌حسابِ ضدِواقع",

    "th_bv_eyebrow": "تعمیم‌پذیری · لوح ۰۱",
    "th_bv_p1": "یادگیریِ بانظارت به‌دنبالِ تابعی است که نه روی داده‌های موجود، بلکه روی "
        "داده‌هایی که هنوز دیده نشده‌اند درست عمل کند. خطای موردانتظارِ آزمون به سه مؤلفهٔ "
        "مستقل تجزیه می‌شود: مجذورِ سوگیری (bias)، واریانس (variance)، و یک کفِ نوفهٔ "
        "تقلیل‌ناپذیر که خودِ داده‌ها آن را تعیین می‌کنند.",
    "th_bv_p2": "سوگیری اندازه می‌گیرد که میانگینِ مدل — روی بسیاری از مجموعه‌های آموزشیِ "
        "فرضی — چقدر از حقیقت فاصله دارد؛ این خطای «بیش‌ازحد ساده‌بودن» است. واریانس "
        "اندازه می‌گیرد که تابعِ برازش‌شده با تغییرِ مجموعهٔ آموزشی چقدر نوسان می‌کند؛ این "
        "خطای «بیش‌ازحد حساس‌بودن» است. مؤلفهٔ نوفه را هیچ مدلی نمی‌تواند حذف کند.",
    "th_bv_p3": "افزایشِ ظرفیت یکی را با دیگری معاوضه می‌کند. ظرفیتِ کم به کم‌برازش "
        "(سوگیریِ بالا) و ظرفیتِ زیاد به بیش‌برازش (واریانسِ بالا) می‌انجامد. بهترین تعمیم "
        "در کمینهٔ مجموعِ این دو قرار دارد، نه در هیچ‌یک از دو سرِ طیف.",
    "th_bv_eqcap": "<b>شکل.</b> خطای مجذورِ موردانتظار در یک نقطه، تجزیه‌شده.",
    "th_bv_call": "تعمیم‌پذیری هنرِ خرجِ ظرفیت دقیقاً در جایی است که سوگیری را سریع‌تر از "
        "افزایشِ واریانس کاهش می‌دهد.",

    "th_vc_eyebrow": "تعمیم‌پذیری · لوح ۰۲",
    "th_vc_p1": "عملکردِ آموزش چقدر می‌تواند دربارهٔ عملکردِ آزمون تضمین دهد؟ نظریهٔ "
        "یادگیریِ آماری با یک کران پاسخ می‌دهد: خطای آزمون حداکثر برابرِ خطای آموزش "
        "به‌علاوهٔ جریمه‌ای از پیچیدگی است که با ظرفیتِ ردهٔ فرضیه‌ها بزرگ‌تر و با بزرگ‌شدنِ "
        "نمونه کوچک‌تر می‌شود.",
    "th_vc_p2": "بُعدِ واپْنیک–چروننکیس (VC) ظرفیت را به‌صورتِ بزرگ‌ترین تعداد نقاطی تعریف "
        "می‌کند که رده می‌تواند «بشکند» — یعنی به هر شکلِ ممکن برچسب بزند. بُعدِ VCِ بالاتر "
        "یعنی تضمینی سست‌تر برای همان مقدارِ داده.",
    "th_vc_p3": "همین، مرزِ میانِ درون‌یابی و برون‌یابی است. درونِ دامنهٔ داده‌های آموزشی "
        "یک مدلِ منعطف می‌تواند با اطمینان درون‌یابی کند؛ بیرون از آن، هیچ میزانی از "
        "برازش روی نقاطِ دیده‌شده رفتار را مقید نمی‌کند و خطای پرمدعا قاعده است.",
    "th_vc_eqcap": "<b>شکل.</b> یک کرانِ تعمیمِ ظرفیت–نمونه (با ثابت‌های نمادین).",
    "th_vc_call": "مدلی که مجموعهٔ آموزشی را به‌طور کامل درون‌یابی می‌کند، دربارهٔ نقاطِ "
        "فراتر از آن هیچ‌چیز ثابت نکرده است — خطای آموزشِ پایین لازم است، اما هرگز کافی نیست.",

    "th_ib_eyebrow": "تعمیم‌پذیری · لوح ۰۳",
    "th_ib_p1": "هیچ یادگیرنده‌ای بدونِ مفروضات تعمیم نمی‌دهد. سوگیریِ استقرایی "
        "(inductive bias) مجموعه‌ای از ترجیح‌ها — مستقل از داده‌های آموزشی — است که وقتی "
        "دو فرضیه به یک اندازه برازش می‌دهند، یکی را بر دیگری برمی‌گزیند. بدونِ آن، تعمیم "
        "در اصل ناممکن است.",
    "th_ib_p2": "این سوگیری از این مسیرها وارد می‌شود: (۱) معماری (مثلاً هم‌ورداییِ "
        "انتقالیِ کانولوشن)، (۲) مهندسیِ ویژگی، (۳) داده‌افزایی که ناوردایی‌ها را با مثال "
        "رمزگذاری می‌کند، (۴) بهینه‌ساز، که منظم‌سازیِ ضمنی‌اش راه‌حل‌های خاصی را ترجیح "
        "می‌دهد، و (۵) تابعِ زیان/جریمه — L2 وزن‌های کوچک و پخش‌شده را و L1 وزن‌های تُنُک را "
        "ترجیح می‌دهد.",
    "th_ib_p3": "انتخابِ سوگیریِ استقراییِ متناسب با مسئله اغلب از ظرفیتِ خام یا حجمِ داده "
        "ارزشمندتر است.",
    "th_ib_eqcap": "<b>شکل.</b> جریمه‌های L1 و L2 به‌مثابهٔ پیشین روی وزن‌ها.",
    "th_ib_call": "سوگیریِ استقراییِ درست، فرضیه‌ای دربارهٔ جهان است که پیشاپیش پرداخت "
        "می‌شود و به‌صورتِ کارآمدیِ داده بازپس داده می‌شود.",

    "th_tl_eyebrow": "انزیاحِ توزیع · لوح ۰۴",
    "th_tl_p1": "مدل‌ها روی یک توزیع آموزش می‌بینند و روی توزیعی دیگر به‌کار گرفته می‌شوند. "
        "این انزیاح شکل‌های نام‌دار دارد: انزیاحِ هم‌متغیر (covariate shift) که توزیعِ "
        "ورودی‌ها تغییر می‌کند اما قاعدهٔ برچسب‌زنی نه؛ انزیاحِ مفهوم (concept shift) که "
        "خودِ قاعده تغییر می‌کند؛ و انزیاحِ پیشین (prior shift) که توازنِ کلاس‌ها تغییر می‌کند.",
    "th_tl_p2": "تطبیقِ دامنهٔ بی‌نظارت به‌دنبالِ بازنمایی‌ای است که در آن مبدأ و مقصد یکسان "
        "به‌نظر برسند. فاصلهٔ میانِ دو توزیعِ ویژگی، بیشینهٔ ناهم‌خوانیِ میانگین (MMD) است: "
        "فاصلهٔ میانِ میانگینِ تعبیهٔ آن‌ها در یک فضای هیلبرتِ هسته‌بازتولید، که دقیقاً هنگامِ "
        "برابریِ دو توزیع صفر می‌شود.",
    "th_tl_p3": "شبکهٔ دامنه‌-خصمانه (DANN) این را یادگرفتنی می‌کند. یک طبقه‌بندِ دامنه "
        "می‌کوشد ویژگی‌های مبدأ را از مقصد تشخیص دهد؛ یک لایهٔ وارونگیِ گرادیان (Gradient "
        "Reversal Layer) گرادیانِ آن را در مسیرِ ورود به استخراج‌گرِ ویژگی در −λ ضرب می‌کند، "
        "تا استخراج‌گر برای شکست‌دادنش آموزش ببیند — و ویژگی‌هایی پدید آیند که نشانِ برچسب "
        "را حمل کنند اما نشانِ دامنه را نه.",
    "th_tl_eqcap": "<b>شکل.</b> MMD میانِ تعبیه‌های مبدأ و مقصد.",
    "th_tl_call": "تطبیق وقتی موفق است که یک طبقه‌بند هنوز بتواند برچسب را بخواند اما دیگر "
        "نتواند بگوید از کدام دامنه آمده است.",

    "th_sam_eyebrow": "بهینه‌سازی · لوح ۰۵",
    "th_sam_p1": "دو مجموعه‌وزن می‌توانند به یک زیانِ آموزشی برسند اما بسیار متفاوت تعمیم "
        "دهند. کمینهٔ تیز (sharp) در تهِ دره‌ای باریک است: اختلالِ کوچکی در پارامترها زیان "
        "را به‌تندی بالا می‌برد. کمینهٔ مسطح (flat) در حوضه‌ای پهن است و اختلال را تحمل "
        "می‌کند — و کمینه‌های مسطح معمولاً بهتر به داده‌های دیده‌نشده منتقل می‌شوند.",
    "th_sam_p2": "کمینه‌سازیِ آگاه‌به‌تیزی (SAM) نه زیانِ نقطهٔ کنونی، بلکه بدترین‌حالتِ زیان "
        "درونِ گویِ به‌شعاعِ ρ پیرامونِ آن را بهینه می‌کند. نخست گامی صعودی به آسیب‌زاترین "
        "نقطهٔ مجاور برمی‌دارد، سپس از آنجا فرود می‌آید و آشکارا به‌دنبالِ همسایگی‌هایی است که "
        "به‌طور یکنواخت پایین‌اند.",
    "th_sam_p3": "ابرپارامترِ ρ شعاعِ آن همسایگی را تعیین می‌کند — اینکه بهینه‌ساز چه میزان "
        "«مسطح‌بودن» را الزامی می‌داند.",
    "th_sam_eqcap": "<b>شکل.</b> هدفِ کمینه–بیشینهٔ SAM روی گویِ ρ.",
    "th_sam_call": "SGD می‌پرسد «آیا این نقطه پایین است؟»؛ SAM می‌پرسد «آیا تمامِ این "
        "همسایگی پایین است؟».",

    "th_cz_eyebrow": "استنتاجِ علّی · لوح ۰۶",
    "th_cz_p1": "پیش‌بینی می‌پرسد چه چیزهایی معمولاً با هم رخ می‌دهند؛ علّیت می‌پرسد اگر "
        "مداخله کنیم چه می‌شود. پارادوکسِ سیمپسون هشدارِ نخست است: همبستگی‌ای که در هر "
        "زیرگروه حاضر است می‌تواند پس از ادغامِ زیرگروه‌ها وارونه شود، زیرا یک مخدوش‌گر "
        "(confounder) هم بر درمان و هم بر پیامد اثر می‌گذارد.",
    "th_cz_p2": "عملگرِ do دیدن را از انجام‌دادن جدا می‌کند. P(Y∣X) بر مشاهدهٔ X شرط "
        "می‌گذارد؛ P(Y∣do(X)) تنظیمِ X با مداخله را توصیف می‌کند و پیکان‌هایی را که معمولاً "
        "به X وارد می‌شوند می‌بُرد. این دو تنها هنگامی یکی می‌شوند که هیچ مخدوش‌گری باقی "
        "نمانده باشد.",
    "th_cz_p3": "ضدِواقع (counterfactual) فراتر می‌رود — اگر شرایط فرق می‌کرد، برای همین "
        "واحد چه می‌شد؟ سه گامِ پِرل پاسخ می‌دهند: ربایش (abduction) یعنی به‌روزرسانیِ باور "
        "دربارهٔ زمینهٔ پنهان بر پایهٔ آنچه مشاهده شد، کنش (action) یعنی اعمالِ مداخلهٔ فرضی "
        "بر مدل، و پیش‌بینی (prediction) یعنی خواندنِ پیامد. پوششِ مارکوف (Markov blanket) — "
        "والدین، فرزندان و سایرِ والدینِ فرزندانِ یک گره — مجموعه‌ای است که آن گره را از "
        "همه‌چیزِ دیگر مستقل می‌کند.",
    "th_cz_eqcap": "<b>شکل.</b> مداخله پیکان‌های ورودی به X را قطع می‌کند.",
    "th_cz_call": "شرط‌گذاری روی یک مخدوش‌گر همان تعدیل‌کردنِ آن نیست؛ تنها یک مداخله — "
        "واقعی یا مدل‌شده — مجوزِ یک ادعای علّی را می‌دهد.",

    "pr_bv_eyebrow": "تمرین · نمایشِ ۰۱",
    "pr_bv_intro": "یک چندجمله‌ای با درجهٔ دلخواه را بر نمونه‌های نوفه‌دارِ یک تابعِ هموار "
        "برازش دهید و معاوضهٔ سوگیری–واریانس را در زمانِ واقعی ببینید. هر عددِ زیر از "
        "نمونه‌گیریِ تازه محاسبه می‌شود — هیچ‌چیز از پیش‌ضبط‌شده نیست.",
    "pr_bv_ctrl_degree": "درجهٔ چندجمله‌ای",
    "pr_bv_ctrl_n": "تعدادِ نقاطِ آموزش",
    "pr_bv_ctrl_noise": "سطحِ نوفه (σ)",
    "pr_bv_ctrl_seed": "بذرِ تصادفی",
    "pr_bv_cap_fit": "<b>شکل ۱.</b> یک برازش در درجهٔ انتخابی. نقطه‌ها نمونه‌های نوفه‌دارِ "
        "آموزش‌اند؛ منحنیِ فیروزه‌ای تابعِ حقیقی و منحنیِ زرشکی چندجمله‌ایِ برازش‌شده است.",
    "pr_bv_cap_err": "<b>شکل ۲.</b> خطای آموزش در برابرِ آزمون روی درجه‌ها (مقیاسِ "
        "لگاریتمی)، میانگین‌گیری‌شده روی نمونه‌گیری‌های متعدد. درهٔ منحنی ظرفیتی را نشان "
        "می‌دهد که بهترین تعمیم را دارد.",
    "pr_bv_cap_comp": "<b>شکل ۳.</b> همان خطا، تفکیک‌شده به سهمِ سوگیری²، واریانس و نوفه "
        "از کل. سوگیری در سمتِ چپ و واریانس در سمتِ راست غالب است.",
    "pr_bv_underfit": "سوگیریِ بالا — مدل بیش‌ازحد ساده است و کم‌برازش می‌کند.",
    "pr_bv_overfit": "واریانسِ بالا — مدل نوفه را دنبال می‌کند و بیش‌برازش می‌کند.",
    "pr_bv_balanced": "نزدیکِ نقطهٔ بهینه — سوگیری و واریانس متوازن‌اند.",

    "pr_dann_eyebrow": "تمرین · نمایشِ ۰۲",
    "pr_dann_intro": "مبدأ و مقصد قاعدهٔ برچسب‌زنیِ یکسانی دارند اما مقصد چرخیده و جابه‌جا "
        "شده است — یک انزیاحِ هم‌متغیر. یک شبکهٔ دامنه‌-خصمانه آموزش دهید و ببینید دقتِ "
        "مقصد چگونه با واداشتنِ ویژگی‌ها به ناوردایی نسبت به دامنه بهبود می‌یابد. λ شدتِ "
        "لایهٔ وارونگیِ گرادیان است؛ λ = ۰ خطِ مبنای فقط-مبدأ است.",
    "pr_dann_ctrl_lambda": "شدتِ خصم λ (GRL)",
    "pr_dann_ctrl_seed": "بذرِ تصادفی",
    "pr_dann_cap_space": "<b>شکل ۱.</b> فضای ورودی: دو-هلالِ مبدأ (تو‌پُر) و مقصد "
        "(تو‌خالی)، همراه با مرزِ تصمیمِ آموخته‌شده.",
    "pr_dann_cap_feat": "<b>شکل ۲.</b> ویژگی‌های آموخته‌شده، تصویرشده به دو بُعد (PCA). "
        "تطبیق دو ابرِ دامنه را به هم نزدیک می‌کند.",
    "pr_dann_baseline": "تطبیق غیرفعال است — این خطِ مبنای فقط-مبدأ است.",
    "pr_dann_adapt": "تطبیق فعال است — استخراج‌گرِ ویژگی به‌سمتِ مغشوش‌کردنِ طبقه‌بندِ "
        "دامنه رانده می‌شود.",
    "pr_dann_training": "در حالِ آموزشِ شبکهٔ دامنه‌-خصمانه…",

    "pr_sam_eyebrow": "تمرین · نمایشِ ۰۳",
    "pr_sam_intro": "یک سیمای زیان با یک کمینهٔ محلیِ باریک و عمیق و یک کمینهٔ سراسریِ "
        "پهن. SGD روی زیانِ حقیقی فرود می‌آید؛ SAM روی بدترین‌حالتِ زیان درونِ گویِ ρ. ρ را "
        "افزایش دهید تا ببینید SAM دیگر دامِ تیز را ترجیح نمی‌دهد و در حوضهٔ مسطح و "
        "تعمیم‌دهنده می‌نشیند.",
    "pr_sam_ctrl_rho": "شعاعِ همسایگی ρ",
    "pr_sam_cap_true": "<b>شکل ۱.</b> سیمای زیانِ حقیقی L(w). چاهِ باریکِ سمتِ چپ کمینهٔ "
        "تیز و چاهِ پهن کمینهٔ مسطح است.",
    "pr_sam_cap_eff": "<b>شکل ۲.</b> سیمای بدترین‌حالت E(w) = max₍‖ε‖≤ρ₎ L(w+ε) که "
        "SAM واقعاً کمینه می‌کند. چاهِ تیز با بزرگ‌شدنِ ρ پُر می‌شود.",
    "pr_sam_cap_traj": "<b>شکل ۳.</b> مسیرهای فرود از یک نقطهٔ آغازِ یکسان. SGD از L و "
        "SAM از E پیروی می‌کند.",
    "pr_sam_flat": "در این ρ، SAM به حوضهٔ مسطح (تعمیم‌دهنده) می‌رسد.",
    "pr_sam_sharp": "در این ρ، SAM هنوز در حوضهٔ تیز می‌نشیند — برای گریز، ρ را افزایش دهید.",

    "pr_simpson_eyebrow": "تمرین · نمایشِ ۰۴",
    "pr_simpson_intro": "درمانی که در هر گروهِ شدت پیروز می‌شود می‌تواند در مجموعِ کل ببازد، "
        "اگر تخصیص با شدت مخدوش شده باشد. اریبیِ تخصیص را تغییر دهید و روشن‌شدنِ پارادوکس "
        "را ببینید.",
    "pr_simpson_ctrl_skew": "اریبیِ تخصیص (شدت ← درمان)",
    "pr_simpson_cap_groups": "<b>شکل ۱.</b> نرخ‌های بهبودِ درون‌گروهی. درمانِ B (فیروزه‌ای) "
        "در هر دو گروهِ خفیف و شدید از A (زرشکی) بهتر است.",
    "pr_simpson_cap_agg": "<b>شکل ۲.</b> نرخ‌های بهبودِ ادغام‌شده. پس از آستانهٔ اریبی، A "
        "از B پیشی می‌گیرد — وارونگی.",
    "pr_simpson_cap_curve": "<b>شکل ۳.</b> نرخ‌های ادغام‌شده در برابرِ اریبی؛ خطِ‌چین جایی "
        "را نشان می‌دهد که پارادوکس پدیدار می‌شود.",
    "pr_simpson_cap_dag": "<b>شکل ۴.</b> مثلثِ مخدوش‌سازی. شدت هم بر تخصیصِ درمان و هم بر "
        "پیامد اثر می‌گذارد.",
    "pr_simpson_on": "پارادوکسِ سیمپسون حاضر است: B در هر گروه بهتر است، اما A در کل بهتر است.",
    "pr_simpson_off": "در این اریبی پارادوکسی نیست: مقایسهٔ ادغام‌شده با زیرگروه‌ها هم‌خوان است.",

    "pr_cf_eyebrow": "تمرین · نمایشِ ۰۵",
    "pr_cf_intro": "یک مدلِ ساختاری با سه نوعِ مشتریِ پنهان به یک پرسشِ ضدِواقع پاسخ می‌دهد: "
        "با دانستنِ اینکه مشتری‌ای که آگهی دید ناراضی ماند، احتمالِ اینکه اگر آگهی را "
        "نمی‌دیدیم راضی می‌شد چقدر است؟ پیشین، مشاهده و مداخله را تنظیم کنید؛ هر سه گام "
        "دقیقاً ردگیری می‌شوند.",
    "pr_cf_ctrl_phater": "P(نوعِ بیزار)",
    "pr_cf_ctrl_psad": "P(نوعِ همیشه-ناراضی)",
    "pr_cf_ctrl_tobs": "درمانِ مشاهده‌شده T",
    "pr_cf_ctrl_yobs": "پیامدِ مشاهده‌شده Y",
    "pr_cf_ctrl_tdo": "ضدِواقع do(T)",
    "pr_cf_step_abduction": "ربایش — وزن‌دهیِ دوبارهٔ انواعِ پنهان به آن‌هایی که می‌توانستند "
        "مشاهده را پدید آورند.",
    "pr_cf_step_action": "کنش — جایگزینیِ درمان با مداخله، با ثابت‌نگه‌داشتنِ نوعِ پنهان.",
    "pr_cf_step_prediction": "پیش‌بینی — خواندنِ توزیعِ پیامد تحتِ مداخله.",
    "pr_cf_cap_post": "<b>شکل ۱.</b> پیشین در برابرِ پسین روی انواعِ پنهان پس از ربایش.",
    "pr_cf_cap_table": "<b>شکل ۲.</b> پاسخِ ساختاریِ هر نوع به T = ۰ و T = ۱.",
    "pr_cf_cap_scm": "<b>شکل ۳.</b> مدلِ ساختاری: نوعِ پنهانِ U و درمانِ T با هم پیامدِ Y "
        "را تعیین می‌کنند.",
    "pr_cf_impossible": "این مشاهده تحتِ مدلِ کنونی ناممکن است — هیچ نوعِ پنهانی آن را "
        "پدید نمی‌آورد. مشاهده یا پیشین را تغییر دهید.",
    "pr_cf_headline": "احتمالِ ضدِواقعِ پیامدِ راضی",
    "pr_cf_responder": "پاسخ‌دهنده",
    "pr_cf_hater": "بیزار",
    "pr_cf_always_sad": "همیشه-ناراضی",

    # ---- theme + byline + assistant ----
    "theme_label": "پوسته",
    "theme_light": "روشن",
    "theme_dark": "تیره",
    "theme_colored": "رنگی",
    "byline_supervisor": "استاد راهنما",
    "byline_author": "تهیه‌کننده",
    "name_supervisor": "Dr. Behrouz Minaei-Bidgoli",
    "name_author": "Hani Akram Mahfoud",
    "assistant_label": "از من بپرس",
}


# =========================================================================== #
# ARABIC                                                                       #
# =========================================================================== #
AR: dict[str, str] = {
    "masthead_eyebrow": "مختبر تعلُّم الآلة الجدير بالثقة",
    "masthead_title": "التعميم والأسس السببية",
    "masthead_subtitle": "مرافِقٌ تفاعليٌّ لمفاضلة التحيُّز–التباين، وانزياح التوزيع، "
        "وحِدّة الدنيا الصغرى، والاستدلال السببي — يَحسِب آنيًّا.",
    "colophon_1": "مقرَّر · تعلُّم الآلة الجدير بالثقة",
    "colophon_2": "القسم الأول · التعميم والأسس السببية",
    "colophon_3": "إصدار ٢٠٢٦٫١",
    "lang_label": "اللغة",
    "sidebar_name": "مختبر التعلُّم الجدير بالثقة",
    "sidebar_sub": "القسم الأول",
    "mode_label": "القسم",
    "mode_theory": "النظرية",
    "mode_practice": "التطبيق",
    "nav_label": "الصفحة",
    "live_badge": "حسابٌ آنيّ — يُعاد حساب كلِّ شكلٍ من عناصر التحكُّم.",

    "th_bv": "مفاضلة التحيُّز–التباين",
    "th_vc": "بُعد VC والتعقيد",
    "th_ib": "التحيُّز الاستقرائي",
    "th_tl": "النقل وتكييف المجال",
    "th_sam": "التحسين الواعي بالحِدّة",
    "th_cz": "الأسس السببية",

    "pr_bv": "محاكي التحيُّز–التباين",
    "pr_dann": "تكييف المجال (DANN)",
    "pr_sam": "سطح SAM مقابل SGD",
    "pr_simpson": "مفارقة سيمبسون",
    "pr_cf": "حاسبة الواقع المضاد",

    "th_bv_eyebrow": "التعميم · لوح ٠١",
    "th_bv_p1": "يسعى التعلُّم المُوجَّه إلى دالةٍ تُصيب لا على البيانات المتوفّرة بل على "
        "بياناتٍ لم تُرَ بعد. ينحلُّ خطأ الاختبار المتوقَّع إلى ثلاثة مكوّناتٍ مستقلّة: مربّع "
        "التحيُّز (bias)، والتباين (variance)، وأرضيةُ ضجيجٍ غير قابلةٍ للاختزال تحدِّدها "
        "البيانات نفسها.",
    "th_bv_p2": "يقيس التحيُّز مدى بُعدِ متوسّط النموذج — عبر كثيرٍ من مجموعات التدريب "
        "الافتراضية — عن الحقيقة؛ وهو خطأ «الإفراط في البساطة». ويقيس التباين مقدارَ تذبذب "
        "الدالة المُلائَمة عند تغيُّر مجموعة التدريب؛ وهو خطأ «الإفراط في الحساسية». أمّا "
        "مكوّن الضجيج فلا يستطيع أيُّ نموذجٍ إزالته.",
    "th_bv_p3": "زيادةُ السَعة تُقايض أحدهما بالآخر. السَعة القليلة تؤدّي إلى نقص الملاءمة "
        "(تحيُّزٌ عالٍ)، والسَعة المفرطة إلى فرط الملاءمة (تباينٌ عالٍ). وأفضلُ تعميمٍ يقع عند "
        "أصغرِ مجموعهما، لا عند أيٍّ من الطرفين.",
    "th_bv_eqcap": "<b>شكل.</b> الخطأ التربيعي المتوقَّع عند نقطة، مُحلَّلًا.",
    "th_bv_call": "التعميم فنُّ إنفاق السَعة في الموضع الذي يَخفِض فيه التحيُّز أسرعَ ممّا "
        "يرفع التباين.",

    "th_vc_eyebrow": "التعميم · لوح ٠٢",
    "th_vc_p1": "إلى أيِّ حدٍّ يَعِد أداءُ التدريب بأداء الاختبار؟ تُجيب نظرية التعلُّم "
        "الإحصائي بحدٍّ أعلى: خطأ الاختبار لا يتجاوز خطأ التدريب مضافًا إليه غرامةُ تعقيدٍ "
        "تكبُر بسَعة فئة الفرضيات وتصغُر بكِبَر العيّنة.",
    "th_vc_p2": "يَصوغ بُعدُ فابنيك–تشيرفوننكيس (VC) السَعةَ بوصفها أكبرَ عددٍ من النقاط "
        "تستطيع الفئةُ «تحطيمه» — أي وسمَه بكلِّ الطرق الممكنة. وبُعد VC الأعلى يعني ضمانًا "
        "أرخى لنفس كمية البيانات.",
    "th_vc_p3": "وهذا أيضًا هو الخطُّ الفاصل بين الاستيفاء والاستقراء الخارجي. داخلَ نطاق "
        "بيانات التدريب يستطيع نموذجٌ مرنٌ الاستيفاءَ بأمان؛ وخارجَه لا يُقيِّد السلوكَ أيُّ "
        "قدرٍ من الملاءمة على النقاط المرئيّة، ويصير الخطأ الواثق هو القاعدة.",
    "th_vc_eqcap": "<b>شكل.</b> حدُّ تعميمٍ بدلالة السَعة والعيّنة (بثوابتَ رمزية).",
    "th_vc_call": "النموذج الذي يَستوفي مجموعةَ التدريب تمامًا لم يُثبِت شيئًا عن النقاط "
        "التي تتجاوزها — فخطأُ التدريب المنخفض ضروريٌّ لا كافٍ أبدًا.",

    "th_ib_eyebrow": "التعميم · لوح ٠٣",
    "th_ib_p1": "لا يُعمِّم أيُّ متعلِّمٍ بلا افتراضات. التحيُّزُ الاستقرائي (inductive bias) "
        "هو مجموعةُ تفضيلاتٍ — مستقلّةٍ عن بيانات التدريب — تختار فرضيةً على أخرى حين "
        "تتساوى ملاءمتُهما. وبدونه يَستحيل التعميم من حيث المبدأ.",
    "th_ib_p2": "يدخل هذا التحيُّز عبر: (١) البنية المعمارية (مثل التكافؤ الانتقالي في "
        "الالتفاف)، (٢) هندسة السمات، (٣) تكثير البيانات الذي يُرمِّز الثوابت بالمثال، (٤) "
        "المُحسِّن، الذي يُفضِّل بتنظيمه الضمني حلولًا بعينها، و(٥) دالة الخسارة/الغرامة — إذ "
        "تُفضِّل L2 أوزانًا صغيرةً موزَّعة، وتُفضِّل L1 أوزانًا متفرِّقة.",
    "th_ib_p3": "واختيارُ تحيُّزٍ استقرائيٍّ مُلائمٍ للمسألة كثيرًا ما يفوق في قيمته السَعةَ "
        "الخام أو حجمَ البيانات.",
    "th_ib_eqcap": "<b>شكل.</b> غرامتا L1 وL2 بوصفهما توزيعًا قَبليًّا على الأوزان.",
    "th_ib_call": "التحيُّزُ الاستقرائي الصحيح فرضيةٌ عن العالم، تُدفَع سَلَفًا وتُستردُّ "
        "كفاءةً في البيانات.",

    "th_tl_eyebrow": "انزياح التوزيع · لوح ٠٤",
    "th_tl_p1": "تُدرَّب النماذج على توزيعٍ وتُنشَر على آخر. ويأتي الانزياح بأشكالٍ مُسمّاة: "
        "انزياحُ المُتغيِّر المُرافِق (covariate shift) حيث يتغيّر توزيعُ المُدخلات دون قاعدة "
        "الوسم؛ وانزياحُ المفهوم (concept shift) حيث تتغيّر القاعدةُ نفسها؛ وانزياحُ القَبليِّ "
        "(prior shift) حيث يتغيّر توازنُ الأصناف.",
    "th_tl_p2": "يسعى تكييفُ المجال غير المُوجَّه إلى تمثيلٍ يتشابه فيه المصدرُ والهدف. "
        "والمسافةُ بين توزيعَي السمات هي التباعدُ الأقصى للمتوسّطات (MMD): الفجوةُ بين "
        "متوسّطَي تضمينِهما في فضاء هِلبرت ذي النواة المُعاوِدة للإنتاج، وهي تساوي صفرًا عند "
        "تطابق التوزيعين تمامًا.",
    "th_tl_p3": "وتجعل الشبكةُ الخَصْمية للمجال (DANN) ذلك قابلًا للتعلُّم. يحاول مُصنِّفُ "
        "المجال تمييزَ سمات المصدر من الهدف؛ وتضرب طبقةُ عكس التدرُّج (Gradient Reversal "
        "Layer) تدرُّجَه في −λ في طريقه إلى مُستخرِج السمات، فيُدرَّب المُستخرِجُ على هزيمته — "
        "فتنشأ سماتٌ تحمل إشارةَ الوسم لا إشارةَ المجال.",
    "th_tl_eqcap": "<b>شكل.</b> MMD بين تضمينَي المصدر والهدف.",
    "th_tl_call": "ينجح التكييف حين يَظلُّ المُصنِّفُ قادرًا على قراءة الوسم لكنّه يعجِز عن "
        "معرفة المجال الذي أتى منه.",

    "th_sam_eyebrow": "التحسين · لوح ٠٥",
    "th_sam_p1": "قد تَبلُغ مجموعتا أوزانٍ الخسارةَ التدريبيةَ نفسها ثم تُعمِّمان تعميمًا "
        "شديدَ الاختلاف. تقع الدنيا الصغرى الحادّة (sharp) في قاع وادٍ ضيّق: اضطرابٌ صغيرٌ "
        "في المُعامِلات يرفع الخسارة بحِدّة. وتقع الدنيا الصغرى المُسطَّحة (flat) في حوضٍ "
        "واسع وتحتمل الاضطراب — والدنيا المُسطَّحة تنتقل عادةً انتقالًا أفضلَ إلى بياناتٍ غير "
        "مرئيّة.",
    "th_sam_p2": "لا يُحسِّن التحسينُ الواعي بالحِدّة (SAM) الخسارةَ عند النقطة الراهنة، بل "
        "أسوأَ خسارةٍ ضمن كُرةٍ نصفُ قطرها ρ حولها. فيأخذ أوّلًا خطوةَ صعودٍ نحو أشدِّ نقطةٍ "
        "مجاورةٍ ضررًا، ثم يهبط منها، طالبًا صراحةً جواراتٍ منخفضةً انخفاضًا منتظمًا.",
    "th_sam_p3": "ويُحدِّد المُعامِلُ الفائق ρ نصفَ قطر ذلك الجوار — أي مقدارَ «التسطُّح» الذي "
        "يَفرِضه المُحسِّن.",
    "th_sam_eqcap": "<b>شكل.</b> هدفُ الأدنى–الأقصى في SAM على كُرة ρ.",
    "th_sam_call": "يسأل SGD: «هل هذه النقطة منخفضة؟»؛ ويسأل SAM: «هل هذا الجوار كلُّه "
        "منخفض؟».",

    "th_cz_eyebrow": "الاستدلال السببي · لوح ٠٦",
    "th_cz_p1": "يسأل التنبؤ عمّا يقترن وقوعُه؛ وتسأل السببيةُ عمّا يحدث لو تدخّلنا. "
        "ومفارقةُ سيمبسون هي الإنذار الأوّل: اقترانٌ حاضرٌ في كلِّ مجموعةٍ فرعية قد ينقلب "
        "عند ضمِّ المجموعات، لأنّ مُربِكًا (confounder) يُحرِّك العلاجَ والنتيجةَ معًا.",
    "th_cz_p2": "يَفصِل مُعامِلُ do الرؤيةَ عن الفعل. فـ P(Y∣X) يشترط مشاهدةَ X؛ أمّا "
        "P(Y∣do(X)) فيصف ضبطَ X بالتدخُّل، قاطعًا السهامَ الداخلةَ إليه عادةً. ولا يتطابق "
        "الاثنان إلّا عند انتفاء كلِّ إرباك.",
    "th_cz_p3": "ويمضي الواقعُ المضاد (counterfactual) أبعدَ — ماذا كان سيحدث لهذه الوحدة "
        "لو اختلفت الأمور؟ تُجيب خطواتُ بِرل الثلاث: الاختطاف (abduction) أي تحديثُ الاعتقاد "
        "عن الخلفية الكامنة بناءً على ما رُئي، والفعل (action) أي تطبيقُ التدخُّل الافتراضي على "
        "النموذج، والتنبؤ (prediction) أي قراءةُ النتيجة. وغلافُ ماركوف (Markov blanket) — "
        "آباءُ العقدة وأبناؤها وسائرُ آباء أبنائها — هو المجموعةُ التي تجعلها مستقلّةً عمّا عداها.",
    "th_cz_eqcap": "<b>شكل.</b> التدخُّل يقطع السهامَ الداخلةَ إلى X.",
    "th_cz_call": "الاشتراطُ على مُربِكٍ ليس تعديلًا له؛ ولا يُجيز ادّعاءً سببيًّا إلّا "
        "تدخُّلٌ — حقيقيٌّ أو مُنمذَج.",

    "pr_bv_eyebrow": "تطبيق · عرض ٠١",
    "pr_bv_intro": "لائِم كثيرَ حدودٍ بالدرجة التي تختارها على عيّناتٍ مشوَّشةٍ من دالةٍ "
        "ملساء، وراقِب مفاضلةَ التحيُّز–التباين تنحلُّ آنيًّا. كلُّ رقمٍ أدناه محسوبٌ من "
        "سحباتٍ جديدة — لا شيءَ مُسجَّلٌ سلفًا.",
    "pr_bv_ctrl_degree": "درجة كثير الحدود",
    "pr_bv_ctrl_n": "نقاط التدريب",
    "pr_bv_ctrl_noise": "مستوى الضجيج (σ)",
    "pr_bv_ctrl_seed": "بذرة عشوائية",
    "pr_bv_cap_fit": "<b>شكل ١.</b> ملاءمةٌ واحدة عند الدرجة المختارة. النقاطُ عيّناتُ "
        "تدريبٍ مشوَّشة؛ والمنحنى الفيروزي هو الدالة الحقيقية، والقرمزي هو كثيرُ الحدود "
        "المُلائَم.",
    "pr_bv_cap_err": "<b>شكل ٢.</b> خطأ التدريب مقابل الاختبار عبر الدرجات (مقياسٌ "
        "لوغاريتمي)، مُتوسَّطًا على سحباتٍ كثيرة. يُشير القاعُ إلى السَعة الأفضل تعميمًا.",
    "pr_bv_cap_comp": "<b>شكل ٣.</b> الخطأُ نفسه مُقسَّمًا إلى حصص التحيُّز² والتباين "
        "والضجيج من الكل. يغلب التحيُّز يسارًا والتباين يمينًا.",
    "pr_bv_underfit": "تحيُّزٌ عالٍ — النموذج مفرطُ البساطة ويُعاني نقصَ الملاءمة.",
    "pr_bv_overfit": "تباينٌ عالٍ — النموذج يطارد الضجيج ويُفرِط في الملاءمة.",
    "pr_bv_balanced": "قرب النقطة المُثلى — التحيُّز والتباين متوازنان.",

    "pr_dann_eyebrow": "تطبيق · عرض ٠٢",
    "pr_dann_intro": "يتقاسم المصدرُ والهدفُ قاعدةَ الوسم نفسها، لكنّ الهدف مُدارٌ ومُزاحٌ "
        "— انزياحُ مُتغيِّرٍ مُرافِق. درِّب شبكةً خَصْميةً للمجال وراقِب دقّةَ الهدف تتعافى مع "
        "دفع السمات إلى عدم تعلُّقها بالمجال. وλ شدّةُ طبقة عكس التدرُّج؛ وλ = ٠ هو خطُّ "
        "الأساس المعتمِد على المصدر وحده.",
    "pr_dann_ctrl_lambda": "شدّة الخَصم λ (GRL)",
    "pr_dann_ctrl_seed": "بذرة عشوائية",
    "pr_dann_cap_space": "<b>شكل ١.</b> فضاء المُدخلات: هلالا المصدر (مصمَتان) والهدف "
        "(مُفرَّغان)، مع حدّ القرار المُتعلَّم.",
    "pr_dann_cap_feat": "<b>شكل ٢.</b> السماتُ المُتعلَّمة مُسقَطةً إلى بُعدين (PCA). "
        "يَجذِب التكييفُ سحابتَي المجالين إحداهما نحو الأخرى.",
    "pr_dann_baseline": "التكييف مُعطَّل — هذا هو خطُّ الأساس المعتمِد على المصدر وحده.",
    "pr_dann_adapt": "التكييف فعّال — يُدفَع مُستخرِجُ السمات نحو إرباك مُصنِّف المجال.",
    "pr_dann_training": "يجري تدريبُ الشبكة الخَصْمية للمجال…",

    "pr_sam_eyebrow": "تطبيق · عرض ٠٣",
    "pr_sam_intro": "سطحُ خسارةٍ فيه دنيا صغرى محلّية ضيّقة وعميقة، ودنيا صغرى عامّة واسعة. "
        "يهبط SGD على الخسارة الحقيقية؛ ويهبط SAM على أسوأ خسارةٍ ضمن كُرة ρ. زِد ρ لترى "
        "SAM يكفُّ عن تفضيل الفخّ الحادّ ويستقرّ في الحوض المُسطَّح المُعمِّم.",
    "pr_sam_ctrl_rho": "نصف قطر الجوار ρ",
    "pr_sam_cap_true": "<b>شكل ١.</b> سطحُ الخسارة الحقيقي L(w). البئرُ الضيّق يسارًا هو "
        "الدنيا الحادّة، والبئرُ الواسع هو المُسطَّح.",
    "pr_sam_cap_eff": "<b>شكل ٢.</b> سطحُ أسوأ الحالات E(w) = max₍‖ε‖≤ρ₎ L(w+ε) الذي "
        "يُصغِّره SAM فعلًا. يمتلئ البئرُ الحادّ كلّما كبُر ρ.",
    "pr_sam_cap_traj": "<b>شكل ٣.</b> مسارا الهبوط من البداية نفسها. يتبع SGD المنحنى L، "
        "ويتبع SAM المنحنى E.",
    "pr_sam_flat": "عند هذا ρ يَبلُغ SAM الحوضَ المُسطَّح (المُعمِّم).",
    "pr_sam_sharp": "عند هذا ρ ما يزال SAM يستقرّ في الحوض الحادّ — زِد ρ للإفلات منه.",

    "pr_simpson_eyebrow": "تطبيق · عرض ٠٤",
    "pr_simpson_intro": "علاجٌ يفوز في كلِّ مجموعةِ شدّةٍ قد يخسر في المجاميع الكلّية إذا "
        "اقترن التخصيصُ بالشدّة. حرِّك انحرافَ التخصيص وراقِب المفارقة تَشتعِل.",
    "pr_simpson_ctrl_skew": "انحراف التخصيص (الشدّة ← العلاج)",
    "pr_simpson_cap_groups": "<b>شكل ١.</b> معدّلات التعافي داخل كلِّ مجموعة. يتفوّق العلاج "
        "B (فيروزي) على A (قرمزي) في الحالتين الخفيفة والشديدة.",
    "pr_simpson_cap_agg": "<b>شكل ٢.</b> معدّلات التعافي المُجمَّعة. بعد عَتَبة الانحراف "
        "يتجاوز A العلاجَ B — الانقلاب.",
    "pr_simpson_cap_curve": "<b>شكل ٣.</b> المعدّلات المُجمَّعة مقابل الانحراف؛ يُحدِّد "
        "الخطُّ المتقطِّع موضعَ ظهور المفارقة.",
    "pr_simpson_cap_dag": "<b>شكل ٤.</b> مثلّث الإرباك. الشدّةُ تُسبِّب تخصيصَ العلاج "
        "والنتيجةَ معًا.",
    "pr_simpson_on": "مفارقةُ سيمبسون حاضرة: B أفضلُ في كلِّ مجموعة، ومع ذلك A أفضلُ إجمالًا.",
    "pr_simpson_off": "لا مفارقةَ عند هذا الانحراف: تتّفق المقارنةُ المُجمَّعة مع المجموعات "
        "الفرعية.",

    "pr_cf_eyebrow": "تطبيق · عرض ٠٥",
    "pr_cf_intro": "نموذجٌ بنيويٌّ بثلاثة أنواعٍ كامنةٍ من الزبائن يُجيب سؤالًا مضادًّا "
        "للواقع: إذا عَلِمنا أنّ زبونًا رأى الإعلانَ وظلَّ غيرَ راضٍ، فما احتمالُ أن يكون "
        "راضيًا لو لم نَعرِض الإعلان؟ اضبط القَبليَّ والمشاهدةَ والتدخُّل؛ وتُتعقَّب الخطواتُ "
        "الثلاث بدقّة.",
    "pr_cf_ctrl_phater": "P(النوع النافر)",
    "pr_cf_ctrl_psad": "P(النوع الدائم الحزن)",
    "pr_cf_ctrl_tobs": "العلاج المُشاهَد T",
    "pr_cf_ctrl_yobs": "النتيجة المُشاهَدة Y",
    "pr_cf_ctrl_tdo": "المضاد للواقع do(T)",
    "pr_cf_step_abduction": "الاختطاف — إعادةُ وزن الأنواع الكامنة إلى ما كان يمكنه إنتاجُ "
        "المشاهدة.",
    "pr_cf_step_action": "الفعل — استبدالُ العلاج بالتدخُّل مع تثبيت النوع الكامن.",
    "pr_cf_step_prediction": "التنبؤ — قراءةُ توزيع النتيجة تحت التدخُّل.",
    "pr_cf_cap_post": "<b>شكل ١.</b> القَبليُّ مقابل البَعديِّ على الأنواع الكامنة بعد "
        "الاختطاف.",
    "pr_cf_cap_table": "<b>شكل ٢.</b> الاستجابةُ البنيوية لكلِّ نوعٍ للعلاجَين T = ٠ وT = ١.",
    "pr_cf_cap_scm": "<b>شكل ٣.</b> النموذج البنيوي: النوعُ الكامن U والعلاجُ T يُحدِّدان "
        "معًا النتيجةَ Y.",
    "pr_cf_impossible": "هذه المشاهدةُ مستحيلةٌ في النموذج الراهن — لا نوعَ كامنٌ يُنتِجها. "
        "غيِّر المشاهدة أو القَبليَّ.",
    "pr_cf_headline": "الاحتمالُ المضادُّ للواقع لنتيجةٍ راضية",
    "pr_cf_responder": "مُستجيب",
    "pr_cf_hater": "نافر",
    "pr_cf_always_sad": "دائم الحزن",

    # ---- theme + byline + assistant ----
    "theme_label": "السمة",
    "theme_light": "فاتح",
    "theme_dark": "داكن",
    "theme_colored": "ملوّن",
    "byline_supervisor": "المشرف",
    "byline_author": "إعداد",
    "name_supervisor": "Dr. Behrouz Minaei-Bidgoli",
    "name_author": "Hani Akram Mahfoud",
    "assistant_label": "اسألني",
}


LANG_DICT: dict[str, dict[str, str]] = {"en": EN, "fa": FA, "ar": AR}

# Merge Section II (XAI) strings, kept in a companion module for readability.
from i18n_xai import EN2, FA2, AR2  # noqa: E402
EN.update(EN2)
FA.update(FA2)
AR.update(AR2)

# Merge Section III (Fairness) strings.
from i18n_fair import EN3, FA3, AR3  # noqa: E402
EN.update(EN3)
FA.update(FA3)
AR.update(AR3)

# Merge Section IV (Robustness) strings.
from i18n_robust import EN4, FA4, AR4  # noqa: E402
EN.update(EN4)
FA.update(FA4)
AR.update(AR4)

# Merge Section V (Privacy) strings.
from i18n_privacy import EN5, FA5, AR5  # noqa: E402
EN.update(EN5)
FA.update(FA5)
AR.update(AR5)

# Merge Section VI (Alignment) strings.
from i18n_align import EN6, FA6, AR6  # noqa: E402
EN.update(EN6)
FA.update(FA6)
AR.update(AR6)

# Merge UI-overhaul chrome strings (hero, roadmap, section cards).
from i18n_ui import EN_UI, FA_UI, AR_UI  # noqa: E402
EN.update(EN_UI)
FA.update(FA_UI)
AR.update(AR_UI)


def t(lang: str, key: str) -> str:
    """Translate ``key`` into ``lang``, falling back to English then the key."""
    table = LANG_DICT.get(lang, EN)
    if key in table:
        return table[key]
    return EN.get(key, key)
