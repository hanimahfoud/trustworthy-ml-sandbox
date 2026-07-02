"""
i18n_privacy.py -- Section V (Privacy, Poisoning & Federated Learning) strings.
Theory prose is deliberately full and explanatory (not bullet points).
Each practice demo carries a what/why/expect explainer trio.
"""
from __future__ import annotations

EN5 = {
    "sec5_title": "V · Privacy",
    "masthead_subtitle_5": "An interactive companion to privacy and poisoning — "
        "backdoor trojans, membership inference, differential privacy, and the "
        "gradient-leakage flaw of federated learning — every attack and defense "
        "computed live on real data.",
    "colophon_5b": "Section V · Privacy, Poisoning & Federated Learning",

    # demo-intro panel labels (localized)
    "di_what": "What this does",
    "di_why": "Why it matters",
    "di_expect": "What to look for",

    # theory nav
    "prv_poison": "Poisoning & Backdoors",
    "prv_privacy": "Privacy Attacks",
    "prv_dp": "Differential Privacy",
    "prv_noise": "Noise Mechanisms",
    "prv_fl": "Federated Learning",
    "prv_leak": "Gradient Leakage",

    # practice nav
    "pp_backdoor": "Backdoor Injection Lab",
    "pp_coin": "Randomized-Response Simulator",
    "pp_laplace": "Laplace Privacy Dashboard",
    "pp_leak": "Gradient-Leakage Simulator",

    # ============ THEORY 1: poisoning & backdoors ============
    "prv_poison_eyebrow": "Privacy · Plate 01",
    "prv_poison_p1": "Evasion attacks (Section IV) strike a finished model at test "
        "time. <em>Poisoning</em> attacks strike earlier and deeper — during "
        "<em>training</em>. By injecting a small amount of malicious data into the "
        "training set, an attacker bends the model's decision boundaries so that it "
        "learns the wrong behaviour from the start. Because the corruption is baked "
        "into the learned weights, it cannot be patched away at inference.",
    "prv_poison_p2": "The most dangerous form is <em>clean-label</em> poisoning. "
        "Here the attacker never changes any label — a picture of a dog stays "
        "labelled “dog”, so a human reviewing the data sees nothing wrong. Instead "
        "the attacker perturbs the image's features in latent space by a tiny, "
        "imperceptible amount so that they drift toward a target class. The model "
        "silently absorbs the poison while every label looks perfectly honest.",
    "prv_poison_p3": "A <em>backdoor</em> (or trojan) is even more theatrical. During "
        "training the attacker plants a <em>trigger</em> — a small sticker in the "
        "corner, or a fixed pixel pattern. The finished model is then a Jekyll and "
        "Hyde: on clean inputs it is perfectly accurate, so it passes every test. "
        "But the instant it sees the trigger on any image, it deliberately "
        "misclassifies. In an <em>all-to-one</em> backdoor every triggered image is "
        "forced to a single target class (say, “goldfish”); in an "
        "<em>all-to-all</em> backdoor the trigger shifts each class to the next.",
    "prv_poison_p4": "Defences try to spot the sabotage: <em>outlier detection</em> "
        "flags poisoned samples that sit oddly in feature space; <em>pruning</em> "
        "removes the dormant neurons that fire only for the trigger; and "
        "<em>randomized smoothing</em> during training blunts the model's "
        "sensitivity to the tiny trigger pattern.",
    "prv_poison_eqcap": "<b>Figure.</b> A backdoored model: accurate on clean "
        "inputs, but the trigger forces a chosen target class.",
    "prv_poison_call": "A model that scores 100% on your test set can still be "
        "betraying you — the test set simply never contained the trigger.",

    # ============ THEORY 2: privacy attacks ============
    "prv_privacy_eyebrow": "Privacy · Plate 02",
    "prv_privacy_p1": "Removing names from a dataset does not make it anonymous. "
        "<em>De-anonymization</em> re-identifies people by cross-referencing an "
        "“anonymous” release against another dataset that shares some of the same "
        "records. The classic case: Netflix published anonymized film ratings; "
        "researchers matched them against public IMDb profiles of the same users, "
        "and recovered private viewing histories — names and all.",
    "prv_privacy_p2": "A subtler threat is the <em>membership inference</em> attack. "
        "The attacker does not try to read the data directly; they only ask whether "
        "a particular person's record was part of the training set. The lever is "
        "overfitting: a model is usually a little more confident on the exact "
        "examples it memorized during training than on data it has never seen.",
    "prv_privacy_p3": "By watching the model's confidence scores, the attacker can "
        "separate “members” (in the training set) from “non-members” with accuracy "
        "well above a coin flip. This is a real privacy breach: merely knowing that "
        "someone's medical scan was in a hospital's training data can reveal that "
        "they have the condition the model was built to detect.",
    "prv_privacy_eqcap": "<b>Figure.</b> Members sit at higher confidence than "
        "non-members — the gap the attacker exploits.",
    "prv_privacy_call": "The wider the gap between training and test performance, "
        "the more the model leaks about who was in its training set.",

    # ============ THEORY 3: differential privacy ============
    "prv_dp_eyebrow": "Privacy · Plate 03",
    "prv_dp_p1": "<em>Differential privacy (DP)</em> is the mathematical gold "
        "standard for privacy. Its promise is precise: the output of an algorithm "
        "should barely change whether or not any single individual's record is "
        "included. If no one record can noticeably move the result, then no output "
        "can be traced back to any one person.",
    "prv_dp_p2": "Formally, an algorithm M is ε-differentially private if, for any "
        "two neighbouring databases D₁ and D₂ that differ in a single record, and "
        "any outcome y, the probabilities are close within a factor of e^ε. This is "
        "the definition a doctoral examiner will ask you to write down exactly.",
    "prv_dp_p3": "The parameter ε is the <em>privacy budget</em>. When ε = 0 we have "
        "e⁰ = 1, so the two probabilities are identical — perfect privacy, but the "
        "model has learned nothing useful. As ε grows, utility rises and privacy "
        "falls: larger ε means the presence of one record is easier to detect. "
        "Choosing ε is therefore an explicit, tunable trade-off between usefulness "
        "and protection.",
    "prv_dp_eqcap": "<b>Figure.</b> ε controls the privacy/utility trade-off: small "
        "ε hides individuals, large ε reveals more.",
    "prv_dp_call": "Differential privacy does not hide the forest to protect a tree; "
        "it guarantees that no single tree changes the shape of the forest.",

    # ============ THEORY 4: noise mechanisms ============
    "prv_noise_eyebrow": "Privacy · Plate 04",
    "prv_noise_p1": "Differential privacy is achieved by adding carefully calibrated "
        "<em>noise</em>. The most intuitive example is <em>randomized response</em>, "
        "a survey trick older than computers. To ask a sensitive question — “did you "
        "cheat on the exam?” — you have each student privately flip a coin. On "
        "heads they answer truthfully; on tails they flip again and answer at "
        "random.",
    "prv_noise_p2": "Now no individual answer is incriminating: any “yes” might just "
        "be the coin talking, so each student enjoys plausible deniability. Yet "
        "because we know the exact coin probabilities, we can algebraically remove "
        "the noise <em>in aggregate</em> and recover the true fraction of cheaters "
        "across the class. Privacy for the individual, accuracy for the population.",
    "prv_noise_p3": "For numeric data we use the <em>Laplace mechanism</em>: add "
        "noise drawn from a Laplace distribution whose scale is Δ/ε. Here Δ, the "
        "<em>sensitivity</em>, is the most that one record can change the answer. "
        "A smaller ε (more privacy) means a larger scale and noisier results; a "
        "larger sensitivity likewise demands more noise.",
    "prv_noise_eqcap": "<b>Figure.</b> Laplace noise of scale Δ/ε masks the true "
        "value while preserving the aggregate.",
    "prv_noise_call": "The art of DP is adding just enough noise to hide the person "
        "but not so much that you erase the pattern.",

    # ============ THEORY 5: federated learning ============
    "prv_fl_eyebrow": "Privacy · Plate 05",
    "prv_fl_p1": "<em>Federated learning (FL)</em> flips the usual pipeline. Instead "
        "of shipping private data (phone photos, hospital records) to a central "
        "server, the server ships the <em>model</em> out to each device. Training "
        "happens locally, and only the resulting <em>weights or gradients</em> are "
        "sent back, where the server aggregates them into an improved global model. "
        "The raw data never leaves the device.",
    "prv_fl_p2": "FL comes in two flavours. <em>Cross-device</em> FL spans millions "
        "of phones — huge in number but weak and intermittent. <em>Cross-silo</em> "
        "FL links a handful of institutions — a few hospitals or banks with "
        "structured, reliable data.",
    "prv_fl_p3": "Three challenges dominate. <em>Statistical heterogeneity</em> "
        "(non-IID data): each client's data follows a different distribution — one "
        "hospital images with X-ray, another with MRI. <em>System heterogeneity</em>: "
        "devices differ wildly in speed and connectivity, and slow “stragglers” "
        "stall synchronization. And <em>communication cost</em>: shuttling "
        "billion-parameter models back and forth is expensive, which is why FL "
        "leans on compression and quantization.",
    "prv_fl_eqcap": "<b>Figure.</b> The model travels to the data; only gradients "
        "return to the server.",
    "prv_fl_call": "Federated learning keeps the data at home — but, as the next "
        "plate shows, sending gradients is not the same as sending nothing.",

    # ============ THEORY 6: gradient leakage ============
    "prv_leak_eyebrow": "Privacy · Plate 06",
    "prv_leak_p1": "Federated learning feels private: only gradients leave the "
        "device, never the images themselves. The unsettling discovery is that this "
        "intuition is wrong. Gradients are computed <em>from</em> the data, and they "
        "carry enough information to reconstruct it.",
    "prv_leak_p2": "The <em>gradient-leakage attack</em> treats reconstruction as an "
        "optimization problem: a malicious server searches for the input that would "
        "have produced the observed gradient, and iteratively refines it. For a "
        "simple model the leak is exact — the gradient of a linear layer on one "
        "example is literally the input scaled by the prediction error, so the "
        "original image can be read straight out of the shared gradient.",
    "prv_leak_p3": "The lesson is that federated learning alone is not a privacy "
        "guarantee; it must be combined with differential privacy (DP-FL) or secure "
        "aggregation so that the gradients themselves are protected before they ever "
        "reach the server.",
    "prv_leak_eqcap": "<b>Figure.</b> From a shared gradient, an attacker "
        "reconstructs the client's private input.",
    "prv_leak_call": "Sending gradients instead of data is not privacy for free — "
        "the data is still hiding inside the numbers.",

    # ============ PRACTICE 1: backdoor lab ============
    "pp_backdoor_eyebrow": "Practice · Demo 18",
    "pp_backdoor": "Backdoor Injection Lab",
    "pp_backdoor_what": "We train a real CNN that has been poisoned with a corner "
        "trigger, then let you flip that trigger on and off on test images and watch "
        "the prediction change.",
    "pp_backdoor_why": "It shows that a model can pass every clean-data test yet hide "
        "a trojan: high accuracy is no proof of trustworthiness.",
    "pp_backdoor_expect": "Clean images are classified correctly; the moment the "
        "trigger appears, the model jumps to the attacker's target class with high "
        "confidence.",
    "pp_backdoor_sample": "Sample image",
    "pp_backdoor_trigger": "Stamp the trigger",
    "pp_backdoor_cap_clean": "<b>Figure 1.</b> The image as seen by the model.",
    "pp_backdoor_cap_pred": "prediction",
    "pp_backdoor_clean_acc": "clean-data accuracy",
    "pp_backdoor_asr": "trigger success rate",
    "pp_backdoor_note": "The backdoored model is accurate on clean data yet obeys the "
        "trigger every time — a trojan you would never catch by measuring accuracy "
        "alone.",

    # ============ PRACTICE 2: randomized response ============
    "pp_coin_eyebrow": "Practice · Demo 19",
    "pp_coin_what": "We simulate a sensitive survey answered with the coin-flip "
        "randomized-response protocol, then recover the true population rate from the "
        "noisy answers.",
    "pp_coin_why": "It is the simplest working example of differential privacy: each "
        "person is protected, yet the aggregate statistic stays accurate.",
    "pp_coin_expect": "No single answer can be trusted about any individual, but the "
        "estimated rate closes in on the real rate as the crowd grows.",
    "pp_coin_true": "True “yes” rate in the population",
    "pp_coin_n": "Number of respondents",
    "pp_coin_ptruth": "Probability of answering truthfully",
    "pp_coin_cap": "<b>Figure.</b> The estimator (from noisy answers) converges to "
        "the true rate as N grows.",
    "pp_coin_est": "estimated rate",
    "pp_coin_actual": "actual rate",
    "pp_coin_note": "We cannot tell whether any one respondent said yes — that is the "
        "privacy — yet the corrected aggregate recovers the true rate. Privacy for "
        "the individual, accuracy for the population.",

    # ============ PRACTICE 3: Laplace dashboard ============
    "pp_laplace_eyebrow": "Practice · Demo 20",
    "pp_laplace_what": "We publish a salary histogram under the Laplace mechanism and "
        "let you move the privacy budget ε to see the noise grow or shrink.",
    "pp_laplace_why": "It makes the privacy/utility trade-off tangible: you are "
        "literally dialing the exchange rate between protection and accuracy.",
    "pp_laplace_expect": "At large ε the private histogram matches the real one; as ε "
        "shrinks, the bars wobble and blur to hide any individual salary.",
    "pp_laplace_eps": "Privacy budget ε",
    "pp_laplace_cap": "<b>Figure.</b> True vs differentially-private salary "
        "histogram at the chosen ε.",
    "pp_laplace_err": "mean distortion",
    "pp_laplace_scale": "Laplace scale (Δ/ε)",
    "pp_laplace_note": "Small ε buys strong privacy at the cost of a noisy, distorted "
        "histogram; large ε reproduces the data almost exactly but protects no one. "
        "There is no free lunch — only a dial.",

    # ============ PRACTICE 4: gradient leakage ============
    "pp_leak_eyebrow": "Practice · Demo 21",
    "pp_leak_what": "A client shares only the gradient of a linear model for one "
        "private image; the server runs the leakage attack and reconstructs that "
        "image from the gradient alone.",
    "pp_leak_why": "It punctures the belief that federated learning is automatically "
        "private — the raw data can be read straight out of the shared gradients.",
    "pp_leak_expect": "Starting from the “obfuscated” gradient, the reconstruction "
        "matches the original image almost perfectly (reconstruction error near "
        "zero).",
    "pp_leak_sample": "Client's private image",
    "pp_leak_run": "Execute gradient-leakage attack",
    "pp_leak_cap_true": "<b>Figure 1.</b> The client's true private image.",
    "pp_leak_cap_rec": "<b>Figure 2.</b> Reconstructed by the server from the "
        "gradient alone.",
    "pp_leak_err": "reconstruction error",
    "pp_leak_note": "Federated learning alone is not enough: the attacker recovered "
        "the private image from the gradients. Real deployments must add "
        "differential privacy (DP-FL) or secure aggregation.",
}


