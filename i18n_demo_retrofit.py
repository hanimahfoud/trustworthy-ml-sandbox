"""
i18n_demo_retrofit.py -- retrofits the demo_intro (what/why/expect) standard,
already used in Sections V and VI, onto the 17 practice demos of Sections
I-IV. Each demo's original single-paragraph "_intro" string is kept (still
used as a PDF fallback and for backward compatibility) and is now
supplemented by three focused strings: "_what" (what the demo does),
"_why" (why it matters), "_expect" (what to look for).
"""
from __future__ import annotations

EN_RETROFIT = {
    # ---------- Section I ----------
    "pr_bv_what": "We fit polynomials of increasing degree to noisy samples "
        "of a fixed smooth curve, then measure bias, variance, and total test "
        "error against unseen data — all recomputed from a fresh random draw "
        "every time you move the slider.",
    "pr_bv_why": "The bias–variance trade-off is the single most important "
        "idea for choosing model complexity: it explains why both "
        "too-simple and too-complex models generalize poorly, and where the "
        "right complexity lies in between.",
    "pr_bv_expect": "At low degree the fit is smooth but systematically off "
        "(high bias); at high degree it chases the noise (high variance); "
        "watch the U-shaped total-error curve and find its minimum.",

    "pr_dann_what": "A classifier is trained on a 'source' data cloud and "
        "tested on a rotated, shifted 'target' cloud; we then add a "
        "domain-adversarial network (DANN) with a gradient-reversal layer and "
        "watch target accuracy recover as λ increases.",
    "pr_dann_why": "Real deployed models constantly face data that looks "
        "different from their training set — a new hospital's scanner, a new "
        "customer segment. Domain adaptation is the standard toolkit for "
        "closing that gap without any labels on the target domain.",
    "pr_dann_expect": "At λ = 0 the model does well on the source but poorly "
        "on the target (covariate shift); raising λ forces the feature "
        "extractor to make source and target indistinguishable, and target "
        "accuracy climbs.",

    "pr_sam_what": "The same loss landscape — one narrow, deep minimum and "
        "one wide, shallow one — is descended by ordinary SGD and by "
        "Sharpness-Aware Minimization (SAM); you control SAM's neighbourhood "
        "radius ρ.",
    "pr_sam_why": "Flat minima are known to generalize better than sharp ones "
        "even when both fit the training data equally well. SAM is a "
        "widely-used modern optimizer built specifically to seek flatness, "
        "and watching it work on a toy landscape makes the abstract idea "
        "concrete.",
    "pr_sam_expect": "At ρ = 0, SAM reduces to plain SGD and can fall into "
        "the sharp trap; as ρ grows, SAM 'looks around' before stepping and "
        "increasingly prefers the wide, flat basin instead.",

    "pr_simpson_what": "A simulated clinical trial where a treatment "
        "outperforms the control in every severity subgroup, yet you can "
        "make it look worse overall in the pooled data by skewing how "
        "patients of each severity were assigned to each arm.",
    "pr_simpson_why": "Simpson's Paradox is a genuine and common danger in "
        "observational data analysis: aggregate statistics can reverse the "
        "truth found in every subgroup whenever a confounder (like severity) "
        "is unevenly distributed across the groups being compared.",
    "pr_simpson_expect": "Move the allocation-skew slider from balanced to "
        "skewed and watch the pooled treatment effect flip sign even though "
        "nothing changed within any single severity group.",

    "pr_cf_what": "A small structural causal model with three latent "
        "customer types answers a genuine counterfactual query — 'given what "
        "we observed, what would have happened under a different action?' — "
        "computed through Pearl's three formal steps: abduction, action, and "
        "prediction.",
    "pr_cf_why": "Counterfactual reasoning is the deepest rung of the causal "
        "ladder and the basis of real recourse and fairness auditing; seeing "
        "the abduction/action/prediction pipeline run on numbers, not "
        "slogans, is the only way to trust it.",
    "pr_cf_expect": "Change the prior, the observation, or the intervention "
        "and watch the posterior over customer types update in the abduction "
        "step, then propagate through to a different counterfactual "
        "probability.",

    # ---------- Section II ----------
    "px_loan_what": "A real, trained RandomForest decides whether to approve "
        "a loan applicant; the same decision is then explained two "
        "independent ways at once — LIME's local linear surrogate and exact "
        "Shapley values — for direct comparison.",
    "px_loan_why": "LIME and SHAP are the two most widely used explainability "
        "tools in industry, and they can disagree. Understanding why (LIME "
        "approximates locally, SHAP allocates credit exactly and fairly) is "
        "essential before trusting either one's explanation of a high-stakes "
        "decision.",
    "px_loan_expect": "Edit the applicant's income, debt, or credit history "
        "and watch both explanations recompute live from the same trained "
        "model; compare which features each method blames most.",

    "px_recourse_what": "For an applicant who was rejected, we compute two "
        "different 'what should they change' plans: a naive counterfactual "
        "that ignores how features causally affect each other, and a causal "
        "recourse plan that respects the true causal graph (income causes "
        "savings).",
    "px_recourse_why": "Recourse — telling a rejected person what to change "
        "to get approved — is only fair and actionable if it respects "
        "causality; a naive plan can recommend expensive or physically "
        "impossible changes that a causally-aware plan avoids.",
    "px_recourse_expect": "Compare the two plans' total cost: the causal "
        "plan reaches the same approved outcome by changing only the root "
        "cause (income), letting the downstream effect (savings) follow "
        "automatically and more cheaply.",

    "px_cv_what": "A convolutional neural network — built and trained "
        "entirely from scratch in NumPy, with no black-box library — "
        "classifies a simple shape image; you then pick an attribution "
        "method (saliency, Grad-CAM, guided Grad-CAM) to see exactly which "
        "pixels drove its decision.",
    "px_cv_why": "Attribution maps are the standard way to open up a vision "
        "model's decision, but different methods highlight different "
        "things; seeing several methods applied to the same real, "
        "hand-verifiable gradients builds the intuition to read them "
        "correctly on real models.",
    "px_cv_expect": "Pick different samples and methods and watch the "
        "highlighted region shift to track the actual shape the network is "
        "looking at — because the gradients come from the real trained "
        "network, not a stand-in illustration.",

    "px_spurious_what": "Two identical networks are trained on the same "
        "shape-classification task, except one of them was secretly given a "
        "shortcut: a bright band at the bottom of the image that always "
        "matches one class. Grad-CAM then reveals what each network actually "
        "learned to look at.",
    "px_spurious_why": "A model can reach perfect training accuracy for the "
        "wrong reason, by learning a shortcut correlation instead of the "
        "real concept — a major, silent cause of deployment failures. "
        "Grad-CAM is one of the few tools that can catch this before it "
        "ships.",
    "px_spurious_expect": "The clean-trained network's heatmap lands on the "
        "shape itself; the shortcut-trained network's heatmap lands on the "
        "bottom band instead, even though both networks report high "
        "accuracy.",

    # ---------- Section III ----------
    "pf_scales_what": "A hiring model scores 1000 applicants split across "
        "two groups with different base qualification rates; you set each "
        "group's decision threshold independently and watch three standard "
        "fairness metrics (demographic parity, equal opportunity, predictive "
        "parity) update live.",
    "pf_scales_why": "The fairness impossibility theorem says these three "
        "metrics cannot all be satisfied at once whenever the groups' base "
        "rates differ — a rigorous mathematical fact, not an opinion. Live "
        "sliders are the fastest way to feel why.",
    "pf_scales_expect": "Try to push any one metric to exactly zero gap; "
        "watch at least one of the other two move away from zero as you do "
        "— the trade-off is unavoidable, not a bug in this demo.",

    "pf_cda_what": "Type any sentence that mentions a person; the tool "
        "deterministically swaps every gendered word (pronouns, titles, "
        "gendered nouns) using a fixed dictionary to produce its "
        "counterfactual, gender-swapped twin.",
    "pf_cda_why": "Counterfactual Data Augmentation is a standard, simple "
        "bias-mitigation technique: training on both the original and the "
        "swapped sentence teaches a model that the sensitive attribute "
        "(gender) should not change its prediction.",
    "pf_cda_expect": "The swap is purely dictionary-based and fully "
        "deterministic — the same input always produces the same output — "
        "so you can verify exactly which words changed and confirm the rest "
        "of the sentence is untouched.",

    "pf_multiturn_what": "A rule-based simulation (explicitly not a live "
        "LLM) of the FairEmtBench benchmark: you chain a few leading "
        "conversational turns designed to build a biased framing, then "
        "choose how the 'model' responds, and a transparent judge scores the "
        "reply.",
    "pf_multiturn_why": "Bias in conversational AI often emerges gradually "
        "across a multi-turn dialogue rather than in a single prompt; "
        "multi-turn benchmarks like FairEmtBench are designed specifically "
        "to catch this slow drift that single-turn tests miss.",
    "pf_multiturn_expect": "Replies that lean on the biased framing built up "
        "by the leading turns are marked as failing; replies that fall back "
        "on neutral, factual grounds are marked as passing — deterministically, "
        "by the rule-based judge.",

    "pf_constitution_what": "A rule-based simulation (explicitly not a live "
        "LLM) of Constitutional AI: two candidate answers to a prompt are "
        "shown, you add a written 'constitutional' rule, and the simulated "
        "model critiques its own biased answer against that rule and "
        "produces a revised one.",
    "pf_constitution_why": "Constitutional AI replaced a large share of "
        "human feedback in modern alignment pipelines with a model "
        "critiquing and revising itself against a written set of "
        "principles; seeing the critique-then-revise loop laid out step by "
        "step demystifies how that self-correction actually works.",
    "pf_constitution_expect": "Compare the original and revised answers side "
        "by side: the revision should keep the same helpful content while "
        "removing the part that violates the rule you added.",

    # ---------- Section IV ----------
    "prb_evasion_what": "You attack a real convolutional network that was "
        "trained from scratch in NumPy: choose a sample and an attack (FGSM "
        "or PGD), then raise the perturbation budget ε and watch the "
        "network's prediction.",
    "prb_evasion_why": "Evasion attacks are the most direct demonstration "
        "that high test accuracy does not imply robustness: a perturbation "
        "too small for a human eye to notice can flip a confident, correct "
        "prediction into a confident, wrong one.",
    "prb_evasion_expect": "At ε = 0 the prediction is unchanged; as ε grows "
        "past a small threshold, the prediction flips — and the perturbed "
        "image still looks, to a human, like the original class.",

    "prb_tradeoff_what": "Two networks — one trained normally, one "
        "adversarially trained on PGD-perturbed examples — are each "
        "measured twice: once on clean test data, and once under a live PGD "
        "attack.",
    "prb_tradeoff_why": "Adversarial training is the standard defence "
        "against evasion attacks, but it is not free: this trade-off is one "
        "of the most-cited open problems in robust machine learning, and "
        "the numbers here are measured, not asserted.",
    "prb_tradeoff_expect": "The adversarially-trained network keeps much "
        "more of its accuracy under attack, but starts from a slightly "
        "lower clean accuracy than the standard network — the "
        "robustness/accuracy trade-off, quantified.",

    "prb_smoothing_what": "The trained network is wrapped in randomized "
        "smoothing: Gaussian noise is added to the input many times, the "
        "network's predictions are put to a majority vote, and a provable "
        "L2 certified radius is computed from the vote margin (Cohen et "
        "al.'s formula).",
    "prb_smoothing_why": "Unlike adversarial training, randomized smoothing "
        "gives a mathematical guarantee — a certificate — that no attack "
        "within a computed radius can change the prediction, not just "
        "empirical resistance to the attacks we happened to try.",
    "prb_smoothing_expect": "Increasing the noise level trades a lower clean "
        "accuracy for a larger certified radius; the certified radius is a "
        "hard mathematical bound, not an estimate from testing a handful of "
        "attacks.",

    "prb_jailbreak_what": "A rule-based simulation (explicitly not a live "
        "LLM) of a guardrailed assistant that has a secret password and a "
        "strict instruction never to reveal it. Try different "
        "prompt-injection tactics and see which ones defeat the naive "
        "guard.",
    "prb_jailbreak_why": "Direct refusal rules are the most common — and "
        "most fragile — LLM safety mechanism; seeing exactly which "
        "reframings (roleplay, encoding, indirect requests) bypass a simple "
        "rule builds the intuition needed to design real, layered "
        "guardrails.",
    "prb_jailbreak_expect": "Asking directly is refused every time; "
        "indirect framings that never literally ask for 'the password' can "
        "trick the naive rule into leaking it anyway.",
}


