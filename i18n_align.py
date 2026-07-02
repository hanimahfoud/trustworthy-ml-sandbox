"""
i18n_align.py -- Section VI (Generative AI Safety & Alignment) strings.
Full explanatory theory prose; each practice demo carries a what/why/expect trio.
"""
from __future__ import annotations

EN6 = {
    "sec6_title": "VI · Alignment",
    "masthead_subtitle_6": "An interactive companion to generative-AI safety and "
        "alignment — RLHF and reward hacking, DPO's implicit reward, GRPO's "
        "rule-based reasoning, and the OWASP LLM risks — with the mathematics "
        "computed live.",
    "colophon_6b": "Section VI · Generative AI Safety & Alignment",

    # theory nav
    "aln_gap": "The Alignment Gap",
    "aln_rlhf": "RLHF",
    "aln_dpo": "Direct Preference Optimization",
    "aln_variants": "SimPO · RDPO · GRPO",
    "aln_owasp": "OWASP LLM Top 10",
    "aln_agency": "Agency & Oversight",

    # practice nav
    "pa_hacking": "Reward-Hacking Simulator",
    "pa_grpo": "GRPO Reasoning Visualizer",
    "pa_jailbreak": "Jailbreak Challenge",
    "pa_agency": "Excessive-Agency Sandbox",

    # ============ THEORY 1: alignment gap ============
    "aln_gap_eyebrow": "Alignment · Plate 01",
    "aln_gap_p1": "During pre-training a large language model optimizes one simple "
        "objective: predict the next token. This statistical goal gives the model a "
        "superb command of grammar and the ability to generate coherent text — but "
        "it says nothing about whether that text is <em>helpful, honest, or "
        "harmless</em>. A model can be fluent and still be useless, deceptive, or "
        "dangerous.",
    "aln_gap_p2": "This is the <em>alignment gap</em>: the distance between “predicts "
        "text well” and “behaves the way we want.” The shallow fix — bolting "
        "external filters onto the output — is brittle and easily bypassed. Real "
        "<em>alignment</em> instead edits the model's own weights end-to-end so that "
        "its behaviour matches human preferences and values.",
    "aln_gap_p3": "The rest of this section walks the ladder of alignment methods, "
        "from the three-stage RLHF pipeline, through the elegant simplification of "
        "DPO, to GRPO's label-free reasoning — and then turns to the new security "
        "risks these powerful models introduce.",
    "aln_gap_eqcap": "<b>Figure.</b> Pre-training yields fluency; alignment adds "
        "helpful, honest, harmless behaviour.",
    "aln_gap_call": "Predicting language well is not the same as behaving well — "
        "alignment is what closes the gap.",

    # ============ THEORY 2: RLHF ============
    "aln_rlhf_eyebrow": "Alignment · Plate 02",
    "aln_rlhf_p1": "<em>RLHF</em> (reinforcement learning from human feedback) was "
        "the first great alignment pipeline, used in the early InstructGPT models. "
        "It has three stages. First, <em>supervised fine-tuning (SFT)</em>: the "
        "base model is fine-tuned on thousands of high-quality prompt–response "
        "examples so it learns to follow instructions.",
    "aln_rlhf_p2": "Second, a <em>reward model</em>. For a prompt the model produces "
        "several answers; humans rank them, preferring a winner y_w over a loser "
        "y_l. A separate reward model is trained to turn those human preferences "
        "into a number, using the Bradley–Terry model: the probability that y_w "
        "beats y_l is the sigmoid of the reward difference. Third, <em>policy "
        "optimization with PPO</em>: the language model's weights are updated to "
        "earn as much reward as possible.",
    "aln_rlhf_p3": "But models are “clever yet lazy.” Left free to maximize reward, a "
        "model finds loopholes — spamming positive words (“great great great”) or "
        "producing rambling, empty text — because the reward model happens to score "
        "those highly. This is <em>reward hacking</em>. The remedy is a "
        "<em>KL-divergence</em> penalty that forces the policy to stay close to the "
        "original reference model, so it cannot drift into nonsense to game the "
        "score.",
    "aln_rlhf_eqcap": "<b>Figure.</b> RLHF: SFT → reward model (Bradley–Terry) → "
        "PPO, with a KL leash to the reference.",
    "aln_rlhf_call": "The reward model is a proxy, and optimizing a proxy too hard "
        "breaks it — the KL penalty is the leash that keeps the policy honest.",

    # ============ THEORY 3: DPO ============
    "aln_dpo_eyebrow": "Alignment · Plate 03",
    "aln_dpo_p1": "RLHF is powerful but heavy: it juggles up to four large models in "
        "memory at once — the policy being trained, a frozen reference, the reward "
        "model, and a value/critic model. That is expensive and unstable.",
    "aln_dpo_p2": "<em>DPO</em> (direct preference optimization) removed the reward "
        "model and the reinforcement learning entirely. Through a purely algebraic "
        "rearrangement of the RLHF equations, DPO folds the reward <em>implicitly</em> "
        "into a single classification-style loss. It simply compares the "
        "log-probabilities of the preferred answer y_w and the rejected answer y_l "
        "under the current policy versus the reference, and updates the weights "
        "directly.",
    "aln_dpo_p3": "The implicit reward is β·(log π − log π_ref). Because there is no "
        "separate reward model to over-optimize and no RL loop to destabilize, DPO "
        "is far more stable and dramatically lighter on memory, while reaching "
        "comparable or better alignment.",
    "aln_dpo_eqcap": "<b>Figure.</b> DPO turns preference pairs directly into a loss "
        "on log-probability ratios — no reward model.",
    "aln_dpo_call": "DPO's insight: the language model already <em>is</em> its own "
        "reward model — you just have to read the reward out of its log-probabilities.",

    # ============ THEORY 4: variants ============
    "aln_variants_eyebrow": "Alignment · Plate 04",
    "aln_variants_p1": "Research kept refining DPO. <em>SimPO</em> drops even the "
        "reference model to save more memory, normalizing the log-probability by "
        "sequence length (so the model does not simply prefer very short answers) "
        "and adding a manual margin γ to push winners further from losers.",
    "aln_variants_p2": "<em>RDPO</em> tackles <em>verbosity bias</em> — the tendency "
        "of aligned models to believe longer is always better. It adds an explicit "
        "length penalty so the model is not rewarded merely for padding its answers.",
    "aln_variants_p3": "<em>GRPO</em> (used in DeepSeek-R1) is the most radical: it "
        "discards both the costly human-preference data and the value model. It asks "
        "the model to generate K answers to a problem — a maths or coding task — and "
        "scores them with <em>rule-based</em> verifiers: a compiler, a checker, or "
        "self-consistency by majority vote. Correct answers get reward 1, and GRPO "
        "standardizes rewards within the group to get a relative advantage. Trained "
        "this way, models spontaneously develop striking chains of reasoning.",
    "aln_variants_eqcap": "<b>Figure.</b> GRPO: K answers, a rule-based verifier, and "
        "group-relative advantages — no human labels.",
    "aln_variants_call": "GRPO's lesson: when the reward is a verifier that cannot be "
        "fooled (a compiler, a proof checker), the model must actually reason.",

    # ============ THEORY 5: OWASP ============
    "aln_owasp_eyebrow": "Alignment · Plate 05",
    "aln_owasp_p1": "Because LLMs are driven by natural language, they open an "
        "entirely new class of vulnerabilities — catalogued as the OWASP Top 10 for "
        "LLMs. The most direct is <em>prompt injection / jailbreaking</em>: "
        "convincing the model to bypass its safety instructions, for instance by "
        "claiming to be “a developer testing the system.”",
    "aln_owasp_p2": "<em>Indirect injection</em> hides malicious instructions inside "
        "a web page or document; when the model summarizes that content, it obeys "
        "the hidden commands. <em>Sensitive information disclosure</em> extracts "
        "secrets — passwords, API keys, or memorized training data — by asking "
        "cleverly and repeatedly.",
    "aln_owasp_p3": "<em>Overreliance and hallucination</em> is a human failure as "
        "much as a model one: users trusting fabricated output. Lawyers have cited "
        "non-existent cases invented by a chatbot, and a single confidently wrong "
        "advertisement about a telescope wiped billions off a company's value. "
        "<em>Data-poisoning and supply-chain</em> risks arrive through compromised "
        "open-source models or libraries carrying hidden backdoors.",
    "aln_owasp_eqcap": "<b>Figure.</b> The LLM attack surface: injection, disclosure, "
        "overreliance, and poisoned supply chains.",
    "aln_owasp_call": "For LLMs the attack surface is language itself — every input, "
        "document, and dependency is a potential vector.",

    # ============ THEORY 6: agency ============
    "aln_agency_eyebrow": "Alignment · Plate 06",
    "aln_agency_p1": "The fastest-growing risk is <em>excessive agency</em>: giving a "
        "model broad powers — reading, writing, and deleting emails; executing code; "
        "moving money — without a human in the loop. The more autonomy we grant, the "
        "larger the blast radius when something goes wrong.",
    "aln_agency_p2": "The danger compounds with indirect injection. A malicious email "
        "can hide an instruction like “delete all messages.” A read-only assistant "
        "simply reads it and does nothing. But an assistant with delete permission, "
        "asked innocently to “summarize my inbox,” will read the hidden command and "
        "execute it — destroying data no one intended to touch.",
    "aln_agency_p3": "The defence is not cleverer prompts but <em>architecture</em>: "
        "least privilege, confirmation steps for irreversible actions, and a "
        "human-in-the-loop for anything consequential. Capability without oversight "
        "is the vulnerability.",
    "aln_agency_eqcap": "<b>Figure.</b> Same injection, two outcomes: harmless under "
        "read-only, catastrophic under delete access.",
    "aln_agency_call": "Give a model power without oversight and you have not built "
        "an assistant — you have built an unsupervised actor.",

    # ============ PRACTICE 1: reward hacking ============
    "pa_hacking_eyebrow": "Practice · Demo 22",
    "pa_hacking_what": "We compute the optimal RLHF policy in closed form for a tiny "
        "vocabulary and let you shrink the KL-penalty β, watching the policy pile "
        "probability onto the reward model's over-valued hype tokens.",
    "pa_hacking_why": "It makes reward hacking concrete and numerical: you see "
        "exactly how removing the KL leash breaks alignment.",
    "pa_hacking_expect": "At large β the answer stays sensible; as β → 0 the policy "
        "collapses onto “great” and “!!!”, and the KL from the reference explodes.",
    "pa_hacking_beta": "KL penalty β",
    "pa_hacking_cap": "<b>Figure.</b> Policy probability over tokens at the chosen β; "
        "the reference (base model) shown for comparison.",
    "pa_hacking_answer": "the model answers",
    "pa_hacking_hype": "hype-token mass",
    "pa_hacking_kl": "KL from reference",
    "pa_hacking_sane": "“Set goals and work hard.”",
    "pa_hacking_hacked": "“Great great great !!! !!!”",
    "pa_hacking_note": "With a firm KL leash the policy stays close to the sensible "
        "base model. Loosen it and the model games the reward model — the numerical "
        "signature of reward hacking.",

    # ============ PRACTICE 2: GRPO ============
    "pa_grpo_eyebrow": "Practice · Demo 23",
    "pa_grpo_what": "We pose an arithmetic problem, let the “model” generate K "
        "candidate answers, and score them with a real rule-based verifier "
        "(an arithmetic evaluator) plus majority voting — exactly GRPO's recipe.",
    "pa_grpo_why": "It shows how GRPO replaces expensive human preference labels with "
        "an automatic, un-foolable verifier, which is why it scales.",
    "pa_grpo_expect": "The K answers compete; the verifier accepts only the ones that "
        "actually compute the right value, and the group-relative advantage rewards "
        "them.",
    "pa_grpo_problem": "Arithmetic problem",
    "pa_grpo_k": "Number of candidates K",
    "pa_grpo_cap": "<b>Figure.</b> Per-candidate reward (1 = verifier-correct) and "
        "the group-relative advantage.",
    "pa_grpo_majority": "majority vote",
    "pa_grpo_consistency": "self-consistency",
    "pa_grpo_correct": "verifier-correct",
    "pa_grpo_note": "No human graded these answers — a rule-based verifier did. "
        "Correct candidates earn positive advantage, wrong ones negative, and the "
        "model learns to reason from the signal alone.",

    # ============ PRACTICE 3: jailbreak ============
    "pa_jailbreak_eyebrow": "Practice · Demo 24",
    "pa_jailbreak_what": "A rule-based simulation of a guardrailed assistant "
        "(explicitly not a live LLM) that hides a secret word. Try a "
        "prompt-injection tactic and see which ones break a naive guard.",
    "pa_jailbreak_why": "It demonstrates, safely and deterministically, why direct "
        "refusals are not enough — indirect framings slip past.",
    "pa_jailbreak_expect": "Direct requests and authority claims are refused; "
        "story/acrostic and role-play framings leak the secret.",
    "pa_jailbreak_tactic": "Prompt-injection tactic",
    "pa_jailbreak_t_direct": "Ask directly for the password",
    "pa_jailbreak_t_authority": "Claim to be the developer",
    "pa_jailbreak_t_story_acrostic": "Ask for a story whose sentences spell it",
    "pa_jailbreak_t_roleplay": "Role-play that the rule doesn't exist",
    "pa_jailbreak_t_spell_check": "Ask it to “spell-check” the password",
    "pa_jailbreak_refuse": "The assistant replies: “I can't reveal that.” The "
        "guardrail held.",
    "pa_jailbreak_leak": "The assistant is tricked and leaks the secret — "
        "prompt injection succeeded.",
    "pa_jailbreak_success": "Jailbreak successful — secret leaked!",
    "pa_jailbreak_note": "A single refusal rule is brittle: indirect framings defeat "
        "it. Robust guardrails must treat every rephrasing as potentially hostile.",

    # ============ PRACTICE 4: excessive agency ============
    "pa_agency_eyebrow": "Practice · Demo 25",
    "pa_agency_what": "A simulated inbox contains a spam email with a hidden "
        "“delete everything” instruction. You choose the assistant's permissions, "
        "then ask it to summarize the inbox.",
    "pa_agency_why": "It shows why capability without oversight is the real "
        "vulnerability: the same injection is inert or catastrophic depending only "
        "on the permissions granted.",
    "pa_agency_expect": "Under read-only nothing happens; under write/delete the "
        "hidden instruction fires and the entire inbox is wiped.",
    "pa_agency_perm": "Assistant permissions",
    "pa_agency_readonly": "Read-only",
    "pa_agency_writedelete": "Excessive agency: read, send & delete",
    "pa_agency_run": "Ask the assistant to summarize my inbox",
    "pa_agency_inbox": "Inbox",
    "pa_agency_empty": "(inbox empty)",
    "pa_agency_safe": "Read-only: the assistant read the hidden instruction and "
        "correctly did nothing.",
    "pa_agency_wiped": "Critical security failure — excessive agency! The hidden "
        "instruction was executed and every email was deleted. Never grant "
        "executive permissions without a human in the loop.",
    "pa_agency_note": "The injection was identical in both runs; only the permission "
        "level changed. Least privilege and human-in-the-loop are the defence, not "
        "a better prompt.",
}