# ---- helper: build FA/AR by starting from EN and overriding (only text keys) ----
FA5 = {
    "sec5_title": "۵ · حریم خصوصی",
    "masthead_subtitle_5": "همراهی تعاملی برای حریم خصوصی و مسموم‌سازی — درهای پشتیِ "
        "تروجان، استنتاج عضویت، حریم خصوصی تفاضلی، و نقصِ نشتِ گرادیانِ یادگیری فدرال — "
        "هر حمله و دفاع زنده روی دادهٔ واقعی محاسبه می‌شود.",
    "colophon_5b": "بخشِ پنجم · حریم خصوصی، مسموم‌سازی و یادگیری فدرال",

    "di_what": "این ابزار چه می‌کند",
    "di_why": "چرا مهم است",
    "di_expect": "به چه چیزی نگاه کنید",

    "prv_poison": "مسموم‌سازی و درهای پشتی",
    "prv_privacy": "حملات حریم خصوصی",
    "prv_dp": "حریم خصوصی تفاضلی",
    "prv_noise": "سازوکارهای نویز",
    "prv_fl": "یادگیری فدرال",
    "prv_leak": "نشتِ گرادیان",

    "pp_backdoor": "آزمایشگاهِ تزریقِ درِ پشتی",
    "pp_coin": "شبیه‌سازِ پاسخِ تصادفی",
    "pp_laplace": "داشبوردِ حریمِ لاپلاس",
    "pp_leak": "شبیه‌سازِ نشتِ گرادیان",

    "prv_poison_eyebrow": "حریم خصوصی · لوح ۰۱",
    "prv_poison_p1": "حملاتِ گریز (بخشِ ۴) مدلِ آماده را هنگامِ آزمون می‌زنند. حملاتِ "
        "<em>مسموم‌سازی</em> زودتر و ژرف‌تر می‌زنند — هنگامِ <em>آموزش</em>. مهاجم با "
        "تزریقِ اندکی دادهٔ خبیث به مجموعهٔ آموزش، مرزهای تصمیمِ مدل را خم می‌کند تا از "
        "آغاز رفتاری نادرست بیاموزد. چون فساد در وزن‌های آموخته پخته شده، در استنتاج "
        "وصله‌پذیر نیست.",
    "prv_poison_p2": "خطرناک‌ترین گونه، مسمومِ <em>برچسب‌پاک</em> است. اینجا مهاجم هیچ "
        "برچسبی را تغییر نمی‌دهد — تصویرِ سگ همچنان «سگ» می‌ماند، پس بازبینِ انسانی "
        "چیزی نمی‌بیند. در عوض ویژگی‌های تصویر را در فضای کامن به‌مقداری ریز و نامحسوس "
        "می‌آشوبد تا به‌سوی کلاسِ هدف بلغزند. مدل بی‌سروصدا زهر را جذب می‌کند حال‌آنکه هر "
        "برچسب کاملاً صادق می‌نماید.",
    "prv_poison_p3": "<em>درِ پشتی</em> (تروجان) حتی نمایشی‌تر است. مهاجم هنگامِ آموزش "
        "یک <em>ماشه</em> می‌کارد — برچسبی کوچک در گوشه یا الگوی پیکسلیِ ثابت. مدلِ "
        "نهایی دوچهره می‌شود: روی ورودیِ پاک کاملاً دقیق است و هر آزمون را می‌گذراند. "
        "اما لحظه‌ای که ماشه را روی هر تصویری ببیند، عمداً بد طبقه‌بندی می‌کند. در درِ "
        "پشتیِ <em>همه‌به‌یک</em> هر تصویرِ ماشه‌دار به یک کلاسِ هدف رانده می‌شود؛ در "
        "<em>همه‌به‌همه</em> ماشه هر کلاس را به کلاسِ بعدی می‌بَرد.",
    "prv_poison_p4": "دفاع‌ها می‌کوشند خرابکاری را بیابند: <em>کشفِ پرت</em> نمونه‌های "
        "مسموم را که در فضای ویژگی ناجور می‌نشینند نشان می‌کند؛ <em>هرس</em> نورون‌های "
        "خفته‌ای را که فقط برای ماشه فعال می‌شوند برمی‌دارد؛ و <em>هموارسازیِ تصادفی</em> "
        "هنگامِ آموزش حساسیتِ مدل به الگوی ریزِ ماشه را کند می‌کند.",
    "prv_poison_eqcap": "<b>شکل.</b> مدلِ درِ‌پشتی‌دار: روی ورودیِ پاک دقیق، اما ماشه "
        "کلاسِ هدفِ برگزیده را تحمیل می‌کند.",
    "prv_poison_call": "مدلی که روی مجموعهٔ آزمونت ۱۰۰٪ می‌گیرد باز هم می‌تواند به تو "
        "خیانت کند — مجموعهٔ آزمون صرفاً هرگز ماشه را نداشت.",

    "prv_privacy_eyebrow": "حریم خصوصی · لوح ۰۲",
    "prv_privacy_p1": "حذفِ نام‌ها از یک مجموعه‌داده آن را ناشناس نمی‌کند. "
        "<em>لغوِ ناشناسی</em> افراد را با ارجاعِ متقابلِ یک انتشارِ «ناشناس» به "
        "مجموعه‌ای دیگر که برخی رکوردهای مشترک دارد بازشناسی می‌کند. نمونهٔ کلاسیک: "
        "نتفلیکس امتیازهای فیلمِ ناشناس‌شده منتشر کرد؛ پژوهشگران آن‌ها را با نیمرخ‌های "
        "عمومیِ IMDb همان کاربران تطبیق دادند و تاریخچهٔ تماشای خصوصی — با نام — را "
        "بازیافتند.",
    "prv_privacy_p2": "تهدیدی ظریف‌تر حملهٔ <em>استنتاجِ عضویت</em> است. مهاجم نمی‌کوشد "
        "داده را مستقیم بخواند؛ فقط می‌پرسد آیا رکوردِ فردی مشخص در مجموعهٔ آموزش بوده "
        "یا نه. اهرم، بیش‌برازش است: مدل معمولاً روی نمونه‌هایی که در آموزش حفظ کرده "
        "اندکی مطمئن‌تر است تا روی داده‌ای که هرگز ندیده.",
    "prv_privacy_p3": "با پاییدنِ نمراتِ اطمینانِ مدل، مهاجم می‌تواند «اعضا» (در "
        "مجموعهٔ آموزش) را از «غیراعضا» با دقتی بسیار بالاتر از پرتابِ سکه جدا کند. این "
        "نقضِ واقعیِ حریم است: صرفِ دانستنِ این‌که اسکنِ پزشکیِ کسی در دادهٔ آموزشِ "
        "بیمارستان بوده می‌تواند فاش کند که او به بیماریِ موردِ تشخیصِ مدل مبتلاست.",
    "prv_privacy_eqcap": "<b>شکل.</b> اعضا در اطمینانِ بالاتر از غیراعضا می‌نشینند — "
        "شکافی که مهاجم بهره‌برداری می‌کند.",
    "prv_privacy_call": "هرچه شکافِ میانِ کاراییِ آموزش و آزمون بزرگ‌تر باشد، مدل بیشتر "
        "دربارهٔ این‌که چه کسی در دادهٔ آموزشش بوده نشت می‌کند.",

    "prv_dp_eyebrow": "حریم خصوصی · لوح ۰۳",
    "prv_dp_p1": "<em>حریم خصوصی تفاضلی (DP)</em> استانداردِ طلاییِ ریاضیِ حریم است. "
        "وعده‌اش دقیق است: خروجیِ یک الگوریتم باید به‌سختی تغییر کند چه رکوردِ هر فردِ "
        "واحد در آن باشد چه نباشد. اگر هیچ رکوردِ واحدی نتواند نتیجه را محسوس جابه‌جا "
        "کند، هیچ خروجی‌ای به فردی ردیابی نمی‌شود.",
    "prv_dp_p2": "به‌طورِ رسمی، الگوریتمِ M دارای حریمِ تفاضلیِ ε است اگر برای هر دو "
        "پایگاهِ همسایهٔ ₁D و ₂D که در یک رکورد فرق دارند و هر پیامدِ y، احتمال‌ها درونِ "
        "ضریبِ e^ε نزدیک باشند. این همان تعریفی است که ممتحنِ دکتری از تو می‌خواهد "
        "دقیق بنویسی.",
    "prv_dp_p3": "پارامترِ ε <em>بودجهٔ حریم</em> است. وقتی ε = ۰ داریم e⁰ = ۱، پس دو "
        "احتمال یکسان‌اند — حریمِ کامل، اما مدل چیزِ مفیدی نیاموخته. با رشدِ ε سودمندی "
        "بالا و حریم پایین می‌رود: εِ بزرگ‌تر یعنی حضورِ یک رکورد آسان‌تر آشکار می‌شود. "
        "پس انتخابِ ε یک بده‌بستانِ صریح و قابلِ‌تنظیم میانِ سودمندی و حفاظت است.",
    "prv_dp_eqcap": "<b>شکل.</b> ε بده‌بستانِ حریم/سودمندی را کنترل می‌کند: εِ کوچک "
        "افراد را پنهان، εِ بزرگ بیشتر را آشکار می‌کند.",
    "prv_dp_call": "حریمِ تفاضلی جنگل را پنهان نمی‌کند تا درختی را حفظ کند؛ تضمین "
        "می‌کند هیچ درختِ واحدی شکلِ جنگل را تغییر ندهد.",

    "prv_noise_eyebrow": "حریم خصوصی · لوح ۰۴",
    "prv_noise_p1": "حریمِ تفاضلی با افزودنِ <em>نویزِ</em> به‌دقت کالیبره‌شده به دست "
        "می‌آید. شهودی‌ترین نمونه <em>پاسخِ تصادفی</em> است، ترفندی نظرسنجی کهن‌تر از "
        "رایانه‌ها. برای پرسشی حساس — «آیا در امتحان تقلب کردی؟» — هر دانشجو پنهانی "
        "سکه‌ای می‌اندازد. رو: راست بگو؛ پشت: دوباره بینداز و تصادفی پاسخ بده.",
    "prv_noise_p2": "اکنون هیچ پاسخِ فردی مجرمانه نیست: هر «بله» شاید صرفاً حرفِ سکه "
        "باشد، پس هر دانشجو انکارپذیریِ موجه دارد. اما چون احتمال‌های دقیقِ سکه را "
        "می‌دانیم، می‌توانیم نویز را <em>در تجمیع</em> جبری حذف کنیم و کسرِ واقعیِ "
        "متقلبان را در کلاس بازیابیم. حریم برای فرد، دقت برای جمعیت.",
    "prv_noise_p3": "برای دادهٔ عددی <em>سازوکارِ لاپلاس</em> را به کار می‌بریم: نویزی "
        "از توزیعِ لاپلاس با مقیاسِ Δ/ε بیفزا. اینجا Δ، <em>حساسیت</em>، بیشترین "
        "تغییری است که یک رکورد در پاسخ می‌دهد. εِ کوچک‌تر (حریمِ بیشتر) یعنی مقیاسِ "
        "بزرگ‌تر و نتایجِ نویزی‌تر؛ حساسیتِ بزرگ‌تر نیز نویزِ بیشتر می‌طلبد.",
    "prv_noise_eqcap": "<b>شکل.</b> نویزِ لاپلاس با مقیاسِ Δ/ε مقدارِ واقعی را می‌پوشاند "
        "و تجمیع را نگه می‌دارد.",
    "prv_noise_call": "هنرِ DP افزودنِ نویزِ درست‌به‌اندازه است تا فرد پنهان شود اما نه "
        "آن‌قدر که الگو محو گردد.",

    "prv_fl_eyebrow": "حریم خصوصی · لوح ۰۵",
    "prv_fl_p1": "<em>یادگیریِ فدرال (FL)</em> خطِ لولهٔ معمول را وارونه می‌کند. به‌جای "
        "فرستادنِ دادهٔ خصوصی (عکس‌های گوشی، پرونده‌های بیمارستان) به خادمِ مرکزی، خادم "
        "<em>مدل</em> را به هر دستگاه می‌فرستد. آموزش محلی رخ می‌دهد و فقط <em>وزن‌ها یا "
        "گرادیان‌های</em> حاصل بازفرستاده می‌شوند تا خادم آن‌ها را در مدلی سراسری و بهتر "
        "تجمیع کند. دادهٔ خام هرگز دستگاه را ترک نمی‌کند.",
    "prv_fl_p2": "FL دو گونه دارد. <em>عبرِ‌دستگاه</em> میلیون‌ها گوشی را دربر می‌گیرد — "
        "بی‌شمار اما ضعیف و منقطع. <em>عبرِ‌سیلو</em> چند نهاد را پیوند می‌دهد — چند "
        "بیمارستان یا بانک با دادهٔ ساخت‌یافته و موثق.",
    "prv_fl_p3": "سه چالش غالب‌اند. <em>ناهمگنیِ آماری</em> (دادهٔ غیرIID): دادهٔ هر "
        "کلاینت توزیعی متفاوت دارد — بیمارستانی با اشعهٔ ایکس، دیگری با MRI. "
        "<em>ناهمگنیِ سیستمی</em>: دستگاه‌ها در سرعت و اتصال بسیار فرق دارند و "
        "«کندروها» مزامنه را متوقف می‌کنند. و <em>هزینهٔ ارتباط</em>: جابه‌جاییِ مدل‌های "
        "میلیارد-پارامتری گران است، ازین‌رو FL به فشرده‌سازی و کوانتش تکیه می‌کند.",
    "prv_fl_eqcap": "<b>شکل.</b> مدل به‌سوی داده سفر می‌کند؛ فقط گرادیان‌ها به خادم "
        "بازمی‌گردند.",
    "prv_fl_call": "یادگیریِ فدرال داده را خانه نگه می‌دارد — اما، چنان‌که لوحِ بعدی "
        "نشان می‌دهد، فرستادنِ گرادیان مانندِ نفرستادنِ چیزی نیست.",

    "prv_leak_eyebrow": "حریم خصوصی · لوح ۰۶",
    "prv_leak_p1": "یادگیریِ فدرال خصوصی می‌نماید: فقط گرادیان‌ها دستگاه را ترک می‌کنند، "
        "نه خودِ تصاویر. کشفِ نگران‌کننده این است که این شهود نادرست است. گرادیان‌ها "
        "<em>از</em> داده محاسبه می‌شوند و اطلاعاتِ کافی برای بازسازیِ آن را حمل "
        "می‌کنند.",
    "prv_leak_p2": "<em>حملهٔ نشتِ گرادیان</em> بازسازی را مسئله‌ای بهینه‌سازی می‌بیند: "
        "خادمِ خبیث ورودی‌ای را می‌جوید که گرادیانِ مشاهده‌شده را می‌ساخت و آن را تکراری "
        "پالایش می‌کند. برای مدلی ساده، نشت دقیق است — گرادیانِ یک لایهٔ خطی روی یک "
        "نمونه عیناً ورودیِ مقیاس‌شده با خطای پیش‌بینی است، پس تصویرِ اصلی را می‌توان "
        "مستقیم از گرادیانِ مشترک خواند.",
    "prv_leak_p3": "درس این است که یادگیریِ فدرال به‌تنهایی تضمینِ حریم نیست؛ باید با "
        "حریمِ تفاضلی (DP-FL) یا تجمیعِ امن ترکیب شود تا خودِ گرادیان‌ها پیش از رسیدن به "
        "خادم محافظت شوند.",
    "prv_leak_eqcap": "<b>شکل.</b> از یک گرادیانِ مشترک، مهاجم ورودیِ خصوصیِ کلاینت را "
        "بازسازی می‌کند.",
    "prv_leak_call": "فرستادنِ گرادیان به‌جای داده حریمِ رایگان نیست — داده هنوز درونِ "
        "اعداد پنهان است.",

    "pp_backdoor_eyebrow": "تمرین · نمایشِ ۱۸",
    "pp_backdoor_what": "یک CNNِ واقعی را که با ماشهٔ گوشه‌ای مسموم شده آموزش می‌دهیم، "
        "سپس می‌گذاریم ماشه را روی تصاویرِ آزمون روشن/خاموش کنی و تغییرِ پیش‌بینی را "
        "ببینی.",
    "pp_backdoor_why": "نشان می‌دهد مدلی می‌تواند هر آزمونِ دادهٔ‌پاک را بگذراند و باز "
        "تروجانی پنهان کند: دقتِ بالا گواهِ اعتماد نیست.",
    "pp_backdoor_expect": "تصاویرِ پاک درست طبقه‌بندی می‌شوند؛ لحظه‌ای که ماشه ظاهر شود، "
        "مدل با اطمینانِ بالا به کلاسِ هدفِ مهاجم می‌پرد.",
    "pp_backdoor_sample": "تصویرِ نمونه",
    "pp_backdoor_trigger": "ماشه را بزن",
    "pp_backdoor_cap_clean": "<b>شکل ۱.</b> تصویر آن‌گونه که مدل می‌بیند.",
    "pp_backdoor_cap_pred": "پیش‌بینی",
    "pp_backdoor_clean_acc": "دقتِ دادهٔ‌پاک",
    "pp_backdoor_asr": "نرخِ موفقیتِ ماشه",
    "pp_backdoor_note": "مدلِ درِ‌پشتی‌دار روی دادهٔ پاک دقیق است اما هر بار از ماشه "
        "اطاعت می‌کند — تروجانی که با سنجشِ دقت به‌تنهایی هرگز نمی‌گیری‌اش.",

    "pp_coin_eyebrow": "تمرین · نمایشِ ۱۹",
    "pp_coin_what": "نظرسنجی‌ای حساس را با پروتکلِ پاسخِ تصادفیِ سکه‌ای شبیه‌سازی می‌کنیم، "
        "سپس نرخِ واقعیِ جمعیت را از پاسخ‌های نویزی بازمی‌یابیم.",
    "pp_coin_why": "ساده‌ترین نمونهٔ کارآمدِ حریمِ تفاضلی است: هر فرد محافظت می‌شود، اما "
        "آمارِ تجمیعی دقیق می‌ماند.",
    "pp_coin_expect": "هیچ پاسخِ واحدی دربارهٔ فرد قابلِ‌اعتماد نیست، اما با رشدِ جمعیت "
        "نرخِ برآوردی به نرخِ واقعی نزدیک می‌شود.",
    "pp_coin_true": "نرخِ واقعیِ «بله» در جمعیت",
    "pp_coin_n": "شمارِ پاسخ‌دهندگان",
    "pp_coin_ptruth": "احتمالِ پاسخِ صادقانه",
    "pp_coin_cap": "<b>شکل.</b> برآوردگر (از پاسخ‌های نویزی) با رشدِ N به نرخِ واقعی "
        "همگرا می‌شود.",
    "pp_coin_est": "نرخِ برآوردی",
    "pp_coin_actual": "نرخِ واقعی",
    "pp_coin_note": "نمی‌توانیم بگوییم آیا فردی «بله» گفته — این همان حریم است — اما "
        "تجمیعِ تصحیح‌شده نرخِ واقعی را بازمی‌یابد. حریم برای فرد، دقت برای جمعیت.",

    "pp_laplace_eyebrow": "تمرین · نمایشِ ۲۰",
    "pp_laplace_what": "هیستوگرامِ حقوق را زیرِ سازوکارِ لاپلاس منتشر می‌کنیم و می‌گذاریم "
        "بودجهٔ حریمِ ε را جابه‌جا کنی تا رشد یا کاهشِ نویز را ببینی.",
    "pp_laplace_why": "بده‌بستانِ حریم/سودمندی را ملموس می‌کند: عملاً نرخِ تبادلِ میانِ "
        "حفاظت و دقت را می‌چرخانی.",
    "pp_laplace_expect": "در εِ بزرگ هیستوگرامِ خصوصی با واقعی می‌خواند؛ با کوچک‌شدنِ ε "
        "میله‌ها می‌لرزند و تار می‌شوند تا هر حقوقِ فردی پنهان شود.",
    "pp_laplace_eps": "بودجهٔ حریم ε",
    "pp_laplace_cap": "<b>شکل.</b> هیستوگرامِ حقوقِ واقعی در برابرِ حریمِ‌تفاضلی در εِ "
        "برگزیده.",
    "pp_laplace_err": "اعوجاجِ میانگین",
    "pp_laplace_scale": "مقیاسِ لاپلاس (Δ/ε)",
    "pp_laplace_note": "εِ کوچک حریمِ قوی می‌خرد به بهای هیستوگرامی نویزی و مخدوش؛ εِ "
        "بزرگ داده را تقریباً عیناً بازتولید می‌کند اما کسی را حفظ نمی‌کند. ناهارِ "
        "مجانی نیست — فقط یک پیچ.",

    "pp_leak_eyebrow": "تمرین · نمایشِ ۲۱",
    "pp_leak_what": "یک کلاینت فقط گرادیانِ یک مدلِ خطی را برای یک تصویرِ خصوصی به "
        "اشتراک می‌گذارد؛ خادم حملهٔ نشت را اجرا و آن تصویر را تنها از گرادیان بازسازی "
        "می‌کند.",
    "pp_leak_why": "این باور را که یادگیریِ فدرال خودبه‌خود خصوصی است می‌شکافد — دادهٔ "
        "خام را می‌توان مستقیم از گرادیان‌های مشترک خواند.",
    "pp_leak_expect": "از گرادیانِ «مبهم» آغاز می‌شود و بازسازی تقریباً کاملاً با تصویرِ "
        "اصلی می‌خواند (خطای بازسازی نزدیکِ صفر).",
    "pp_leak_sample": "تصویرِ خصوصیِ کلاینت",
    "pp_leak_run": "اجرای حملهٔ نشتِ گرادیان",
    "pp_leak_cap_true": "<b>شکل ۱.</b> تصویرِ خصوصیِ واقعیِ کلاینت.",
    "pp_leak_cap_rec": "<b>شکل ۲.</b> بازسازی‌شده توسطِ خادم تنها از گرادیان.",
    "pp_leak_err": "خطای بازسازی",
    "pp_leak_note": "یادگیریِ فدرال به‌تنهایی کافی نیست: مهاجم تصویرِ خصوصی را از "
        "گرادیان‌ها بازیافت. استقرارِ واقعی باید حریمِ تفاضلی (DP-FL) یا تجمیعِ امن "
        "بیفزاید.",
}