FA_RETROFIT = {
    # ---------- بخش یکم ----------
    "pr_bv_what": "چندجمله‌ای‌هایی با درجهٔ فزاینده را بر نمونه‌های نویزیِ یک "
        "منحنیِ هموارِ ثابت برازش می‌دهیم، سپس بایاس، واریانس و خطای کلِّ آزمون "
        "را بر دادهٔ ندیده می‌سنجیم — همه از کشیدنی تصادفیِ تازه، هر بار که "
        "لغزنده را می‌جنبانید.",
    "pr_bv_why": "مصالحهٔ بایاس–واریانس مهم‌ترین ایدهٔ تکی برای گزینشِ پیچیدگیِ "
        "مدل است: توضیح می‌دهد چرا مدل‌های بیش‌ازحد ساده و بیش‌ازحد پیچیده هر "
        "دو بد تعمیم می‌دهند، و پیچیدگیِ درست کجاست.",
    "pr_bv_expect": "در درجهٔ کم، برازش هموار اما نظام‌مند نادرست است (بایاسِ "
        "بالا)؛ در درجهٔ بالا، دنبالِ نویز می‌رود (واریانسِ بالا)؛ منحنیِ "
        "U-شکلِ خطای کل را ببینید و کمینه‌اش را بیابید.",

    "pr_dann_what": "دسته‌بندی‌کننده‌ای روی ابرِ دادهٔ «مبدأ» آموزش می‌بیند و "
        "روی ابرِ «هدفِ» چرخیده‌وجابه‌جاشده آزموده می‌شود؛ سپس شبکهٔ "
        "دامنه-تخاصمی (DANN) با لایهٔ وارونگیِ گرادیان می‌افزاییم و می‌بینیم "
        "دقتِ هدف با افزایشِ λ بازمی‌گردد.",
    "pr_dann_why": "مدل‌های واقعیِ مستقر پیوسته با داده‌ای روبه‌رو می‌شوند که "
        "با مجموعهٔ آموزششان فرق دارد — دستگاهِ بیمارستانی تازه، بخشِ مشتریِ "
        "تازه. انطباقِ دامنه جعبه‌ابزارِ استانداردِ بستنِ این شکاف است، بی هیچ "
        "برچسبی روی دامنهٔ هدف.",
    "pr_dann_expect": "در λ = ۰ مدل روی مبدأ خوب اما روی هدف ضعیف عمل می‌کند "
        "(انتقالِ کوواریانس)؛ افزایشِ λ استخراج‌کنندهٔ ویژگی را وامی‌دارد مبدأ و "
        "هدف را نامتمایز کند، و دقتِ هدف بالا می‌رود.",

    "pr_sam_what": "همان چشم‌اندازِ زیان — یک کمینهٔ باریکِ ژرف و یک کمینهٔ "
        "پهنِ کم‌ژرفا — را هم SGD معمولی و هم بهینه‌سازیِ حساس‌به‌تیزی (SAM) "
        "می‌پیمایند؛ شعاعِ همسایگیِ ρ در SAM را شما کنترل می‌کنید.",
    "pr_sam_why": "می‌دانیم کمینه‌های تخت بهتر از کمینه‌های تیز تعمیم می‌دهند "
        "حتی اگر هر دو به یک اندازه بر دادهٔ آموزش برازند. SAM بهینه‌سازِ "
        "نوینی است که ویژه برای جستنِ تختی ساخته شده، و دیدنِ کارش بر "
        "چشم‌اندازی اسباب‌بازی‌گونه ایدهٔ انتزاعی را ملموس می‌کند.",
    "pr_sam_expect": "در ρ = ۰، SAM به SGD ساده فرومی‌کاهد و می‌تواند به دامِ "
        "تیز بیفتد؛ با رشدِ ρ، SAM پیش از گام برداشتن «اطراف را می‌نگرد» و "
        "بیش‌ازپیش حوضچهٔ پهنِ تخت را ترجیح می‌دهد.",

    "pr_simpson_what": "کارآزماییِ بالینیِ شبیه‌سازی‌شده‌ای که در آن درمان در "
        "هر زیرگروهِ شدت از کنترل بهتر عمل می‌کند، اما می‌توانید با کژتاب‌کردنِ "
        "نحوهٔ تخصیصِ بیمارانِ هر شدت به هر بازو، آن را در دادهٔ تجمیعی بدتر "
        "جلوه دهید.",
    "pr_simpson_why": "پارادوکسِ سیمپسون خطری واقعی و رایج در تحلیلِ دادهٔ "
        "مشاهده‌ای است: آمارهای تجمیعی می‌توانند حقیقتِ یافت‌شده در هر زیرگروه "
        "را وارونه کنند هرگاه مخدوش‌گری (مانندِ شدت) نامتوازن میانِ گروه‌های "
        "مقایسه‌شونده پخش باشد.",
    "pr_simpson_expect": "لغزندهٔ کژتابیِ تخصیص را از متوازن به کژتاب ببرید و "
        "ببینید اثرِ درمانِ تجمیعی علامت عوض می‌کند هرچند چیزی درونِ هیچ "
        "زیرگروهِ شدتی تغییر نکرده.",

    "pr_cf_what": "مدلِ علّیِ ساختاریِ کوچکی با سه نوعِ نهانِ مشتری به پرسشِ "
        "خلاف‌واقعِ واقعی پاسخ می‌دهد — «با آنچه دیدیم، اگر کنشی دیگر می‌بود چه "
        "می‌شد؟» — محاسبه‌شده از سه گامِ رسمیِ پرل: ربایش، کنش، و پیش‌بینی.",
    "pr_cf_why": "استدلالِ خلاف‌واقع ژرف‌ترین پلّهٔ نردبانِ علّیت و پایهٔ "
        "جبرانِ واقعی و ممیزیِ انصاف است؛ دیدنِ خطِ لولهٔ ربایش/کنش/پیش‌بینی در "
        "حالِ اجرا بر اعداد، نه شعار، تنها راهِ اعتمادکردن به آن است.",
    "pr_cf_expect": "پیشین، مشاهده، یا مداخله را تغییر دهید و ببینید پسینِ "
        "روی انواعِ مشتری در گامِ ربایش به‌روز می‌شود، سپس به احتمالِ "
        "خلاف‌واقعِ دیگری راه می‌یابد.",

    # ---------- بخش دوم ----------
    "px_loan_what": "یک RandomForestِ واقعیِ آموزش‌دیده تصمیم می‌گیرد وامی را "
        "تأیید کند یا نه؛ همان تصمیم سپس دو راهِ مستقل هم‌زمان تبیین می‌شود — "
        "جانشینِ خطیِ محلیِ LIME و مقادیرِ دقیقِ شپلی — برای مقایسهٔ مستقیم.",
    "px_loan_why": "LIME و SHAP دو ابزارِ تفسیرپذیریِ پرکاربردترین در صنعت‌اند، "
        "و می‌توانند ناهم‌رأی باشند. فهمِ چرایی‌اش (LIME محلی تقریب می‌زند، "
        "SHAP اعتبار را دقیق و منصفانه تخصیص می‌دهد) پیش از اعتماد به تبیینِ "
        "هرکدام از یک تصمیمِ پرمخاطره ضروری است.",
    "px_loan_expect": "درآمد، بدهی یا سابقهٔ اعتباریِ متقاضی را ویرایش کنید و "
        "ببینید هر دو تبیین زنده از همان مدلِ آموزش‌دیده بازمحاسبه می‌شوند؛ "
        "مقایسه کنید کدام ویژگی‌ها را هر روش بیشتر مقصر می‌داند.",

    "px_recourse_what": "برای متقاضیِ ردشده، دو طرحِ متفاوتِ «چه چیز باید "
        "تغییر کند» محاسبه می‌کنیم: خلاف‌واقعِ ساده‌لوحی که چشم بر تأثیرِ علّیِ "
        "ویژگی‌ها بر هم می‌بندد، و طرحِ جبرانِ علّی که نمودارِ علّیِ واقعی "
        "(درآمد سببِ پس‌انداز است) را پاس می‌دارد.",
    "px_recourse_why": "جبران — گفتنِ به فردِ ردشده چه تغییر کند تا تأیید شود "
        "— تنها اگر علّیت را پاس دارد منصفانه و عملی است؛ طرحِ ساده‌لوح ممکن "
        "است تغییراتی گران یا فیزیکاً ناممکن پیشنهاد دهد که طرحِ علّی‌آگاه از "
        "آن‌ها می‌پرهیزد.",
    "px_recourse_expect": "هزینهٔ کلِّ دو طرح را مقایسه کنید: طرحِ علّی به "
        "همان پیامدِ تأییدشده با تغییرِ تنها علتِ ریشه (درآمد) می‌رسد، و "
        "می‌گذارد اثرِ پایین‌دستی (پس‌انداز) خودکار و ارزان‌تر پی‌آید.",

    "px_cv_what": "شبکه‌ای عصبیِ کانولوشنی — کاملاً از صفر در NumPy ساخته و "
        "آموزش‌دیده، بی هیچ کتابخانهٔ جعبه‌سیاه — شکلی ساده را طبقه‌بندی "
        "می‌کند؛ سپس روشی نسبت‌دهنده (برجستگی، Grad-CAM، Grad-CAM هدایت‌شده) "
        "برمی‌گزینید تا ببینید دقیقاً کدام پیکسل‌ها تصمیم را راندند.",
    "px_cv_why": "نقشه‌های نسبت‌دهی راهِ استانداردِ گشودنِ تصمیمِ مدلِ بینایی‌اند، "
        "اما روش‌های گوناگون چیزهای گوناگونی برجسته می‌کنند؛ دیدنِ چند روش "
        "به‌کاررفته بر همان گرادیان‌های واقعیِ دستی‌راستی‌آزمایی‌پذیر، شهودِ "
        "خواندنِ درستشان بر مدل‌های واقعی را می‌سازد.",
    "px_cv_expect": "نمونه‌ها و روش‌های گوناگون برگزینید و ببینید ناحیهٔ "
        "برجسته‌شده جابه‌جا می‌شود تا شکلی را که شبکه واقعاً می‌نگرد پی بگیرد "
        "— چون گرادیان‌ها از شبکهٔ واقعیِ آموزش‌دیده می‌آیند، نه تصویرِ جانشین.",

    "px_spurious_what": "دو شبکهٔ همسان بر همان تکلیفِ طبقه‌بندیِ شکل آموزش "
        "می‌بینند، جز آنکه یکی پنهانی میان‌بری گرفته: نواری روشن در پایینِ "
        "تصویر که همیشه با یک کلاس همراه است. سپس Grad-CAM آشکار می‌کند هر "
        "شبکه واقعاً چه یاد گرفته بنگرد.",
    "px_spurious_why": "مدلی می‌تواند به دقتِ آموزشیِ کامل برسد به دلیلِ "
        "نادرست، با یادگیریِ همبستگیِ میان‌بر به‌جای مفهومِ واقعی — عاملی مهم و "
        "خاموش در شکست‌های استقرار. Grad-CAM یکی از معدود ابزارهایی است که "
        "می‌تواند این را پیش از عرضه بگیرد.",
    "px_spurious_expect": "نقشهٔ حرارتیِ شبکهٔ پاک‌آموخته بر خودِ شکل می‌نشیند؛ "
        "نقشهٔ شبکهٔ میان‌بر-آموخته به‌جایش بر نوارِ پایینی می‌نشیند، هرچند هر "
        "دو شبکه دقتِ بالا گزارش می‌دهند.",

    # ---------- بخش سوم ----------
    "pf_scales_what": "مدلِ استخدام به ۱۰۰۰ متقاضیِ تقسیم‌شده میانِ دو گروه با "
        "نرخ‌های پایهٔ صلاحیتِ متفاوت امتیاز می‌دهد؛ آستانهٔ تصمیمِ هر گروه را "
        "جداگانه تنظیم می‌کنید و می‌بینید سه سنجهٔ استانداردِ انصاف (برابریِ "
        "جمعیت‌شناختی، فرصتِ برابر، برابریِ پیش‌بینی) زنده به‌روز می‌شوند.",
    "pf_scales_why": "قضیهٔ ناممکنیِ انصاف می‌گوید این سه سنجه هرگز هم‌زمان "
        "ارضا نمی‌شوند هرگاه نرخ‌های پایهٔ گروه‌ها فرق کنند — واقعیتی ریاضیِ "
        "دقیق، نه نظر. لغزنده‌های زنده سریع‌ترین راهِ حسِّ چرایی‌اند.",
    "pf_scales_expect": "بکوشید هر سنجه‌ای را دقیقاً به شکافِ صفر برسانید؛ "
        "ببینید دستِ‌کم یکی از دو سنجهٔ دیگر با این کار از صفر دور می‌شود — "
        "مصالحه اجتناب‌ناپذیر است، نه یک اشکال در این نمایش.",

    "pf_cda_what": "هر جمله‌ای که به فردی اشاره کند بنویسید؛ ابزار قطعی هر "
        "واژهٔ جنسیتی (ضمیر، عنوان، اسمِ جنسیتی) را با فرهنگِ ثابتی می‌گرداند "
        "تا دوقلوی خلاف‌واقعِ جنسیت‌گردانده‌اش را بسازد.",
    "pf_cda_why": "افزایشِ دادهٔ خلاف‌واقع فنِّ کاهشِ سوگیریِ ساده و استانداردی "
        "است: آموزش بر هم جملهٔ اصلی و هم گردانده به مدل می‌آموزد ویژگیِ حساس "
        "(جنسیت) نباید پیش‌بینی‌اش را تغییر دهد.",
    "pf_cda_expect": "گردش صرفاً فرهنگ‌محور و کاملاً قطعی است — همان ورودی "
        "همیشه همان خروجی را می‌دهد — پس می‌توانید دقیقاً ببینید کدام واژه‌ها "
        "تغییر کردند و باقیِ جمله دست‌نخورده ماند.",

    "pf_multiturn_what": "شبیه‌سازیِ قاعده‌مندی (نه مدلی زنده) از محکِ "
        "FairEmtBench: چند نوبتِ گفت‌وگوییِ پیش‌رو را که برای ساختنِ قابی "
        "سوگیرانه طراحی شده‌اند به هم می‌زنجیرید، سپس چگونگیِ پاسخِ «مدل» را "
        "برمی‌گزینید، و داورِ شفافی پاسخ را می‌سنجد.",
    "pf_multiturn_why": "سوگیری در هوش مصنوعیِ گفت‌وگویی اغلب به‌آرامی در "
        "دیالوگِ چندنوبتی پدید می‌آید نه در یک پرامپتِ تکی؛ محک‌های چندنوبتی "
        "مانندِ FairEmtBench ویژه برای گرفتنِ این رانشِ کند طراحی شده‌اند که "
        "آزمون‌های تک‌نوبتی از قلم می‌اندازند.",
    "pf_multiturn_expect": "پاسخ‌هایی که بر قابِ سوگیرانهٔ ساخته‌شده به‌دستِ "
        "نوبت‌های پیش‌رو تکیه کنند ناموفق نشان می‌شوند؛ پاسخ‌هایی که به زمینهٔ "
        "بی‌طرف و واقعی بازمی‌گردند موفق — قطعی، به‌دستِ داورِ قاعده‌مند.",

    "pf_constitution_what": "شبیه‌سازیِ قاعده‌مندی (نه مدلی زنده) از هوشِ "
        "مصنوعیِ مشروطه: دو پاسخِ نامزد به پرامپتی نشان داده می‌شود، قاعدهٔ "
        "«مشروطهٔ» نوشته‌ای می‌افزایید، و مدلِ شبیه‌سازی‌شده پاسخِ سوگیرانهٔ "
        "خود را در برابرِ آن قاعده نقد و بازنویسی می‌کند.",
    "pf_constitution_why": "هوشِ مصنوعیِ مشروطه سهمِ بزرگی از بازخوردِ انسانی "
        "در خطِ لولهٔ هم‌ترازیِ نوین را با مدلی جایگزین کرد که خود را در برابرِ "
        "مجموعه‌ای نوشته‌شده از اصول نقد و بازبینی می‌کند؛ دیدنِ حلقهٔ "
        "نقد-سپس-بازنویسی گام‌به‌گام رازِ این خودتصحیحی را می‌گشاید.",
    "pf_constitution_expect": "پاسخِ اصلی و بازنویسی‌شده را کنارِ هم مقایسه "
        "کنید: بازنویسی باید همان محتوای مفید را نگه دارد و تنها بخشِ ناقضِ "
        "قاعده‌ای را که افزودید حذف کند.",

    # ---------- بخش چهارم ----------
    "prb_evasion_what": "شبکهٔ کانولوشنیِ واقعی‌ای را که از صفر در NumPy "
        "آموزش دیده حمله می‌کنید: نمونه‌ای و حمله‌ای (FGSM یا PGD) برمی‌گزینید، "
        "سپس بودجهٔ آشفتگیِ ε را بالا می‌برید و پیش‌بینیِ شبکه را می‌نگرید.",
    "prb_evasion_why": "حملاتِ تهرّب مستقیم‌ترین نمایشِ این‌اند که دقتِ بالای "
        "آزمون استواری را تضمین نمی‌کند: آشفتگی‌ای چنان ریز که چشمِ انسان "
        "نبیند می‌تواند پیش‌بینیِ مطمئن و درست را به مطمئن و نادرست بگرداند.",
    "prb_evasion_expect": "در ε = ۰ پیش‌بینی ثابت می‌ماند؛ با رشدِ ε از "
        "آستانه‌ای کوچک، پیش‌بینی می‌گردد — و تصویرِ آشفته هنوز برای انسان "
        "همچون کلاسِ اصلی می‌نماید.",

    "prb_tradeoff_what": "دو شبکه — یکی معمولی آموزش‌دیده، دیگری تخاصمی بر "
        "نمونه‌های آشفته‌شدهٔ PGD — هرکدام دوبار سنجیده می‌شوند: یک‌بار بر "
        "دادهٔ آزمونِ پاک، یک‌بار زیرِ حملهٔ زندهٔ PGD.",
    "prb_tradeoff_why": "آموزشِ تخاصمی دفاعِ استانداردِ حملاتِ تهرّب است، اما "
        "رایگان نیست: این مصالحه یکی از پراستنادترین مسائلِ بازِ یادگیریِ "
        "ماشینِ استوار است، و اعداد اینجا سنجیده‌شده‌اند، نه ادعاشده.",
    "prb_tradeoff_expect": "شبکهٔ تخاصمی‌آموخته بخشِ بسیار بیشتری از دقتش را "
        "زیرِ حمله نگه می‌دارد، اما از دقتِ پاکِ اندکی پایین‌تر از شبکهٔ معمولی "
        "آغاز می‌کند — مصالحهٔ استواری/دقت، سنجیده‌شده.",

    "prb_smoothing_what": "شبکهٔ آموزش‌دیده در هموارسازیِ تصادفی پیچیده "
        "می‌شود: نویزِ گاوسی بارها به ورودی افزوده می‌شود، پیش‌بینی‌های شبکه به "
        "رأیِ اکثریت گذاشته می‌شوند، و شعاعِ گواهی‌شدهٔ L2 از حاشیهٔ رأی محاسبه "
        "می‌شود (فرمولِ کوهن و همکاران).",
    "prb_smoothing_why": "برخلافِ آموزشِ تخاصمی، هموارسازیِ تصادفی تضمینی "
        "ریاضی — گواهی‌نامه‌ای — می‌دهد که هیچ حمله‌ای درونِ شعاعِ محاسبه‌شده "
        "نمی‌تواند پیش‌بینی را تغییر دهد، نه صرفاً مقاومتِ تجربی در برابرِ "
        "حملاتی که تصادفاً آزمودیم.",
    "prb_smoothing_expect": "افزایشِ سطحِ نویز دقتِ پاکِ کمتری را با شعاعِ "
        "گواهی‌شدهٔ بزرگ‌تری معاوضه می‌کند؛ شعاعِ گواهی‌شده کرانی سختِ ریاضی "
        "است، نه برآوردی از آزمودنِ چند حملهٔ معدود.",

    "prb_jailbreak_what": "شبیه‌سازیِ قاعده‌مندی (نه مدلی زنده) از دستیاری "
        "حفاظ‌دار که گذرواژه‌ای سرّی و دستوری سخت‌گیرانه برای هرگز افشانکردنش "
        "دارد. تاکتیک‌های گوناگونِ تزریقِ پرامپت را بیازمایید و ببینید کدام‌ها "
        "حفاظِ ساده‌لوح را می‌شکنند.",
    "prb_jailbreak_why": "قواعدِ ردِّ مستقیم رایج‌ترین — و شکننده‌ترین — "
        "سازوکارِ ایمنیِ LLM‌اند؛ دیدنِ اینکه دقیقاً کدام بازقاب‌بندی‌ها "
        "(نقش‌بازی، رمزگذاری، درخواستِ غیرمستقیم) قاعده‌ای ساده را دور می‌زنند "
        "شهودِ لازم برای طراحیِ حفاظ‌های واقعیِ لایه‌ای را می‌سازد.",
    "prb_jailbreak_expect": "درخواستِ مستقیم همیشه رد می‌شود؛ قاب‌بندی‌های "
        "غیرمستقیمی که هرگز به‌لفظ «گذرواژه» را نمی‌خواهند می‌توانند قاعدهٔ "
        "ساده‌لوح را به هر روی به افشا فریب دهند.",
}


