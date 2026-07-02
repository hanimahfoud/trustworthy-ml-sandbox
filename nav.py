"""
nav.py -- the navigation registry shared by app.py and pdf_export.py.

Only the *keys* live here (order matters); app.py maps them to render
functions, and pdf_export.py maps them to i18n text. Keeping this in one place
means the sidebar, the router and the PDF can never drift out of sync.
"""
SECTIONS = ["sec1", "sec2", "sec3", "sec4", "sec5", "sec6"]

THEORY = {
    "sec1": ["th_bv", "th_vc", "th_ib", "th_tl", "th_sam", "th_cz"],
    "sec2": ["xai_interp", "xai_black", "xai_tab", "xai_recourse",
             "xai_cv", "xai_vlm"],
    "sec3": ["fair_intro", "fair_metrics", "fair_llm", "fair_mitig",
             "fair_fap", "fair_align"],
    "sec4": ["rob_intro", "rob_formulation", "rob_attacks", "rob_defense",
             "rob_certified", "rob_llm"],
    "sec5": ["prv_poison", "prv_privacy", "prv_dp", "prv_noise",
             "prv_fl", "prv_leak"],
    "sec6": ["aln_gap", "aln_rlhf", "aln_dpo", "aln_variants",
             "aln_owasp", "aln_agency"],
}

PRACTICE = {
    "sec1": ["pr_bv", "pr_dann", "pr_sam", "pr_simpson", "pr_cf"],
    "sec2": ["px_loan", "px_recourse", "px_cv", "px_spurious"],
    "sec3": ["pf_scales", "pf_cda", "pf_multiturn", "pf_constitution"],
    "sec4": ["prb_evasion", "prb_tradeoff", "prb_smoothing", "prb_jailbreak"],
    "sec5": ["pp_backdoor", "pp_coin", "pp_laplace", "pp_leak"],
    "sec6": ["pa_hacking", "pa_grpo", "pa_jailbreak", "pa_agency"],
}
