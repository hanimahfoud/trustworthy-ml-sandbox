"""
i18n_xai.py -- Section II (Explainability / XAI) strings, merged into the main
LANG_DICT by i18n.py. Same conventions as Section I: English is the base,
equations live in the modules, chart series/tags stay in English.
"""
from __future__ import annotations

# =========================================================================== #
# ENGLISH                                                                     #
# =========================================================================== #
EN2 = {
    # ---- section + nav chrome ----
    "section_label": "Section",
    "sec1_title": "I · Generalization",
    "sec2_title": "II · Explainability",
    "masthead_subtitle_2": "An interactive companion to interpretability and "
        "explainability — glass-box vs black-box models, LIME and SHAP, causal "
        "recourse, and the saliency of a convolutional network — computed live.",
    "colophon_2b": "Section II · Transparency & Explainability (XAI)",

    # ---- theory nav titles ----
    "xai_interp": "Interpretability vs Explainability",
    "xai_black": "The Black-Box Problem",
    "xai_tab": "LIME & SHAP",
    "xai_recourse": "Recourse & Counterfactuals",
    "xai_cv": "Vision XAI: Grad-CAM",
    "xai_vlm": "Vision-Language Models",

    # ---- practice nav titles ----
    "px_loan": "LIME vs SHAP · Loan",
    "px_recourse": "Causal Recourse",
    "px_cv": "Vision XAI Scanner",
    "px_spurious": "Spurious-Correlation Detector",

    # ===================== THEORY =====================
    # 1) Interpretability vs Explainability
    "xai_interp_eyebrow": "Transparency · Plate 01",
    "xai_interp_p1": "Models divide by transparency. A <em>glass box</em> is "
        "interpretable by construction: linear regression exposes a weight per "
        "feature, a decision tree a path from root to leaf. Its question is "
        "<em>how</em> the model works.",
    "xai_interp_p2": "A <em>black box</em> — a deep network, a random forest — is "
        "opaque; we cannot read its internal logic, so we attach <em>post-hoc</em> "
        "methods that justify individual decisions. Its question is <em>why</em> "
        "this particular output was produced.",
    "xai_interp_p3": "Interpretability is a property of the model; explainability "
        "is a technique applied to it. The rest of this section is mostly about the "
        "second, because the most accurate models are usually the least transparent.",
    "xai_interp_eqcap": "<b>Figure.</b> A glass-box linear model exposes one "
        "weight per feature.",
    "xai_interp_call": "Accuracy and transparency pull in opposite directions; "
        "explainability is how we recover trust without giving up the accurate model.",

    # 2) The black-box problem
    "xai_black_eyebrow": "Transparency · Plate 02",
    "xai_black_p1": "Why explain at all? Because a confident, accurate model can be "
        "right for the wrong reason. <em>Spurious correlations</em>: a classifier "
        "may read a chest X-ray from a metal tag left by one hospital's equipment "
        "rather than from the pathology.",
    "xai_black_p2": "<em>Shortcuts</em>: a network may label a photo “whale” because "
        "it memorized that a blue background means water, not because it learned the "
        "animal. On new data where the shortcut breaks, the model fails silently.",
    "xai_black_p3": "Explanation is the instrument that catches this: it shows "
        "<em>where</em> the evidence came from, so a shortcut becomes visible before "
        "deployment rather than after a costly mistake.",
    "xai_black_eqcap": "<b>Figure.</b> A model can attend to the background cue "
        "instead of the object.",
    "xai_black_call": "A correct prediction from the wrong evidence is a failure "
        "waiting for the distribution to shift.",

    # 3) LIME & SHAP
    "xai_tab_eyebrow": "Tabular XAI · Plate 03",
    "xai_tab_p1": "<em>LIME</em> explains one prediction locally: it perturbs the "
        "instance, labels the perturbations with the black box, weights them by "
        "proximity, and fits a simple linear surrogate. Its coefficients are the "
        "local attributions — reliable only in a small neighborhood.",
    "xai_tab_p2": "<em>SHAP</em> is grounded in game theory. Each feature is a "
        "player; its Shapley value is its average marginal contribution across all "
        "coalitions of features. Uniquely, the attributions are additive: they sum "
        "exactly to the gap between the prediction and the base value.",
    "xai_tab_p3": "Variants trade generality for speed: Kernel SHAP (any model, by "
        "sampling), Tree SHAP (exact and fast for trees), Deep SHAP (networks, via "
        "backprop).",
    "xai_tab_eqcap": "<b>Figure.</b> The Shapley value averages marginal "
        "contributions over coalitions; SHAP attributions are additive.",
    "xai_tab_call": "LIME asks what a local linear model would say; SHAP asks what "
        "each feature is worth, and guarantees the parts sum to the whole.",

    # 4) Recourse
    "xai_recourse_eyebrow": "Actionability · Plate 04",
    "xai_recourse_p1": "A counterfactual explanation tells a rejected applicant what "
        "to change to be accepted (“raise income by 15%”). <em>Recourse</em> sharpens "
        "this with two constraints that make the advice usable.",
    "xai_recourse_p2": "First, <em>cost</em>: moving income from $0 to $100 is far "
        "harder than $800 to $900, and the recommendation should minimize real "
        "effort. Second, <em>causality</em>: if income is a cause of savings, raising "
        "income raises savings for free — so the cheapest plan acts on the parent, "
        "not on every symptom, and never proposes the impossible.",
    "xai_recourse_p3": "Recourse is thus a constrained optimization over the causal "
        "model: the least-cost, feasible, causally-consistent change that flips the "
        "decision.",
    "xai_recourse_eqcap": "<b>Figure.</b> Minimum-cost actionable change subject to "
        "the causal structure.",
    "xai_recourse_call": "Good recourse respects both the wallet and the causal "
        "graph: cheapest to do, and possible to do.",

    # 5) Vision XAI
    "xai_cv_eyebrow": "Computer Vision · Plate 05",
    "xai_cv_p1": "How does a vision model “see”? <em>Saliency maps</em> take the "
        "gradient of the class score with respect to each input pixel: the pixels "
        "whose small change most moves the score are the ones the model relied on.",
    "xai_cv_p2": "<em>CAM</em> requires a Global Average Pooling head and reads the "
        "class weights over feature maps. <em>Grad-CAM</em> removes that "
        "architectural constraint: it weights each feature map by the average "
        "gradient of the class score flowing into it, then keeps the positive part "
        "— a coarse heatmap of “where the class evidence is.”",
    "xai_cv_p3": "<em>Guided Grad-CAM</em> multiplies the coarse Grad-CAM by a "
        "guided-backprop saliency map to recover crisp, pixel-level detail. "
        "<em>Feature visualization</em> asks the dual question: which synthetic "
        "input maximally excites a chosen neuron?",
    "xai_cv_eqcap": "<b>Figure.</b> Grad-CAM weights feature maps by the pooled "
        "gradient of the class score.",
    "xai_cv_call": "Grad-CAM turns the gradient that trained the network into a map "
        "of what it looked at.",

    # 6) Vision-Language Models
    "xai_vlm_eyebrow": "Multimodal · Plate 06",
    "xai_vlm_p1": "Models that fuse text and image expose a new handle: "
        "<em>cross-modal attention</em>. It reveals how a text token (say “dog”) "
        "attends to a region of the image, aligning language with pixels.",
    "xai_vlm_p2": "Attention in one layer is not the whole story. <em>Attention "
        "rollout</em> multiplies the (residual-augmented) attention matrices across "
        "layers to trace influence from output back to input; <em>LRP</em> "
        "(Layer-wise Relevance Propagation) redistributes the decision's relevance "
        "backward through the network to the inputs.",
    "xai_vlm_p3": "Together these turn a transformer's opaque stack into a legible "
        "chain of evidence from a word to the patch that justified it.",
    "xai_vlm_eqcap": "<b>Figure.</b> Attention rollout composes attention across "
        "layers to link tokens to image patches.",
    "xai_vlm_call": "In multimodal models the explanation is a bridge: which words "
        "looked at which pixels.",

    # ===================== PRACTICE =====================
    # px_loan (LIME vs SHAP dashboard)
    "px_loan_eyebrow": "Practice · Demo 06",
    "px_loan_intro": "A real RandomForest decides a loan. Enter an applicant and "
        "explain the decision two ways at once: LIME's local linear surrogate and "
        "exact Shapley values. Every bar is computed live from the same trained "
        "model — nothing is scripted.",
    "px_loan_age": "Age",
    "px_loan_income": "Monthly income ($)",
    "px_loan_debt": "Debt ($)",
    "px_loan_savings": "Savings ($)",
    "px_loan_home": "Owns home",
    "px_loan_decision_approved": "Loan decision: APPROVED",
    "px_loan_decision_rejected": "Loan decision: REJECTED",
    "px_loan_cap_lime": "<b>Figure 1. LIME.</b> Local linear attributions — how "
        "each feature pushes this single decision (crimson = toward rejection, teal "
        "= toward approval).",
    "px_loan_cap_shap": "<b>Figure 2. SHAP.</b> Exact Shapley force plot from the "
        "base rate to this prediction; contributions are additive.",
    "px_loan_note": "LIME and SHAP usually agree on the sign and rough order of the "
        "drivers, but SHAP's parts sum exactly to the output while LIME is a local "
        "approximation.",

    # px_recourse
    "px_recourse_eyebrow": "Practice · Demo 07",
    "px_recourse_intro": "For a rejected applicant, compare a naive counterfactual "
        "with causal recourse. Because income causes savings, the causal plan "
        "reaches the same approved outcome while paying only for the income change.",
    "px_recourse_cap_bars": "<b>Figure 1.</b> Cost of each plan in standardized "
        "effort units. The causal plan is cheaper by exactly the savings it gets "
        "for free.",
    "px_recourse_cap_dag": "<b>Figure 2.</b> The structural edge the causal plan "
        "exploits: income is a parent of savings.",
    "px_recourse_normal": "Naive plan: change income AND savings independently.",
    "px_recourse_causal": "Causal recourse: change income only — savings follows.",
    "px_recourse_infeasible": "No feasible recourse within reach — the applicant is "
        "already approved, or no bounded change flips the model.",

    # px_cv (scanner)
    "px_cv_eyebrow": "Practice · Demo 08",
    "px_cv_intro": "A convolutional network — built and trained from scratch in "
        "NumPy — classifies a shape. Pick a sample and an attribution method and see "
        "exactly which pixels drove the decision. The gradients are the real "
        "gradients of the trained network.",
    "px_cv_method": "Attribution method",
    "px_cv_sample": "Sample image",
    "px_cv_target": "Target class",
    "px_cv_cap_input": "<b>Figure 1.</b> The input image.",
    "px_cv_cap_map": "<b>Figure 2.</b> {method} for the target class, overlaid on "
        "the image.",
    "px_cv_m_gradcam": "Grad-CAM",
    "px_cv_m_saliency": "Saliency",
    "px_cv_m_guided": "Guided Grad-CAM",
    "px_cv_class0": "Circle",
    "px_cv_class1": "Square",
    "px_cv_pred": "The network predicts",

    # px_spurious
    "px_spurious_eyebrow": "Practice · Demo 09",
    "px_spurious_intro": "Two networks classify the same shapes. One saw clean data; "
        "the other saw data where a bright bottom band always accompanied one class. "
        "Grad-CAM reveals which network learned the object and which learned the "
        "shortcut.",
    "px_spurious_cap_clean": "<b>Figure 1. Honest model.</b> Grad-CAM concentrates "
        "on the object itself.",
    "px_spurious_cap_short": "<b>Figure 2. Shortcut model.</b> Grad-CAM lights up "
        "the background band, not the shape.",
    "px_spurious_energy_clean": "Object attention (clean model)",
    "px_spurious_energy_short": "Band attention (shortcut model)",
    "px_spurious_warn": "Warning: the shortcut model is right for the wrong reason. "
        "It did not learn the shape — it memorized that the band means this class. "
        "This is a black box that will fail the moment the band disappears.",

    # ---- PDF export ----
    "pdf_button": "PDF",
    "pdf_prep": "Preparing the document…",
    "pdf_theory_heading": "Theory",
    "pdf_practice_heading": "Practice",
    "pdf_generated": "Generated from the Trustworthy ML sandbox",
}


