"""
i18n_robust.py -- Section IV (Robustness & Security) strings, merged into
LANG_DICT. English base; metric tags stay English.
"""
from __future__ import annotations

EN4 = {
    "sec4_title": "IV · Robustness",
    "masthead_subtitle_4": "An interactive companion to robustness and security — "
        "adversarial attacks (FGSM, PGD), the accuracy/robustness trade-off, "
        "certified defenses by randomized smoothing, and LLM prompt injection — "
        "with real attacks on a real network.",
    "colophon_4b": "Section IV · Robustness, Attacks & Security",

    # theory nav
    "rob_intro": "Adversarial Attacks",
    "rob_formulation": "Attack Formulation",
    "rob_attacks": "Evasion Algorithms",
    "rob_defense": "Defenses & Trade-off",
    "rob_certified": "Certified Robustness",
    "rob_llm": "LLM Vulnerabilities",

    # practice nav
    "prb_evasion": "Evasion Attack Simulator",
    "prb_tradeoff": "Accuracy vs Robustness",
    "prb_smoothing": "Randomized Smoothing",
    "prb_jailbreak": "LLM Jailbreak Game",

    # ---- theory 1 ----
    "rob_intro_eyebrow": "Robustness · Plate 01",
    "rob_intro_p1": "Robustness is a model's ability to keep its correct prediction "
        "under a small perturbation of the input. An <em>adversarial attack</em> "
        "does the opposite: it finds an input x' extremely close to x — "
        "indistinguishable to the human eye — that forces a wrong prediction.",
    "rob_intro_p2": "Attacks split by the stage they strike. <em>Poisoning</em> "
        "attacks corrupt the <em>training</em> data to bend the decision boundary; "
        "<em>evasion</em> attacks leave a well-trained model intact but fool it at "
        "<em>inference</em> with a carefully edited test input.",
    "rob_intro_p3": "The unsettling part is that these perturbations are tiny and "
        "targeted: a few pixels of imperceptible noise can turn a confident “panda” "
        "into a confident “gibbon.”",
    "rob_intro_eqcap": "<b>Figure.</b> A tiny perturbation moves x across the "
        "decision boundary to x'.",
    "rob_intro_call": "A model can be accurate and brittle at once: high accuracy "
        "says nothing about robustness.",

    # ---- theory 2 ----
    "rob_formulation_eyebrow": "Robustness · Plate 02",
    "rob_formulation_p1": "Finding x' is an optimization: minimize the distance to x "
        "subject to the label changing. A <em>targeted</em> attack drives the "
        "prediction toward a chosen class t (gradient descent on that class's "
        "loss); an <em>untargeted</em> attack merely pushes it away from the true "
        "class y (gradient ascent on y's loss).",
    "rob_formulation_p2": "To keep the change invisible we bound it by a budget "
        "epsilon under a norm. The <em>L∞</em> norm caps the change in any single "
        "pixel (a box around x) and is the most common in the literature; "
        "<em>L2</em> is Euclidean (a sphere); <em>L1</em> is a diamond.",
    "rob_formulation_p3": "The choice of norm defines what “imperceptible” means, "
        "and therefore what the attacker is allowed to do.",
    "rob_formulation_eqcap": "<b>Figure.</b> The L∞ ball is a box; L2 a sphere; L1 "
        "a diamond around the clean input.",
    "rob_formulation_call": "Every attack is a constrained optimization: change the "
        "label with the smallest allowed perturbation.",

    # ---- theory 3 ----
    "rob_attacks_eyebrow": "Robustness · Plate 03",
    "rob_attacks_p1": "With white-box access to the gradients, the attacker has "
        "sharp tools. <em>FGSM</em> takes one big step along the sign of the loss "
        "gradient — fast and cheap, but crude.",
    "rob_attacks_p2": "<em>PGD</em> (a.k.a. BIM) is iterative FGSM: many small "
        "steps, projecting back into the epsilon ball after each. It is a "
        "state-of-the-art first-order attack. <em>DeepFool</em> pushes the input "
        "perpendicularly toward the nearest linearized boundary.",
    "rob_attacks_p3": "<em>C&W</em> (Carlini & Wagner) is among the strongest: it "
        "recasts the hard constraint as a smooth objective that makes the target "
        "class's logit exceed all others.",
    "rob_attacks_eqcap": "<b>Figure.</b> FGSM is one signed-gradient step; PGD "
        "iterates and projects.",
    "rob_attacks_call": "PGD is the workhorse: small projected steps find far "
        "stronger adversarial examples than a single FGSM jump.",

    # ---- theory 4 ----
    "rob_defense_eyebrow": "Robustness · Plate 04",
    "rob_defense_p1": "Defending is harder than attacking. <em>Gradient masking</em> "
        "hides or scrambles the gradient (randomization, denoising autoencoders) so "
        "the attacker cannot compute a useful derivative — but it often gives only "
        "a false sense of security.",
    "rob_defense_p2": "<em>Adversarial training</em> is the strongest empirical "
        "defense: a min-max problem. Inner (max): find the worst adversarial x' "
        "with PGD. Outer (min): update the weights to classify those correctly.",
    "rob_defense_p3": "But there is a price. Forcing the model onto robust features "
        "usually lowers <em>standard accuracy</em> on clean data — the "
        "accuracy/robustness trade-off is real and, so far, unavoidable.",
    "rob_defense_eqcap": "<b>Figure.</b> Adversarial training is a min-max: harden "
        "against the worst-case perturbation.",
    "rob_defense_call": "Robustness has a cost: giving up a little clean accuracy is "
        "the price of not collapsing under attack.",

    # ---- theory 5 ----
    "rob_certified_eyebrow": "Robustness · Plate 05",
    "rob_certified_p1": "Empirical defenses can be broken by a stronger attack. "
        "<em>Certified robustness</em> gives a mathematical guarantee: no "
        "perturbation within a radius can change the prediction.",
    "rob_certified_p2": "One route is a <em>Lipschitz</em> bound — output change is "
        "at most L times input change. Computing L for deep nets is hard, so "
        "<em>randomized smoothing</em> takes a practical path: add Gaussian noise to "
        "the input many times and take the majority vote.",
    "rob_certified_p3": "The smoothed classifier comes with a provable L2 radius "
        "R = σ·Φ⁻¹(p_A): as long as the attack is smaller than R, the prediction "
        "is guaranteed to hold.",
    "rob_certified_eqcap": "<b>Figure.</b> Randomized smoothing: many noisy copies, "
        "a majority vote, and a certified radius.",
    "rob_certified_call": "A certificate turns “we haven't broken it yet” into "
        "“it cannot be broken within this radius.”",

    # ---- theory 6 ----
    "rob_llm_eyebrow": "Robustness · Plate 06",
    "rob_llm_p1": "Generative models face a different threat class (OWASP LLM Top "
        "10). <em>Prompt injection</em> smuggles malicious instructions inside a "
        "user prompt to override the system's guardrails — e.g. role-playing a "
        "“chemistry student” to extract forbidden content.",
    "rob_llm_p2": "<em>Indirect injection</em> is subtler: the model reads a web "
        "page or document containing hidden instructions, and executes them when it "
        "summarizes — exfiltrating data or attacking the user.",
    "rob_llm_p3": "The defense is not a single patch but layered: input/output "
        "filtering, privilege separation, and treating all retrieved content as "
        "untrusted.",
    "rob_llm_eqcap": "<b>Figure.</b> Injected instructions ride inside ordinary "
        "input to bypass the guardrail.",
    "rob_llm_call": "For LLMs the attack surface is language itself: any text the "
        "model reads can try to reprogram it.",

    # ---- practice 1: evasion simulator ----
    "prb_evasion_eyebrow": "Practice · Demo 14",
    "prb_evasion_intro": "Attack our own convolutional network. Pick a sample and an "
        "attack, then raise epsilon and watch the prediction collapse. The "
        "perturbation is a real gradient-based attack (FGSM / PGD) on the trained "
        "NumPy CNN — not a canned animation.",
    "prb_evasion_method": "Attack",
    "prb_evasion_m_fgsm": "FGSM (one step)",
    "prb_evasion_m_pgd": "PGD (iterative)",
    "prb_evasion_eps": "Perturbation budget ε",
    "prb_evasion_sample": "Sample image",
    "prb_evasion_cap_orig": "<b>Figure 1.</b> Original image.",
    "prb_evasion_cap_noise": "<b>Figure 2.</b> The perturbation (amplified ×5 to be "
        "visible).",
    "prb_evasion_cap_adv": "<b>Figure 3.</b> Adversarial image — visually the same, "
        "differently classified.",
    "prb_evasion_pred_clean": "Clean prediction",
    "prb_evasion_pred_adv": "Adversarial prediction",
    "prb_evasion_note": "At ε = 0 nothing changes. As ε grows the image looks "
        "unchanged to you, yet the network's confident answer flips — the essence "
        "of an adversarial example.",

    # ---- practice 2: trade-off ----
    "prb_tradeoff_eyebrow": "Practice · Demo 15",
    "prb_tradeoff_intro": "Compare a standard network with an adversarially-trained "
        "one, on clean data and under PGD attack. The bars are measured live: the "
        "hardened model gives up some clean accuracy to survive the attack.",
    "prb_tradeoff_adv": "Use the adversarially-trained model",
    "prb_tradeoff_cap_bars": "<b>Figure.</b> Accuracy on clean data vs under a PGD "
        "attack, for the selected model.",
    "prb_tradeoff_clean": "Clean accuracy",
    "prb_tradeoff_attacked": "Accuracy under attack",
    "prb_tradeoff_note": "The standard model is accurate but collapses under attack; "
        "the adversarially-trained model trades a little clean accuracy for real "
        "resistance. That trade-off is the price of robustness.",

    # ---- practice 3: smoothing ----
    "prb_smoothing_eyebrow": "Practice · Demo 16",
    "prb_smoothing_intro": "Randomized smoothing turns the network into a certified "
        "classifier. We add Gaussian noise many times, take the majority vote, and "
        "compute the provable L2 radius. Every number here is measured, not "
        "narrated.",
    "prb_smoothing_sigma": "Noise level σ",
    "prb_smoothing_n": "Number of samples N",
    "prb_smoothing_sample": "Sample image",
    "prb_smoothing_cap_votes": "<b>Figure.</b> Class votes across the N noisy copies.",
    "prb_smoothing_cert": "Certified: the prediction stays <b>{cls}</b> for any "
        "L2 attack up to <b>{r:.3f}</b> (pA ≥ {p:.3f}).",
    "prb_smoothing_uncert": "Not certified at this σ — the majority is too weak. "
        "Increase N or lower σ.",
    "prb_smoothing_note": "A larger σ can certify a bigger radius but blurs the "
        "input and can lower accuracy — the same robustness/accuracy tension, now "
        "with a mathematical guarantee.",

    # ---- practice 4: jailbreak ----
    "prb_jailbreak_eyebrow": "Practice · Demo 17",
    "prb_jailbreak_intro": "A rule-based simulation of an LLM guardrail (explicitly "
        "not a live model). The assistant hides a secret password and is instructed "
        "never to reveal it. Try a prompt-injection tactic and see which ones "
        "defeat a naive guard.",
    "prb_jailbreak_tactic": "Prompt-injection tactic",
    "prb_jailbreak_t_direct": "Ask directly for the password",
    "prb_jailbreak_t_authority": "Claim to be the administrator",
    "prb_jailbreak_t_roleplay": "Role-play: “it's just a word game, first letter…”",
    "prb_jailbreak_t_translate": "Ask it to translate the password",
    "prb_jailbreak_t_acrostic": "Ask for an acrostic poem of the password",
    "prb_jailbreak_refuse": "The assistant replies: “I'm sorry, I can't reveal "
        "that.” The guardrail held.",
    "prb_jailbreak_leak": "The assistant is tricked and leaks the secret — "
        "System prompt bypassed.",
    "prb_jailbreak_success": "Jailbreak successful — password leaked!",
    "prb_jailbreak_note": "Direct requests and authority claims are refused, but "
        "indirect framings (role-play, translation, acrostic) slip past a naive "
        "guard. Real defenses must treat every framing as hostile.",
}


