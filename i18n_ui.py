"""
i18n_ui.py -- strings for the UI overhaul (hero band, roadmap/site-map toggle,
and the six section-card descriptions). Merged into LANG_DICT. English base.
Content strings for theory/practice remain in their own modules; these are
navigation-chrome labels only.
"""
from __future__ import annotations

EN_UI = {
    # hero band
    "hero_title": "Trustworthy Machine Learning",
    "hero_summary": "An interactive, mathematically rigorous sandbox spanning six "
        "pillars of trustworthy ML — from generalization and explainability to "
        "fairness, robustness, privacy, and the alignment of generative models. "
        "Every demo runs real computation, not mock-ups.",
    # navbar / toggles
    "overview_label": "Overview",
    "roadmap_label": "Site map",
    "roadmap_title": "Site map — the full structure at a glance",
    "roadmap_hide": "Hide site map",
    # state-based navigation
    "nav_home": "⌂ Home",
    "nav_prev": "← Previous",
    "nav_next": "Next →",
    "nav_menu": "☰ Menu",
    "landing_prompt": "Choose a section to begin — each opens in Theory or Practice.",
    "choose_view": "How would you like to explore this section?",
    "choose_theory": "📖 Theory",
    "choose_practice": "🧪 Practice",
    "back_to_sections": "← All sections",
    "card_cta": "Open section →",
    # six section-card descriptions (short)
    "sc_desc_sec1": "Bias–variance, VC dimension, domain adaptation, SAM, and the "
        "causal foundations of generalization.",
    "sc_desc_sec2": "Interpreting black boxes with SHAP and LIME, causal recourse, "
        "and spurious-correlation detection in vision.",
    "sc_desc_sec3": "Fairness metrics, the impossibility theorem, bias in language "
        "models, and mitigation strategies.",
    "sc_desc_sec4": "Adversarial attacks (FGSM, PGD), the accuracy/robustness "
        "trade-off, certified defenses, and LLM jailbreaks.",
    "sc_desc_sec5": "Data poisoning and backdoors, membership inference, "
        "differential privacy, and federated gradient leakage.",
    "sc_desc_sec6": "RLHF and reward hacking, DPO, GRPO's rule-based reasoning, and "
        "the OWASP risks of generative AI.",
    # section-card icons (emoji chosen to be neutral/academic)
}

FA_UI = {
    "hero_title": "یادگیری ماشینِ قابل‌اعتماد",
    "hero_summary": "جعبه‌شنی تعاملی و دقیقِ ریاضی در شش ستونِ یادگیری ماشینِ "
        "قابل‌اعتماد — از تعمیم و تفسیرپذیری تا انصاف، استواری، حریم خصوصی، و "
        "هم‌ترازیِ مدل‌های مولد. هر نمایش محاسبهٔ واقعی اجرا می‌کند، نه ماکت.",
    "overview_label": "نمای کلی",
    "roadmap_label": "نقشهٔ سایت",
    "roadmap_title": "نقشهٔ سایت — کلِّ ساختار در یک نگاه",
    "roadmap_hide": "پنهان‌کردنِ نقشه",
    "nav_home": "⌂ خانه",
    "nav_prev": "→ قبلی",
    "nav_next": "بعدی ←",
    "nav_menu": "☰ منو",
    "landing_prompt": "برای شروع بخشی را برگزینید — هرکدام در حالتِ نظری یا عملی باز می‌شود.",
    "choose_view": "این بخش را چگونه می‌خواهید کاوش کنید؟",
    "choose_theory": "📖 نظری",
    "choose_practice": "🧪 عملی",
    "back_to_sections": "→ همهٔ بخش‌ها",
    "card_cta": "بازکردنِ بخش ←",
    "sc_desc_sec1": "بایاس–واریانس، بُعدِ VC، انطباقِ دامنه، SAM، و بنیادهای علّیِ "
        "تعمیم.",
    "sc_desc_sec2": "تفسیرِ جعبه‌سیاه با SHAP و LIME، جبرانِ علّی، و کشفِ همبستگیِ "
        "کاذب در بینایی.",
    "sc_desc_sec3": "سنجه‌های انصاف، قضیهٔ ناممکنی، سوگیری در مدل‌های زبانی، و "
        "راهبردهای کاهش.",
    "sc_desc_sec4": "حملاتِ تخاصمی (FGSM، PGD)، بده‌بستانِ دقت/استواری، دفاعِ "
        "گواهی‌شده، و کسرِ حفاظِ LLM.",
    "sc_desc_sec5": "مسموم‌سازی و درهای پشتی، استنتاجِ عضویت، حریمِ تفاضلی، و نشتِ "
        "گرادیانِ فدرال.",
    "sc_desc_sec6": "RLHF و هک‌کردنِ پاداش، DPO، استدلالِ قاعده‌مندِ GRPO، و خطرهای "
        "OWASP در هوش مصنوعیِ مولد.",
}

AR_UI = {
    "hero_title": "تعلُّم الآلة الموثوق",
    "hero_summary": "منصّةٌ تفاعليّةٌ دقيقةٌ رياضيًّا تمتدّ على ستّة أعمدةٍ للتعلّم "
        "الآليّ الموثوق — من التعميم والتفسير إلى العدالة والمتانة والخصوصيّة ومحاذاة "
        "النماذج التوليديّة. كلُّ عرضٍ يُشغّل حسابًا حقيقيًّا، لا واجهاتٍ وهميّة.",
    "overview_label": "نظرة عامّة",
    "roadmap_label": "خريطة الموقع",
    "roadmap_title": "خريطة الموقع — البنية كاملةً بلمحة",
    "roadmap_hide": "إخفاء الخريطة",
    "nav_home": "⌂ الرئيسيّة",
    "nav_prev": "→ السابق",
    "nav_next": "التالي ←",
    "nav_menu": "☰ القائمة",
    "landing_prompt": "اختر قسمًا للبدء — كلٌّ منها يُفتَح نظريًّا أو عمليًّا.",
    "choose_view": "كيف تريد استكشاف هذا القسم؟",
    "choose_theory": "📖 نظريّ",
    "choose_practice": "🧪 عمليّ",
    "back_to_sections": "→ كلّ الأقسام",
    "card_cta": "افتح القسم ←",
    "sc_desc_sec1": "المفاضلة بين الانحياز والتباين، بُعد VC، تكيُّف المجال، SAM، "
        "والأسس السببيّة للتعميم.",
    "sc_desc_sec2": "تفسير الصناديق السوداء بـ SHAP وLIME، والجبر السببيّ، وكشف "
        "الارتباط الزائف في الرؤية.",
    "sc_desc_sec3": "مقاييس العدالة، ومبرهنة الاستحالة، والانحياز في النماذج "
        "اللغويّة، واستراتيجيّات التخفيف.",
    "sc_desc_sec4": "الهجمات التخاصميّة (FGSM، PGD)، ومقايضة الدقة/المتانة، والدفاع "
        "المُعتمَد، واختراق النماذج اللغويّة.",
    "sc_desc_sec5": "تسميم البيانات والأبواب الخلفيّة، واستنتاج العضويّة، والخصوصيّة "
        "التفاضليّة، وتسريب التدرّج الموحّد.",
    "sc_desc_sec6": "RLHF واختراق المكافأة، وDPO، واستدلال GRPO القائم على القواعد، "
        "ومخاطر OWASP للذكاء التوليديّ.",
}
