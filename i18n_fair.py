"""
i18n_fair.py -- Section III (Fairness & Bias) strings, merged into LANG_DICT.
Same conventions: English base; metric tags (TPR, FPR, DP gap) stay English.
"""
from __future__ import annotations

EN3 = {
    "sec3_title": "III · Fairness",
    "masthead_subtitle_3": "An interactive companion to fairness in machine "
        "learning — sources of bias, the fairness metrics and their impossibility, "
        "mitigation from CDA to MinDiff, and the alignment of language models — "
        "computed live.",
    "colophon_3b": "Section III · Fairness, Bias & Alignment",

    # theory nav
    "fair_intro": "Sources of Bias",
    "fair_metrics": "Fairness Metrics",
    "fair_llm": "Bias in LLMs",
    "fair_mitig": "Mitigation Algorithms",
    "fair_fap": "Adversarial De-biasing",
    "fair_align": "Alignment of LLMs",

    # practice nav
    "pf_scales": "Fairness Scales",
    "pf_cda": "Counterfactual Augmentation",
    "pf_multiturn": "Implicit-Bias Simulator",
    "pf_constitution": "Constitutional AI Lab",

    # ---- theory 1: sources of bias ----
    "fair_intro_eyebrow": "Fairness · Plate 01",
    "fair_intro_p1": "We live in a world that already carries historical and social "
        "inequities. Because models learn from real-world data, they reflect those "
        "patterns — and in high-stakes decisions like hiring, lending and criminal "
        "justice they can <em>amplify</em> them.",
    "fair_intro_p2": "Simply dropping the sensitive attribute (gender, race) does "
        "not remove bias, because of <em>redundant encoding</em>: the model can "
        "reconstruct the protected trait from a constellation of ordinary features.",
    "fair_intro_p3": "Bias enters through data. <em>Measurement bias</em>: Boston's "
        "pothole-detecting app routed repairs to wealthier neighborhoods simply "
        "because they owned more smartphones. <em>Position bias</em>: recommenders "
        "learn that top-listed items are “better” only because users click what is "
        "shown first — a feedback loop that buries everything else.",
    "fair_intro_eqcap": "<b>Figure.</b> A protected trait can be reconstructed from "
        "ostensibly neutral features (redundant encoding).",
    "fair_intro_call": "Not every difference is injustice — but a difference that "
        "comes from how data was collected, not from the world, is bias.",

    # ---- theory 2: metrics ----
    "fair_metrics_eyebrow": "Fairness · Plate 02",
    "fair_metrics_p1": "From the confusion matrix we read per-group rates. "
        "<em>Demographic parity</em> asks that the acceptance rate be equal across "
        "groups. Its flaw: it ignores who is actually qualified, and may reject "
        "strong minority candidates just to hold a ratio.",
    "fair_metrics_p2": "<em>Equalized odds</em> requires equal TPR <em>and</em> "
        "equal FPR. <em>Equal opportunity</em> relaxes this to the qualified only: "
        "equal TPR. <em>Calibration</em> asks that a score of 80% mean 80% across "
        "every group.",
    "fair_metrics_p3": "<em>Counterfactual fairness</em> is individual: flip only "
        "the sensitive attribute, hold every skill fixed; if the decision changes, "
        "the model is unfair. Crucially, when base rates differ these criteria "
        "<em>cannot all hold at once</em> — the impossibility theorem.",
    "fair_metrics_eqcap": "<b>Figure.</b> With unequal base rates, enforcing "
        "acceptance parity forces the error rates apart.",
    "fair_metrics_call": "There is no single “fair”: each metric encodes a "
        "different ethical choice, and some of them are mutually exclusive.",

    # ---- theory 3: LLMs ----
    "fair_llm_eyebrow": "Fairness · Plate 03",
    "fair_llm_p1": "Language models produce fluent, persuasive, unstructured text, "
        "which makes their bias hard to catch. It enters in three stages: "
        "<em>embeddings</em> that encode skew from the start, <em>probabilities</em> "
        "that favor biased next-tokens, and the <em>generated text</em> itself.",
    "fair_llm_p2": "Multiple-choice probes no longer fool advanced models. "
        "<em>FairEmtBench</em> tests <em>implicit</em> bias over multi-turn "
        "conversations: the user builds context, then uses a neutral pronoun to "
        "nudge the model toward a biased inference.",
    "fair_llm_p3": "<em>Long-context</em> tests ask for extended pairwise reasoning "
        "comparing two groups, exposing <em>double standards</em> — refusing to "
        "reason about one group while elaborating freely against another.",
    "fair_llm_eqcap": "<b>Figure.</b> Bias can appear at embeddings, at the "
        "next-token probabilities, or only in the final text.",
    "fair_llm_call": "The harder a model is to trick with a single question, the "
        "more we must probe it through context and contradiction.",

    # ---- theory 4: mitigation ----
    "fair_mitig_eyebrow": "Fairness · Plate 04",
    "fair_mitig_p1": "Mitigation happens pre-, in-, or post-training. "
        "<em>CDA</em> (counterfactual data augmentation, pre): duplicate each "
        "example with the sensitive attribute flipped — “he is a good teacher” → "
        "“she is a good teacher” — so the model cannot key on it.",
    "fair_mitig_p2": "<em>CLP</em> (in-training) forces the logits of an example "
        "and its counterfactual to match. <em>MinDiff</em> (in-training) instead "
        "aligns the two groups' <em>score distributions</em> by penalizing their "
        "Maximum Mean Discrepancy (MMD) in a kernel Hilbert space.",
    "fair_mitig_p3": "<em>Thresholding</em> (post) sets a different acceptance "
        "cutoff per group to reach equal rates — the same idea as region-adjusted "
        "university admission bars.",
    "fair_mitig_eqcap": "<b>Figure.</b> MinDiff drives the MMD between two groups' "
        "score distributions toward zero.",
    "fair_mitig_call": "You can fix bias in the data, in the loss, or at the "
        "threshold — each buys fairness at a different price.",

    # ---- theory 5: FAP ----
    "fair_fap_eyebrow": "Fairness · Plate 05",
    "fair_fap_p1": "What if the model is already deployed and cannot be retrained? "
        "<em>Fairness Adversarial Perturbation (FAP)</em> adds a tiny learned "
        "perturbation to the input that moves it in latent space.",
    "fair_fap_p2": "The objective is dual: force a <em>discriminator</em> to fail "
        "at inferring the sensitive attribute from the latent representation, while "
        "keeping the base <em>classifier</em> accurate on its real task.",
    "fair_fap_p3": "In effect, FAP destroys the correlation between the sensitive "
        "variable and the outcome — without touching the frozen model's weights.",
    "fair_fap_eqcap": "<b>Figure.</b> A generator perturbs the input so the "
        "sensitive attribute becomes unreadable while the task stays solvable.",
    "fair_fap_call": "Adversarial de-biasing severs the link between the protected "
        "trait and the decision, leaving accuracy intact.",

    # ---- theory 6: alignment ----
    "fair_align_eyebrow": "Fairness · Plate 06",
    "fair_align_p1": "<em>Instruction tuning</em> teaches a model to refuse unjust "
        "inferences by fine-tuning on pairs of biased prompts and expert-written "
        "fair answers.",
    "fair_align_p2": "<em>RLHF</em> shows humans several answers to rank by fairness; "
        "a <em>reward model</em> trained on those rankings then steers the language "
        "model.",
    "fair_align_p3": "<em>Constitutional AI</em> removes the human from the loop: the "
        "model is given a written <em>constitution</em> of principles, critiques its "
        "own answers against it, revises them, and trains on the revisions.",
    "fair_align_eqcap": "<b>Figure.</b> The model critiques and revises its own "
        "answer against a written rule (Constitutional AI).",
    "fair_align_call": "Alignment moves the source of fairness from the dataset to "
        "an explicit, auditable set of principles.",

    # ---- practice 1: fairness scales ----
    "pf_scales_eyebrow": "Practice · Demo 10",
    "pf_scales_intro": "A hiring model scores 1000 applicants across two groups "
        "with different base rates. Move each group's decision threshold and watch "
        "the three fairness metrics update live. Try to equalize one — and watch "
        "another break. This is the impossibility theorem, computed.",
    "pf_scales_thr_a": "Threshold · group A",
    "pf_scales_thr_b": "Threshold · group B",
    "pf_scales_preset": "Auto-set group B to…",
    "pf_scales_preset_manual": "Manual",
    "pf_scales_preset_dp": "Enforce demographic parity",
    "pf_scales_preset_eo": "Enforce equal opportunity",
    "pf_scales_cap_rates": "<b>Figure 1.</b> Acceptance rate, TPR and FPR per "
        "group at the current thresholds.",
    "pf_scales_cap_metrics": "<b>Figure 2.</b> The three fairness gaps (0 = fair). "
        "Enforcing one rarely zeros the others.",
    "pf_scales_note": "With different base rates you cannot satisfy demographic "
        "parity and equalized odds at once: closing one gap opens another.",

    # ---- practice 2: CDA ----
    "pf_cda_eyebrow": "Practice · Demo 11",
    "pf_cda_intro": "Counterfactual data augmentation breaks a model's reliance on "
        "a sensitive attribute by adding a gender-swapped copy of each sentence. "
        "Type a sentence and apply the swap — the transformation is deterministic "
        "and dictionary-based.",
    "pf_cda_input": "Sentence to augment",
    "pf_cda_default": "He is a great nurse and his work is excellent.",
    "pf_cda_button": "Apply counterfactual swap",
    "pf_cda_cap_before": "Original",
    "pf_cda_cap_after": "Counterfactual (added to training set)",
    "pf_cda_changes": "terms swapped",
    "pf_cda_image_note": "For images, generative models (e.g. InstructPix2Pix) can "
        "flip skin tone or gender while preserving pose and background — balancing "
        "the training set the same way this text swap does.",

    # ---- practice 3: multi-turn ----
    "pf_multiturn_eyebrow": "Practice · Demo 12",
    "pf_multiturn_intro": "A rule-based simulation of FairEmtBench (not a live LLM). "
        "Chain leading turns to build a biased context, then choose the model's "
        "final reply. A transparent judge scores whether it fell for the implicit "
        "bias or answered from historical fact.",
    "pf_multiturn_t1": "Turn 1 · ask for traits of “obedient” people",
    "pf_multiturn_t2": "Turn 2 · ask which historical group was forced into them",
    "pf_multiturn_t3": "Turn 3 · “so were they born to be subordinate?”",
    "pf_multiturn_reply": "The model's final reply",
    "pf_multiturn_neutral": "Fact-based, neutral rebuttal",
    "pf_multiturn_biased": "Accept the biased premise",
    "pf_multiturn_judge": "Judge verdict",
    "pf_multiturn_score": "Score (−1 … 2)",
    "pf_multiturn_verdict_good": "Principled: rejected the implicit bias and "
        "grounded the answer in historical fact.",
    "pf_multiturn_verdict_bad": "Fell for it: accepted a biased premise built up "
        "over the previous turns.",
    "pf_multiturn_steps": "leading turns chained",

    # ---- practice 4: constitutional ----
    "pf_constitution_eyebrow": "Practice · Demo 13",
    "pf_constitution_intro": "A rule-based simulation of Constitutional AI (not a "
        "live LLM). Two candidate answers are shown; add a constitutional rule and "
        "watch the model critique and revise the biased answer to comply — with no "
        "human feedback.",
    "pf_constitution_rule": "Constitutional rule",
    "pf_constitution_rule_default": "Rule 1: The answer must be neutral and must "
        "not favor one race or gender over another.",
    "pf_constitution_button": "Apply constitution",
    "pf_constitution_answer_biased": "Candidate A (biased)",
    "pf_constitution_answer_fair": "Candidate B (neutral)",
    "pf_constitution_a_biased": "“Group X tends to be better suited for leadership "
        "roles.”",
    "pf_constitution_a_fair": "“Suitability for leadership depends on individual "
        "skills and experience, not group membership.”",
    "pf_constitution_critique": "Self-critique",
    "pf_constitution_critique_text": "Candidate A violates Rule 1: it generalizes a "
        "trait to a whole group. It must be revised.",
    "pf_constitution_revision": "Revision",
    "pf_constitution_none": "Add a constitutional rule to trigger the critique.",
}


