"""Unit tests for the alignment engine (Section VI)."""
import numpy as np

from core import alignment_core as A


def test_reward_model_learns_preferences():
    # winners have a higher value on feature 0; the RM should learn w[0] > 0
    rng = np.random.default_rng(0)
    n = 200
    Xw = rng.normal(0, 1, (n, 3)); Xw[:, 0] += 1.5
    Xl = rng.normal(0, 1, (n, 3)); Xl[:, 0] -= 1.5
    out = A.train_reward_model(Xw, Xl, epochs=300, lr=0.2, seed=0)
    assert out["w"][0] > 0.5                       # learned the right direction
    assert out["losses"][-1] < out["losses"][0]    # loss went down
    # the RM ranks winners above losers on average
    assert (Xw @ out["w"]).mean() > (Xl @ out["w"]).mean()


def test_kl_divergence_basic():
    p = np.array([0.5, 0.5])
    assert abs(A.kl_divergence(p, p)) < 1e-9        # KL(p||p) = 0
    assert A.kl_divergence(np.array([0.9, 0.1]), np.array([0.5, 0.5])) > 0


def test_reward_hacking_grows_as_beta_shrinks():
    # with a strong KL anchor the policy stays sane; with none it hacks
    strong = A.reward_hacking_demo(beta=1.0)
    weak = A.reward_hacking_demo(beta=0.05)
    none = A.reward_hacking_demo(beta=0.0)
    assert weak["hype_mass"] > strong["hype_mass"]
    assert none["hype_mass"] >= weak["hype_mass"]
    assert none["hype_mass"] > 0.9                  # collapses onto hype token
    # KL from the reference grows as the anchor weakens
    assert weak["kl"] > strong["kl"]


def test_dpo_loss_decreases_when_margin_favors_winner():
    # if the policy already prefers winners more than the reference, loss is low
    logp_w_pi = np.array([-1.0, -1.2]); logp_l_pi = np.array([-3.0, -3.5])
    logp_w_ref = np.array([-1.5, -1.5]); logp_l_ref = np.array([-2.0, -2.0])
    loss_good, margin = A.dpo_loss(logp_w_pi, logp_l_pi, logp_w_ref, logp_l_ref)
    # flip winner/loser -> the loss must be larger
    loss_bad, _ = A.dpo_loss(logp_l_pi, logp_w_pi, logp_l_ref, logp_w_ref)
    assert loss_good < loss_bad
    assert margin.mean() > 0


def test_grpo_verifier_and_majority_vote():
    # question: 6 * 7 = 42; some candidates right, some wrong
    cands = ["6*7", "42", "6*7+1", "40", "(6*7)", "42 ", "7*6", "6*8"]
    r = A.grpo_group_score(cands, target=42)
    assert r["n_correct"] == 5                      # five evaluate to 42
    assert r["majority"] == 42.0
    assert 0 < r["consistency"] <= 1
    # correct answers get positive advantage, wrong ones negative
    adv = r["advantages"]; rew = r["rewards"]
    assert (adv[rew == 1] > 0).all()
    assert (adv[rew == 0] < 0).all()


def test_grpo_rejects_unsafe_expressions():
    assert A._safe_eval_arithmetic("__import__('os')") is None
    assert A._safe_eval_arithmetic("2+2") == 4.0
    assert A._safe_eval_arithmetic("open('x')") is None


def test_jailbreak_rules_deterministic():
    assert A.jailbreak_attempt("direct") == (False, "refuse")
    assert A.jailbreak_attempt("authority")[0] is False
    assert A.jailbreak_attempt("story_acrostic")[0] is True
    assert A.jailbreak_attempt("roleplay")[0] is True


def test_excessive_agency_only_fires_with_write_access():
    inbox = A.DEFAULT_INBOX
    safe, ev1, wiped1 = A.excessive_agency_step(inbox, "read_only")
    assert len(safe) == len(inbox) and wiped1 is False
    danger, ev2, wiped2 = A.excessive_agency_step(inbox, "write_delete")
    assert danger == [] and wiped2 is True          # inbox wiped by injection