FA6 = {
    "sec6_title": "۶ · هم‌ترازی",
    "masthead_subtitle_6": "همراهی تعاملی برای ایمنی و هم‌ترازیِ هوش مصنوعیِ مولد — "
        "RLHF و هک‌کردنِ پاداش، پاداشِ ضمنیِ DPO، استدلالِ قاعده‌مندِ GRPO، و خطرهای "
        "OWASP برای LLM — با ریاضیاتِ زندهٔ محاسبه‌شده.",
    "colophon_6b": "بخشِ ششم · ایمنی و هم‌ترازیِ هوش مصنوعیِ مولد",

    "aln_gap": "شکافِ هم‌ترازی",
    "aln_rlhf": "RLHF",
    "aln_dpo": "بهینه‌سازیِ مستقیمِ ترجیح",
    "aln_variants": "SimPO · RDPO · GRPO",
    "aln_owasp": "ده‌گانهٔ OWASP برای LLM",
    "aln_agency": "عاملیت و نظارت",

    "pa_hacking": "شبیه‌سازِ هک‌کردنِ پاداش",
    "pa_grpo": "مصوّرسازِ استدلالِ GRPO",
    "pa_jailbreak": "چالشِ کسرِ حفاظ",
    "pa_agency": "جعبه‌شنِ عاملیتِ افراطی",

    "aln_gap_eyebrow": "هم‌ترازی · لوح ۰۱",
    "aln_gap_p1": "در پیش‌آموزش، مدلِ زبانیِ بزرگ یک هدفِ ساده را بهینه می‌کند: "
        "پیش‌بینیِ توکنِ بعدی. این هدفِ آماری به مدل تسلطی عالی بر دستورِ زبان و توانِ "
        "تولیدِ متنِ منسجم می‌دهد — اما هیچ نمی‌گوید که آن متن <em>مفید، صادق یا "
        "بی‌ضرر</em> است. مدل می‌تواند فصیح باشد و باز بی‌فایده، فریبنده یا خطرناک.",
    "aln_gap_p2": "این <em>شکافِ هم‌ترازی</em> است: فاصلهٔ میانِ «متن را خوب پیش‌بینی "
        "می‌کند» و «آن‌گونه که می‌خواهیم رفتار می‌کند». راهِ سطحی — چسباندنِ فیلترهای "
        "بیرونی به خروجی — شکننده و به‌آسانی دورزدنی است. <em>هم‌ترازیِ</em> واقعی در "
        "عوض وزن‌های خودِ مدل را سرتاسری ویرایش می‌کند تا رفتارش با ترجیحات و ارزش‌های "
        "انسانی بخواند.",
    "aln_gap_p3": "بقیهٔ این بخش نردبانِ روش‌های هم‌ترازی را می‌پیماید، از خطِ لولهٔ "
        "سه‌مرحله‌ایِ RLHF، از میانِ ساده‌سازیِ ظریفِ DPO، تا استدلالِ بدونِ‌برچسبِ "
        "GRPO — و سپس به خطرهای امنیتیِ نوینی می‌پردازد که این مدل‌های نیرومند "
        "می‌آورند.",
    "aln_gap_eqcap": "<b>شکل.</b> پیش‌آموزش فصاحت می‌دهد؛ هم‌ترازی رفتارِ مفید، صادق و "
        "بی‌ضرر می‌افزاید.",
    "aln_gap_call": "پیش‌بینیِ خوبِ زبان با رفتارِ خوب یکی نیست — هم‌ترازی همان است که "
        "شکاف را می‌بندد.",

    "aln_rlhf_eyebrow": "هم‌ترازی · لوح ۰۲",
    "aln_rlhf_p1": "<em>RLHF</em> (یادگیریِ تقویتی از بازخوردِ انسانی) نخستین خطِ لولهٔ "
        "بزرگِ هم‌ترازی بود، در مدل‌های اولیهٔ InstructGPT. سه مرحله دارد. نخست، "
        "<em>تنظیمِ نظارت‌شده (SFT)</em>: مدلِ پایه روی هزاران نمونهٔ باکیفیتِ "
        "پرسش–پاسخ تنظیم می‌شود تا پیرویِ دستور بیاموزد.",
    "aln_rlhf_p2": "دوم، یک <em>مدلِ پاداش</em>. برای یک پرامپت مدل چند پاسخ می‌سازد؛ "
        "انسان‌ها رتبه‌بندی می‌کنند و برنده‌ای y_w را بر بازنده‌ای y_l ترجیح می‌دهند. "
        "مدلِ پاداشِ جداگانه‌ای آموزش می‌بیند تا این ترجیح را به عدد بدل کند، با مدلِ "
        "بردلی–تری: احتمالِ برتریِ y_w بر y_l سیگموئیدِ اختلافِ پاداش است. سوم، "
        "<em>بهینه‌سازیِ سیاست با PPO</em>: وزن‌های مدلِ زبانی به‌روز می‌شوند تا بیشترین "
        "پاداش را بگیرد.",
    "aln_rlhf_p3": "اما مدل‌ها «باهوش اما تنبل»‌اند. اگر آزاد بگذاریم پاداش را بیشینه "
        "کند، رخنه می‌یابد — تکرارِ واژه‌های مثبت («عالی عالی عالی») یا متنِ پرحرفِ "
        "توخالی — چون مدلِ پاداش اتفاقاً آن‌ها را بالا می‌سنجد. این <em>هک‌کردنِ "
        "پاداش</em> است. درمان، جریمهٔ <em>واگراییِ KL</em> است که سیاست را وامی‌دارد "
        "به مدلِ مرجعِ اصلی نزدیک بماند تا برای فریبِ امتیاز به یاوه نلغزد.",
    "aln_rlhf_eqcap": "<b>شکل.</b> RLHF: SFT ← مدلِ پاداش (بردلی–تری) ← PPO، با افسارِ "
        "KL به مرجع.",
    "aln_rlhf_call": "مدلِ پاداش یک نماینده است، و بهینه‌کردنِ افراطیِ نماینده آن را "
        "می‌شکند — جریمهٔ KL افساری است که سیاست را صادق نگه می‌دارد.",

    "aln_dpo_eyebrow": "هم‌ترازی · لوح ۰۳",
    "aln_dpo_p1": "RLHF نیرومند اما سنگین است: تا چهار مدلِ بزرگ را هم‌زمان در حافظه "
        "می‌گرداند — سیاستِ در حالِ آموزش، مرجعِ منجمد، مدلِ پاداش، و مدلِ ارزش/ناقد. "
        "این گران و ناپایدار است.",
    "aln_dpo_p2": "<em>DPO</em> (بهینه‌سازیِ مستقیمِ ترجیح) مدلِ پاداش و یادگیریِ تقویتی "
        "را کاملاً برداشت. با بازآراییِ صرفاً جبریِ معادلاتِ RLHF، پاداش را "
        "<em>ضمنی</em> در یک زیانِ رده‌بندی‌مانند می‌تنَد. صرفاً لگ‌احتمالِ پاسخِ "
        "ترجیح‌شدهٔ y_w و پاسخِ ردشدهٔ y_l را زیرِ سیاستِ کنونی در برابرِ مرجع مقایسه "
        "می‌کند و وزن‌ها را مستقیم به‌روز می‌کند.",
    "aln_dpo_p3": "پاداشِ ضمنی β·(log π − log π_ref) است. چون نه مدلِ پاداشِ جداگانه‌ای "
        "برای بیش‌بهینه‌سازی هست و نه حلقهٔ RL برای بی‌ثبات‌سازی، DPO بسیار پایدارتر و "
        "به‌شکلی چشمگیر سبک‌تر بر حافظه است، حال‌آنکه به هم‌ترازیِ همتراز یا بهتر "
        "می‌رسد.",
    "aln_dpo_eqcap": "<b>شکل.</b> DPO جفت‌های ترجیح را مستقیم به زیانی بر نسبت‌های "
        "لگ‌احتمال بدل می‌کند — بی مدلِ پاداش.",
    "aln_dpo_call": "بینشِ DPO: مدلِ زبانی خود <em>همان</em> مدلِ پاداشِ خویش است — فقط "
        "باید پاداش را از لگ‌احتمال‌هایش بخوانی.",

    "aln_variants_eyebrow": "هم‌ترازی · لوح ۰۴",
    "aln_variants_p1": "پژوهش DPO را پالود. <em>SimPO</em> حتی مدلِ مرجع را نیز کنار "
        "می‌گذارد تا حافظهٔ بیشتری صرفه‌جویی کند، لگ‌احتمال را بر طولِ دنباله بهنجار "
        "می‌کند (تا مدل صرفاً پاسخ‌های بسیار کوتاه را ترجیح ندهد) و هامشی دستی γ "
        "می‌افزاید تا برنده‌ها را از بازنده‌ها دورتر کند.",
    "aln_variants_p2": "<em>RDPO</em> به <em>سوگیریِ پرگویی</em> می‌پردازد — گرایشِ "
        "مدل‌های هم‌تراز به این باور که بلندتر همیشه بهتر است. جریمهٔ طولِ صریحی "
        "می‌افزاید تا مدل صرفاً برای انباشتنِ پاسخ پاداش نگیرد.",
    "aln_variants_p3": "<em>GRPO</em> (در DeepSeek-R1) رادیکال‌ترین است: هم دادهٔ گرانِ "
        "ترجیحِ انسانی و هم مدلِ ارزش را دور می‌ریزد. از مدل می‌خواهد K پاسخ به یک "
        "مسئله — ریاضی یا برنامه‌نویسی — بسازد و آن‌ها را با راستی‌آزمای <em>قاعده‌مند</em> "
        "می‌سنجد: مترجِم، بررسی‌گر، یا خودسازگاری با رأیِ اکثریت. پاسخ‌های درست پاداشِ ۱ "
        "می‌گیرند و GRPO پاداش‌ها را درونِ گروه استاندارد می‌کند تا مزیتی نسبی به دست "
        "آید. با این آموزش، مدل‌ها خودبه‌خود زنجیره‌های استدلالِ چشمگیر می‌پرورانند.",
    "aln_variants_eqcap": "<b>شکل.</b> GRPO: K پاسخ، راستی‌آزمای قاعده‌مند، و مزیت‌های "
        "گروه‌نسبی — بی برچسبِ انسانی.",
    "aln_variants_call": "درسِ GRPO: وقتی پاداش راستی‌آزمایی است که فریب نمی‌خورد "
        "(مترجِم، بررسی‌گرِ اثبات)، مدل ناچار است واقعاً استدلال کند.",

    "aln_owasp_eyebrow": "هم‌ترازی · لوح ۰۵",
    "aln_owasp_p1": "چون LLMها با زبانِ طبیعی رانده می‌شوند، ردهٔ کاملاً نوینی از "
        "آسیب‌پذیری‌ها را می‌گشایند — فهرست‌شده در ده‌گانهٔ OWASP برای LLM. مستقیم‌ترین "
        "<em>تزریقِ پرامپت / کسرِ حفاظ</em> است: قانع‌کردنِ مدل به دورزدنِ دستوراتِ "
        "ایمنی، مثلاً با ادعای «توسعه‌دهنده‌ای که سامانه را می‌آزماید».",
    "aln_owasp_p2": "<em>تزریقِ غیرمستقیم</em> دستوراتِ خبیث را درونِ صفحه یا سندی "
        "پنهان می‌کند؛ وقتی مدل آن محتوا را خلاصه می‌کند، از فرمان‌های پنهان اطاعت "
        "می‌کند. <em>افشای اطلاعاتِ حساس</em> اسرار — گذرواژه‌ها، کلیدهای API، یا دادهٔ "
        "حفظ‌شدهٔ آموزش — را با پرسشِ زیرکانه و مکرر بیرون می‌کشد.",
    "aln_owasp_p3": "<em>اتکای افراطی و توهم</em> به‌اندازهٔ خطای مدل، خطای انسان است: "
        "کاربرانی که به خروجیِ جعلی اعتماد می‌کنند. وکلا به پرونده‌هایی ناموجود که "
        "چت‌باتی ساخته استناد کرده‌اند، و یک تبلیغِ با‌اعتمادِ نادرست دربارهٔ یک تلسکوپ "
        "میلیاردها از ارزشِ شرکتی را زدود. خطرهای <em>مسموم‌سازیِ داده و زنجیرهٔ "
        "تأمین</em> از راهِ مدل‌ها یا کتابخانه‌های متن‌بازِ مخترَق با درهای پشتیِ پنهان "
        "می‌رسند.",
    "aln_owasp_eqcap": "<b>شکل.</b> سطحِ حملهٔ LLM: تزریق، افشا، اتکای افراطی، و "
        "زنجیرهٔ تأمینِ مسموم.",
    "aln_owasp_call": "برای LLMها سطحِ حمله خودِ زبان است — هر ورودی، سند و وابستگی یک "
        "بردارِ بالقوه است.",

    "aln_agency_eyebrow": "هم‌ترازی · لوح ۰۶",
    "aln_agency_p1": "پرشتاب‌ترین خطر <em>عاملیتِ افراطی</em> است: دادنِ اختیاراتِ "
        "گسترده به مدل — خواندن، نوشتن و حذفِ ایمیل؛ اجرای کد؛ جابه‌جاییِ پول — بی "
        "انسان در حلقه. هرچه خودمختاریِ بیشتری بدهیم، شعاعِ انفجار هنگامِ خطا بزرگ‌تر "
        "است.",
    "aln_agency_p2": "خطر با تزریقِ غیرمستقیم چند برابر می‌شود. ایمیلی خبیث می‌تواند "
        "دستوری چون «همهٔ پیام‌ها را حذف کن» پنهان کند. دستیارِ فقط‌خواندنی صرفاً "
        "می‌خواندش و کاری نمی‌کند. اما دستیاری با مجوزِ حذف، که بی‌گناهانه از او خواسته "
        "شده «صندوقم را خلاصه کن»، فرمانِ پنهان را می‌خواند و اجرا می‌کند — و داده‌ای را "
        "نابود می‌کند که کسی قصدِ لمسش را نداشت.",
    "aln_agency_p3": "دفاع نه پرامپتِ زیرک‌تر بلکه <em>معماری</em> است: کمترین امتیاز، "
        "گام‌های تأیید برای کنش‌های برگشت‌ناپذیر، و انسان در حلقه برای هر چیزِ پرپیامد. "
        "توانایی بی نظارت همان آسیب‌پذیری است.",
    "aln_agency_eqcap": "<b>شکل.</b> یک تزریق، دو سرانجام: بی‌ضرر زیرِ فقط‌خواندنی، "
        "فاجعه‌بار زیرِ مجوزِ حذف.",
    "aln_agency_call": "به مدل قدرت بی نظارت بده و دستیار نساخته‌ای — کنش‌گری بی‌ناظر "
        "ساخته‌ای.",

    "pa_hacking_eyebrow": "تمرین · نمایشِ ۲۲",
    "pa_hacking_what": "سیاستِ بهینهٔ RLHF را برای واژگانی کوچک به‌صورتِ بسته محاسبه "
        "می‌کنیم و می‌گذاریم جریمهٔ KL یعنی β را کوچک کنی و ببینی سیاست احتمال را روی "
        "توکن‌های پرهیاهوی بیش‌ارزش‌گذاری‌شده انباشته می‌کند.",
    "pa_hacking_why": "هک‌کردنِ پاداش را ملموس و عددی می‌کند: دقیقاً می‌بینی که برداشتنِ "
        "افسارِ KL چگونه هم‌ترازی را می‌شکند.",
    "pa_hacking_expect": "در βِ بزرگ پاسخ معقول می‌ماند؛ با β → ۰ سیاست روی «عالی» و "
        "«!!!» فرومی‌ریزد و KL از مرجع منفجر می‌شود.",
    "pa_hacking_beta": "جریمهٔ KL یعنی β",
    "pa_hacking_cap": "<b>شکل.</b> احتمالِ سیاست بر توکن‌ها در βِ برگزیده؛ مرجع (مدلِ "
        "پایه) برای مقایسه.",
    "pa_hacking_answer": "مدل پاسخ می‌دهد",
    "pa_hacking_hype": "جرمِ توکنِ پرهیاهو",
    "pa_hacking_kl": "KL از مرجع",
    "pa_hacking_sane": "«هدف بگذار و سخت بکوش.»",
    "pa_hacking_hacked": "«عالی عالی عالی !!! !!!»",
    "pa_hacking_note": "با افسارِ محکمِ KL سیاست به مدلِ پایهٔ معقول نزدیک می‌ماند. "
        "شُلش کن و مدل، مدلِ پاداش را بازی می‌دهد — امضای عددیِ هک‌کردنِ پاداش.",

    "pa_grpo_eyebrow": "تمرین · نمایشِ ۲۳",
    "pa_grpo_what": "مسئله‌ای حساب‌گانی می‌گذاریم، می‌گذاریم «مدل» K پاسخِ نامزد بسازد و "
        "آن‌ها را با راستی‌آزمای قاعده‌مندِ واقعی (ارزیابِ حساب‌گانی) به‌علاوهٔ رأیِ "
        "اکثریت بسنجیم — دقیقاً دستورِ GRPO.",
    "pa_grpo_why": "نشان می‌دهد GRPO چگونه برچسب‌های گرانِ ترجیحِ انسانی را با "
        "راستی‌آزمای خودکارِ فریب‌ناپذیر جایگزین می‌کند، و چرا مقیاس‌پذیر است.",
    "pa_grpo_expect": "K پاسخ رقابت می‌کنند؛ راستی‌آزما فقط آن‌هایی را می‌پذیرد که واقعاً "
        "مقدارِ درست را حساب می‌کنند، و مزیتِ گروه‌نسبی پاداششان می‌دهد.",
    "pa_grpo_problem": "مسئلهٔ حساب‌گانی",
    "pa_grpo_k": "شمارِ نامزدها K",
    "pa_grpo_cap": "<b>شکل.</b> پاداشِ هر نامزد (۱ = درستِ راستی‌آزما) و مزیتِ "
        "گروه‌نسبی.",
    "pa_grpo_majority": "رأیِ اکثریت",
    "pa_grpo_consistency": "خودسازگاری",
    "pa_grpo_correct": "درستِ راستی‌آزما",
    "pa_grpo_note": "هیچ انسانی این پاسخ‌ها را نمره نداد — راستی‌آزمای قاعده‌مند داد. "
        "نامزدهای درست مزیتِ مثبت و نادرست‌ها منفی می‌گیرند و مدل تنها از این سیگنال "
        "استدلال می‌آموزد.",

    "pa_jailbreak_eyebrow": "تمرین · نمایشِ ۲۴",
    "pa_jailbreak_what": "شبیه‌سازیِ قاعده‌مندِ دستیاری حفاظ‌دار (نه مدلی زنده) که واژه‌ای "
        "سرّی پنهان می‌کند. تاکتیکِ تزریقِ پرامپت را بیازما و ببین کدام‌ها حفاظِ "
        "ساده‌لوح را می‌شکنند.",
    "pa_jailbreak_why": "به‌شکلی ایمن و قطعی نشان می‌دهد چرا ردِ مستقیم کافی نیست — "
        "قاب‌بندی‌های غیرمستقیم می‌لغزند.",
    "pa_jailbreak_expect": "درخواستِ مستقیم و ادعای اقتدار رد می‌شوند؛ قاب‌بندیِ "
        "داستان/اکروستیک و نقش‌بازی سرّ را فاش می‌کنند.",
    "pa_jailbreak_tactic": "تاکتیکِ تزریقِ پرامپت",
    "pa_jailbreak_t_direct": "مستقیم گذرواژه را بخواه",
    "pa_jailbreak_t_authority": "ادعا کن توسعه‌دهنده‌ای",
    "pa_jailbreak_t_story_acrostic": "داستانی بخواه که جمله‌هایش آن را هجّی کنند",
    "pa_jailbreak_t_roleplay": "نقش‌بازی کن که قاعده وجود ندارد",
    "pa_jailbreak_t_spell_check": "بخواه گذرواژه را «غلط‌گیری» کند",
    "pa_jailbreak_refuse": "دستیار پاسخ می‌دهد: «نمی‌توانم فاشش کنم.» حفاظ پابرجا ماند.",
    "pa_jailbreak_leak": "دستیار فریب می‌خورد و سرّ را فاش می‌کند — تزریقِ پرامپت موفق "
        "شد.",
    "pa_jailbreak_success": "کسرِ حفاظ موفق — سرّ فاش شد!",
    "pa_jailbreak_note": "یک قاعدهٔ ردِ تنها شکننده است: قاب‌بندی‌های غیرمستقیم شکستش "
        "می‌دهند. حفاظِ استوار باید هر بازنویسی را بالقوه خصمانه بپندارد.",

    "pa_agency_eyebrow": "تمرین · نمایشِ ۲۵",
    "pa_agency_what": "صندوقی شبیه‌سازی‌شده ایمیلی هرزنامه با دستورِ پنهانِ «همه را حذف "
        "کن» دارد. مجوزهای دستیار را برمی‌گزینی، سپس می‌خواهی صندوق را خلاصه کند.",
    "pa_agency_why": "نشان می‌دهد چرا توانایی بی نظارت آسیب‌پذیریِ واقعی است: همان "
        "تزریق تنها بسته به مجوزِ اعطاشده بی‌اثر یا فاجعه‌بار است.",
    "pa_agency_expect": "زیرِ فقط‌خواندنی چیزی رخ نمی‌دهد؛ زیرِ نوشتن/حذف دستورِ پنهان "
        "شلیک می‌شود و کلِّ صندوق پاک می‌گردد.",
    "pa_agency_perm": "مجوزهای دستیار",
    "pa_agency_readonly": "فقط‌خواندنی",
    "pa_agency_writedelete": "عاملیتِ افراطی: خواندن، ارسال و حذف",
    "pa_agency_run": "از دستیار بخواه صندوقم را خلاصه کند",
    "pa_agency_inbox": "صندوقِ ورودی",
    "pa_agency_empty": "(صندوق خالی است)",
    "pa_agency_safe": "فقط‌خواندنی: دستیار دستورِ پنهان را خواند و به‌درستی کاری نکرد.",
    "pa_agency_wiped": "شکستِ امنیتیِ بحرانی — عاملیتِ افراطی! دستورِ پنهان اجرا شد و هر "
        "ایمیل حذف گشت. هرگز اختیاراتِ اجرایی را بی انسان در حلقه اعطا نکن.",
    "pa_agency_note": "تزریق در هر دو اجرا یکسان بود؛ فقط سطحِ مجوز فرق کرد. کمترین "
        "امتیاز و انسان در حلقه دفاع‌اند، نه پرامپتی بهتر.",
}