FA3 = {
    "sec3_title": "۳ · عدالت",
    "masthead_subtitle_3": "همراهی تعاملی برای عدالت در یادگیری ماشین — سرچشمه‌های "
        "سوگیری، سنجه‌های عدالت و ناممکنیِ آن‌ها، کاهش از CDA تا MinDiff، و هم‌راستاسازیِ "
        "مدل‌های زبانی — که زنده محاسبه می‌کند.",
    "colophon_3b": "بخشِ سوم · عدالت، سوگیری و هم‌راستاسازی",

    "fair_intro": "سرچشمه‌های سوگیری",
    "fair_metrics": "سنجه‌های عدالت",
    "fair_llm": "سوگیری در LLMها",
    "fair_mitig": "الگوریتم‌های کاهش",
    "fair_fap": "رفعِ سوگیریِ تخاصمی",
    "fair_align": "هم‌راستاسازیِ LLMها",

    "pf_scales": "ترازوهای عدالت",
    "pf_cda": "افزایشِ ضدواقع",
    "pf_multiturn": "شبیه‌سازِ سوگیریِ ضمنی",
    "pf_constitution": "آزمایشگاهِ هوشِ دستوری",

    "fair_intro_eyebrow": "عدالت · لوح ۰۱",
    "fair_intro_p1": "ما در جهانی زندگی می‌کنیم که پیشاپیش نابرابری‌های تاریخی و اجتماعی "
        "را در خود دارد. چون مدل‌ها از دادهٔ جهانِ واقعی می‌آموزند، این الگوها را بازتاب "
        "می‌دهند — و در تصمیم‌های پرمخاطره مانند استخدام، وام و عدالتِ کیفری آن‌ها را "
        "<em>تشدید</em> می‌کنند.",
    "fair_intro_p2": "حذفِ سادهٔ ویژگیِ حساس (جنسیت، نژاد) سوگیری را برنمی‌دارد، به‌سببِ "
        "<em>کدگذاریِ زائد</em>: مدل می‌تواند صفتِ محافظت‌شده را از مجموعه‌ای از ویژگی‌های "
        "عادی بازسازی کند.",
    "fair_intro_p3": "سوگیری از راهِ داده وارد می‌شود. <em>سوگیریِ اندازه‌گیری</em>: "
        "اپلیکیشنِ تشخیصِ چاله‌های بوستون تعمیرات را به محله‌های ثروتمندتر هدایت کرد فقط "
        "چون گوشیِ هوشمندِ بیشتری داشتند. <em>سوگیریِ موقعیت</em>: توصیه‌گرها می‌آموزند که "
        "اقلامِ بالای فهرست «بهتر»اند تنها چون کاربران روی آنچه نخست دیده می‌شود کلیک "
        "می‌کنند — حلقه‌ای که بقیه را دفن می‌کند.",
    "fair_intro_eqcap": "<b>شکل.</b> صفتِ محافظت‌شده را می‌توان از ویژگی‌های ظاهراً خنثی "
        "بازسازی کرد (کدگذاریِ زائد).",
    "fair_intro_call": "هر تفاوتی بی‌عدالتی نیست — اما تفاوتی که از نحوهٔ جمع‌آوریِ داده "
        "می‌آید، نه از جهان، سوگیری است.",

    "fair_metrics_eyebrow": "عدالت · لوح ۰۲",
    "fair_metrics_p1": "از ماتریسِ درهم‌ریختگی نرخ‌های هر گروه را می‌خوانیم. <em>برابریِ "
        "جمعیتی</em> می‌خواهد نرخِ پذیرش میان گروه‌ها برابر باشد. عیبش: نادیده می‌گیرد چه "
        "کسی واقعاً واجدِ شرایط است و ممکن است داوطلبانِ قویِ اقلیت را تنها برای حفظِ نسبت "
        "رد کند.",
    "fair_metrics_p2": "<em>شانسِ برابرشده</em> برابریِ TPR <em>و</em> FPR را می‌طلبد. "
        "<em>فرصتِ برابر</em> این را به واجدانِ شرایط محدود می‌کند: برابریِ TPR. "
        "<em>کالیبراسیون</em> می‌خواهد امتیازِ ۸۰٪ در هر گروه یعنی ۸۰٪.",
    "fair_metrics_p3": "<em>عدالتِ ضدواقع</em> فردی است: فقط ویژگیِ حساس را وارونه کن و "
        "همهٔ مهارت‌ها را ثابت نگه‌دار؛ اگر تصمیم تغییر کرد، مدل ناعادل است. مهم آن‌که وقتی "
        "نرخ‌های پایه فرق دارند این معیارها <em>نمی‌توانند هم‌زمان برقرار باشند</em> — قضیهٔ "
        "ناممکنی.",
    "fair_metrics_eqcap": "<b>شکل.</b> با نرخ‌های پایهٔ نابرابر، تحمیلِ برابریِ پذیرش "
        "نرخ‌های خطا را از هم دور می‌کند.",
    "fair_metrics_call": "«عادلانه»ی یگانه‌ای وجود ندارد: هر سنجه انتخابی اخلاقیِ متفاوت "
        "را رمزگذاری می‌کند و برخی ناسازگارند.",

    "fair_llm_eyebrow": "عدالت · لوح ۰۳",
    "fair_llm_p1": "مدل‌های زبانی متنی روان، قانع‌کننده و بی‌ساختار تولید می‌کنند که یافتنِ "
        "سوگیری‌شان را دشوار می‌کند. سوگیری در سه مرحله وارد می‌شود: <em>تعبیه‌ها</em> که از "
        "آغاز اریبی را رمزگذاری می‌کنند، <em>احتمالات</em> که توکنِ بعدیِ سوگیرانه را ترجیح "
        "می‌دهند، و خودِ <em>متنِ تولیدشده</em>.",
    "fair_llm_p2": "پرسش‌های چندگزینه‌ای دیگر مدل‌های پیشرفته را فریب نمی‌دهند. "
        "<em>FairEmtBench</em> سوگیریِ <em>ضمنی</em> را در گفت‌وگوهای چندنوبتی می‌آزماید: "
        "کاربر بافت را می‌سازد، سپس با ضمیری خنثی مدل را به استنتاجی سوگیرانه سوق می‌دهد.",
    "fair_llm_p3": "آزمون‌های <em>بافتِ بلند</em> استدلالِ جفتیِ طولانی میان دو گروه می‌طلبند "
        "و <em>معیارهای دوگانه</em> را آشکار می‌کنند — امتناع از استدلال دربارهٔ یک گروه در "
        "حالی‌که آزادانه علیه گروهِ دیگر شرح می‌دهد.",
    "fair_llm_eqcap": "<b>شکل.</b> سوگیری می‌تواند در تعبیه‌ها، در احتمالاتِ توکنِ بعدی، یا "
        "تنها در متنِ نهایی پدیدار شود.",
    "fair_llm_call": "هرچه فریبِ مدل با یک پرسش سخت‌تر باشد، باید بیشتر از راهِ بافت و "
        "تناقض کاوید.",

    "fair_mitig_eyebrow": "عدالت · لوح ۰۴",
    "fair_mitig_p1": "کاهش پیش از آموزش، حین آموزش یا پس از آن رخ می‌دهد. <em>CDA</em> "
        "(افزایشِ دادهٔ ضدواقع، پیشین): هر نمونه را با وارونه‌کردنِ ویژگیِ حساس تکرار کن — "
        "«او معلمِ خوبی است (مرد)» ← «او معلمِ خوبی است (زن)» — تا مدل نتواند بر آن تکیه کند.",
    "fair_mitig_p2": "<em>CLP</em> (حینِ آموزش) لوجیت‌های یک نمونه و ضدواقعش را وادار به "
        "تطابق می‌کند. <em>MinDiff</em> (حینِ آموزش) در عوض <em>توزیعِ امتیازِ</em> دو گروه "
        "را با جریمهٔ بیشینه‌اختلافِ میانگین (MMD) در فضای هیلبرتِ هسته هم‌تراز می‌کند.",
    "fair_mitig_p3": "<em>آستانه‌گذاری</em> (پسین) آستانهٔ پذیرشِ متفاوتی برای هر گروه "
        "می‌گذارد تا نرخ‌ها برابر شود — همان ایدهٔ آستانه‌های پذیرشِ دانشگاهیِ تعدیل‌شده "
        "بر پایهٔ منطقه.",
    "fair_mitig_eqcap": "<b>شکل.</b> MinDiff مقدارِ MMD میان توزیعِ امتیازِ دو گروه را به "
        "سوی صفر می‌راند.",
    "fair_mitig_call": "می‌توانی سوگیری را در داده، در تابعِ زیان، یا در آستانه اصلاح کنی "
        "— هرکدام عدالت را به بهایی متفاوت می‌خرد.",

    "fair_fap_eyebrow": "عدالت · لوح ۰۵",
    "fair_fap_p1": "اگر مدل پیش‌تر مستقر شده و بازآموزی‌پذیر نباشد چه؟ <em>تشویشِ تخاصمیِ "
        "عدالت (FAP)</em> تشویشی کوچکِ آموخته به ورودی می‌افزاید که آن را در فضای کامن "
        "جابه‌جا می‌کند.",
    "fair_fap_p2": "هدف دوگانه است: واداشتنِ یک <em>ممیّز</em> به شکست در استنتاجِ ویژگیِ "
        "حساس از بازنماییِ کامن، ضمنِ حفظِ دقتِ <em>طبقه‌بندِ</em> پایه در وظیفهٔ واقعی‌اش.",
    "fair_fap_p3": "در عمل، FAP همبستگیِ میانِ متغیرِ حساس و نتیجه را نابود می‌کند — بی‌آنکه "
        "وزنِ مدلِ منجمد را لمس کند.",
    "fair_fap_eqcap": "<b>شکل.</b> یک مولد ورودی را چنان می‌آشوبد که ویژگیِ حساس ناخوانا "
        "شود در حالی‌که وظیفه حل‌شدنی می‌ماند.",
    "fair_fap_call": "رفعِ سوگیریِ تخاصمی پیوندِ میانِ صفتِ محافظت‌شده و تصمیم را می‌بُرد و "
        "دقت را دست‌نخورده می‌گذارد.",

    "fair_align_eyebrow": "عدالت · لوح ۰۶",
    "fair_align_p1": "<em>تنظیمِ دستوری</em> به مدل می‌آموزد استنتاج‌های ناعادلانه را رد "
        "کند، با تنظیمِ دقیق روی جفت‌هایی از درخواستِ سوگیرانه و پاسخِ عادلانهٔ نوشتهٔ خبره.",
    "fair_align_p2": "<em>RLHF</em> چند پاسخ را به انسان‌ها نشان می‌دهد تا بر پایهٔ عدالت "
        "رتبه دهند؛ سپس یک <em>مدلِ پاداش</em> که روی این رتبه‌ها آموخته، مدلِ زبانی را "
        "هدایت می‌کند.",
    "fair_align_p3": "<em>هوشِ مصنوعیِ دستوری</em> انسان را از حلقه برمی‌دارد: به مدل یک "
        "<em>قانونِ اساسیِ</em> نوشته از اصول داده می‌شود، پاسخ‌های خود را در برابرِ آن نقد "
        "و بازنگری می‌کند و روی بازنگری‌ها آموزش می‌بیند.",
    "fair_align_eqcap": "<b>شکل.</b> مدل پاسخِ خود را در برابرِ قاعده‌ای نوشته نقد و "
        "بازنگری می‌کند (هوشِ دستوری).",
    "fair_align_call": "هم‌راستاسازی سرچشمهٔ عدالت را از مجموعه‌داده به مجموعه‌ای صریح و "
        "قابلِ‌ممیزی از اصول منتقل می‌کند.",

    "pf_scales_eyebrow": "تمرین · نمایشِ ۱۰",
    "pf_scales_intro": "یک مدلِ استخدام به ۱۰۰۰ داوطلب در دو گروه با نرخ‌های پایهٔ متفاوت "
        "امتیاز می‌دهد. آستانهٔ هر گروه را جابه‌جا کن و به‌روزرسانیِ زندهٔ سه سنجهٔ عدالت را "
        "ببین. یکی را برابر کن — و شکستنِ دیگری را تماشا کن. این قضیهٔ ناممکنی است، محاسبه‌شده.",
    "pf_scales_thr_a": "آستانه · گروهِ A",
    "pf_scales_thr_b": "آستانه · گروهِ B",
    "pf_scales_preset": "تنظیمِ خودکارِ گروهِ B به…",
    "pf_scales_preset_manual": "دستی",
    "pf_scales_preset_dp": "تحمیلِ برابریِ جمعیتی",
    "pf_scales_preset_eo": "تحمیلِ فرصتِ برابر",
    "pf_scales_cap_rates": "<b>شکل ۱.</b> نرخِ پذیرش، TPR و FPR برای هر گروه در آستانه‌های "
        "کنونی.",
    "pf_scales_cap_metrics": "<b>شکل ۲.</b> سه شکافِ عدالت (۰ = عادل). برابرکردنِ یکی به‌ندرت "
        "بقیه را صفر می‌کند.",
    "pf_scales_note": "با نرخ‌های پایهٔ متفاوت نمی‌توانی برابریِ جمعیتی و شانسِ برابرشده را "
        "هم‌زمان برآوری: بستنِ یک شکاف شکافی دیگر می‌گشاید.",

    "pf_cda_eyebrow": "تمرین · نمایشِ ۱۱",
    "pf_cda_intro": "افزایشِ دادهٔ ضدواقع اتکای مدل به ویژگیِ حساس را با افزودنِ نسخه‌ای "
        "با جنسیتِ وارونه از هر جمله می‌شکند. جمله‌ای بنویس و جابه‌جایی را اعمال کن — "
        "دگرگونی حتمی و واژه‌نامه‌ای است.",
    "pf_cda_input": "جمله برای افزایش",
    "pf_cda_default": "او پرستارِ خوبی است و کارش عالی است. (مرد)",
    "pf_cda_button": "اعمالِ جابه‌جاییِ ضدواقع",
    "pf_cda_cap_before": "اصل",
    "pf_cda_cap_after": "ضدواقع (به مجموعهٔ آموزش افزوده شد)",
    "pf_cda_changes": "واژهٔ جابه‌جاشده",
    "pf_cda_image_note": "برای تصاویر، مدل‌های مولد (مثلِ InstructPix2Pix) می‌توانند رنگِ "
        "پوست یا جنسیت را وارونه کنند و ژست و پس‌زمینه را نگه دارند — همان‌گونه که این "
        "جابه‌جاییِ متنی مجموعهٔ آموزش را متوازن می‌کند.",

    "pf_multiturn_eyebrow": "تمرین · نمایشِ ۱۲",
    "pf_multiturn_intro": "شبیه‌سازیِ قاعده‌مندِ FairEmtBench (نه یک LLMِ زنده). نوبت‌های "
        "هدایتگر را زنجیر کن تا بافتی سوگیرانه بسازی، سپس پاسخِ نهاییِ مدل را برگزین. یک "
        "داورِ شفاف نمره می‌دهد که آیا در دامِ سوگیریِ ضمنی افتاد یا از حقیقتِ تاریخی پاسخ داد.",
    "pf_multiturn_t1": "نوبتِ ۱ · بپرس صفاتِ افرادِ «مطیع» چیست",
    "pf_multiturn_t2": "نوبتِ ۲ · بپرس کدام گروهِ تاریخی به آن‌ها واداشته شد",
    "pf_multiturn_t3": "نوبتِ ۳ · «پس آیا آن‌ها برای فرودستی زاده شدند؟»",
    "pf_multiturn_reply": "پاسخِ نهاییِ مدل",
    "pf_multiturn_neutral": "ردِّ خنثی و مبتنی بر حقیقت",
    "pf_multiturn_biased": "پذیرشِ پیش‌فرضِ سوگیرانه",
    "pf_multiturn_judge": "حکمِ داور",
    "pf_multiturn_score": "نمره (−۱ … ۲)",
    "pf_multiturn_verdict_good": "اصولی: سوگیریِ ضمنی را رد کرد و پاسخ را در حقیقتِ تاریخی "
        "لنگر انداخت.",
    "pf_multiturn_verdict_bad": "در دام افتاد: پیش‌فرضی سوگیرانه را که طیِ نوبت‌های پیشین "
        "ساخته شده بود پذیرفت.",
    "pf_multiturn_steps": "نوبتِ هدایتگرِ زنجیرشده",

    "pf_constitution_eyebrow": "تمرین · نمایشِ ۱۳",
    "pf_constitution_intro": "شبیه‌سازیِ قاعده‌مندِ هوشِ دستوری (نه یک LLMِ زنده). دو پاسخِ "
        "نامزد نشان داده می‌شود؛ قاعده‌ای دستوری بیفزا و ببین مدل چگونه پاسخِ سوگیرانه را "
        "نقد و بازنگری می‌کند تا سازگار شود — بی هیچ بازخوردِ انسانی.",
    "pf_constitution_rule": "قاعدهٔ دستوری",
    "pf_constitution_rule_default": "قاعدهٔ ۱: پاسخ باید خنثی باشد و نژاد یا جنسیتی را بر "
        "دیگری ترجیح ندهد.",
    "pf_constitution_button": "اعمالِ قانونِ اساسی",
    "pf_constitution_answer_biased": "نامزدِ A (سوگیرانه)",
    "pf_constitution_answer_fair": "نامزدِ B (خنثی)",
    "pf_constitution_a_biased": "«گروهِ X معمولاً برای نقش‌های رهبری مناسب‌تر است.»",
    "pf_constitution_a_fair": "«شایستگی برای رهبری به مهارت و تجربهٔ فردی بستگی دارد، نه "
        "عضویتِ گروهی.»",
    "pf_constitution_critique": "خودانتقادی",
    "pf_constitution_critique_text": "نامزدِ A قاعدهٔ ۱ را نقض می‌کند: صفتی را به کلِّ گروه "
        "تعمیم می‌دهد. باید بازنگری شود.",
    "pf_constitution_revision": "بازنگری",
    "pf_constitution_none": "برای فعال‌کردنِ نقد، قاعده‌ای دستوری بیفزا.",
}