# =========================================================================== #
# PERSIAN                                                                      #
# =========================================================================== #
FA2 = {
    "section_label": "بخش",
    "sec1_title": "۱ · تعمیم‌پذیری",
    "sec2_title": "۲ · تفسیرپذیری",
    "masthead_subtitle_2": "همراهی تعاملی برای تفسیرپذیری و توضیح‌پذیری — مدل‌های "
        "جعبه‌شیشه‌ای در برابر جعبه‌سیاه، LIME و SHAP، جبرانِ علّی، و برجستگیِ یک شبکهٔ "
        "کانولوشنی — که زنده محاسبه می‌کند.",
    "colophon_2b": "بخشِ دوم · شفافیت و توضیح‌پذیری (XAI)",

    "xai_interp": "تفسیرپذیری در برابر توضیح‌پذیری",
    "xai_black": "مسئلهٔ جعبه‌سیاه",
    "xai_tab": "LIME و SHAP",
    "xai_recourse": "جبران و ضدواقع‌ها",
    "xai_cv": "تفسیرِ بینایی: Grad-CAM",
    "xai_vlm": "مدل‌های زبانی-بصری",

    "px_loan": "LIME در برابر SHAP · وام",
    "px_recourse": "جبرانِ علّی",
    "px_cv": "پویشگرِ تفسیرِ بینایی",
    "px_spurious": "آشکارسازِ همبستگیِ کاذب",

    "xai_interp_eyebrow": "شفافیت · لوح ۰۱",
    "xai_interp_p1": "مدل‌ها بر پایهٔ شفافیت تقسیم می‌شوند. یک <em>جعبهٔ شیشه‌ای</em> "
        "ذاتاً تفسیرپذیر است: رگرسیونِ خطی برای هر ویژگی یک وزن آشکار می‌کند و درختِ "
        "تصمیم مسیری از ریشه تا برگ. پرسشِ آن این است که مدل <em>چگونه</em> کار می‌کند.",
    "xai_interp_p2": "یک <em>جعبهٔ سیاه</em> — شبکهٔ عمیق یا جنگلِ تصادفی — کدر است؛ "
        "منطقِ درونی‌اش خوانده نمی‌شود، پس روش‌های <em>پس‌ازوقوع</em> را به آن می‌افزاییم "
        "تا تصمیم‌های منفرد را توجیه کنند. پرسشِ آن این است که <em>چرا</em> این خروجی "
        "پدید آمد.",
    "xai_interp_p3": "تفسیرپذیری خاصیتی از خودِ مدل است و توضیح‌پذیری تکنیکی که بر آن "
        "اعمال می‌شود. باقیِ این بخش عمدتاً دربارهٔ دومی است، زیرا دقیق‌ترین مدل‌ها معمولاً "
        "کم‌شفاف‌ترین‌اند.",
    "xai_interp_eqcap": "<b>شکل.</b> مدلِ خطیِ جعبه‌شیشه‌ای برای هر ویژگی یک وزن آشکار "
        "می‌کند.",
    "xai_interp_call": "دقت و شفافیت در دو جهتِ مخالف می‌کشند؛ توضیح‌پذیری راهی است "
        "برای بازیابیِ اعتماد بی‌آنکه مدلِ دقیق را رها کنیم.",

    "xai_black_eyebrow": "شفافیت · لوح ۰۲",
    "xai_black_p1": "چرا اصلاً توضیح؟ چون مدلی مطمئن و دقیق می‌تواند به دلیلِ نادرست "
        "درست باشد. <em>همبستگی‌های کاذب</em>: یک طبقه‌بند ممکن است تصویرِ اشعهٔ ایکس را "
        "از رویِ برچسبِ فلزیِ تجهیزاتِ یک بیمارستان بخواند، نه از رویِ آسیب‌شناسی.",
    "xai_black_p2": "<em>میان‌بُرها</em>: شبکه ممکن است عکسی را «نهنگ» برچسب بزند چون "
        "حفظ کرده که پس‌زمینهٔ آبی یعنی آب، نه چون شکلِ جانور را آموخته. روی داده‌ای که "
        "میان‌بُر می‌شکند، مدل خاموش شکست می‌خورد.",
    "xai_black_p3": "توضیح ابزاری است که این را می‌گیرد: نشان می‌دهد شاهد <em>از کجا</em> "
        "آمده، تا میان‌بُر پیش از استقرار دیده شود نه پس از خطایی پرهزینه.",
    "xai_black_eqcap": "<b>شکل.</b> مدل می‌تواند به‌جای شیء به نشانهٔ پس‌زمینه توجه کند.",
    "xai_black_call": "پیش‌بینیِ درست از شاهدِ نادرست، شکستی است در انتظارِ تغییرِ توزیع.",

    "xai_tab_eyebrow": "تفسیرِ جدولی · لوح ۰۳",
    "xai_tab_p1": "<em>LIME</em> یک پیش‌بینی را محلی توضیح می‌دهد: نمونه را آشفته "
        "می‌کند، آشفته‌ها را با جعبهٔ سیاه برچسب می‌زند، بر پایهٔ نزدیکی وزن می‌دهد و یک "
        "جانشینِ خطیِ ساده برازش می‌کند. ضرایبش نسبت‌دهیِ محلی‌اند — تنها در همسایگیِ کوچک "
        "معتبر.",
    "xai_tab_p2": "<em>SHAP</em> بر نظریهٔ بازی‌ها استوار است. هر ویژگی یک بازیکن است؛ "
        "مقدارِ شپلیِ آن میانگینِ مشارکتِ حاشیه‌ای‌اش در همهٔ ائتلاف‌هاست. به‌طور یکتا، "
        "نسبت‌دهی‌ها جمع‌پذیرند: دقیقاً برابرِ فاصلهٔ میانِ پیش‌بینی و مقدارِ پایه جمع می‌شوند.",
    "xai_tab_p3": "گونه‌ها عمومیت را با سرعت معاوضه می‌کنند: Kernel SHAP (هر مدل، با "
        "نمونه‌گیری)، Tree SHAP (دقیق و سریع برای درخت‌ها)، Deep SHAP (شبکه‌ها، با پس‌انتشار).",
    "xai_tab_eqcap": "<b>شکل.</b> مقدارِ شپلی میانگینِ مشارکت‌های حاشیه‌ای روی ائتلاف‌هاست؛ "
        "نسبت‌دهی‌های SHAP جمع‌پذیرند.",
    "xai_tab_call": "LIME می‌پرسد یک مدلِ خطیِ محلی چه می‌گوید؛ SHAP می‌پرسد هر ویژگی چقدر "
        "می‌ارزد و تضمین می‌کند که اجزا با کل برابرند.",

    "xai_recourse_eyebrow": "کنش‌پذیری · لوح ۰۴",
    "xai_recourse_p1": "یک توضیحِ ضدواقع به متقاضیِ رَدشده می‌گوید چه تغییر دهد تا پذیرفته "
        "شود («درآمد را ۱۵٪ افزایش بده»). <em>جبران (Recourse)</em> این را با دو قید "
        "تیزتر می‌کند که توصیه را کاربردی می‌سازند.",
    "xai_recourse_p2": "نخست، <em>هزینه</em>: بردنِ درآمد از ۰ به ۱۰۰ بسیار سخت‌تر از ۸۰۰ "
        "به ۹۰۰ است، و توصیه باید تلاشِ واقعی را کمینه کند. دوم، <em>علّیت</em>: اگر درآمد "
        "علتِ پس‌انداز باشد، افزایشِ درآمد پس‌انداز را رایگان بالا می‌برد — پس ارزان‌ترین "
        "نقشه بر والد اثر می‌گذارد نه بر هر نشانه، و هرگز ناممکن را پیشنهاد نمی‌کند.",
    "xai_recourse_p3": "پس جبران یک بهینه‌سازیِ مقیّد روی مدلِ علّی است: کم‌هزینه‌ترین "
        "تغییرِ شدنی و سازگار با علّیت که تصمیم را برمی‌گرداند.",
    "xai_recourse_eqcap": "<b>شکل.</b> کم‌هزینه‌ترین تغییرِ کنش‌پذیر با قیدِ ساختارِ علّی.",
    "xai_recourse_call": "جبرانِ خوب هم به جیب احترام می‌گذارد هم به گرافِ علّی: "
        "ارزان‌ترین و شدنی‌ترین کار.",

    "xai_cv_eyebrow": "بینایی ماشین · لوح ۰۵",
    "xai_cv_p1": "یک مدلِ بینایی چگونه «می‌بیند»؟ <em>نقشه‌های برجستگی</em> گرادیانِ امتیازِ "
        "کلاس را نسبت به هر پیکسلِ ورودی می‌گیرند: پیکسل‌هایی که تغییرِ کوچکشان بیشترین "
        "اثر را بر امتیاز دارد، همان‌هایی‌اند که مدل به آن‌ها تکیه کرده است.",
    "xai_cv_p2": "<em>CAM</em> به یک سرِ میانگین‌گیریِ سراسری (GAP) نیاز دارد و وزن‌های "
        "کلاس روی نقشه‌های ویژگی را می‌خواند. <em>Grad-CAM</em> این قیدِ معماری را برمی‌دارد: "
        "هر نقشهٔ ویژگی را با میانگینِ گرادیانِ امتیازِ کلاس که به آن وارد می‌شود وزن می‌دهد "
        "و سپس بخشِ مثبت را نگه می‌دارد — نقشهٔ حرارتیِ درشتی از «کجا شاهدِ کلاس است».",
    "xai_cv_p3": "<em>Guided Grad-CAM</em> نقشهٔ درشتِ Grad-CAM را در برجستگیِ "
        "پس‌انتشارِ هدایت‌شده ضرب می‌کند تا جزئیاتِ تیزِ پیکسلی بازیابی شود. <em>تجسمِ "
        "ویژگی</em> پرسشِ دوگان را می‌پرسد: کدام ورودیِ ترکیبی یک نورونِ خاص را بیشینه "
        "برمی‌انگیزد؟",
    "xai_cv_eqcap": "<b>شکل.</b> Grad-CAM نقشه‌های ویژگی را با گرادیانِ تجمیع‌شدهٔ امتیازِ "
        "کلاس وزن می‌دهد.",
    "xai_cv_call": "Grad-CAM همان گرادیانی را که شبکه را آموزش داد به نقشه‌ای از آنچه "
        "نگریسته بدل می‌کند.",

    "xai_vlm_eyebrow": "چندوجهی · لوح ۰۶",
    "xai_vlm_p1": "مدل‌هایی که متن و تصویر را می‌آمیزند دستگیرهٔ تازه‌ای آشکار می‌کنند: "
        "<em>توجهِ میان‌وجهی</em>. نشان می‌دهد یک توکنِ متنی (مثلاً «سگ») چگونه به ناحیه‌ای "
        "از تصویر توجه می‌کند و زبان را با پیکسل‌ها هم‌تراز می‌سازد.",
    "xai_vlm_p2": "توجه در یک لایه همهٔ داستان نیست. <em>Attention Rollout</em> ماتریس‌های "
        "توجهِ (تقویت‌شده با پیوندِ باقیمانده) را در طولِ لایه‌ها ضرب می‌کند تا اثر را از "
        "خروجی به ورودی ردگیری کند؛ <em>LRP</em> ربطِ تصمیم را روبه‌عقب در شبکه تا ورودی‌ها "
        "بازتوزیع می‌کند.",
    "xai_vlm_p3": "این‌ها با هم انبوهٔ کدرِ ترانسفورمر را به زنجیره‌ای خوانا از شاهد بدل "
        "می‌کنند — از یک واژه تا وصله‌ای که آن را توجیه کرد.",
    "xai_vlm_eqcap": "<b>شکل.</b> Attention Rollout توجه را در طولِ لایه‌ها ترکیب می‌کند تا "
        "توکن‌ها را به وصله‌های تصویر پیوند دهد.",
    "xai_vlm_call": "در مدل‌های چندوجهی، توضیح یک پل است: کدام واژه‌ها به کدام پیکسل‌ها "
        "نگریستند.",

    "px_loan_eyebrow": "تمرین · نمایشِ ۰۶",
    "px_loan_intro": "یک جنگلِ تصادفیِ واقعی دربارهٔ وام تصمیم می‌گیرد. یک متقاضی وارد "
        "کنید و تصمیم را هم‌زمان به دو روش توضیح دهید: جانشینِ خطیِ محلیِ LIME و مقادیرِ "
        "دقیقِ شپلی. هر میله زنده از همان مدلِ آموخته محاسبه می‌شود — هیچ‌چیز از پیش‌نوشته "
        "نیست.",
    "px_loan_age": "سن",
    "px_loan_income": "درآمدِ ماهانه ($)",
    "px_loan_debt": "بدهی ($)",
    "px_loan_savings": "پس‌انداز ($)",
    "px_loan_home": "مالکِ خانه",
    "px_loan_decision_approved": "تصمیمِ وام: پذیرفته شد",
    "px_loan_decision_rejected": "تصمیمِ وام: رَد شد",
    "px_loan_cap_lime": "<b>شکل ۱. LIME.</b> نسبت‌دهیِ خطیِ محلی — هر ویژگی این تصمیمِ "
        "واحد را چگونه می‌راند (زرشکی = به‌سوی رَد، فیروزه‌ای = به‌سوی پذیرش).",
    "px_loan_cap_shap": "<b>شکل ۲. SHAP.</b> نمودارِ نیرویِ شپلیِ دقیق از نرخِ پایه تا این "
        "پیش‌بینی؛ مشارکت‌ها جمع‌پذیرند.",
    "px_loan_note": "LIME و SHAP معمولاً بر علامت و ترتیبِ تقریبیِ محرک‌ها هم‌داستان‌اند، "
        "اما اجزای SHAP دقیقاً با خروجی جمع می‌شوند حال آنکه LIME تقریبی محلی است.",

    "px_recourse_eyebrow": "تمرین · نمایشِ ۰۷",
    "px_recourse_intro": "برای متقاضیِ رَدشده، یک ضدواقعِ ساده‌لوح را با جبرانِ علّی "
        "مقایسه کنید. چون درآمد علتِ پس‌انداز است، نقشهٔ علّی به همان نتیجهٔ پذیرفته‌شده "
        "می‌رسد در حالی‌که فقط بهایِ تغییرِ درآمد را می‌پردازد.",
    "px_recourse_cap_bars": "<b>شکل ۱.</b> هزینهٔ هر نقشه در واحدهای استانداردِ تلاش. "
        "نقشهٔ علّی دقیقاً به اندازهٔ پس‌اندازی که رایگان می‌گیرد ارزان‌تر است.",
    "px_recourse_cap_dag": "<b>شکل ۲.</b> یالِ ساختاری‌ای که نقشهٔ علّی از آن بهره می‌برد: "
        "درآمد والدِ پس‌انداز است.",
    "px_recourse_normal": "نقشهٔ ساده‌لوح: درآمد و پس‌انداز را مستقل تغییر بده.",
    "px_recourse_causal": "جبرانِ علّی: فقط درآمد را تغییر بده — پس‌انداز دنبال می‌کند.",
    "px_recourse_infeasible": "جبرانِ شدنی در دسترس نیست — یا متقاضی همین حالا پذیرفته "
        "است یا هیچ تغییرِ کران‌دار مدل را برنمی‌گرداند.",

    "px_cv_eyebrow": "تمرین · نمایشِ ۰۸",
    "px_cv_intro": "یک شبکهٔ کانولوشنی — که از صفر با NumPy ساخته و آموزش داده شده — یک "
        "شکل را طبقه‌بندی می‌کند. یک نمونه و یک روشِ نسبت‌دهی برگزینید و ببینید دقیقاً کدام "
        "پیکسل‌ها تصمیم را راندند. گرادیان‌ها گرادیان‌های واقعیِ شبکهٔ آموخته‌اند.",
    "px_cv_method": "روشِ نسبت‌دهی",
    "px_cv_sample": "تصویرِ نمونه",
    "px_cv_target": "کلاسِ هدف",
    "px_cv_cap_input": "<b>شکل ۱.</b> تصویرِ ورودی.",
    "px_cv_cap_map": "<b>شکل ۲.</b> {method} برای کلاسِ هدف، روی تصویر هم‌پوشانده.",
    "px_cv_m_gradcam": "Grad-CAM",
    "px_cv_m_saliency": "برجستگی",
    "px_cv_m_guided": "Guided Grad-CAM",
    "px_cv_class0": "دایره",
    "px_cv_class1": "مربع",
    "px_cv_pred": "شبکه پیش‌بینی می‌کند",

    "px_spurious_eyebrow": "تمرین · نمایشِ ۰۹",
    "px_spurious_intro": "دو شبکه همان شکل‌ها را طبقه‌بندی می‌کنند. یکی داده‌های پاک دید؛ "
        "دیگری داده‌ای که در آن یک نوارِ روشنِ پایینی همیشه همراهِ یک کلاس بود. Grad-CAM "
        "آشکار می‌کند کدام شبکه شیء را آموخت و کدام میان‌بُر را.",
    "px_spurious_cap_clean": "<b>شکل ۱. مدلِ صادق.</b> Grad-CAM بر خودِ شیء متمرکز می‌شود.",
    "px_spurious_cap_short": "<b>شکل ۲. مدلِ میان‌بُر.</b> Grad-CAM نوارِ پس‌زمینه را "
        "روشن می‌کند نه شکل را.",
    "px_spurious_energy_clean": "توجه به شیء (مدلِ پاک)",
    "px_spurious_energy_short": "توجه به نوار (مدلِ میان‌بُر)",
    "px_spurious_warn": "هشدار: مدلِ میان‌بُر به دلیلِ نادرست درست است. شکل را نیاموخت — "
        "حفظ کرد که نوار یعنی این کلاس. این جعبهٔ سیاهی است که لحظهٔ ناپدیدشدنِ نوار شکست "
        "خواهد خورد.",

    "pdf_button": "PDF",
    "pdf_prep": "در حالِ آماده‌سازیِ سند…",
    "pdf_theory_heading": "نظری",
    "pdf_practice_heading": "عملی",
    "pdf_generated": "تولیدشده از سندباکسِ یادگیریِ ماشینِ قابلِ‌اعتماد",
}