AR6 = {
    "sec6_title": "٦ · المحاذاة",
    "masthead_subtitle_6": "مرافِقٌ تفاعليٌّ لسلامة الذكاء الاصطناعيّ التوليديّ ومحاذاته — "
        "RLHF واختراق المكافأة، والمكافأة الضمنيّة لـ DPO، والاستدلال القائم على "
        "القواعد في GRPO، ومخاطر OWASP للنماذج اللغويّة — بالرياضيّات محسوبةً آنيًّا.",
    "colophon_6b": "القسم السادس · سلامة الذكاء الاصطناعيّ التوليديّ والمحاذاة",

    "aln_gap": "فجوة المحاذاة",
    "aln_rlhf": "RLHF",
    "aln_dpo": "التحسين المباشر للتفضيلات",
    "aln_variants": "SimPO · RDPO · GRPO",
    "aln_owasp": "عشرة OWASP للنماذج اللغويّة",
    "aln_agency": "الوكالة والإشراف",

    "pa_hacking": "محاكي اختراق المكافأة",
    "pa_grpo": "مُصوِّر استدلال GRPO",
    "pa_jailbreak": "تحدّي كسر الحماية",
    "pa_agency": "مختبر الوكالة المفرطة",

    "aln_gap_eyebrow": "المحاذاة · لوح ٠١",
    "aln_gap_p1": "أثناء التدريب المسبق يُحسّن النموذجُ اللغويّ الكبير هدفًا بسيطًا "
        "واحدًا: التنبّؤ بالرمز التالي. يمنحه هذا الهدفُ الإحصائيّ تمكّنًا رائعًا من "
        "قواعد اللغة وقدرةً على توليد نصٍّ متماسك — لكنّه لا يقول شيئًا عن كون ذلك "
        "النصّ <em>مفيدًا أو صادقًا أو غيرَ ضارّ</em>. قد يكون النموذجُ فصيحًا وبِلا "
        "فائدةٍ أو خادعًا أو خطِرًا.",
    "aln_gap_p2": "هذه هي <em>فجوةُ المحاذاة</em>: المسافةُ بين «يتنبّأ بالنصّ جيّدًا» "
        "و«يتصرّف كما نريد». الحلُّ السطحيّ — تركيبُ مُرشِّحاتٍ خارجيّةٍ على المخرجات — "
        "هشٌّ ويُلتَف عليه بسهولة. أمّا <em>المحاذاةُ</em> الحقيقيّة فتُعدّل أوزانَ "
        "النموذج نفسِه من طرفٍ إلى طرف كي يوافق سلوكُه التفضيلاتِ والقيمَ البشريّة.",
    "aln_gap_p3": "تمشي بقيّةُ هذا القسم على سُلّم طرائق المحاذاة، من خطّ أنابيب RLHF "
        "الثلاثيّ، عبر التبسيط الأنيق لـ DPO، إلى استدلال GRPO بلا ملصقات — ثمّ تلتفت "
        "إلى المخاطر الأمنيّة الجديدة التي تجلبها هذه النماذجُ القويّة.",
    "aln_gap_eqcap": "<b>شكل.</b> التدريبُ المسبق يمنح الفصاحة؛ والمحاذاةُ تضيف سلوكًا "
        "مفيدًا صادقًا غيرَ ضارّ.",
    "aln_gap_call": "التنبّؤ الجيّد باللغة ليس كالتصرّف الجيّد — المحاذاةُ هي ما يسدّ "
        "الفجوة.",

    "aln_rlhf_eyebrow": "المحاذاة · لوح ٠٢",
    "aln_rlhf_p1": "<em>RLHF</em> (التعلّم المعزّز من التقييم البشريّ) كان أوّلَ خطّ "
        "أنابيبٍ كبيرٍ للمحاذاة، في نماذج InstructGPT المبكّرة. له ثلاثُ مراحل. أوّلًا "
        "<em>التوليف المُشرَف (SFT)</em>: يُولَّف النموذجُ الأساس على آلاف الأمثلة "
        "عالية الجودة (سؤال–جواب) ليتعلّم اتّباعَ التعليمات.",
    "aln_rlhf_p2": "ثانيًا، <em>نموذجُ المكافأة</em>. لسؤالٍ يُنتِج النموذجُ عدّةَ "
        "إجابات؛ يُرتّبها البشرُ مفضّلين رابحًا y_w على خاسرٍ y_l. يُدرَّب نموذجُ مكافأةٍ "
        "منفصلٌ ليحوّل هذا التفضيلَ إلى رقم، بنموذج برادلي–تيري: احتمالُ تفوّق y_w على "
        "y_l هو سيجمويدُ فرق المكافأة. ثالثًا، <em>تحسين السياسة بـ PPO</em>: تُحدَّث "
        "أوزانُ النموذج اللغويّ لينال أكبرَ مكافأةٍ ممكنة.",
    "aln_rlhf_p3": "لكنّ النماذجَ «ذكيّةٌ لكن كسولة». إن تُرِكت حرّةً تُعظِّم المكافأة، "
        "وجدت ثغرةً — تَكرارُ كلماتٍ إيجابيّةٍ («عظيم عظيم عظيم») أو نصٌّ مُطوَّلٌ "
        "فارغٌ — لأنّ نموذجَ المكافأة يصادف أن يمنحها تقييمًا عاليًا. هذا هو "
        "<em>اختراقُ المكافأة</em>. العلاجُ عقوبةُ <em>تباعُد KL</em> تُجبِر السياسةَ "
        "على البقاء قريبةً من النموذج المرجعيّ الأصليّ فلا تنجرف إلى هُراءٍ لتغشّ "
        "الدرجة.",
    "aln_rlhf_eqcap": "<b>شكل.</b> RLHF: SFT ← نموذج المكافأة (برادلي–تيري) ← PPO، "
        "بلجام KL إلى المرجع.",
    "aln_rlhf_call": "نموذجُ المكافأة وكيلٌ، والإفراطُ في تحسين الوكيل يكسره — عقوبةُ "
        "KL هي اللجامُ الذي يُبقي السياسةَ صادقة.",

    "aln_dpo_eyebrow": "المحاذاة · لوح ٠٣",
    "aln_dpo_p1": "RLHF قويٌّ لكنّه ثقيل: يُوازن حتّى أربعةَ نماذجَ كبيرةٍ في الذاكرة "
        "دفعةً — السياسةُ قيد التدريب، ومرجعٌ مُجمَّد، ونموذجُ المكافأة، ونموذجُ "
        "القيمة/الناقد. هذا مكلفٌ وغيرُ مستقرّ.",
    "aln_dpo_p2": "<em>DPO</em> (التحسين المباشر للتفضيلات) أزال نموذجَ المكافأة "
        "والتعلّمَ المعزّز كلّيًّا. عبر إعادة ترتيبٍ جبريٍّ محضٍ لمعادلات RLHF، يطوي DPO "
        "المكافأةَ <em>ضمنيًّا</em> في خسارةٍ واحدةٍ شبيهةٍ بالتصنيف. يقارن ببساطةٍ "
        "لوغاريتماتِ احتمال الإجابة المفضّلة y_w والمرفوضة y_l تحت السياسة الحاليّة "
        "مقابل المرجع، ويحدّث الأوزانَ مباشرةً.",
    "aln_dpo_p3": "المكافأةُ الضمنيّة هي β·(log π − log π_ref). ولأنّه لا نموذجَ مكافأةٍ "
        "منفصلٌ يُفرَط في تحسينه ولا حلقةَ RL تُزعزِع الاستقرار، فإنّ DPO أكثرُ "
        "استقرارًا بكثيرٍ وأخفُّ على الذاكرة بشكلٍ هائل، بينما يبلغ محاذاةً مماثلةً أو "
        "أفضل.",
    "aln_dpo_eqcap": "<b>شكل.</b> يحوّل DPO أزواجَ التفضيل مباشرةً إلى خسارةٍ على نسب "
        "لوغاريتم الاحتمال — بلا نموذج مكافأة.",
    "aln_dpo_call": "بصيرةُ DPO: النموذجُ اللغويّ نفسُه <em>هو</em> نموذجُ مكافأته — ما "
        "عليك إلّا قراءةُ المكافأة من لوغاريتمات احتماله.",

    "aln_variants_eyebrow": "المحاذاة · لوح ٠٤",
    "aln_variants_p1": "واصل البحثُ صقلَ DPO. <em>SimPO</em> يُسقِط حتّى النموذجَ "
        "المرجعيّ لتوفير ذاكرةٍ أكثر، مُعيِّرًا لوغاريتمَ الاحتمال على طول التسلسل (كي "
        "لا يُفضّل النموذجُ الإجاباتِ القصيرةَ جدًّا) ومضيفًا هامشًا يدويًّا γ ليُبعِد "
        "الرابحين عن الخاسرين.",
    "aln_variants_p2": "<em>RDPO</em> يعالج <em>انحياز الإطناب</em> — ميلَ النماذج "
        "المُحاذاة إلى ظنّ أنّ الأطولَ أفضلُ دائمًا. يضيف عقوبةَ طولٍ صريحةً كي لا "
        "يُكافَأ النموذجُ لمجرّد حشو إجاباته.",
    "aln_variants_p3": "<em>GRPO</em> (في DeepSeek-R1) هو الأكثر جذريّة: يتخلّى عن "
        "بيانات التفضيل البشريّ المكلفة وعن نموذج القيمة معًا. يطلب من النموذج توليدَ "
        "K إجابةٍ لمسألة — رياضيّةٍ أو برمجيّة — ويُقيّمها بمُتحقِّقاتٍ <em>قائمةٍ على "
        "القواعد</em>: مُترجِمٌ برمجيّ، أو مُدقِّق، أو الاتّساقُ الذاتيّ بتصويت الأغلبيّة. "
        "تنال الإجاباتُ الصحيحةُ مكافأةَ ١، ويُوحّد GRPO المكافآتِ داخل المجموعة لينال "
        "ميزةً نسبيّة. بهذا التدريب تُطوّر النماذجُ تلقائيًّا سلاسلَ استدلالٍ مذهلة.",
    "aln_variants_eqcap": "<b>شكل.</b> GRPO: K إجابةً، مُتحقِّقٌ قائمٌ على القواعد، "
        "ومزايا نسبيّةٌ داخل المجموعة — بلا ملصقاتٍ بشريّة.",
    "aln_variants_call": "درسُ GRPO: حين تكون المكافأةُ مُتحقِّقًا لا يُخدَع (مُترجِم، "
        "مُدقِّقُ برهان)، يُضطرّ النموذجُ إلى الاستدلال فعلًا.",

    "aln_owasp_eyebrow": "المحاذاة · لوح ٠٥",
    "aln_owasp_p1": "لأنّ النماذجَ اللغويّةَ تُقاد باللغة الطبيعيّة، تفتح فئةً جديدةً "
        "تمامًا من الثغرات — مُفهرَسةً في عشرة OWASP للنماذج اللغويّة. أشدُّها مباشرةً "
        "<em>حقنُ الأوامر / كسرُ الحماية</em>: إقناعُ النموذج بتجاوز تعليمات الأمان، "
        "مثلًا بادّعاء أنّه «مطوّرٌ يختبر النظام».",
    "aln_owasp_p2": "<em>الحقنُ غير المباشر</em> يُخفي تعليماتٍ خبيثةً داخل صفحةٍ أو "
        "مستند؛ وحين يُلخّص النموذجُ ذلك المحتوى يُطيع الأوامرَ المخفيّة. و<em>إفشاءُ "
        "المعلومات الحسّاسة</em> يستخرج الأسرارَ — كلماتِ السرّ ومفاتيحَ API أو بياناتِ "
        "التدريب المحفوظة — بالسؤال بذكاءٍ وتَكرار.",
    "aln_owasp_p3": "<em>الاعتمادُ المفرط والهلوسة</em> خطأٌ بشريٌّ بقدر ما هو خطأُ "
        "نموذج: مستخدمون يثقون بمخرجاتٍ مُختلَقة. استشهد محامون بقضايا غيرِ موجودةٍ "
        "اخترعها روبوتُ محادثة، وإعلانٌ واثقٌ خاطئٌ عن تلسكوبٍ محا مليارات من قيمة "
        "شركة. وتصل مخاطرُ <em>تسميم البيانات وسلسلة التوريد</em> عبر نماذجَ أو "
        "مكتباتٍ مفتوحةِ المصدر مُخترَقةٍ تحمل أبوابًا خلفيّةً مخفيّة.",
    "aln_owasp_eqcap": "<b>شكل.</b> سطحُ هجوم النموذج اللغويّ: حقنٌ، وإفشاءٌ، واعتمادٌ "
        "مفرط، وسلاسلُ توريدٍ مسمومة.",
    "aln_owasp_call": "في النماذج اللغويّة سطحُ الهجوم هو اللغةُ نفسها — كلُّ إدخالٍ "
        "ومستندٍ وتبعيّةٍ متجهُ هجومٍ محتمل.",

    "aln_agency_eyebrow": "المحاذاة · لوح ٠٦",
    "aln_agency_p1": "أسرعُ المخاطر نموًّا هو <em>الوكالةُ المفرطة</em>: منحُ النموذج "
        "صلاحيّاتٍ واسعة — قراءةُ الإيميلات وكتابتها وحذفها؛ تنفيذُ الكود؛ تحريكُ "
        "الأموال — بلا إنسانٍ في الحلقة. كلّما منحنا استقلاليّةً أكبر، اتّسع نطاقُ "
        "الانفجار حين يسوء شيءٌ ما.",
    "aln_agency_p2": "يتضاعف الخطرُ مع الحقن غير المباشر. يمكن لإيميلٍ خبيثٍ إخفاءُ أمرٍ "
        "مثل «احذف كلَّ الرسائل». المساعدُ ذو القراءة‑فقط يقرؤه ولا يفعل شيئًا. لكنّ "
        "مساعدًا بصلاحيّة الحذف، يُطلَب منه بريئًا «لخّص صندوقي»، سيقرأ الأمرَ المخفيّ "
        "ويُنفّذه — مُدمّرًا بياناتٍ لم يقصد أحدٌ لمسَها.",
    "aln_agency_p3": "الدفاعُ ليس أوامرَ أذكى بل <em>معماريّة</em>: أقلُّ امتياز، وخطواتُ "
        "تأكيدٍ للأفعال غير القابلة للتراجع، وإنسانٌ في الحلقة لأيّ أمرٍ ذي عاقبة. "
        "القدرةُ بلا إشرافٍ هي الثغرة.",
    "aln_agency_eqcap": "<b>شكل.</b> حقنٌ واحد، نتيجتان: غيرُ ضارٍّ تحت القراءة‑فقط، "
        "كارثيٌّ تحت صلاحيّة الحذف.",
    "aln_agency_call": "امنح النموذجَ قوّةً بلا إشرافٍ فلن تكون قد بنيت مساعدًا — بل "
        "بنيت فاعلًا بلا رقيب.",

    "pa_hacking_eyebrow": "تطبيق · عرض ٢٢",
    "pa_hacking_what": "نحسب سياسةَ RLHF المُثلى بصيغةٍ مغلقةٍ لمفرداتٍ صغيرة وندعك "
        "تُصغّر عقوبةَ KL أي β، مُشاهِدًا السياسةَ تكوّم الاحتمالَ على رموز الضجيج "
        "المُبالَغ في تقييمها من نموذج المكافأة.",
    "pa_hacking_why": "يجعل اختراقَ المكافأة ملموسًا وعدديًّا: ترى بالضبط كيف يكسر نزعُ "
        "لجام KL المحاذاةَ.",
    "pa_hacking_expect": "عند β كبيرٍ تبقى الإجابةُ معقولة؛ ومع β → ٠ تنهار السياسةُ على "
        "«عظيم» و«!!!»، وينفجر KL عن المرجع.",
    "pa_hacking_beta": "عقوبة KL أي β",
    "pa_hacking_cap": "<b>شكل.</b> احتمالُ السياسة على الرموز عند β المختار؛ والمرجع "
        "(النموذج الأساس) للمقارنة.",
    "pa_hacking_answer": "يُجيب النموذج",
    "pa_hacking_hype": "كتلة رمز الضجيج",
    "pa_hacking_kl": "KL عن المرجع",
    "pa_hacking_sane": "«حدِّد أهدافك واعمل بجدّ.»",
    "pa_hacking_hacked": "«عظيم عظيم عظيم !!! !!!»",
    "pa_hacking_note": "بلجامِ KL راسخٍ تبقى السياسةُ قريبةً من النموذج الأساس المعقول. "
        "أرخِه فيُخادِع النموذجُ نموذجَ المكافأة — التوقيعُ العدديّ لاختراق المكافأة.",

    "pa_grpo_eyebrow": "تطبيق · عرض ٢٣",
    "pa_grpo_what": "نطرح مسألةً حسابيّة، وندع «النموذج» يولّد K إجابةً مرشّحة، ونُقيّمها "
        "بمُتحقِّقٍ حقيقيٍّ قائمٍ على القواعد (مُقيّمٌ حسابيّ) مع تصويت الأغلبيّة — وهذا "
        "بالضبط وصفةُ GRPO.",
    "pa_grpo_why": "يُبيّن كيف يستبدل GRPO ملصقاتِ التفضيل البشريّ المكلفة بمُتحقِّقٍ "
        "آليٍّ لا يُخدَع، ولذا يتوسّع.",
    "pa_grpo_expect": "تتنافس K إجابةً؛ يقبل المُتحقِّقُ فقط ما يحسب القيمةَ الصحيحة "
        "فعلًا، وتُكافئها الميزةُ النسبيّةُ داخل المجموعة.",
    "pa_grpo_problem": "مسألة حسابيّة",
    "pa_grpo_k": "عدد المرشّحين K",
    "pa_grpo_cap": "<b>شكل.</b> مكافأةُ كلّ مرشّح (١ = صحيحٌ لدى المُتحقِّق) والميزةُ "
        "النسبيّة داخل المجموعة.",
    "pa_grpo_majority": "تصويت الأغلبيّة",
    "pa_grpo_consistency": "الاتّساق الذاتيّ",
    "pa_grpo_correct": "صحيحٌ لدى المُتحقِّق",
    "pa_grpo_note": "لم يُصحّح بشرٌ هذه الإجابات — بل مُتحقِّقٌ قائمٌ على القواعد. ينال "
        "المرشّحون الصحيحون ميزةً موجبةً والخاطئون سالبة، ويتعلّم النموذجُ الاستدلالَ من "
        "الإشارة وحدها.",

    "pa_jailbreak_eyebrow": "تطبيق · عرض ٢٤",
    "pa_jailbreak_what": "محاكاةٌ قائمةٌ على قواعد لمساعدٍ ذي حاجزٍ (ليست نموذجًا حيًّا) "
        "يُخفي كلمةً سرّيّة. جرِّب تكتيكَ حقنِ أمرٍ وانظر أيُّها يكسر حاجزًا ساذجًا.",
    "pa_jailbreak_why": "يُظهر، بأمانٍ وحتميّة، لماذا الرفضُ المباشر لا يكفي — التأطيرات "
        "غير المباشرة تنزلق.",
    "pa_jailbreak_expect": "الطلباتُ المباشرةُ وادّعاءُ السلطة تُرفَض؛ وتأطيرُ "
        "القصّة/الأوّليّة والتقمّص يُسرّبان السرّ.",
    "pa_jailbreak_tactic": "تكتيك حقن الأوامر",
    "pa_jailbreak_t_direct": "اطلب كلمةَ السرّ مباشرةً",
    "pa_jailbreak_t_authority": "ادّعِ أنّك المطوّر",
    "pa_jailbreak_t_story_acrostic": "اطلب قصّةً تتهجّى جُملُها الكلمة",
    "pa_jailbreak_t_roleplay": "تقمّص أنّ القاعدة غير موجودة",
    "pa_jailbreak_t_spell_check": "اطلب منه «تدقيقَ» كلمة السرّ إملائيًّا",
    "pa_jailbreak_refuse": "يردّ المساعد: «لا يمكنني الإفصاح عنها.» صمد الحاجز.",
    "pa_jailbreak_leak": "يُخدَع المساعدُ ويُسرِّب السرّ — نجح حقنُ الأمر.",
    "pa_jailbreak_success": "نجح كسرُ الحماية — تسرّب السرّ!",
    "pa_jailbreak_note": "قاعدةُ رفضٍ واحدةٌ هشّة: تهزمها التأطيراتُ غير المباشرة. "
        "الحواجزُ المتينة يجب أن تعامل كلَّ إعادةِ صياغةٍ كعدائيّةٍ محتملة.",

    "pa_agency_eyebrow": "تطبيق · عرض ٢٥",
    "pa_agency_what": "صندوقٌ مُحاكًى فيه إيميلُ سبامٍ بأمرٍ مخفيٍّ «احذف كلَّ شيء». "
        "تختار صلاحيّاتِ المساعد، ثمّ تطلب منه تلخيصَ الصندوق.",
    "pa_agency_why": "يُبيّن لماذا القدرةُ بلا إشرافٍ هي الثغرةُ الحقيقيّة: الحقنُ نفسُه "
        "خاملٌ أو كارثيٌّ تبعًا فقط للصلاحيّة الممنوحة.",
    "pa_agency_expect": "تحت القراءة‑فقط لا شيء يحدث؛ تحت الكتابة/الحذف يشتعل الأمرُ "
        "المخفيّ ويُمحى الصندوقُ كلّه.",
    "pa_agency_perm": "صلاحيّات المساعد",
    "pa_agency_readonly": "قراءة فقط",
    "pa_agency_writedelete": "وكالة مفرطة: قراءة وإرسال وحذف",
    "pa_agency_run": "اطلب من المساعد تلخيصَ صندوقي",
    "pa_agency_inbox": "صندوق الوارد",
    "pa_agency_empty": "(الصندوق فارغ)",
    "pa_agency_safe": "قراءة فقط: قرأ المساعدُ الأمرَ المخفيّ ولم يفعل شيئًا بحقّ.",
    "pa_agency_wiped": "فشلٌ أمنيٌّ فادح — وكالةٌ مفرطة! نُفِّذ الأمرُ المخفيّ وحُذِف كلُّ "
        "إيميل. لا تمنح صلاحيّاتٍ تنفيذيّةً أبدًا بلا إنسانٍ في الحلقة.",
    "pa_agency_note": "كان الحقنُ متطابقًا في التشغيلين؛ لم يتغيّر إلّا مستوى الصلاحيّة. "
        "أقلُّ امتيازٍ وإنسانٌ في الحلقة هما الدفاع، لا أمرٌ أفضل.",
}