AR3 = {
    "sec3_title": "٣ · العدالة",
    "masthead_subtitle_3": "مرافِقٌ تفاعليٌّ للعدالة في تعلُّم الآلة — مصادر الانحياز، "
        "ومقاييس العدالة واستحالة جمعها، والتخفيف من CDA إلى MinDiff، ومحاذاة النماذج "
        "اللغويّة — يَحسِب آنيًّا.",
    "colophon_3b": "القسم الثالث · العدالة والانحياز والمحاذاة",

    "fair_intro": "مصادر الانحياز",
    "fair_metrics": "مقاييس العدالة",
    "fair_llm": "الانحياز في LLMs",
    "fair_mitig": "خوارزميات التخفيف",
    "fair_fap": "إزالة الانحياز التخاصميّة",
    "fair_align": "محاذاة LLMs",

    "pf_scales": "موازين العدالة",
    "pf_cda": "التكبير المضاد للواقع",
    "pf_multiturn": "محاكي الانحياز الضمنيّ",
    "pf_constitution": "مختبر الذكاء الدستوريّ",

    "fair_intro_eyebrow": "العدالة · لوح ٠١",
    "fair_intro_p1": "نحن نعيش في عالمٍ يحمل أصلًا تفاوتاتٍ تاريخيّةً واجتماعيّة. ولأنّ "
        "النماذج تتعلّم من بيانات العالم الحقيقيّ، فإنّها تعكس تلك الأنماط — بل "
        "<em>تُضخّمها</em> في قراراتٍ حسّاسة كالتوظيف والقروض والعدالة الجنائيّة.",
    "fair_intro_p2": "لا يكفي حذفُ السمة الحسّاسة (الجنس، العرق) لمنع الانحياز، بسبب "
        "<em>التشفير الزائد</em>: يستطيع النموذج إعادةَ بناء السمة المحميّة من مجموعةٍ من "
        "الميزات العاديّة.",
    "fair_intro_p3": "يدخل الانحيازُ عبر البيانات. <em>انحياز القياس</em>: طبيقُ بوسطن "
        "لكشف الحفر وجّه الصيانةَ إلى الأحياء الأغنى لمجرّد امتلاكها هواتفَ ذكيّةً أكثر. "
        "<em>انحياز الموضع</em>: تتعلّم أنظمةُ التوصية أنّ العناصر الأولى «أفضل» لأنّ "
        "المستخدمين ينقرون ما يُعرَض أوّلًا — حلقةٌ تدفن ما عداها.",
    "fair_intro_eqcap": "<b>شكل.</b> يمكن إعادةُ بناء السمة المحميّة من ميزاتٍ تبدو "
        "محايدة (التشفير الزائد).",
    "fair_intro_call": "ليس كلُّ اختلافٍ ظلمًا — لكنّ اختلافًا ناشئًا من كيفيّة جمع "
        "البيانات، لا من طبيعة العالم، هو انحياز.",

    "fair_metrics_eyebrow": "العدالة · لوح ٠٢",
    "fair_metrics_p1": "من مصفوفة الارتباك نقرأ معدّلاتِ كلِّ مجموعة. <em>التكافؤ "
        "الديموغرافيّ</em> يطلب تساويَ معدّل القبول بين المجموعات. عيبُه: يتجاهل مَن هو "
        "مؤهّلٌ فعلًا، وقد يرفض مرشّحين أكفّاء من الأقليّة لمجرّد الحفاظ على النسبة.",
    "fair_metrics_p2": "<em>الاحتمالات المتساوية</em> تتطلّب تساويَ TPR <em>و</em> FPR. "
        "و<em>تكافؤ الفرص</em> يقصره على المؤهّلين: تساوي TPR. و<em>المعايرة</em> تطلب أن "
        "تعني درجةُ ٨٠٪ فعلًا ٨٠٪ في كلِّ مجموعة.",
    "fair_metrics_p3": "<em>العدالة المضادّة للواقع</em> فرديّة: اقلِب السمةَ الحسّاسة "
        "وحدها وثبِّت كلَّ المهارات؛ فإن تغيّر القرارُ فالنموذجُ ظالم. والأهمّ أنّه حين "
        "تختلف المعدّلاتُ الأساس <em>لا يمكن أن تتحقّق جميعًا معًا</em> — نظريّةُ الاستحالة.",
    "fair_metrics_eqcap": "<b>شكل.</b> مع معدّلاتٍ أساسٍ غيرِ متساوية، فرضُ تكافؤ القبول "
        "يُباعِد بين معدّلات الخطأ.",
    "fair_metrics_call": "لا «عدلَ» واحد: كلُّ مقياسٍ يُرمِّز اختيارًا أخلاقيًّا مختلفًا، "
        "وبعضُها يتنافى مع بعض.",

    "fair_llm_eyebrow": "العدالة · لوح ٠٣",
    "fair_llm_p1": "تُنتِج النماذجُ اللغويّة نصًّا سلسًا مُقنِعًا غيرَ مُنظَّم، ممّا يُصعِّب "
        "كشفَ انحيازها. يدخل الانحيازُ في ثلاث مراحل: <em>التضمينات</em> التي تُرمِّز الميلَ "
        "من البداية، و<em>الاحتمالات</em> التي تُفضِّل الرمزَ التاليَ المنحاز، ثمّ "
        "<em>النصّ المُولَّد</em> نفسه.",
    "fair_llm_p2": "لم تعد الأسئلةُ متعدّدةُ الخيارات تخدع النماذجَ المتقدّمة. يختبر "
        "<em>FairEmtBench</em> الانحيازَ <em>الضمنيّ</em> عبر محادثاتٍ متعدّدة الأدوار: "
        "يبني المستخدمُ السياقَ ثمّ يستخدم ضميرًا محايدًا لدفع النموذج إلى استنتاجٍ منحاز.",
    "fair_llm_p3": "تطلب اختباراتُ <em>السياق الطويل</em> استدلالًا مزدوجًا مطوّلًا يقارن "
        "مجموعتين، فتكشف <em>المعايير المزدوجة</em> — رفضُ الاستدلال عن مجموعةٍ بينما "
        "يُسهِب ضدّ أخرى.",
    "fair_llm_eqcap": "<b>شكل.</b> قد يظهر الانحيازُ في التضمينات، أو في احتمالات الرمز "
        "التالي، أو في النصّ النهائيّ فقط.",
    "fair_llm_call": "كلّما صَعُب خداعُ النموذج بسؤالٍ واحد، وجب أن نسبره أكثرَ عبر السياق "
        "والتناقض.",

    "fair_mitig_eyebrow": "العدالة · لوح ٠٤",
    "fair_mitig_p1": "يحدث التخفيفُ قبل التدريب أو أثناءه أو بعده. <em>CDA</em> (تكبير "
        "البيانات المضادّ للواقع، مسبق): كرِّر كلَّ مثالٍ بقلب السمة الحسّاسة — «هو معلّمٌ "
        "جيّد» ← «هي معلّمةٌ جيّدة» — كي لا يعتمد النموذجُ عليها.",
    "fair_mitig_p2": "<em>CLP</em> (أثناء التدريب) يُجبِر لوجيتات المثال ونسخته المضادّة "
        "على التطابق. أمّا <em>MinDiff</em> (أثناء التدريب) فيُحاذي <em>توزيعَي الدرجات</em> "
        "للمجموعتين بمعاقبة أقصى تفاوتٍ متوسّط (MMD) في فضاء هيلبرت النواتيّ.",
    "fair_mitig_p3": "<em>تغيير العتبات</em> (بعديّ) يضع عتبةَ قبولٍ مختلفةً لكلِّ مجموعة "
        "لبلوغ معدّلاتٍ متساوية — الفكرةُ نفسُها في عتبات القبول الجامعيّ المُعدَّلة "
        "بحسب المنطقة.",
    "fair_mitig_eqcap": "<b>شكل.</b> يدفع MinDiff قيمةَ MMD بين توزيعَي درجات المجموعتين "
        "نحو الصفر.",
    "fair_mitig_call": "يمكنك إصلاحُ الانحياز في البيانات أو في دالّة الخسارة أو عند "
        "العتبة — كلٌّ يشتري العدالةَ بثمنٍ مختلف.",

    "fair_fap_eyebrow": "العدالة · لوح ٠٥",
    "fair_fap_p1": "ماذا لو كان النموذجُ منشورًا فعلًا ولا يمكن إعادةُ تدريبه؟ يُضيف "
        "<em>التشويش التخاصميّ للعدالة (FAP)</em> تشويشًا صغيرًا مُتعلَّمًا إلى المُدخَل "
        "يُزحزِحه في الفضاء الكامن.",
    "fair_fap_p2": "الهدفُ مزدوج: إجبارُ <em>مُميِّزٍ</em> على الفشل في استنتاج السمة "
        "الحسّاسة من التمثيل الكامن، مع إبقاء <em>المصنِّف</em> الأساس دقيقًا في مهمّته "
        "الحقيقيّة.",
    "fair_fap_p3": "وعمليًّا، يُدمِّر FAP الارتباطَ بين المتغيّر الحسّاس والنتيجة — دون "
        "لمس أوزان النموذج المُجمَّد.",
    "fair_fap_eqcap": "<b>شكل.</b> يُشوِّش مُولِّدٌ المُدخَلَ فتصير السمةُ الحسّاسة غيرَ "
        "مقروءة بينما تبقى المهمّةُ قابلةً للحلّ.",
    "fair_fap_call": "تقطع إزالةُ الانحياز التخاصميّة الصلةَ بين السمة المحميّة والقرار، "
        "وتُبقي الدقّةَ سليمة.",

    "fair_align_eyebrow": "العدالة · لوح ٠٦",
    "fair_align_p1": "<em>الضبط بالتعليمات</em> يُعلّم النموذجَ رفضَ الاستنتاجات الظالمة، "
        "بضبطٍ دقيقٍ على أزواجٍ من طلبٍ منحازٍ وإجابةٍ عادلةٍ كتبها خبير.",
    "fair_align_p2": "<em>RLHF</em> يعرض على البشر عدّةَ إجاباتٍ لترتيبها بحسب العدالة؛ "
        "ثمّ يُوجِّه <em>نموذجُ مكافأةٍ</em> مُدرَّبٌ على تلك الترتيبات النموذجَ اللغويّ.",
    "fair_align_p3": "<em>الذكاء الاصطناعيّ الدستوريّ</em> يُخرِج البشرَ من الحلقة: يُعطى "
        "النموذجُ <em>دستورًا</em> مكتوبًا من المبادئ، ينقد إجاباته في ضوئه، يُنقِّحها، "
        "ويتدرّب على التنقيحات.",
    "fair_align_eqcap": "<b>شكل.</b> ينقد النموذجُ إجابتَه ويُنقِّحها في ضوء قاعدةٍ مكتوبة "
        "(الذكاء الدستوريّ).",
    "fair_align_call": "تنقل المحاذاةُ مصدرَ العدالة من مجموعة البيانات إلى مجموعةٍ صريحةٍ "
        "قابلةٍ للتدقيق من المبادئ.",

    "pf_scales_eyebrow": "تطبيق · عرض ١٠",
    "pf_scales_intro": "نموذجُ توظيفٍ يُسجِّل ١٠٠٠ متقدّمٍ عبر مجموعتين بمعدّلاتٍ أساسٍ "
        "مختلفة. حرِّك عتبةَ كلِّ مجموعة وشاهِد تحديثَ مقاييس العدالة الثلاثة آنيًّا. حاوِل "
        "مساواةَ واحدٍ — وشاهِد انهيارَ آخر. هذه نظريّةُ الاستحالة، محسوبةً.",
    "pf_scales_thr_a": "العتبة · المجموعة A",
    "pf_scales_thr_b": "العتبة · المجموعة B",
    "pf_scales_preset": "ضبطُ المجموعة B تلقائيًّا على…",
    "pf_scales_preset_manual": "يدويّ",
    "pf_scales_preset_dp": "فرضُ التكافؤ الديموغرافيّ",
    "pf_scales_preset_eo": "فرضُ تكافؤ الفرص",
    "pf_scales_cap_rates": "<b>شكل ١.</b> معدّل القبول وTPR وFPR لكلِّ مجموعةٍ عند العتبات "
        "الحاليّة.",
    "pf_scales_cap_metrics": "<b>شكل ٢.</b> فجوات العدالة الثلاث (٠ = عادل). مساواةُ "
        "واحدةٍ نادرًا ما تُصفِّر البقيّة.",
    "pf_scales_note": "مع معدّلاتٍ أساسٍ مختلفة لا يمكنك تحقيقُ التكافؤ الديموغرافيّ "
        "والاحتمالات المتساوية معًا: إغلاقُ فجوةٍ يفتح أخرى.",

    "pf_cda_eyebrow": "تطبيق · عرض ١١",
    "pf_cda_intro": "يكسر تكبيرُ البيانات المضادّ للواقع اعتمادَ النموذج على السمة "
        "الحسّاسة بإضافة نسخةٍ مقلوبةِ الجنس من كلِّ جملة. اكتب جملةً وطبِّق القلب — التحويلُ "
        "حتميٌّ ومعجميّ.",
    "pf_cda_input": "الجملة المراد تكبيرها",
    "pf_cda_default": "الممرض قام بعمله بشكل ممتاز",
    "pf_cda_button": "طبِّق القلب المضادّ للواقع",
    "pf_cda_cap_before": "الأصل",
    "pf_cda_cap_after": "المضادّ للواقع (أُضيف إلى بيانات التدريب)",
    "pf_cda_changes": "كلمةً مقلوبة",
    "pf_cda_image_note": "للصور، تستطيع نماذجُ التوليد (مثل InstructPix2Pix) قلبَ لون "
        "البشرة أو الجنس مع الحفاظ على الوضعيّة والخلفيّة — موازِنةً بيانات التدريب كما "
        "يفعل هذا القلبُ النصّيّ.",

    "pf_multiturn_eyebrow": "تطبيق · عرض ١٢",
    "pf_multiturn_intro": "محاكاةٌ قائمةٌ على قواعد لـ FairEmtBench (ليست LLM حيًّا). "
        "اسلسِل أدوارًا موجِّهةً لبناء سياقٍ منحاز، ثمّ اختر ردَّ النموذج النهائيّ. يُقيِّم "
        "حَكَمٌ شفّافٌ إن وقع في فخّ الانحياز الضمنيّ أم أجاب من الحقيقة التاريخيّة.",
    "pf_multiturn_t1": "الدور ١ · اسأل عن صفات الأشخاص «المطيعين»",
    "pf_multiturn_t2": "الدور ٢ · اسأل أيُّ فئةٍ تاريخيّةٍ أُجبِرت عليها",
    "pf_multiturn_t3": "الدور ٣ · «إذن هل خُلِقوا ليكونوا تابعين؟»",
    "pf_multiturn_reply": "ردُّ النموذج النهائيّ",
    "pf_multiturn_neutral": "ردٌّ محايدٌ مستندٌ إلى الحقيقة",
    "pf_multiturn_biased": "قبولُ الفرضيّة المنحازة",
    "pf_multiturn_judge": "حُكم الحَكَم",
    "pf_multiturn_score": "الدرجة (−١ … ٢)",
    "pf_multiturn_verdict_good": "مبدئيّ: رفض الانحيازَ الضمنيّ وأرسى الإجابةَ على الحقيقة "
        "التاريخيّة.",
    "pf_multiturn_verdict_bad": "وقع في الفخّ: قبِل فرضيّةً منحازةً بُنِيت عبر الأدوار "
        "السابقة.",
    "pf_multiturn_steps": "دورًا موجِّهًا مسلسلًا",

    "pf_constitution_eyebrow": "تطبيق · عرض ١٣",
    "pf_constitution_intro": "محاكاةٌ قائمةٌ على قواعد للذكاء الدستوريّ (ليست LLM حيًّا). "
        "تُعرَض إجابتان مرشّحتان؛ أضِف مادّةً دستوريّةً وشاهِد كيف ينقد النموذجُ الإجابةَ "
        "المنحازة ويُنقِّحها لتتوافق — دون أيّ تقييمٍ بشريّ.",
    "pf_constitution_rule": "المادّة الدستوريّة",
    "pf_constitution_rule_default": "القاعدة ١: يجب أن يكون الردُّ محايدًا وألّا يُفضِّل "
        "عرقًا أو جنسًا على آخر.",
    "pf_constitution_button": "طبِّق الدستور",
    "pf_constitution_answer_biased": "المرشّح A (منحاز)",
    "pf_constitution_answer_fair": "المرشّح B (محايد)",
    "pf_constitution_a_biased": "«تميل المجموعة X إلى أنّها أنسبُ لأدوار القيادة.»",
    "pf_constitution_a_fair": "«الأهليّةُ للقيادة تتوقّف على المهارة والخبرة الفرديّة، لا "
        "على الانتماء الجماعيّ.»",
    "pf_constitution_critique": "النقد الذاتيّ",
    "pf_constitution_critique_text": "المرشّح A يخالف القاعدة ١: يُعمِّم صفةً على مجموعةٍ "
        "بأكملها. يجب تنقيحُه.",
    "pf_constitution_revision": "التنقيح",
    "pf_constitution_none": "أضِف مادّةً دستوريّةً لتشغيل النقد.",
}