AR5 = {
    "sec5_title": "٥ · الخصوصيّة",
    "masthead_subtitle_5": "مرافِقٌ تفاعليٌّ للخصوصيّة والتسميم — الأبواب الخلفيّة "
        "التروجانيّة، واستنتاج العضويّة، والخصوصيّة التفاضليّة، وثغرة تسريب التدرّج في "
        "التعلّم الموحّد — كلُّ هجومٍ ودفاعٍ يُحسَب آنيًّا على بياناتٍ حقيقيّة.",
    "colophon_5b": "القسم الخامس · الخصوصيّة والتسميم والتعلّم الموحّد",

    "di_what": "ماذا يفعل هذا التطبيق",
    "di_why": "لماذا يهمّ",
    "di_expect": "ما الذي تراقبه",

    "prv_poison": "التسميم والأبواب الخلفيّة",
    "prv_privacy": "هجمات الخصوصيّة",
    "prv_dp": "الخصوصيّة التفاضليّة",
    "prv_noise": "آليات الضجيج",
    "prv_fl": "التعلّم الموحّد",
    "prv_leak": "تسريب التدرّج",

    "pp_backdoor": "مختبر زرع الباب الخلفيّ",
    "pp_coin": "محاكي الاستجابة العشوائيّة",
    "pp_laplace": "لوحة خصوصيّة لابلاس",
    "pp_leak": "محاكي تسريب التدرّج",

    "prv_poison_eyebrow": "الخصوصيّة · لوح ٠١",
    "prv_poison_p1": "هجماتُ التهرّب (القسم الرابع) تضرب نموذجًا جاهزًا وقتَ الاختبار. "
        "أمّا هجماتُ <em>التسميم</em> فتضرب أبكرَ وأعمق — أثناء <em>التدريب</em>. بحقن "
        "قدرٍ صغيرٍ من البيانات الخبيثة في مجموعة التدريب، يُزيح المهاجمُ حدودَ قرار "
        "النموذج فيتعلّم سلوكًا خاطئًا من البداية. ولأنّ الفساد مخبوزٌ في الأوزان "
        "المُتعلَّمة، لا يمكن ترقيعُه وقتَ الاستنتاج.",
    "prv_poison_p2": "أخطرُ صورةٍ هي التسميمُ <em>نظيفُ الملصق</em>. هنا لا يُغيّر "
        "المهاجمُ أيَّ ملصق — تبقى صورةُ الكلب مُوسَمةً «كلب»، فلا يرى المراجعُ البشريّ "
        "خطأً. بل يُشوّش ميزاتِ الصورة في الفضاء الكامن بقدرٍ ضئيلٍ غيرِ محسوسٍ لتنجرف "
        "نحو صنفٍ هدف. يمتصّ النموذجُ الزهرَ بصمتٍ بينما يبدو كلُّ ملصقٍ صادقًا تمامًا.",
    "prv_poison_p3": "و<em>البابُ الخلفيّ</em> (التروجان) أكثرُ مسرحيّة. أثناء التدريب "
        "يزرع المهاجمُ <em>مُشغّلًا</em> — ملصقًا صغيرًا في الزاوية أو نمطَ بكسلاتٍ "
        "ثابتًا. يصير النموذجُ النهائيّ ذا وجهين: على المُدخَلات النظيفة دقيقٌ تمامًا "
        "فيجتاز كلَّ اختبار. لكن لحظةَ يرى المُشغّلَ على أيّ صورة، يُخطئ عمدًا. في بابٍ "
        "خلفيٍّ <em>من الكلّ إلى واحد</em> تُدفَع كلُّ صورةٍ مُشغَّلةٍ إلى صنفٍ هدفٍ واحد؛ "
        "وفي <em>من الكلّ إلى الكلّ</em> يُزيح المُشغّلُ كلَّ صنفٍ إلى التالي.",
    "prv_poison_p4": "تحاول الدفاعاتُ رصدَ التخريب: <em>كشفُ الشواذّ</em> يُعلِّم "
        "العيّناتِ المسمومةَ التي تجلس شاذّةً في فضاء الميزات؛ و<em>التقليمُ</em> يزيل "
        "الخلايا العصبيّة الخاملة التي لا تنشط إلّا للمُشغّل؛ و<em>التنعيمُ العشوائيّ</em> "
        "أثناء التدريب يُثلِم حساسيّةَ النموذج لنمط المُشغّل الصغير.",
    "prv_poison_eqcap": "<b>شكل.</b> نموذجٌ ذو بابٍ خلفيّ: دقيقٌ على المُدخَلات "
        "النظيفة، لكنّ المُشغّلَ يفرض صنفَ الهدف المختار.",
    "prv_poison_call": "النموذجُ الذي يُحرِز ١٠٠٪ على مجموعة اختبارك قد يظلّ يخونك — "
        "مجموعةُ الاختبار ببساطةٍ لم تحوِ المُشغّلَ قطّ.",

    "prv_privacy_eyebrow": "الخصوصيّة · لوح ٠٢",
    "prv_privacy_p1": "حذفُ الأسماء من مجموعة بيانات لا يجعلها مجهولة. "
        "<em>إلغاءُ المجهوليّة</em> يُعيد التعرّفَ على الأشخاص بالمطابقة المتقاطعة بين "
        "إصدارٍ «مجهول» ومجموعةٍ أخرى تشترك في بعض السجلّات. الحالةُ الكلاسيكيّة: نشرت "
        "نتفليكس تقييماتِ أفلامٍ مجهولة؛ طابقها الباحثون مع ملفّات IMDb العامّة لنفس "
        "المستخدمين، فاستعادوا سجلّاتِ مشاهدةٍ خاصّة — بالأسماء.",
    "prv_privacy_p2": "تهديدٌ أدهى هو هجومُ <em>استنتاج العضويّة</em>. لا يحاول المهاجمُ "
        "قراءةَ البيانات مباشرةً؛ يسأل فقط إن كان سجلُّ شخصٍ بعينه جزءًا من مجموعة "
        "التدريب. الرافعةُ هي فرطُ التخصيص: يكون النموذجُ عادةً أكثرَ ثقةً قليلًا على "
        "الأمثلة التي حفظها أثناء التدريب منه على بياناتٍ لم يرها قطّ.",
    "prv_privacy_p3": "بمراقبة درجات ثقة النموذج، يستطيع المهاجمُ فصلَ «الأعضاء» (في "
        "مجموعة التدريب) عن «غير الأعضاء» بدقّةٍ أعلى بكثيرٍ من رمي العملة. هذا خرقٌ "
        "حقيقيٌّ للخصوصيّة: مجرّدُ معرفة أنّ فحصَ شخصٍ الطبّيّ كان في بيانات تدريب "
        "المستشفى قد يكشف أنّه مصابٌ بالمرض الذي بُني النموذجُ لكشفه.",
    "prv_privacy_eqcap": "<b>شكل.</b> يجلس الأعضاءُ عند ثقةٍ أعلى من غير الأعضاء — "
        "الفجوةُ التي يستغلّها المهاجم.",
    "prv_privacy_call": "كلّما اتّسعت الفجوةُ بين أداء التدريب والاختبار، تسرّب النموذجُ "
        "أكثرَ عمّن كان في بيانات تدريبه.",

    "prv_dp_eyebrow": "الخصوصيّة · لوح ٠٣",
    "prv_dp_p1": "<em>الخصوصيّةُ التفاضليّة (DP)</em> هي المعيارُ الذهبيّ الرياضيّ "
        "للخصوصيّة. وعدُها دقيق: يجب ألّا يتغيّر مخرجُ الخوارزميّة إلّا بالكاد سواءٌ "
        "أُدرِج سجلُّ أيّ فردٍ واحد أم لا. فإن لم يستطع أيُّ سجلٍّ واحدٍ تحريكَ النتيجة "
        "بوضوح، فلا يمكن تعقّبُ أيّ مخرجٍ إلى أيّ شخص.",
    "prv_dp_p2": "رسميًّا، تكون الخوارزميّةُ M خصوصيّةً تفاضليّةً بمعامل ε إذا كان لأيّ "
        "قاعدتَي بياناتٍ متجاورتين ₁D و₂D تختلفان في سجلٍّ واحد، ولأيّ نتيجة y، "
        "الاحتمالان متقاربَين ضمن عامل e^ε. هذا هو التعريفُ الذي سيطلب ممتحنُ الدكتوراه "
        "أن تكتبه بدقّة.",
    "prv_dp_p3": "المعاملُ ε هو <em>ميزانيّةُ الخصوصيّة</em>. عند ε = ٠ يكون e⁰ = ١، "
        "فالاحتمالان متطابقان — خصوصيّةٌ كاملة، لكنّ النموذجَ لم يتعلّم شيئًا مفيدًا. "
        "ومع نموّ ε ترتفع الفائدةُ وتنخفض الخصوصيّة: ε أكبر يعني أنّ وجودَ سجلٍّ واحدٍ "
        "أسهلُ اكتشافًا. فاختيارُ ε مقايضةٌ صريحةٌ قابلةٌ للضبط بين الفائدة والحماية.",
    "prv_dp_eqcap": "<b>شكل.</b> يضبط ε مقايضةَ الخصوصيّة/الفائدة: ε صغيرٌ يُخفي "
        "الأفراد، وε كبيرٌ يكشف أكثر.",
    "prv_dp_call": "الخصوصيّةُ التفاضليّة لا تُخفي الغابةَ لحماية شجرة؛ بل تضمن ألّا "
        "تُغيّر أيُّ شجرةٍ واحدةٍ شكلَ الغابة.",

    "prv_noise_eyebrow": "الخصوصيّة · لوح ٠٤",
    "prv_noise_p1": "تتحقّق الخصوصيّةُ التفاضليّة بإضافة <em>ضجيجٍ</em> مُعايَرٍ بعناية. "
        "أوضحُ مثالٍ هو <em>الاستجابةُ العشوائيّة</em>، حيلةُ استطلاعٍ أقدمُ من الحواسيب. "
        "لطرح سؤالٍ حسّاس — «هل غششتَ في الامتحان؟» — يرمي كلُّ طالبٍ عملةً سرًّا. وجه: "
        "قُل الحقيقة؛ كتابة: ارمِ ثانيةً وأجِب عشوائيًّا.",
    "prv_noise_p2": "الآن لا إجابةَ فرديّةٌ تُدين: أيُّ «نعم» قد تكون مجرّدَ كلامِ "
        "العملة، فينال كلُّ طالبٍ إنكارًا معقولًا. ومع ذلك، لأنّنا نعرف احتمالاتِ العملة "
        "بدقّة، نستطيع إزالةَ الضجيج جبريًّا <em>في التجميع</em> واستعادةَ النسبة "
        "الحقيقيّة للغشّاشين في الصفّ. خصوصيّةٌ للفرد، ودقّةٌ للجماعة.",
    "prv_noise_p3": "للبيانات الرقميّة نستخدم <em>آليّةَ لابلاس</em>: أضِف ضجيجًا "
        "مسحوبًا من توزيع لابلاس مقياسُه Δ/ε. هنا Δ، <em>الحساسيّة</em>، هو أقصى ما "
        "يُغيّره سجلٌّ واحدٌ في الجواب. ε أصغر (خصوصيّةٌ أكثر) يعني مقياسًا أكبرَ ونتائجَ "
        "أكثرَ ضجيجًا؛ وحساسيّةٌ أكبر تطلب ضجيجًا أكثر كذلك.",
    "prv_noise_eqcap": "<b>شكل.</b> ضجيجُ لابلاس بمقياس Δ/ε يُقنّع القيمةَ الحقيقيّة "
        "ويحفظ التجميع.",
    "prv_noise_call": "فنُّ DP هو إضافةُ ضجيجٍ يكفي لإخفاء الشخص دون أن يُمحوَ النمط.",

    "prv_fl_eyebrow": "الخصوصيّة · لوح ٠٥",
    "prv_fl_p1": "<em>التعلّمُ الموحّد (FL)</em> يقلب خطَّ الأنابيب المعتاد. بدل شحن "
        "البيانات الخاصّة (صور الهواتف، سجلّات المستشفيات) إلى خادمٍ مركزيّ، يشحن "
        "الخادمُ <em>النموذجَ</em> إلى كلّ جهاز. يجري التدريبُ محلّيًّا، ولا تُرسَل إلّا "
        "<em>الأوزانُ أو التدرّجات</em> الناتجة، فيدمجها الخادمُ في نموذجٍ عالميٍّ محسّن. "
        "البياناتُ الخام لا تغادر الجهاز أبدًا.",
    "prv_fl_p2": "لـ FL نكهتان. <em>عبرَ الأجهزة</em> يمتدّ على ملايين الهواتف — هائلٌ "
        "عددًا لكنّه ضعيفٌ ومتقطّع. و<em>عبرَ المؤسّسات</em> يربط حفنةً من المؤسّسات — "
        "بضعةَ مستشفياتٍ أو بنوكٍ ببياناتٍ مهيكلةٍ موثوقة.",
    "prv_fl_p3": "تهيمن ثلاثةُ تحدّيات. <em>عدمُ التجانس الإحصائيّ</em> (بيانات "
        "غيرُ مستقلّةٍ ومتطابقة): بياناتُ كلِّ عميلٍ بتوزيعٍ مختلف — مستشفًى يصوّر "
        "بالأشعّة السينيّة وآخرُ بالرنين. و<em>عدمُ التجانس النظاميّ</em>: تتفاوت الأجهزةُ "
        "كثيرًا في السرعة والاتّصال، فتُعطّل «المتباطئاتُ» المزامنة. و<em>كلفةُ "
        "الاتّصال</em>: نقلُ نماذجَ بمليارات المعاملات ذهابًا وإيابًا مكلف، ولذا يتّكئ FL "
        "على الضغط والتكميم.",
    "prv_fl_eqcap": "<b>شكل.</b> يسافر النموذجُ إلى البيانات؛ ولا يعود إلى الخادم إلّا "
        "التدرّجات.",
    "prv_fl_call": "يُبقي التعلّمُ الموحّد البياناتِ في البيت — لكن، كما يُظهر اللوحُ "
        "التالي، إرسالُ التدرّجات ليس كإرسال لا شيء.",

    "prv_leak_eyebrow": "الخصوصيّة · لوح ٠٦",
    "prv_leak_p1": "يبدو التعلّمُ الموحّد خصوصيًّا: لا تغادر الجهازَ إلّا التدرّجات، لا "
        "الصورُ نفسها. الاكتشافُ المُقلِق أنّ هذا الحدسَ خاطئ. تُحسَب التدرّجاتُ "
        "<em>من</em> البيانات، وتحمل معلوماتٍ كافيةً لإعادة بنائها.",
    "prv_leak_p2": "يعامل <em>هجومُ تسريب التدرّج</em> إعادةَ البناء كمسألة تحسين: يبحث "
        "خادمٌ خبيثٌ عن المُدخَل الذي كان سيُنتِج التدرّجَ المُلاحَظ، ويُنقّحه تكراريًّا. "
        "لنموذجٍ بسيطٍ يكون التسريبُ دقيقًا — تدرّجُ طبقةٍ خطيّةٍ على مثالٍ واحدٍ هو حرفيًّا "
        "المُدخَلُ مضروبًا في خطأ التنبؤ، فيمكن قراءةُ الصورة الأصليّة مباشرةً من التدرّج "
        "المُشترَك.",
    "prv_leak_p3": "الدرسُ أنّ التعلّمَ الموحّد وحدَه ليس ضمانًا للخصوصيّة؛ يجب دمجُه مع "
        "الخصوصيّة التفاضليّة (DP-FL) أو التجميع الآمن كي تُحمى التدرّجاتُ نفسُها قبل أن "
        "تصل الخادمَ أصلًا.",
    "prv_leak_eqcap": "<b>شكل.</b> من تدرّجٍ مُشترَك، يُعيد المهاجمُ بناءَ مُدخَل العميل "
        "الخاصّ.",
    "prv_leak_call": "إرسالُ التدرّجات بدل البيانات ليس خصوصيّةً مجّانيّة — البياناتُ ما "
        "زالت مختبئةً داخل الأرقام.",

    "pp_backdoor_eyebrow": "تطبيق · عرض ١٨",
    "pp_backdoor_what": "نُدرّب شبكةً التفافيّةً حقيقيّةً سُمِّمت بمُشغّلٍ في الزاوية، ثمّ "
        "ندعك تُشغّل المُشغّل وتُطفئه على صور الاختبار وتشاهد تغيُّر التنبؤ.",
    "pp_backdoor_why": "يُبيّن أنّ نموذجًا قد يجتاز كلَّ اختبارِ بياناتٍ نظيفةٍ ويُخفي "
        "تروجانًا: الدقّةُ العاليةُ ليست دليلَ ثقة.",
    "pp_backdoor_expect": "تُصنَّف الصورُ النظيفةُ صحيحًا؛ ولحظةَ يظهر المُشغّل، يقفز "
        "النموذجُ إلى صنف هدف المهاجم بثقةٍ عالية.",
    "pp_backdoor_sample": "الصورة العيّنة",
    "pp_backdoor_trigger": "اطبع المُشغّل",
    "pp_backdoor_cap_clean": "<b>شكل ١.</b> الصورة كما يراها النموذج.",
    "pp_backdoor_cap_pred": "التنبؤ",
    "pp_backdoor_clean_acc": "دقّة البيانات النظيفة",
    "pp_backdoor_asr": "نسبة نجاح المُشغّل",
    "pp_backdoor_note": "النموذجُ ذو الباب الخلفيّ دقيقٌ على البيانات النظيفة لكنّه يطيع "
        "المُشغّلَ كلَّ مرّة — تروجانٌ لن تكشفه بقياس الدقّة وحدها.",

    "pp_coin_eyebrow": "تطبيق · عرض ١٩",
    "pp_coin_what": "نحاكي استطلاعًا حسّاسًا يُجاب بروتوكولَ الاستجابة العشوائيّة برمي "
        "العملة، ثمّ نستعيد النسبةَ الحقيقيّة للجمهور من الإجابات المشوّشة.",
    "pp_coin_why": "أبسطُ مثالٍ عمليٍّ للخصوصيّة التفاضليّة: يُحمى كلُّ فرد، ومع ذلك يبقى "
        "الإحصاءُ التجميعيّ دقيقًا.",
    "pp_coin_expect": "لا إجابةَ واحدةٌ يُوثَق بها عن أيّ فرد، لكنّ النسبةَ المُقدَّرة "
        "تقترب من النسبة الحقيقيّة كلّما كبر الجمهور.",
    "pp_coin_true": "نسبة «نعم» الحقيقيّة في الجمهور",
    "pp_coin_n": "عدد المستجيبين",
    "pp_coin_ptruth": "احتمال الإجابة الصادقة",
    "pp_coin_cap": "<b>شكل.</b> المُقدِّر (من الإجابات المشوّشة) يتقارب إلى النسبة "
        "الحقيقيّة كلّما نما N.",
    "pp_coin_est": "النسبة المُقدَّرة",
    "pp_coin_actual": "النسبة الحقيقيّة",
    "pp_coin_note": "لا نستطيع معرفةَ إن قال مستجيبٌ بعينه نعم — تلك هي الخصوصيّة — لكنّ "
        "التجميعَ المُصحَّح يستعيد النسبةَ الحقيقيّة. خصوصيّةٌ للفرد، ودقّةٌ للجماعة.",

    "pp_laplace_eyebrow": "تطبيق · عرض ٢٠",
    "pp_laplace_what": "ننشر مُدرَّجَ رواتبَ تحت آليّة لابلاس وندعك تُحرّك ميزانيّةَ "
        "الخصوصيّة ε لترى الضجيجَ يكبر أو يصغر.",
    "pp_laplace_why": "يجعل مقايضةَ الخصوصيّة/الفائدة ملموسة: أنت حرفيًّا تُدير سعرَ "
        "الصرف بين الحماية والدقّة.",
    "pp_laplace_expect": "عند ε كبيرٍ يطابق المُدرَّجُ الخاصّ الحقيقيّ؛ ومع صِغَر ε تهتزّ "
        "الأعمدةُ وتتشوّش لإخفاء أيّ راتبٍ فرديّ.",
    "pp_laplace_eps": "ميزانيّة الخصوصيّة ε",
    "pp_laplace_cap": "<b>شكل.</b> مُدرَّجُ الرواتب الحقيقيّ مقابل الخصوصيّ‑التفاضليّ عند "
        "ε المختار.",
    "pp_laplace_err": "متوسّط التشويه",
    "pp_laplace_scale": "مقياس لابلاس (Δ/ε)",
    "pp_laplace_note": "ε صغيرٌ يشتري خصوصيّةً قويّةً بثمن مُدرَّجٍ مشوّشٍ مُحرَّف؛ وε "
        "كبيرٌ يُعيد إنتاجَ البيانات بدقّةٍ تقريبًا لكن لا يحمي أحدًا. لا غداءَ مجّانيًّا "
        "— مجرّدُ مِقبَض.",

    "pp_leak_eyebrow": "تطبيق · عرض ٢١",
    "pp_leak_what": "يُشارك عميلٌ تدرّجَ نموذجٍ خطيٍّ فقط لصورةٍ خاصّةٍ واحدة؛ يُنفّذ "
        "الخادمُ هجومَ التسريب ويُعيد بناءَ تلك الصورة من التدرّج وحده.",
    "pp_leak_why": "يثقب الاعتقادَ أنّ التعلّمَ الموحّد خصوصيٌّ تلقائيًّا — يمكن قراءةُ "
        "البيانات الخام مباشرةً من التدرّجات المُشترَكة.",
    "pp_leak_expect": "بدءًا من التدرّج «المُبهَم»، تُطابِق إعادةُ البناء الصورةَ الأصليّة "
        "تقريبًا تمامًا (خطأُ إعادة البناء قربَ الصفر).",
    "pp_leak_sample": "صورة العميل الخاصّة",
    "pp_leak_run": "نفِّذ هجوم تسريب التدرّج",
    "pp_leak_cap_true": "<b>شكل ١.</b> صورة العميل الخاصّة الحقيقيّة.",
    "pp_leak_cap_rec": "<b>شكل ٢.</b> أعاد الخادمُ بناءها من التدرّج وحده.",
    "pp_leak_err": "خطأ إعادة البناء",
    "pp_leak_note": "التعلّمُ الموحّد وحدَه لا يكفي: استعاد المهاجمُ الصورةَ الخاصّة من "
        "التدرّجات. يجب أن يضيف النشرُ الحقيقيّ الخصوصيّةَ التفاضليّة (DP-FL) أو التجميعَ "
        "الآمن.",
}