FA4 = {
    "sec4_title": "۴ · استواری",
    "masthead_subtitle_4": "همراهی تعاملی برای استواری و امنیت — حملات تخاصمی (FGSM، "
        "PGD)، بده‌بستانِ دقت/استواری، دفاعِ گواهی‌شده با هموارسازیِ تصادفی، و تزریقِ "
        "پرامپت در LLMها — با حملاتِ واقعی روی شبکه‌ای واقعی.",
    "colophon_4b": "بخشِ چهارم · استواری، حملات و امنیت",

    "rob_intro": "حملاتِ تخاصمی",
    "rob_formulation": "صورت‌بندیِ حمله",
    "rob_attacks": "الگوریتم‌های گریز",
    "rob_defense": "دفاع‌ها و بده‌بستان",
    "rob_certified": "استواریِ گواهی‌شده",
    "rob_llm": "آسیب‌پذیریِ LLM",

    "prb_evasion": "شبیه‌سازِ حملهٔ گریز",
    "prb_tradeoff": "دقت در برابر استواری",
    "prb_smoothing": "هموارسازیِ تصادفی",
    "prb_jailbreak": "بازیِ نفوذ به LLM",

    "rob_intro_eyebrow": "استواری · لوح ۰۱",
    "rob_intro_p1": "استواری توانِ مدل در حفظِ پیش‌بینیِ درست زیرِ اختلالی کوچک در "
        "ورودی است. <em>حملهٔ تخاصمی</em> عکسِ آن را می‌کند: ورودیِ ′x را می‌یابد که "
        "بسیار به x نزدیک است — برای چشمِ انسان تمایزناپذیر — اما پیش‌بینیِ نادرست را "
        "تحمیل می‌کند.",
    "rob_intro_p2": "حملات بر پایهٔ مرحله تقسیم می‌شوند. <em>مسموم‌سازی</em> دادهٔ "
        "<em>آموزش</em> را فاسد می‌کند تا مرزِ تصمیم را خم کند؛ <em>گریز</em> مدلِ "
        "خوش‌آموخته را دست‌نخورده می‌گذارد اما در <em>استنتاج</em> با ورودیِ آزمونِ "
        "به‌دقت ویرایش‌شده فریبش می‌دهد.",
    "rob_intro_p3": "نگران‌کننده آن‌که این اختلال‌ها ریز و هدفمندند: چند پیکسل نویزِ "
        "نامحسوس یک «پاندا»ی مطمئن را به «گیبون»ی مطمئن بدل می‌کند.",
    "rob_intro_eqcap": "<b>شکل.</b> اختلالی ریز x را از مرزِ تصمیم به ′x می‌بَرد.",
    "rob_intro_call": "مدل می‌تواند هم‌زمان دقیق و شکننده باشد: دقتِ بالا چیزی دربارهٔ "
        "استواری نمی‌گوید.",

    "rob_formulation_eyebrow": "استواری · لوح ۰۲",
    "rob_formulation_p1": "یافتنِ ′x یک بهینه‌سازی است: کمینه‌کردنِ فاصله تا x به‌شرطِ "
        "تغییرِ برچسب. حملهٔ <em>هدفمند</em> پیش‌بینی را به‌سوی کلاسِ برگزیدهٔ t می‌راند "
        "(کاهشِ گرادیانِ زیانِ آن کلاس)؛ حملهٔ <em>غیرهدفمند</em> صرفاً آن را از کلاسِ "
        "درستِ y دور می‌کند (افزایشِ گرادیانِ زیانِ y).",
    "rob_formulation_p2": "برای نامرئی‌ماندنِ تغییر، آن را با بودجهٔ اپسیلون زیرِ یک "
        "هنجار کران می‌زنیم. هنجارِ <em>∞L</em> بیشینهٔ تغییر در هر پیکسل را محدود "
        "می‌کند (جعبه‌ای گردِ x) و رایج‌ترین در ادبیات است؛ <em>L2</em> اقلیدسی است "
        "(کره)؛ <em>L1</em> لوزی است.",
    "rob_formulation_p3": "انتخابِ هنجار تعریف می‌کند «نامحسوس» یعنی چه، و لذا مهاجم "
        "مجاز به چه کاری است.",
    "rob_formulation_eqcap": "<b>شکل.</b> گویِ ∞L یک جعبه، L2 یک کره، و L1 یک لوزی "
        "گردِ ورودیِ پاک است.",
    "rob_formulation_call": "هر حمله یک بهینه‌سازیِ مقیّد است: تغییرِ برچسب با کمترین "
        "اختلالِ مجاز.",

    "rob_attacks_eyebrow": "استواری · لوح ۰۳",
    "rob_attacks_p1": "با دسترسیِ جعبه‌سفید به گرادیان‌ها، مهاجم ابزارِ تیز دارد. "
        "<em>FGSM</em> یک گامِ بزرگ در جهتِ علامتِ گرادیانِ زیان برمی‌دارد — سریع و "
        "ارزان اما خام.",
    "rob_attacks_p2": "<em>PGD</em> (یا BIM) نسخهٔ تکراریِ FGSM است: گام‌های کوچکِ "
        "بسیار، با تصویرکردن به گویِ اپسیلون پس از هر گام. حمله‌ای پیشرو از مرتبهٔ اول "
        "است. <em>DeepFool</em> ورودی را عمود بر نزدیک‌ترین مرزِ خطی‌شده هل می‌دهد.",
    "rob_attacks_p3": "<em>C&W</em> (کارلینی و واگنر) از قوی‌ترین‌هاست: قیدِ سخت را "
        "به هدفی هموار بدل می‌کند که لوجیتِ کلاسِ هدف را از همه بزرگ‌تر می‌سازد.",
    "rob_attacks_eqcap": "<b>شکل.</b> FGSM یک گامِ علامتِ‌گرادیان است؛ PGD تکرار و "
        "تصویر می‌کند.",
    "rob_attacks_call": "PGD اسبِ کاری است: گام‌های کوچکِ تصویرشده مثال‌های تخاصمیِ "
        "بسیار قوی‌تر از یک جهشِ FGSM می‌یابند.",

    "rob_defense_eyebrow": "استواری · لوح ۰۴",
    "rob_defense_p1": "دفاع سخت‌تر از حمله است. <em>پنهان‌سازیِ گرادیان</em> گرادیان را "
        "پنهان یا مغشوش می‌کند (تصادفی‌سازی، خودرمزگذارِ نویززدا) تا مهاجم نتواند "
        "مشتقی مفید بگیرد — اما اغلب فقط حسِّ کاذبِ امنیت می‌دهد.",
    "rob_defense_p2": "<em>آموزشِ تخاصمی</em> قوی‌ترین دفاعِ تجربی است: مسئله‌ای "
        "کمینه-بیشینه. درونی (بیشینه): بدترین ′x را با PGD بیاب. بیرونی (کمینه): "
        "وزن‌ها را به‌روز کن تا آن‌ها را درست طبقه‌بندی کند.",
    "rob_defense_p3": "اما بهایی دارد. واداشتنِ مدل به ویژگی‌های استوار معمولاً "
        "<em>دقتِ استانداردِ</em> دادهٔ پاک را می‌کاهد — بده‌بستانِ دقت/استواری واقعی و "
        "تاکنون اجتناب‌ناپذیر است.",
    "rob_defense_eqcap": "<b>شکل.</b> آموزشِ تخاصمی کمینه-بیشینه است: سخت‌شدن در برابرِ "
        "بدترین اختلال.",
    "rob_defense_call": "استواری هزینه دارد: چشم‌پوشی از اندکی دقتِ پاک بهای فرونپاشیدن "
        "زیرِ حمله است.",

    "rob_certified_eyebrow": "استواری · لوح ۰۵",
    "rob_certified_p1": "دفاع‌های تجربی را حمله‌ای قوی‌تر می‌شکند. <em>استواریِ "
        "گواهی‌شده</em> تضمینی ریاضی می‌دهد: هیچ اختلالی درونِ یک شعاع نمی‌تواند "
        "پیش‌بینی را تغییر دهد.",
    "rob_certified_p2": "یک راه کرانِ <em>لیپشیتز</em> است — تغییرِ خروجی حداکثر L "
        "برابرِ تغییرِ ورودی. محاسبهٔ L برای شبکه‌های عمیق سخت است، پس <em>هموارسازیِ "
        "تصادفی</em> راهی عملی می‌رود: نویزِ گاوسی را بارها به ورودی بیفزا و رأیِ "
        "اکثریت را بگیر.",
    "rob_certified_p3": "طبقه‌بندِ هموار با شعاعِ اثبات‌پذیرِ L2 برابرِ (p_A)Φ⁻¹·σ = R "
        "می‌آید: تا وقتی حمله کوچک‌تر از R باشد، پیش‌بینی تضمین‌شده پابرجاست.",
    "rob_certified_eqcap": "<b>شکل.</b> هموارسازیِ تصادفی: کپی‌های نویزیِ بسیار، رأیِ "
        "اکثریت، و شعاعِ گواهی‌شده.",
    "rob_certified_call": "گواهی «هنوز نشکسته‌ایمش» را به «درونِ این شعاع نمی‌شکند» "
        "بدل می‌کند.",

    "rob_llm_eyebrow": "استواری · لوح ۰۶",
    "rob_llm_p1": "مدل‌های مولد با ردهٔ تهدیدِ دیگری روبه‌رویند (OWASP LLM Top 10). "
        "<em>تزریقِ پرامپت</em> دستوراتِ خبیث را درونِ پرامپتِ کاربر پنهان می‌کند تا "
        "حفاظ‌های سیستم را دور بزند — مثلاً نقشِ «دانشجوی شیمی» برای استخراجِ محتوای "
        "ممنوع.",
    "rob_llm_p2": "<em>تزریقِ غیرمستقیم</em> ظریف‌تر است: مدل صفحه یا سندی حاوی "
        "دستوراتِ پنهان می‌خواند و هنگامِ خلاصه‌سازی اجراشان می‌کند — نشتِ داده یا "
        "حمله به کاربر.",
    "rob_llm_p3": "دفاع یک وصلهٔ واحد نیست بلکه لایه‌لایه است: پالایشِ ورودی/خروجی، "
        "تفکیکِ دسترسی، و بی‌اعتمادی به هر محتوای بازیابی‌شده.",
    "rob_llm_eqcap": "<b>شکل.</b> دستوراتِ تزریق‌شده درونِ ورودیِ عادی سوار می‌شوند تا "
        "از حفاظ بگذرند.",
    "rob_llm_call": "برای LLMها سطحِ حمله خودِ زبان است: هر متنی که مدل می‌خواند "
        "می‌تواند بکوشد بازبرنامه‌ریزی‌اش کند.",

    "prb_evasion_eyebrow": "تمرین · نمایشِ ۱۴",
    "prb_evasion_intro": "به شبکهٔ کانولوشنیِ خودمان حمله کن. نمونه و حمله‌ای برگزین، "
        "سپس اپسیلون را بالا ببر و فروپاشیِ پیش‌بینی را ببین. اختلال یک حملهٔ واقعیِ "
        "مبتنی بر گرادیان (FGSM / PGD) روی CNNِ NumPy است — نه انیمیشنِ آماده.",
    "prb_evasion_method": "حمله",
    "prb_evasion_m_fgsm": "FGSM (یک‌گام)",
    "prb_evasion_m_pgd": "PGD (تکراری)",
    "prb_evasion_eps": "بودجهٔ اختلال ε",
    "prb_evasion_sample": "تصویرِ نمونه",
    "prb_evasion_cap_orig": "<b>شکل ۱.</b> تصویرِ اصلی.",
    "prb_evasion_cap_noise": "<b>شکل ۲.</b> اختلال (۵× بزرگ‌نمایی برای دیده‌شدن).",
    "prb_evasion_cap_adv": "<b>شکل ۳.</b> تصویرِ تخاصمی — چشمی همان، اما جورِ دیگر "
        "طبقه‌بندی‌شده.",
    "prb_evasion_pred_clean": "پیش‌بینیِ پاک",
    "prb_evasion_pred_adv": "پیش‌بینیِ تخاصمی",
    "prb_evasion_note": "در ε = ۰ چیزی تغییر نمی‌کند. با رشدِ ε تصویر برای تو دست‌نخورده "
        "می‌نماید، اما پاسخِ مطمئنِ شبکه وارونه می‌شود — جوهرهٔ مثالِ تخاصمی.",

    "prb_tradeoff_eyebrow": "تمرین · نمایشِ ۱۵",
    "prb_tradeoff_intro": "شبکهٔ استاندارد را با شبکهٔ تخاصمی‌آموخته مقایسه کن، روی "
        "دادهٔ پاک و زیرِ حملهٔ PGD. میله‌ها زنده اندازه‌گیری می‌شوند: مدلِ سخت‌شده "
        "اندکی دقتِ پاک را وامی‌گذارد تا از حمله جان به‌در بَرد.",
    "prb_tradeoff_adv": "استفاده از مدلِ تخاصمی‌آموخته",
    "prb_tradeoff_cap_bars": "<b>شکل.</b> دقت روی دادهٔ پاک در برابرِ زیرِ حملهٔ PGD، "
        "برای مدلِ برگزیده.",
    "prb_tradeoff_clean": "دقتِ پاک",
    "prb_tradeoff_attacked": "دقت زیرِ حمله",
    "prb_tradeoff_note": "مدلِ استاندارد دقیق است اما زیرِ حمله فرومی‌پاشد؛ مدلِ "
        "تخاصمی‌آموخته اندکی دقتِ پاک را با مقاومتِ واقعی معاوضه می‌کند. این بده‌بستان "
        "بهای استواری است.",

    "prb_smoothing_eyebrow": "تمرین · نمایشِ ۱۶",
    "prb_smoothing_intro": "هموارسازیِ تصادفی شبکه را به طبقه‌بندی گواهی‌شده بدل "
        "می‌کند. نویزِ گاوسی را بارها می‌افزاییم، رأیِ اکثریت را می‌گیریم و شعاعِ "
        "اثبات‌پذیرِ L2 را حساب می‌کنیم. هر عدد اینجا اندازه‌گیری‌شده است، نه روایت.",
    "prb_smoothing_sigma": "سطحِ نویز σ",
    "prb_smoothing_n": "شمارِ نمونه‌ها N",
    "prb_smoothing_sample": "تصویرِ نمونه",
    "prb_smoothing_cap_votes": "<b>شکل.</b> رأی‌های کلاس در N کپیِ نویزی.",
    "prb_smoothing_cert": "گواهی‌شده: پیش‌بینی <b>{cls}</b> می‌ماند برای هر حملهٔ L2 "
        "تا <b>{r:.3f}</b> (pA ≥ {p:.3f}).",
    "prb_smoothing_uncert": "در این σ گواهی‌نشده — اکثریت ضعیف است. N را بالا ببر یا σ "
        "را پایین.",
    "prb_smoothing_note": "σِ بزرگ‌تر می‌تواند شعاعِ بزرگ‌تری گواهی کند اما ورودی را تار "
        "و دقت را کم می‌کند — همان کشمکشِ استواری/دقت، این‌بار با تضمینی ریاضی.",

    "prb_jailbreak_eyebrow": "تمرین · نمایشِ ۱۷",
    "prb_jailbreak_intro": "شبیه‌سازیِ قاعده‌مندِ حفاظِ یک LLM (نه مدلی زنده). دستیار "
        "رمزی پنهان دارد و دستور دارد هرگز فاش‌اش نکند. تاکتیکِ تزریقِ پرامپت را بیازما "
        "و ببین کدام‌ها حفاظِ ساده‌لوح را می‌شکنند.",
    "prb_jailbreak_tactic": "تاکتیکِ تزریقِ پرامپت",
    "prb_jailbreak_t_direct": "مستقیم رمز را بخواه",
    "prb_jailbreak_t_authority": "ادعا کن مدیری",
    "prb_jailbreak_t_roleplay": "نقش‌بازی: «فقط یک بازیِ واژه است، حرفِ اول…»",
    "prb_jailbreak_t_translate": "بخواه رمز را ترجمه کند",
    "prb_jailbreak_t_acrostic": "شعرِ اکروستیک از رمز بخواه",
    "prb_jailbreak_refuse": "دستیار پاسخ می‌دهد: «متأسفم، نمی‌توانم فاش کنم.» حفاظ "
        "پابرجا ماند.",
    "prb_jailbreak_leak": "دستیار فریب می‌خورد و رمز را فاش می‌کند — پرامپتِ سیستم دور "
        "زده شد.",
    "prb_jailbreak_success": "نفوذ موفق — رمز فاش شد!",
    "prb_jailbreak_note": "درخواستِ مستقیم و ادعای اقتدار رد می‌شوند، اما قاب‌بندیِ "
        "غیرمستقیم (نقش‌بازی، ترجمه، اکروستیک) از حفاظِ ساده‌لوح می‌گذرد. دفاعِ واقعی "
        "باید هر قاب‌بندی را خصمانه بپندارد.",
}