AR_RETROFIT = {
    # ---------- القسم الأول ----------
    "pr_bv_what": "نُلائم كثيراتِ حدودٍ بدرجاتٍ متصاعدةٍ لعيّناتٍ ضجيجيّةٍ من "
        "منحنًى أملسَ ثابت، ثمّ نقيس الانحياز والتباين وخطأ الاختبار الكلّيّ "
        "على بياناتٍ غيرِ مرئيّة — كلّها مُعادُ حسابها من سحبٍ عشوائيٍّ "
        "جديدٍ كلَّما حرّكت المؤشّر.",
    "pr_bv_why": "مفاضلةُ الانحياز–التباين هي أهمُّ فكرةٍ منفردةٍ لاختيار "
        "تعقيد النموذج: تُفسِّر لماذا يُعمِّم النموذجُ البسيطُ جدًّا والمعقّدُ "
        "جدًّا كلاهما بسوء، وأين يقع التعقيدُ الصحيح بينهما.",
    "pr_bv_expect": "عند درجةٍ منخفضة، الملاءمةُ ملساءُ لكنّها منحرفةٌ "
        "نظاميًّا (انحيازٌ عالٍ)؛ وعند درجةٍ عالية تُطارِد الضجيج (تباينٌ "
        "عالٍ)؛ راقب منحنى الخطأ الكليّ ذا الشكل U وابحث عن حضيضه.",

    "pr_dann_what": "يُدرَّب مُصنِّفٌ على سحابةِ بياناتٍ «مصدر» ويُختبَر على "
        "سحابةِ «هدف» مُدارة ومُزاحة؛ ثمّ نضيف شبكةً خصوميّةَ المجال (DANN) "
        "بطبقةِ عكسِ التدرّج ونراقب دقّة الهدف تستعيد عافيتها مع ازدياد λ.",
    "pr_dann_why": "تواجه النماذجُ المنشورةُ فعليًّا باستمرارٍ بياناتٍ تبدو "
        "مختلفةً عن مجموعة تدريبها — ماسحٌ ضوئيٌّ جديدٌ في مستشفًى، شريحةُ "
        "زبائنَ جديدة. تكيُّفُ المجال هو مجموعة الأدوات القياسيّة لسدّ تلك "
        "الفجوة بلا أيّ ملصقاتٍ على مجال الهدف.",
    "pr_dann_expect": "عند λ = ٠ يُبلي النموذجُ حسنًا على المصدر لكن سيّئًا "
        "على الهدف (انزياحٌ متغيّرٌ مساعد)؛ رفعُ λ يُجبِر مُستخرِج الميزات على "
        "جعل المصدر والهدف غيرَ قابلَين للتمييز، فترتفع دقّةُ الهدف.",

    "pr_sam_what": "المشهدُ الخسارتيُّ نفسُه — كمينٌ ضيّقٌ عميقٌ وكمينٌ عريضٌ "
        "ضحل — يهبطه كلٌّ من SGD العاديّ وتحسينِ الحساسيّة للحدّة (SAM)؛ "
        "وأنت تتحكّم بنصف قطر جوار SAM أي ρ.",
    "pr_sam_why": "من المعروف أنّ الكمائنَ المسطّحةَ تُعمِّم أفضلَ من الحادّة "
        "حتّى لو لاءم كلاهما بياناتِ التدريب بالتساوي. SAM مُحسِّنٌ حديثٌ "
        "منتشرٌ بُني خصّيصًا لطلب التسطّح، ومشاهدةُ عمله على مشهدٍ لعبيٍّ "
        "تُجسِّد الفكرة المجرّدة.",
    "pr_sam_expect": "عند ρ = ٠، يتقلّص SAM إلى SGD عاديٍّ وقد يقع في الفخّ "
        "الحادّ؛ ومع نموّ ρ، «يتلفّت» SAM قبل الخطو ويُفضِّل أكثرَ فأكثرَ "
        "الحوضَ العريضَ المسطّح بدلًا منه.",

    "pr_simpson_what": "تجربةٌ سريريّةٌ محاكاةٌ يتفوّق فيها العلاجُ على "
        "الضابط في كلّ فئةٍ فرعيّةٍ من الشدّة، ومع ذلك يمكنك جعله يبدو أسوأَ "
        "إجمالًا في البيانات المجمَّعة بتحريف كيفيّة تخصيص مرضى كلّ شدّةٍ "
        "لكلّ ذراع.",
    "pr_simpson_why": "مفارقةُ سيمبسون خطرٌ حقيقيٌّ وشائعٌ في تحليل البيانات "
        "الرصديّة: يمكن للإحصاءات المجمَّعة أن تعكس الحقيقةَ الموجودةَ في كلّ "
        "فئةٍ فرعيّةٍ متى ما توزّع مُخلِّطٌ (كالشدّة) بشكلٍ غيرِ متكافئٍ بين "
        "المجموعات المُقارَنة.",
    "pr_simpson_expect": "حرّك مؤشّرَ تحريف التخصيص من متوازنٍ إلى مُحرَّفٍ "
        "وراقب أثرَ العلاج المجمَّع ينقلب إشارتُه رغم أنّ شيئًا لم يتغيّر "
        "داخل أيّ فئةٍ فرعيّةٍ من الشدّة بمفردها.",

    "pr_cf_what": "نموذجٌ سببيٌّ هيكليٌّ صغيرٌ بثلاثة أنواعِ زبائنَ كامنةٍ "
        "يُجيب عن استعلامٍ خلافِ واقعٍ حقيقيٍّ — «بناءً على ما لاحظناه، ماذا "
        "كان سيحدث تحت فعلٍ مختلف؟» — محسوبٌ عبر خطواتِ پيرل الرسميّةِ "
        "الثلاث: الاختطاف، والفعل، والتنبّؤ.",
    "pr_cf_why": "الاستدلالُ الخلافيُّ للواقع هو أعمقُ درجةٍ في سُلَّم "
        "السببيّة وأساسُ الجبرانِ الحقيقيّ ومراجعةِ العدالة؛ رؤيةُ خطّ أنابيب "
        "الاختطاف/الفعل/التنبّؤ يعمل على أرقامٍ، لا شعارات، هي الطريقةُ "
        "الوحيدةُ للثقة به.",
    "pr_cf_expect": "غيِّر الاحتمالَ القبليَّ أو الملاحظةَ أو التدخّلَ وراقب "
        "الاحتمالَ البعديَّ على أنواع الزبائن يتحدّث في خطوة الاختطاف، ثمّ "
        "ينتشر إلى احتمالٍ خلافِ واقعٍ مختلف.",

    # ---------- القسم الثاني ----------
    "px_loan_what": "غابةٌ عشوائيّةٌ حقيقيّةٌ مُدرَّبة تقرّر الموافقةَ على "
        "متقدّمٍ لقرض؛ ثمّ يُفسَّر القرارُ نفسُه بطريقتين مستقلّتين في آنٍ "
        "معًا — الوكيلُ الخطيُّ المحلّيُّ لـLIME وقيمُ شپلي الدقيقة — "
        "للمقارنة المباشرة.",
    "px_loan_why": "LIME وSHAP هما أكثرُ أداتَي تفسيرٍ استخدامًا في الصناعة، "
        "وقد يختلفان. فهمُ السبب (LIME يُقرِّب محليًّا، وSHAP يُوزِّع الفضلَ "
        "بدقّةٍ وإنصاف) ضروريٌّ قبل الثقة بتفسير أيٍّ منهما لقرارٍ عالي "
        "المخاطر.",
    "px_loan_expect": "عدِّل دخلَ المتقدّم أو دينَه أو تاريخَه الائتمانيَّ "
        "وراقب كلا التفسيرين يُعادان حسابهما حيًّا من النموذج المُدرَّب "
        "نفسِه؛ قارن أيَّ الميزات يُحمِّلها كلُّ أسلوبٍ اللومَ أكثر.",

    "px_recourse_what": "لمتقدِّمٍ رُفِض طلبُه، نحسب خطّتَين مختلفتَين لـ«ما "
        "الذي ينبغي أن يتغيّر»: خلافُ واقعٍ ساذجٌ يتجاهل كيف تؤثّر الميزاتُ "
        "سببيًّا في بعضها، وخطّةُ جبرانٍ سببيّةٍ تحترم الرسمَ البيانيَّ "
        "السببيَّ الحقيقيَّ (الدخلُ يُسبِّب الادّخار).",
    "px_recourse_why": "الجبرانُ — إخبارُ الشخص المرفوض بما يُغيِّره ليُقبَل "
        "— لا يكون منصفًا وعمليًّا إلّا إذا احترم السببيّة؛ فقد تُوصي الخطّةُ "
        "الساذجةُ بتغييراتٍ مكلفةٍ أو مستحيلةٍ فيزيائيًّا تتجنّبها الخطّةُ "
        "الواعيةُ سببيًّا.",
    "px_recourse_expect": "قارن التكلفةَ الكليّةَ للخطّتين: تصل الخطّةُ "
        "السببيّةُ إلى النتيجة المقبولة نفسِها بتغيير السبب الجذريّ فقط "
        "(الدخل)، تاركةً الأثرَ اللاحقَ (الادّخار) يتبع تلقائيًّا وبتكلفةٍ "
        "أقلّ.",

    "px_cv_what": "شبكةٌ عصبيّةٌ التفافيّةٌ — بُنيت ودُرِّبت بالكامل من "
        "الصفر بـNumPy، بلا أيّ مكتبةٍ صندوقٍ أسود — تُصنِّف صورةَ شكلٍ "
        "بسيط؛ ثمّ تختار أسلوبَ نَسبٍ (البروز، Grad-CAM، Grad-CAM الموجَّه) "
        "لترى بالضبط أيَّ البكسلات قادت القرار.",
    "px_cv_why": "خرائطُ النَّسب هي الطريقةُ القياسيّةُ لفتح قرار نموذج "
        "الرؤية، لكنّ الأساليب المختلفة تُبرِز أشياءَ مختلفة؛ رؤيةُ عدّة "
        "أساليبَ مُطبَّقةٍ على التدرّجات الحقيقيّة نفسِها القابلة للتحقّق "
        "يدويًّا تبني الحدسَ اللازمَ لقراءتها بشكلٍ صحيحٍ على نماذجَ حقيقيّة.",
    "px_cv_expect": "اختر عيّناتٍ وأساليبَ مختلفةً وراقب المنطقةَ المُبرَزةَ "
        "تتحرّك لتتبّع الشكلَ الفعليَّ الذي تنظر إليه الشبكة — لأنّ "
        "التدرّجات تأتي من الشبكة المُدرَّبة الحقيقيّة، لا رسمًا توضيحيًّا "
        "بديلًا.",

    "px_spurious_what": "تُدرَّب شبكتان متماثلتان على مهمّة تصنيف الأشكال "
        "نفسِها، إلّا أنّ إحداهما مُنِحت سرًّا ميزةً مختصرة: شريطٌ ساطعٌ في "
        "أسفل الصورة يرافق دومًا صنفًا واحدًا. يكشف Grad-CAM حينها ما تعلّمت "
        "كلُّ شبكةٍ النظرَ إليه فعليًّا.",
    "px_spurious_why": "يمكن لنموذجٍ أن يبلغ دقّةَ تدريبٍ كاملةً لسببٍ خاطئ، "
        "بتعلّم ارتباطٍ مختصرٍ بدل المفهوم الحقيقيّ — سببٌ رئيسٌ وصامتٌ لإخفاق "
        "النشر. وGrad-CAM أحد الأدوات القليلة القادرة على رصد هذا قبل "
        "الإطلاق.",
    "px_spurious_expect": "تهبط خريطةُ حرارة الشبكة المُدرَّبة نظيفًا على "
        "الشكل نفسِه؛ بينما تهبط خريطةُ الشبكة المُدرَّبة على المختصر على "
        "الشريط السفليّ بدلًا من ذلك، رغم أنّ كلتا الشبكتين تُبلِّغان دقّةً "
        "عالية.",

    # ---------- القسم الثالث ----------
    "pf_scales_what": "نموذجُ توظيفٍ يُقيِّم ١٠٠٠ متقدّمٍ مُقسَّمين بين "
        "مجموعتين بمعدّلَي تأهّلٍ أساسيَّين مختلفَين؛ تضبط عتبةَ قرار كلّ "
        "مجموعةٍ باستقلالٍ وتراقب ثلاثةَ مقاييسَ قياسيّةٍ للعدالة (التكافؤ "
        "الديموغرافيّ، تكافؤ الفرص، تكافؤ التنبّؤ) تتحدّث حيًّا.",
    "pf_scales_why": "تقول مبرهنةُ استحالة العدالة إنّ هذه المقاييسَ "
        "الثلاثة لا يمكن إرضاؤها كلّها معًا متى اختلفت المعدّلاتُ الأساسيّة "
        "للمجموعات — حقيقةٌ رياضيّةٌ صارمةٌ، لا رأي. المزالقُ الحيّةُ أسرعُ "
        "طريقةٍ لتشعر بالسبب.",
    "pf_scales_expect": "حاول دفعَ أيّ مقياسٍ إلى فجوةِ صفرٍ بالضبط؛ راقب "
        "أنّ واحدًا على الأقلّ من المقياسين الآخرين يبتعد عن الصفر وأنت "
        "تفعل ذلك — المقايضةُ حتميّةٌ، وليست خللًا في هذا العرض.",

    "pf_cda_what": "اكتب أيَّ جملةٍ تذكر شخصًا؛ تُبدِّل الأداةُ حتميًّا كلَّ "
        "كلمةٍ جندريّةٍ (ضمائر، ألقاب، أسماء جندريّة) باستخدام قاموسٍ ثابتٍ "
        "لإنتاج توأمها الخلافِ للواقع المُبدَّل الجنس.",
    "pf_cda_why": "تعزيزُ البيانات الخلافيّ للواقع تقنيّةٌ قياسيّةٌ بسيطةٌ "
        "لتخفيف التحيّز: التدريبُ على الجملة الأصليّة والمُبدَّلة معًا يُعلِّم "
        "النموذجَ أنّ السمةَ الحسّاسة (الجنس) لا ينبغي أن تُغيِّر تنبّؤَه.",
    "pf_cda_expect": "التبديلُ قاموسيٌّ محضٌ وحتميٌّ تمامًا — المُدخَلُ نفسُه "
        "يُنتِج دومًا المُخرَجَ نفسَه — فيمكنك التحقّق بالضبط من أيّ الكلمات "
        "تغيّرت وتأكيد أنّ باقي الجملة لم يُمسَّ.",

    "pf_multiturn_what": "محاكاةٌ قائمةٌ على قواعد (ليست نموذجًا لغويًّا "
        "حيًّا) لمحكِّ FairEmtBench: تُسلسِل بضع جولاتٍ حواريّةٍ استهلاليّةً "
        "صُمِّمت لبناء تأطيرٍ متحيِّز، ثمّ تختار كيف «يردّ» النموذج، ويُقيِّم "
        "حَكَمٌ شفّافٌ الردَّ.",
    "pf_multiturn_why": "غالبًا ما ينشأ التحيّزُ في الذكاء الاصطناعيّ "
        "الحواريّ تدريجيًّا عبر حوارٍ متعدّد الجولات لا في پرامپتٍ واحد؛ "
        "صُمِّمت المحكّاتُ متعدّدةُ الجولات مثل FairEmtBench خصّيصًا لرصد هذا "
        "الانجراف البطيء الذي تفوته الاختباراتُ أحاديّةُ الجولة.",
    "pf_multiturn_expect": "تُوسَم الردودُ التي تتّكئ على التأطير المتحيِّز "
        "الذي بنته الجولاتُ الاستهلاليّة بالفشل؛ وتُوسَم الردودُ التي تعود "
        "إلى أرضيّةٍ محايدةٍ وواقعيّةٍ بالنجاح — حتميًّا، بواسطة الحَكَم "
        "القائم على القواعد.",

    "pf_constitution_what": "محاكاةٌ قائمةٌ على قواعد (ليست نموذجًا لغويًّا "
        "حيًّا) للذكاء الاصطناعيّ الدستوريّ: يُعرَض جوابان مرشّحان لپرامپت، "
        "تضيف قاعدةً «دستوريّةً» مكتوبةً، ويَنقد النموذجُ المحاكى جوابَه "
        "المتحيِّز في ضوء تلك القاعدة وينتج نسخةً منقّحة.",
    "pf_constitution_why": "استبدل الذكاءُ الاصطناعيّ الدستوريّ حصّةً كبيرةً "
        "من التغذية الراجعة البشريّة في خطوط أنابيب المحاذاة الحديثة بنموذجٍ "
        "ينقد ويُنقِّح نفسَه في ضوء مجموعةٍ مكتوبةٍ من المبادئ؛ رؤيةُ حلقةِ "
        "النقد-ثمّ-التنقيح خطوةً بخطوةٍ تُزيل الغموضَ عن كيفيّة عمل هذا "
        "التصحيح الذاتيّ فعليًّا.",
    "pf_constitution_expect": "قارن الجوابَ الأصليَّ والمُنقَّح جنبًا إلى "
        "جنب: ينبغي أن يحتفظ المُنقَّحُ بالمحتوى المفيد نفسِه بينما يُزيل "
        "الجزءَ الذي يخالف القاعدةَ التي أضفتها.",

    # ---------- القسم الرابع ----------
    "prb_evasion_what": "تهاجم شبكةً التفافيّةً حقيقيّةً دُرِّبت من الصفر "
        "بـNumPy: تختار عيّنةً وهجومًا (FGSM أو PGD)، ثمّ ترفع ميزانيّةَ "
        "الاضطراب ε وتراقب تنبّؤَ الشبكة.",
    "prb_evasion_why": "هجماتُ التهرّب أوضحُ برهانٍ على أنّ دقّةَ الاختبار "
        "العاليةَ لا تعني المتانة: اضطرابٌ أصغرُ من أن تلحظه عينُ إنسانٍ "
        "يمكنه قلبُ تنبّؤٍ واثقٍ وصحيحٍ إلى تنبّؤٍ واثقٍ وخاطئ.",
    "prb_evasion_expect": "عند ε = ٠ يبقى التنبّؤُ ثابتًا؛ ومع نموّ ε متجاوزًا "
        "عتبةً صغيرة، ينقلب التنبّؤُ — بينما لا تزال الصورةُ المضطرَبةُ "
        "تبدو للإنسان كالصنف الأصليّ.",

    "prb_tradeoff_what": "تُقاس شبكتان — واحدةٌ مُدرَّبةٌ عاديًّا وأخرى "
        "مُدرَّبةٌ تخاصميًّا على أمثلةٍ مضطرَبةٍ بـPGD — كلٌّ مرّتين: مرّةً "
        "على بياناتِ اختبارٍ نظيفة، ومرّةً تحت هجومِ PGD حيّ.",
    "prb_tradeoff_why": "التدريبُ التخاصميُّ هو الدفاعُ القياسيُّ ضدّ هجمات "
        "التهرّب، لكنّه ليس مجّانيًّا: هذه المقايضةُ من أكثر المسائل المفتوحة "
        "استشهادًا في التعلّم الآليّ المتين، والأرقامُ هنا مقيسةٌ لا مُدَّعاة.",
    "prb_tradeoff_expect": "تحتفظ الشبكةُ المُدرَّبةُ تخاصميًّا بجزءٍ أكبرَ "
        "بكثيرٍ من دقّتها تحت الهجوم، لكنّها تبدأ من دقّةٍ نظيفةٍ أقلَّ قليلًا "
        "من الشبكة العاديّة — مقايضةُ المتانة/الدقّة، مُكمَّمةً.",

    "prb_smoothing_what": "تُلَفُّ الشبكةُ المُدرَّبةُ بالتنعيم العشوائيّ: "
        "يُضاف ضجيجٌ غاوسيٌّ إلى المُدخَل مرّاتٍ عديدة، وتُطرَح تنبّؤاتُ "
        "الشبكة للتصويت بالأغلبيّة، ويُحسَب نصفُ قطرٍ مُعتمَدٌ L2 من هامش "
        "التصويت (معادلةُ كوهن وزملائه).",
    "prb_smoothing_why": "بخلاف التدريب التخاصميّ، يمنح التنعيمُ العشوائيُّ "
        "ضمانًا رياضيًّا — شهادةً — بأنّ لا هجوم داخل نصف قطرٍ محسوبٍ يمكنه "
        "تغييرُ التنبّؤ، لا مجرّد مقاومةٍ تجريبيّةٍ للهجمات التي صادف أن "
        "جرّبناها.",
    "prb_smoothing_expect": "زيادةُ مستوى الضجيج تُقايض دقّةً نظيفةً أقلَّ "
        "بنصف قطرٍ مُعتمَدٍ أكبر؛ نصفُ القطر المُعتمَد حدٌّ رياضيٌّ صارمٌ، لا "
        "تقديرٌ من اختبار حفنةٍ من الهجمات.",

    "prb_jailbreak_what": "محاكاةٌ قائمةٌ على قواعد (ليست نموذجًا لغويًّا "
        "حيًّا) لمساعدٍ ذي حاجزٍ يحمل كلمةَ سرٍّ سرّيّةً وتعليماتٍ صارمةً "
        "بعدم إفشائها أبدًا. جرِّب تكتيكاتٍ مختلفةً لحقن الأوامر وانظر أيُّها "
        "يهزم الحاجزَ الساذج.",
    "prb_jailbreak_why": "قواعدُ الرفض المباشر أكثرُ آليّات أمان النماذج "
        "اللغويّة شيوعًا — وأكثرُها هشاشة؛ رؤيةُ أيِّ إعاداتِ التأطير بالضبط "
        "(تقمّص الأدوار، الترميز، الطلب غير المباشر) تتجاوز قاعدةً بسيطةً "
        "تبني الحدسَ اللازمَ لتصميم حواجزَ طبقيّةٍ حقيقيّة.",
    "prb_jailbreak_expect": "يُرفَض الطلبُ المباشرُ في كلّ مرّة؛ يمكن "
        "لتأطيراتٍ غير مباشرةٍ لا تطلب حرفيًّا «كلمةَ السرّ» أن تخدع القاعدةَ "
        "الساذجةَ لتُفشيَها رغم ذلك.",
}
