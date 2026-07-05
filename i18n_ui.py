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
    "open_sections": "☰ Choose section",
    "footer_text": "© 2026 ExploreTML · Trustworthy Machine Learning Laboratory · "
        "Iran University of Science and Technology (IUST). All rights reserved.",
    "landing_prompt": "Choose a section to begin — each opens in Theory or Practice.",
    "choose_view": "How would you like to explore this section?",
    "choose_theory": "📖 Theory",
    "choose_practice": "🧪 Practice",
    "back_to_sections": "← All sections",
    "card_cta": "Open section →",
    # top-bar pages
    "nav_about": "About",
    "nav_contact": "Contact",
    "about_title": "About this platform",
    "about_body": "ExploreTML is an interactive, mathematically rigorous sandbox "
        "for Trustworthy Machine Learning, spanning six pillars — generalization, "
        "explainability, fairness, robustness, privacy, and the alignment of "
        "generative models. Every practice demo runs real computation on real "
        "data (NumPy, scikit-learn, SciPy), not mock-ups. It was developed by "
        "Hani Akram Mahfoud under the supervision of Prof. Behrouz "
        "Minaei-Bidgoli at Iran University of Science and Technology (IUST).",
    "contact_title": "Contact",
    "contact_body": "For questions about the platform or the course, please reach "
        "out through the university. This sandbox accompanies the Trustworthy "
        "Machine Learning course at IUST.",
    "contact_author": "Author",
    "contact_supervisor": "Supervisor",
    "contact_institution": "Institution",
    "contact_inst_val": "Iran University of Science and Technology (IUST)",
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
    "open_sections": "☰ انتخابِ بخش",
    "footer_text": "© ۲۰۲۶ ExploreTML · آزمایشگاهِ یادگیری ماشینِ قابل‌اعتماد · "
        "دانشگاه علم و صنعت ایران (IUST). همهٔ حقوق محفوظ است.",
    "landing_prompt": "برای شروع بخشی را برگزینید — هرکدام در حالتِ نظری یا عملی باز می‌شود.",
    "choose_view": "این بخش را چگونه می‌خواهید کاوش کنید؟",
    "choose_theory": "📖 نظری",
    "choose_practice": "🧪 عملی",
    "back_to_sections": "→ همهٔ بخش‌ها",
    "card_cta": "بازکردنِ بخش ←",
    "nav_about": "درباره",
    "nav_contact": "تماس",
    "about_title": "دربارهٔ این سکو",
    "about_body": "ExploreTML یک جعبه‌شنِ تعاملی و دقیقِ ریاضی برای یادگیری ماشینِ "
        "قابل‌اعتماد است که شش ستون را دربر می‌گیرد — تعمیم، تفسیرپذیری، انصاف، "
        "استواری، حریم خصوصی، و هم‌ترازیِ مدل‌های مولد. هر نمایشِ عملی محاسبهٔ واقعی "
        "روی دادهٔ واقعی اجرا می‌کند (NumPy، scikit-learn، SciPy)، نه ماکت. این سکو "
        "توسط هانی اکرم محفوظ زیرِ نظرِ پروفسور بهروز مینائی-بیدگلی در دانشگاه علم و "
        "صنعت ایران (IUST) توسعه یافته است.",
    "contact_title": "تماس",
    "contact_body": "برای پرسش دربارهٔ سکو یا درس، لطفاً از طریقِ دانشگاه در تماس "
        "باشید. این جعبه‌شن همراهِ درسِ یادگیری ماشینِ قابل‌اعتماد در IUST است.",
    "contact_author": "مؤلف",
    "contact_supervisor": "استادِ راهنما",
    "contact_institution": "دانشگاه",
    "contact_inst_val": "دانشگاه علم و صنعت ایران (IUST)",
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
    "open_sections": "☰ اختر القسم",
    "footer_text": "© ٢٠٢٦ ExploreTML · مختبر تعلُّم الآلة الموثوق · "
        "جامعة العلوم والتكنولوجيا الإيرانيّة (IUST). جميع الحقوق محفوظة.",
    "landing_prompt": "اختر قسمًا للبدء — كلٌّ منها يُفتَح نظريًّا أو عمليًّا.",
    "choose_view": "كيف تريد استكشاف هذا القسم؟",
    "choose_theory": "📖 نظريّ",
    "choose_practice": "🧪 عمليّ",
    "back_to_sections": "→ كلّ الأقسام",
    "card_cta": "افتح القسم ←",
    "nav_about": "من نحن",
    "nav_contact": "اتّصل بنا",
    "about_title": "عن هذه المنصّة",
    "about_body": "ExploreTML منصّةٌ تفاعليّةٌ دقيقةٌ رياضيًّا للتعلّم الآليّ الموثوق، "
        "تمتدّ على ستّة أعمدة — التعميم، والتفسير، والعدالة، والمتانة، والخصوصيّة، "
        "ومحاذاة النماذج التوليديّة. كلُّ عرضٍ عمليٍّ يُشغّل حسابًا حقيقيًّا على بياناتٍ "
        "حقيقيّة (NumPy وscikit-learn وSciPy)، لا واجهاتٍ وهميّة. طُوِّرت المنصّة على "
        "يد هاني أكرم محفوظ بإشراف البروفيسور بهروز مينائي-بيدجلي في جامعة العلوم "
        "والتكنولوجيا الإيرانيّة (IUST).",
    "contact_title": "اتّصل بنا",
    "contact_body": "للاستفسار عن المنصّة أو المادّة، يُرجى التواصل عبر الجامعة. "
        "هذه المنصّة مرافِقةٌ لمادّة التعلّم الآليّ الموثوق في جامعة IUST.",
    "contact_author": "المؤلّف",
    "contact_supervisor": "المشرف",
    "contact_institution": "الجامعة",
    "contact_inst_val": "جامعة العلوم والتكنولوجيا الإيرانيّة (IUST)",
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
