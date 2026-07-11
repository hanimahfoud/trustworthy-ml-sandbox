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
    "hero_practice_note": "Choose Theory to read the rigorous explanation, or "
        "Practice to see the concept happen live — move a slider or press a "
        "button and watch the real computation unfold before you.",
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
    "open_sections": "☰ Sections",
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
    "contact_phone": "Author's phone",
    "contact_phone_val": "09309456655 · +98 930 945 6655",
    "contact_apps": "Available on",
    "contact_apps_val": "Eitaa · Bale · WhatsApp · Telegram",
    "contact_email": "Email",
    "contact_whatsapp_btn": "💬 Message me on WhatsApp",
    "contact_email_btn": "✉ Send an email",
    "contact_support_note": "If anything goes wrong while using the site, please "
        "do not hesitate to call or message me directly — I will be glad to help.",
    # acknowledgment (dedication under the hero + About panel)
    "ack_title": "Acknowledgment",
    "ack_body": "With sincere gratitude to the supervisor, Prof. Dr. Behrouz "
        "Minaei-Bidgoli — the lectures and material of his Trustworthy Machine "
        "Learning course at IUST are the source and foundation of everything "
        "presented on this platform.",
    # sidebar language picker
    "lang_pick": "Choose language",
    # PDF cover page: a wisdom quote matched to each section's subject
    "pdf_cover_doc": "Course Reader — Theory & Practice",
    "pdf_quote_sec1": "All models are wrong, but some are useful.",
    "pdf_quote_by_sec1": "George E. P. Box",
    "pdf_quote_sec2": "What I cannot create, I do not understand.",
    "pdf_quote_by_sec2": "Richard Feynman",
    "pdf_quote_sec3": "Injustice anywhere is a threat to justice everywhere.",
    "pdf_quote_by_sec3": "Martin Luther King Jr.",
    "pdf_quote_sec4": "Know the enemy and know yourself, and in a hundred "
        "battles you will never be in peril.",
    "pdf_quote_by_sec4": "Sun Tzu — The Art of War",
    "pdf_quote_sec5": "Arguing that you don't care about privacy because you "
        "have nothing to hide is no different than saying you don't care about "
        "free speech because you have nothing to say.",
    "pdf_quote_by_sec5": "Edward Snowden",
    "pdf_quote_sec6": "We had better be quite sure that the purpose put into "
        "the machine is the purpose which we really desire.",
    "pdf_quote_by_sec6": "Norbert Wiener",
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
    "hero_practice_note": "بخشِ نظری را برای شرحِ دقیق برگزینید، یا بخشِ عملی را تا "
        "ببینید مفهوم زنده اتفاق می‌افتد — لغزنده‌ای را بجنبانید یا دکمه‌ای را بزنید و "
        "محاسبهٔ واقعی را پیشِ چشمانتان تماشا کنید.",
    "overview_label": "نمای کلی",
    "roadmap_label": "نقشهٔ سایت",
    "roadmap_title": "نقشهٔ سایت — کلِّ ساختار در یک نگاه",
    "roadmap_hide": "پنهان‌کردنِ نقشه",
    "nav_home": "⌂ خانه",
    "nav_prev": "→ قبلی",
    "nav_next": "بعدی ←",
    "nav_menu": "☰ منو",
    "open_sections": "☰ بخش‌ها",
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
    "contact_phone": "تلفنِ مؤلف",
    "contact_phone_val": "09309456655 · +98 930 945 6655",
    "contact_apps": "در دسترس در",
    "contact_apps_val": "ایتا · بله · واتساپ · تلگرام",
    "contact_email": "ایمیل",
    "contact_whatsapp_btn": "💬 پیام در واتساپ",
    "contact_email_btn": "✉ ارسالِ ایمیل",
    "contact_support_note": "اگر هنگامِ کار با سایت به مشکلی برخوردید، لطفاً "
        "مستقیماً با من تماس بگیرید یا پیام بدهید — با کمالِ میل کمک می‌کنم.",
    "ack_title": "سپاسگزاری",
    "ack_body": "با سپاسِ فراوان از استادِ راهنما، پروفسور بهروز مینائی-بیدگلی — "
        "درس‌گفتارها و مطالبِ درسِ یادگیری ماشینِ قابل‌اعتمادِ ایشان در دانشگاه علم "
        "و صنعت ایران، سرچشمه و بنیادِ همهٔ آنچه در این سکو ارائه شده است.",
    "lang_pick": "زبان را برگزینید",
    "pdf_cover_doc": "جزوهٔ درس — نظری و عملی",
    "pdf_quote_sec1": "همهٔ مدل‌ها غلط‌اند، اما بعضی سودمندند.",
    "pdf_quote_by_sec1": "جورج باکس",
    "pdf_quote_sec2": "آنچه را نمی‌توانم بسازم، نمی‌فهمم.",
    "pdf_quote_by_sec2": "ریچارد فاینمن",
    "pdf_quote_sec3": "بی‌عدالتی در هر جا، تهدیدی است برای عدالت در همه‌جا.",
    "pdf_quote_by_sec3": "مارتین لوتر کینگ",
    "pdf_quote_sec4": "دشمن را بشناس و خود را بشناس؛ در صد نبرد هرگز در خطر "
        "نخواهی بود.",
    "pdf_quote_by_sec4": "سون تزو — هنر جنگ",
    "pdf_quote_sec5": "اینکه بگویی حریم خصوصی برایت مهم نیست چون چیزی برای "
        "پنهان‌کردن نداری، مثل این است که بگویی آزادی بیان برایت مهم نیست چون "
        "حرفی برای گفتن نداری.",
    "pdf_quote_by_sec5": "ادوارد اسنودن",
    "pdf_quote_sec6": "بهتر است کاملاً مطمئن شویم هدفی که در ماشین می‌گذاریم "
        "همان هدفی است که به‌راستی می‌خواهیم.",
    "pdf_quote_by_sec6": "نوربرت وینر",
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
    "hero_practice_note": "اختر النظريّ لقراءة الشرح الدقيق، أو العمليّ لترى المفهوم "
        "يحدث حيًّا أمامك — حرّك مؤشّرًا أو اضغط زرًّا وشاهد الحساب الحقيقيّ يتكشّف "
        "أمامك.",
    "overview_label": "نظرة عامّة",
    "roadmap_label": "خريطة الموقع",
    "roadmap_title": "خريطة الموقع — البنية كاملةً بلمحة",
    "roadmap_hide": "إخفاء الخريطة",
    "nav_home": "⌂ الرئيسيّة",
    "nav_prev": "→ السابق",
    "nav_next": "التالي ←",
    "nav_menu": "☰ القائمة",
    "open_sections": "☰ الأقسام",
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
    "contact_phone": "هاتف المؤلّف",
    "contact_phone_val": "09309456655 · +98 930 945 6655",
    "contact_apps": "متوفّر عبر",
    "contact_apps_val": "إيتا · بله · واتساب · تلغرام",
    "contact_email": "البريد الإلكترونيّ",
    "contact_whatsapp_btn": "💬 راسلني على واتساب",
    "contact_email_btn": "✉ أرسل بريدًا إلكترونيًّا",
    "contact_support_note": "في حال واجهتك أيّة مشكلة أثناء استخدام الموقع، لا "
        "تتردّد في الاتصال بي أو مراسلتي مباشرةً — يسعدني تقديم المساعدة.",
    "ack_title": "شكر وتقدير",
    "ack_body": "بخالص الشكر والتقدير للأستاذ المشرف البروفيسور بهروز "
        "مينائي-بيدجلي — فمحاضراتُ مادّته «تعلُّم الآلة الموثوق» في جامعة العلوم "
        "والتكنولوجيا الإيرانيّة كانت المصدرَ والأساسَ لكلِّ ما تقدّمه هذه المنصّة.",
    "lang_pick": "اختر اللغة",
    "pdf_cover_doc": "كتيّب المادّة — النظريّ والعمليّ",
    "pdf_quote_sec1": "كلُّ النماذج خاطئة، لكنّ بعضها نافع.",
    "pdf_quote_by_sec1": "جورج بوكس",
    "pdf_quote_sec2": "ما لا أستطيع بناءه، لا أفهمه.",
    "pdf_quote_by_sec2": "ريتشارد فاينمان",
    "pdf_quote_sec3": "الظلم في أيّ مكانٍ تهديدٌ للعدل في كلّ مكان.",
    "pdf_quote_by_sec3": "مارتن لوثر كينغ الابن",
    "pdf_quote_sec4": "اعرف عدوّك واعرف نفسك، تَخُض مئة معركةٍ دون أن تكون في "
        "خطر.",
    "pdf_quote_by_sec4": "صن تزو — فنّ الحرب",
    "pdf_quote_sec5": "قولُك إنّك لا تكترث للخصوصيّة لأنْ لا شيء عندك تخفيه، "
        "كقولِك إنّك لا تكترث لحرّيّة التعبير لأنْ لا شيء عندك تقوله.",
    "pdf_quote_by_sec5": "إدوارد سنودن",
    "pdf_quote_sec6": "حريٌّ بنا أن نتيقّن أنّ الغاية التي نضعها في الآلة هي "
        "الغاية التي نريدها حقًّا.",
    "pdf_quote_by_sec6": "نوربرت فينر",
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