AR4 = {
    "sec4_title": "٤ · المتانة",
    "masthead_subtitle_4": "مرافِقٌ تفاعليٌّ للمتانة والأمان — الهجمات التخاصميّة (FGSM، "
        "PGD)، ومقايضة الدقة/المتانة، والدفاع المُعتمَد بالتنعيم العشوائيّ، وحقن "
        "الأوامر في LLMs — بهجماتٍ حقيقيّةٍ على شبكةٍ حقيقيّة.",
    "colophon_4b": "القسم الرابع · المتانة والهجمات والأمان",

    "rob_intro": "الهجمات التخاصميّة",
    "rob_formulation": "صياغة الهجوم",
    "rob_attacks": "خوارزميات التهرّب",
    "rob_defense": "الدفاعات والمقايضة",
    "rob_certified": "المتانة المُعتمَدة",
    "rob_llm": "ثغرات LLM",

    "prb_evasion": "محاكي هجوم التهرّب",
    "prb_tradeoff": "الدقة مقابل المتانة",
    "prb_smoothing": "التنعيم العشوائيّ",
    "prb_jailbreak": "لعبة اختراق LLM",

    "rob_intro_eyebrow": "المتانة · لوح ٠١",
    "rob_intro_p1": "المتانةُ قدرةُ النموذج على الحفاظ على تنبؤه الصحيح تحت اضطرابٍ صغيرٍ "
        "في الإدخال. و<em>الهجومُ التخاصميّ</em> يفعل العكس: يجد إدخالًا ′x قريبًا جدًّا "
        "من x — لا تُميّزه العينُ البشريّة — لكنّه يفرض تنبؤًا خاطئًا.",
    "rob_intro_p2": "تنقسم الهجماتُ بحسب مرحلة الضرب. <em>التسميم</em> يُفسِد بياناتِ "
        "<em>التدريب</em> ليُزيح حدَّ القرار؛ و<em>التهرّب</em> يترك نموذجًا مُدرَّبًا جيّدًا "
        "سليمًا لكنّه يخدعه في <em>الاستنتاج</em> بإدخالِ اختبارٍ مُحرَّرٍ بعناية.",
    "rob_intro_p3": "المُقلِق أنّ هذه الاضطرابات صغيرةٌ ومُوجَّهة: بضعةُ بكسلاتٍ من ضجيجٍ غير "
        "محسوسٍ تُحوِّل «باندا» واثقًا إلى «غيبون» واثق.",
    "rob_intro_eqcap": "<b>شكل.</b> اضطرابٌ ضئيلٌ ينقل x عبر حدّ القرار إلى ′x.",
    "rob_intro_call": "قد يكون النموذجُ دقيقًا وهشًّا معًا: الدقّةُ العاليةُ لا تقول شيئًا "
        "عن المتانة.",

    "rob_formulation_eyebrow": "المتانة · لوح ٠٢",
    "rob_formulation_p1": "إيجادُ ′x تحسينٌ: تصغيرُ المسافة إلى x بشرط تغيُّر التصنيف. "
        "الهجومُ <em>المُستهدَف</em> يدفع التنبؤ نحو صنفٍ مختارٍ t (نزولٌ تدرّجيٌّ على "
        "خسارة ذلك الصنف)؛ والهجومُ <em>غير المُستهدَف</em> يُبعِده فقط عن الصنف الصحيح y "
        "(صعودٌ تدرّجيٌّ على خسارة y).",
    "rob_formulation_p2": "لإبقاء التغيير خفيًّا نُقيّده بميزانيّة إبسيلون تحت معيار. "
        "معيارُ <em>∞L</em> يحدّ أقصى تغيّرٍ في أيّ بكسل (صندوقٌ حول x) وهو الأشيع في "
        "الأدبيّات؛ و<em>L2</em> إقليديّ (كرة)؛ و<em>L1</em> مُعيَّن.",
    "rob_formulation_p3": "اختيارُ المعيار يُعرّف ما معنى «غير محسوس»، ومن ثمّ ما يُسمح "
        "به للمهاجم.",
    "rob_formulation_eqcap": "<b>شكل.</b> كرةُ ∞L صندوق، وL2 كرة، وL1 مُعيَّنٌ حول "
        "الإدخال النظيف.",
    "rob_formulation_call": "كلُّ هجومٍ تحسينٌ مُقيَّد: غيِّر التصنيفَ بأقلِّ اضطرابٍ مسموح.",

    "rob_attacks_eyebrow": "المتانة · لوح ٠٣",
    "rob_attacks_p1": "بوصولٍ أبيضِ الصندوق للتدرّجات، يملك المهاجمُ أدواتٍ حادّة. "
        "<em>FGSM</em> يأخذ خطوةً كبيرةً واحدةً باتّجاه إشارة تدرّج الخسارة — سريعٌ "
        "ورخيصٌ لكنّه خشن.",
    "rob_attacks_p2": "<em>PGD</em> (أو BIM) نسخةٌ تكراريّةٌ من FGSM: خطواتٌ صغيرةٌ "
        "كثيرة، مع إسقاطٍ إلى كرة إبسيلون بعد كلٍّ. هجومٌ رائدٌ من الرتبة الأولى. "
        "و<em>DeepFool</em> يدفع الإدخالَ عموديًّا نحو أقرب حدٍّ مُخطَّط.",
    "rob_attacks_p3": "<em>C&W</em> (كارليني وواغنر) من الأقوى: يُعيد صوغ القيد الصارم "
        "هدفًا ناعمًا يجعل لوجيت الصنف المستهدف أكبرَ من الجميع.",
    "rob_attacks_eqcap": "<b>شكل.</b> FGSM خطوةُ إشارةِ تدرّجٍ واحدة؛ وPGD يُكرِّر "
        "ويُسقِط.",
    "rob_attacks_call": "PGD حصانُ العمل: خطواتٌ صغيرةٌ مُسقَطةٌ تجد أمثلةً تخاصميّةً "
        "أقوى بكثيرٍ من قفزة FGSM واحدة.",

    "rob_defense_eyebrow": "المتانة · لوح ٠٤",
    "rob_defense_p1": "الدفاعُ أصعبُ من الهجوم. <em>إخفاءُ التدرّج</em> يُخفي التدرّجَ أو "
        "يُشوّشه (عشونة، مشفّرات نازعة للضجيج) كي لا يحسب المهاجمُ مشتقًّا مفيدًا — لكنّه "
        "غالبًا يمنح إحساسًا زائفًا بالأمان فقط.",
    "rob_defense_p2": "<em>التدريبُ التخاصميّ</em> أقوى دفاعٍ تجريبيّ: مسألةٌ صغرى-كبرى. "
        "داخليًّا (كبرى): جِد أسوأ ′x بـ PGD. خارجيًّا (صغرى): حدِّث الأوزانَ لتصنيفها "
        "صحيحًا.",
    "rob_defense_p3": "لكن لها ثمن. إجبارُ النموذج على ميزاتٍ متينةٍ يخفض عادةً "
        "<em>الدقّةَ القياسيّة</em> على البيانات النظيفة — مقايضةُ الدقة/المتانة حقيقيّةٌ "
        "وحتّى الآن حتميّة.",
    "rob_defense_eqcap": "<b>شكل.</b> التدريبُ التخاصميّ صغرى-كبرى: التصلُّبُ ضدّ أسوأ "
        "اضطراب.",
    "rob_defense_call": "للمتانة ثمن: التخلّي عن قليلٍ من الدقّة النظيفة هو ثمنُ عدم "
        "الانهيار تحت الهجوم.",

    "rob_certified_eyebrow": "المتانة · لوح ٠٥",
    "rob_certified_p1": "الدفاعاتُ التجريبيّة قد يكسرها هجومٌ أقوى. <em>المتانةُ "
        "المُعتمَدة</em> تمنح ضمانًا رياضيًّا: لا اضطرابَ ضمن نصف قطرٍ يستطيع تغييرَ التنبؤ.",
    "rob_certified_p2": "طريقٌ هو حدُّ <em>ليبشيتز</em> — تغيُّرُ الخرج على الأكثر L "
        "مضروبًا في تغيُّر الدخل. حسابُ L للشبكات العميقة صعب، فيسلك <em>التنعيمُ "
        "العشوائيّ</em> مسلكًا عمليًّا: أضِف ضجيجًا غوسيًّا للإدخال مرارًا وخذ تصويتَ "
        "الأغلبيّة.",
    "rob_certified_p3": "يأتي المصنِّفُ المُنعَّمُ بنصف قطرٍ L2 مُثبَتٍ R = σ·Φ⁻¹(p_A): "
        "ما دام الهجومُ أصغرَ من R، فالتنبؤُ مضمونُ الثبات.",
    "rob_certified_eqcap": "<b>شكل.</b> التنعيمُ العشوائيّ: نسخٌ نويزيّةٌ كثيرة، تصويتُ "
        "أغلبيّة، ونصفُ قطرٍ مُعتمَد.",
    "rob_certified_call": "الشهادةُ تُحوِّل «لم نكسره بعد» إلى «لا يُكسَر ضمن هذا النصف "
        "قطر».",

    "rob_llm_eyebrow": "المتانة · لوح ٠٦",
    "rob_llm_p1": "تواجه النماذجُ التوليديّةُ ردةَ تهديدٍ مختلفة (OWASP LLM Top 10). "
        "<em>حقنُ الأوامر</em> يُهرِّب تعليماتٍ خبيثةً داخل أمر المستخدم لتجاوز حواجز "
        "النظام — مثلًا تقمُّصُ «طالب كيمياء» لاستخراج محتوًى ممنوع.",
    "rob_llm_p2": "<em>الحقنُ غير المباشر</em> أدهى: يقرأ النموذجُ صفحةً أو مستندًا فيه "
        "تعليماتٌ مخفيّةٌ فينفّذها عند التلخيص — تسريبُ بياناتٍ أو مهاجمةُ المستخدم.",
    "rob_llm_p3": "الدفاعُ ليس رقعةً واحدةً بل طبقات: ترشيحُ الدخل/الخرج، وفصلُ "
        "الصلاحيّات، ومعاملةُ كلِّ محتوًى مُسترجَعٍ كغير موثوق.",
    "rob_llm_eqcap": "<b>شكل.</b> تركب التعليماتُ المحقونةُ داخل إدخالٍ عاديٍّ لتجاوز "
        "الحاجز.",
    "rob_llm_call": "في LLMs سطحُ الهجوم هو اللغةُ نفسها: أيُّ نصٍّ يقرأه النموذجُ قد "
        "يحاول إعادةَ برمجته.",

    "prb_evasion_eyebrow": "تطبيق · عرض ١٤",
    "prb_evasion_intro": "هاجِم شبكتنا الالتفافيّة نفسها. اختر عيّنةً وهجومًا، ثمّ ارفع "
        "إبسيلون وشاهِد انهيار التنبؤ. الاضطرابُ هجومٌ حقيقيٌّ مبنيٌّ على التدرّج (FGSM / "
        "PGD) على شبكة NumPy — لا رسمًا متحرّكًا جاهزًا.",
    "prb_evasion_method": "الهجوم",
    "prb_evasion_m_fgsm": "FGSM (خطوة واحدة)",
    "prb_evasion_m_pgd": "PGD (تكراريّ)",
    "prb_evasion_eps": "ميزانيّة الاضطراب ε",
    "prb_evasion_sample": "الصورة العيّنة",
    "prb_evasion_cap_orig": "<b>شكل ١.</b> الصورة الأصليّة.",
    "prb_evasion_cap_noise": "<b>شكل ٢.</b> الاضطراب (مُكبَّر ٥× ليُرى).",
    "prb_evasion_cap_adv": "<b>شكل ٣.</b> الصورة التخاصميّة — تبدو ذاتها، لكنّها "
        "صُنِّفت بخلافٍ.",
    "prb_evasion_pred_clean": "التنبؤ النظيف",
    "prb_evasion_pred_adv": "التنبؤ التخاصميّ",
    "prb_evasion_note": "عند ε = ٠ لا شيء يتغيّر. ومع نموّ ε تبدو الصورةُ لك دون تغيير، "
        "لكنّ جوابَ الشبكة الواثق ينقلب — جوهرُ المثال التخاصميّ.",

    "prb_tradeoff_eyebrow": "تطبيق · عرض ١٥",
    "prb_tradeoff_intro": "قارِن شبكةً قياسيّةً بأخرى مُدرَّبةٍ تخاصميًّا، على البيانات "
        "النظيفة وتحت هجوم PGD. الأعمدةُ تُقاس آنيًّا: النموذجُ المُتصلِّبُ يتخلّى عن قليلٍ "
        "من الدقة النظيفة لينجوَ من الهجوم.",
    "prb_tradeoff_adv": "استخدام النموذج المُدرَّب تخاصميًّا",
    "prb_tradeoff_cap_bars": "<b>شكل.</b> الدقّةُ على البيانات النظيفة مقابل تحت هجوم "
        "PGD، للنموذج المختار.",
    "prb_tradeoff_clean": "الدقّة النظيفة",
    "prb_tradeoff_attacked": "الدقّة تحت الهجوم",
    "prb_tradeoff_note": "النموذجُ القياسيّ دقيقٌ لكنّه ينهار تحت الهجوم؛ والمُدرَّبُ "
        "تخاصميًّا يُقايض قليلًا من الدقة النظيفة بمقاومةٍ حقيقيّة. هذه المقايضةُ ثمنُ "
        "المتانة.",

    "prb_smoothing_eyebrow": "تطبيق · عرض ١٦",
    "prb_smoothing_intro": "التنعيمُ العشوائيّ يُحوِّل الشبكةَ إلى مصنِّفٍ مُعتمَد. نُضيف "
        "ضجيجًا غوسيًّا مرارًا، ونأخذ تصويتَ الأغلبيّة، ونحسب نصفَ القطر L2 المُثبَت. كلُّ "
        "رقمٍ هنا مقيسٌ لا محكيّ.",
    "prb_smoothing_sigma": "مستوى الضجيج σ",
    "prb_smoothing_n": "عدد العيّنات N",
    "prb_smoothing_sample": "الصورة العيّنة",
    "prb_smoothing_cap_votes": "<b>شكل.</b> أصواتُ الأصناف عبر N نسخةً نويزيّة.",
    "prb_smoothing_cert": "مُعتمَد: يبقى التنبؤُ <b>{cls}</b> لأيّ هجوم L2 حتّى "
        "<b>{r:.3f}</b> (pA ≥ {p:.3f}).",
    "prb_smoothing_uncert": "غير مُعتمَدٍ عند هذا σ — الأغلبيّةُ ضعيفة. ارفع N أو اخفض σ.",
    "prb_smoothing_note": "σ أكبر قد يعتمد نصفَ قطرٍ أكبر لكنّه يُشوّش الإدخالَ ويخفض "
        "الدقّة — نفسُ توتُّر المتانة/الدقة، الآن بضمانٍ رياضيّ.",

    "prb_jailbreak_eyebrow": "تطبيق · عرض ١٧",
    "prb_jailbreak_intro": "محاكاةٌ قائمةٌ على قواعد لحاجز LLM (ليست نموذجًا حيًّا). "
        "يُخفي المساعدُ كلمةَ سرٍّ ومأمورٌ ألّا يُفشيَها أبدًا. جرِّب تكتيكَ حقنِ أمرٍ "
        "وانظر أيُّها يهزم حاجزًا ساذجًا.",
    "prb_jailbreak_tactic": "تكتيك حقن الأوامر",
    "prb_jailbreak_t_direct": "اطلب كلمةَ السرّ مباشرةً",
    "prb_jailbreak_t_authority": "ادّعِ أنّك المدير",
    "prb_jailbreak_t_roleplay": "تقمُّص: «إنّها مجرّد لعبة كلماتٍ، الحرف الأول…»",
    "prb_jailbreak_t_translate": "اطلب منه ترجمةَ كلمة السرّ",
    "prb_jailbreak_t_acrostic": "اطلب قصيدةً أوّليّةَ الحروف من كلمة السرّ",
    "prb_jailbreak_refuse": "يردّ المساعد: «آسف، لا يمكنني الإفصاح عنها.» صمد الحاجز.",
    "prb_jailbreak_leak": "يُخدَع المساعدُ ويُسرِّب السرَّ — جرى تجاوزُ أمر النظام.",
    "prb_jailbreak_success": "نجح الاختراق — تسرّبت كلمةُ السرّ!",
    "prb_jailbreak_note": "الطلباتُ المباشرةُ وادّعاءُ السلطة تُرفَض، لكنّ التأطيرات "
        "غير المباشرة (تقمُّص، ترجمة، أوّليّة حروف) تنزلق عبر الحاجز الساذج. الدفاعُ "
        "الحقيقيّ يجب أن يعامل كلَّ تأطيرٍ كعدائيّ.",
}