# =========================================================================== #
# ARABIC                                                                       #
# =========================================================================== #
AR2 = {
    "section_label": "القسم",
    "sec1_title": "١ · التعميم",
    "sec2_title": "٢ · التفسير",
    "masthead_subtitle_2": "مرافِقٌ تفاعليٌّ للتفسيريّة والتوضيحيّة — النماذج الزجاجيّة "
        "مقابل الصندوق الأسود، وLIME وSHAP، والجبر السببيّ، وبروز شبكةٍ التفافيّة — "
        "يَحسِب آنيًّا.",
    "colophon_2b": "القسم الثاني · الشفافية والتوضيحيّة (XAI)",

    "xai_interp": "التفسيريّة مقابل التوضيحيّة",
    "xai_black": "مشكلة الصندوق الأسود",
    "xai_tab": "LIME وSHAP",
    "xai_recourse": "الجبر والواقع المضاد",
    "xai_cv": "تفسير الرؤية: Grad-CAM",
    "xai_vlm": "النماذج اللغويّة البصريّة",

    "px_loan": "LIME مقابل SHAP · قرض",
    "px_recourse": "الجبر السببيّ",
    "px_cv": "ماسح تفسير الرؤية",
    "px_spurious": "كاشف الارتباط الكاذب",

    "xai_interp_eyebrow": "الشفافية · لوح ٠١",
    "xai_interp_p1": "تنقسم النماذج بحسب الشفافية. <em>الصندوق الزجاجيّ</em> تفسيريٌّ "
        "ببنيته: الانحدار الخطيّ يُظهر وزنًا لكلِّ سمة، وشجرةُ القرار مسارًا من الجذر إلى "
        "الورقة. وسؤالُه: <em>كيف</em> يعمل النموذج؟",
    "xai_interp_p2": "أمّا <em>الصندوق الأسود</em> — شبكةٌ عميقة أو غابةٌ عشوائيّة — فمُعتِمٌ؛ "
        "لا نقرأ منطقَه الداخليّ، فنُلحِق به طرائقَ <em>بَعْديّة</em> تُبرِّر القرارات الفرديّة. "
        "وسؤالُه: <em>لماذا</em> صدر هذا الخرج؟",
    "xai_interp_p3": "التفسيريّة خاصيّةٌ في النموذج نفسه، والتوضيحيّة تقنيّةٌ تُطبَّق عليه. "
        "وبقيّةُ هذا القسم عن الثانية غالبًا، لأنّ أدقَّ النماذج عادةً أقلُّها شفافيّة.",
    "xai_interp_eqcap": "<b>شكل.</b> النموذج الخطيّ الزجاجيّ يُظهِر وزنًا لكلِّ سمة.",
    "xai_interp_call": "الدقّةُ والشفافيّةُ تتجاذبان في اتّجاهين؛ والتوضيحيّةُ هي كيف "
        "نستعيد الثقة دون التخلّي عن النموذج الدقيق.",

    "xai_black_eyebrow": "الشفافية · لوح ٠٢",
    "xai_black_p1": "لماذا نُفسِّر أصلًا؟ لأنّ نموذجًا واثقًا دقيقًا قد يُصيب لسببٍ خاطئ. "
        "<em>الارتباطات الكاذبة</em>: قد يقرأ مُصنِّفٌ صورةَ أشعّةٍ من قطعةٍ معدنيّةٍ خلّفتها "
        "معدّاتُ مستشفًى بعينه، لا من العضو المريض.",
    "xai_black_p2": "<em>الطرق المختصرة</em>: قد يَسِمُ نموذجٌ صورةً بأنّها «حوت» لأنّه حفِظ "
        "أنّ الخلفيّة الزرقاء تعني ماءً، لا لأنّه تعلّم شكلَ الحيوان. وعلى بياناتٍ جديدةٍ "
        "ينكسر فيها المختصر، يفشل النموذجُ صامتًا.",
    "xai_black_p3": "والتوضيحُ هو الأداةُ التي تُمسِك هذا: يُظهِر <em>من أين</em> جاء الدليل، "
        "فيصير المختصرُ مرئيًّا قبل النشر لا بعد خطأٍ مكلِّف.",
    "xai_black_eqcap": "<b>شكل.</b> قد يلتفت النموذجُ إلى إشارة الخلفيّة بدل الشيء.",
    "xai_black_call": "تنبؤٌ صحيحٌ من دليلٍ خاطئ هو فشلٌ ينتظر انزياحَ التوزيع.",

    "xai_tab_eyebrow": "تفسير جدوليّ · لوح ٠٣",
    "xai_tab_p1": "<em>LIME</em> يُفسِّر تنبؤًا واحدًا محلّيًّا: يُشوّش العيّنة، ويَسِمُ التشويشات "
        "بالصندوق الأسود، ويُرجِّح بحسب القرب، ويُلائم بديلًا خطّيًّا بسيطًا. ومعامِلاتُه هي "
        "الإسنادُ المحلّيّ — موثوقةٌ في جوارٍ صغيرٍ فقط.",
    "xai_tab_p2": "<em>SHAP</em> مؤسَّسٌ على نظرية الألعاب. كلُّ سمةٍ لاعب؛ وقيمةُ شابلي لها "
        "متوسّطُ مساهمتها الهامشيّة عبر كلِّ التحالفات. وفريدًا، الإسنادات جمعيّة: تُجمَع "
        "تمامًا لتساوي الفجوةَ بين التنبؤ والقيمة الأساس.",
    "xai_tab_p3": "تُقايض الأنواعُ العموميّةَ بالسرعة: Kernel SHAP (أيّ نموذج، بالمعاينة)، "
        "وTree SHAP (دقيقٌ وسريعٌ للأشجار)، وDeep SHAP (الشبكات، بالانتشار الخلفيّ).",
    "xai_tab_eqcap": "<b>شكل.</b> قيمةُ شابلي متوسّطُ المساهمات الهامشيّة عبر التحالفات؛ "
        "وإسنادات SHAP جمعيّة.",
    "xai_tab_call": "يسأل LIME ماذا يقول نموذجٌ خطّيٌّ محلّيّ؛ ويسأل SHAP كم تساوي كلُّ سمة، "
        "ويضمن أنّ الأجزاء تساوي الكل.",

    "xai_recourse_eyebrow": "القابليّة للفعل · لوح ٠٤",
    "xai_recourse_p1": "يُخبِر التوضيحُ المضادُّ للواقع متقدِّمًا مرفوضًا بما يُغيِّره ليُقبَل "
        "(«زِد الدخل ١٥٪»). و<em>الجبر (Recourse)</em> يُحدِّد هذا بقيدين يجعلان النصيحةَ "
        "قابلةً للتطبيق.",
    "xai_recourse_p2": "أوّلًا، <em>التكلفة</em>: نقلُ الدخل من ٠ إلى ١٠٠ أصعبُ بكثيرٍ من ٨٠٠ "
        "إلى ٩٠٠، وينبغي للتوصية أن تُقلِّل الجهدَ الحقيقيّ. ثانيًا، <em>السببيّة</em>: إن كان "
        "الدخلُ علّةً للمدّخرات، فرفعُ الدخل يرفع المدّخرات مجّانًا — فأرخصُ خطّةٍ تعمل على "
        "الأصل لا على كلِّ عَرَض، ولا تقترح المستحيل.",
    "xai_recourse_p3": "فالجبرُ إذًا تحسينٌ مُقيَّدٌ على النموذج السببيّ: أقلُّ تغييرٍ كلفةً "
        "ومُمكِنًا ومتّسقًا سببيًّا يقلب القرار.",
    "xai_recourse_eqcap": "<b>شكل.</b> أقلُّ تغييرٍ قابلٍ للفعل كلفةً بقيد البنية السببيّة.",
    "xai_recourse_call": "الجبرُ الجيّد يحترم الجيبَ والغرافَ السببيّ معًا: الأرخصُ فعلًا، "
        "والمُمكِنُ فعلًا.",

    "xai_cv_eyebrow": "الرؤية الحاسوبيّة · لوح ٠٥",
    "xai_cv_p1": "كيف «يرى» نموذجُ الرؤية؟ <em>خرائطُ البروز</em> تأخذ تدرُّجَ درجة الصنف "
        "بالنسبة لكلِّ بكسلِ إدخال: البكسلاتُ التي يُحرِّك تغيُّرها الصغير الدرجةَ أكثرَ هي "
        "التي اعتمد عليها النموذج.",
    "xai_cv_p2": "تتطلّب <em>CAM</em> رأسَ تجميعٍ متوسّطٍ شاملٍ (GAP) وتقرأ أوزانَ الصنف فوق "
        "خرائط السمات. و<em>Grad-CAM</em> تُزيل هذا القيدَ المعماريّ: تُرجِّح كلَّ خريطةِ سمةٍ "
        "بمتوسّط تدرُّج درجة الصنف الداخل إليها، ثم تُبقي الجزءَ الموجب — خريطةٌ حراريّةٌ خشنةٌ "
        "لِـ«أين دليلُ الصنف».",
    "xai_cv_p3": "و<em>Guided Grad-CAM</em> تضرب خريطةَ Grad-CAM الخشنة في بروزِ انتشارٍ "
        "خلفيٍّ موجَّه لاستعادة تفاصيلَ بكسليّةٍ حادّة. و<em>تصوُّرُ السمات</em> يطرح السؤالَ "
        "المقابل: أيُّ مُدخَلٍ مُصطنَعٍ يُثير عصبونًا بعينه إلى أقصاه؟",
    "xai_cv_eqcap": "<b>شكل.</b> Grad-CAM تُرجِّح خرائطَ السمات بتدرُّج درجة الصنف المُجمَّع.",
    "xai_cv_call": "تُحوِّل Grad-CAM التدرُّجَ الذي درّب الشبكةَ إلى خريطةٍ لِما نظرت إليه.",

    "xai_vlm_eyebrow": "متعدّد الوسائط · لوح ٠٦",
    "xai_vlm_p1": "النماذجُ التي تدمج النصَّ بالصورة تكشف مِقبضًا جديدًا: <em>الانتباه "
        "المتبادل بين الوسائط</em>. يُظهِر كيف يلتفت توكِنٌ نصّيّ (مثلًا «كلب») إلى منطقةٍ من "
        "الصورة، فيُحاذي اللغةَ بالبكسلات.",
    "xai_vlm_p2": "الانتباهُ في طبقةٍ واحدةٍ ليس القصّةَ كلَّها. <em>Attention Rollout</em> "
        "يضرب مصفوفاتِ الانتباه (المُعزَّزة بالوصلة المتبقّية) عبر الطبقات لتتبُّع الأثر من "
        "الخرج إلى الدخل؛ و<em>LRP</em> يُعيد توزيعَ صِلة القرار رجوعًا عبر الشبكة إلى المدخلات.",
    "xai_vlm_p3": "وهذان معًا يُحوِّلان كومةَ المُحوِّل المُعتِمة إلى سلسلةٍ مقروءةٍ من الدليل — "
        "من كلمةٍ إلى الرقعة التي بَرَّرَتها.",
    "xai_vlm_eqcap": "<b>شكل.</b> Attention Rollout يُركِّب الانتباه عبر الطبقات لربط "
        "التوكِنات برقع الصورة.",
    "xai_vlm_call": "في النماذج متعدّدة الوسائط، التوضيحُ جسر: أيُّ الكلمات نظرت إلى أيِّ "
        "البكسلات.",

    "px_loan_eyebrow": "تطبيق · عرض ٠٦",
    "px_loan_intro": "غابةٌ عشوائيّةٌ حقيقيّةٌ تُقرِّر قرضًا. أدخِل متقدِّمًا وفسِّر القرارَ "
        "بطريقتين معًا: البديلُ الخطّيّ المحلّيّ في LIME، وقيمُ شابلي الدقيقة. كلُّ عمودٍ "
        "يُحسَب آنيًّا من النموذج المُدرَّب نفسه — لا شيءَ مكتوبٌ سلفًا.",
    "px_loan_age": "العمر",
    "px_loan_income": "الدخل الشهريّ ($)",
    "px_loan_debt": "الدَّيْن ($)",
    "px_loan_savings": "المدّخرات ($)",
    "px_loan_home": "يمتلك منزلًا",
    "px_loan_decision_approved": "قرار القرض: مقبول",
    "px_loan_decision_rejected": "قرار القرض: مرفوض",
    "px_loan_cap_lime": "<b>شكل ١. LIME.</b> إسنادٌ خطّيٌّ محلّيّ — كيف تدفع كلُّ سمةٍ هذا "
        "القرارَ الواحد (قرمزيّ = نحو الرفض، فيروزيّ = نحو القبول).",
    "px_loan_cap_shap": "<b>شكل ٢. SHAP.</b> مخطّطُ قوّةٍ شابليٍّ دقيقٌ من المعدّل الأساس إلى "
        "هذا التنبؤ؛ والمساهماتُ جمعيّة.",
    "px_loan_note": "يتّفق LIME وSHAP عادةً على إشارة المحرِّكات وترتيبها التقريبيّ، لكنّ "
        "أجزاء SHAP تُجمَع تمامًا لتساوي الخرج بينما LIME تقريبٌ محلّيّ.",

    "px_recourse_eyebrow": "تطبيق · عرض ٠٧",
    "px_recourse_intro": "لمتقدِّمٍ مرفوض، قارِن واقعًا مضادًّا ساذجًا بالجبر السببيّ. ولأنّ "
        "الدخلَ يُسبِّب المدّخرات، تبلغ الخطّةُ السببيّةُ النتيجةَ المقبولةَ نفسها بينما لا "
        "تدفع إلّا ثمنَ تغيير الدخل.",
    "px_recourse_cap_bars": "<b>شكل ١.</b> تكلفةُ كلِّ خطّةٍ بوحدات جهدٍ مِعياريّة. الخطّةُ "
        "السببيّةُ أرخصُ تمامًا بمقدار المدّخرات التي تنالها مجّانًا.",
    "px_recourse_cap_dag": "<b>شكل ٢.</b> اليالُ البنيويّ الذي تستغلّه الخطّةُ السببيّة: "
        "الدخلُ والدٌ للمدّخرات.",
    "px_recourse_normal": "الخطّةُ الساذجة: غيِّر الدخلَ والمدّخراتِ مستقلَّين.",
    "px_recourse_causal": "الجبرُ السببيّ: غيِّر الدخلَ وحده — والمدّخراتُ تتبع.",
    "px_recourse_infeasible": "لا جبرَ مُمكِنٌ في المتناول — إمّا أنّ المتقدِّم مقبولٌ أصلًا أو "
        "لا تغييرَ محدودٌ يقلب النموذج.",

    "px_cv_eyebrow": "تطبيق · عرض ٠٨",
    "px_cv_intro": "شبكةٌ التفافيّةٌ — بُنِيَت ودُرِّبت من الصفر بـ NumPy — تُصنِّف شكلًا. اختر "
        "عيّنةً وطريقةَ إسنادٍ وشاهِد بالضبط أيُّ البكسلات قاد القرار. والتدرُّجاتُ هي "
        "التدرُّجاتُ الحقيقيّة للشبكة المُدرَّبة.",
    "px_cv_method": "طريقة الإسناد",
    "px_cv_sample": "الصورة العيّنة",
    "px_cv_target": "الصنف الهدف",
    "px_cv_cap_input": "<b>شكل ١.</b> صورة الإدخال.",
    "px_cv_cap_map": "<b>شكل ٢.</b> {method} للصنف الهدف، مُركَّبةً على الصورة.",
    "px_cv_m_gradcam": "Grad-CAM",
    "px_cv_m_saliency": "البروز",
    "px_cv_m_guided": "Guided Grad-CAM",
    "px_cv_class0": "دائرة",
    "px_cv_class1": "مربّع",
    "px_cv_pred": "تتنبّأ الشبكة بـ",

    "px_spurious_eyebrow": "تطبيق · عرض ٠٩",
    "px_spurious_intro": "شبكتان تُصنِّفان الأشكالَ نفسها. رأت إحداهما بياناتٍ نظيفة؛ "
        "والأخرى بياناتٍ رافَق فيها شريطٌ سفليٌّ ساطعٌ صنفًا واحدًا دائمًا. وGrad-CAM تكشف "
        "أيّ شبكةٍ تعلّمت الشيءَ وأيّها تعلّمت المختصر.",
    "px_spurious_cap_clean": "<b>شكل ١. النموذج الأمين.</b> تتركّز Grad-CAM على الشيء نفسه.",
    "px_spurious_cap_short": "<b>شكل ٢. نموذج المختصر.</b> تُضيء Grad-CAM شريطَ الخلفيّة لا "
        "الشكل.",
    "px_spurious_energy_clean": "الانتباه للشيء (النموذج النظيف)",
    "px_spurious_energy_short": "الانتباه للشريط (نموذج المختصر)",
    "px_spurious_warn": "تحذير: نموذجُ المختصر مُصيبٌ لسببٍ خاطئ. لم يتعلّم الشكل — حفِظ أنّ "
        "الشريطَ يعني هذا الصنف. هذا صندوقٌ أسودُ سيفشل لحظةَ اختفاء الشريط.",

    "pdf_button": "PDF",
    "pdf_prep": "يجري تجهيز المستند…",
    "pdf_theory_heading": "النظري",
    "pdf_practice_heading": "العملي",
    "pdf_generated": "مُولَّد من مختبر تعلُّم الآلة الجدير بالثقة",
}
