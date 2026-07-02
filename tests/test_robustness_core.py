"""Unit tests for the robustness engine (real attacks on the NumPy CNN)."""
import numpy as np

from core import vision_core as V
from core import robustness_core as R


def _trained():
    return V.train_cnn(spurious=False, seed=0, epochs=18, n_train=500)


def test_fgsm_and_pgd_stay_in_epsilon_ball_and_valid():
    net, _ = _trained()
    X, y, _ = V.make_shapes_dataset(6, spurious=False, seed=5)
    x = X[0:1]
    eps = 0.1
    for xa in (R.fgsm(net, x, int(y[0]), eps),
               R.pgd(net, x, int(y[0]), eps, steps=8)):
        assert xa.shape == x.shape
        assert xa.min() >= 0.0 and xa.max() <= 1.0
        assert np.abs(xa - x).max() <= eps + 1e-6


def test_attacks_flip_predictions_at_large_epsilon():
    net, _ = _trained()
    X, y, _ = V.make_shapes_dataset(30, spurious=False, seed=5)
    # at a visible epsilon the attack should break most correct predictions
    sr = R.attack_success_rate(net, X, y, epsilon=0.30, method="pgd", steps=12)
    assert sr > 0.5


def test_pgd_at_least_as_strong_as_fgsm():
    net, _ = _trained()
    X, y, _ = V.make_shapes_dataset(30, spurious=False, seed=7)
    fs = R.attack_success_rate(net, X, y, 0.15, method="fgsm")
    ps = R.attack_success_rate(net, X, y, 0.15, method="pgd", steps=12)
    assert ps >= fs - 1e-9


def test_small_epsilon_barely_hurts():
    net, _ = _trained()
    X, y, _ = V.make_shapes_dataset(30, spurious=False, seed=9)
    sr = R.attack_success_rate(net, X, y, epsilon=0.0, method="pgd", steps=5)
    assert sr == 0.0            # no perturbation -> no flips


def test_adversarial_training_improves_robustness():
    Xt, yt, _ = V.make_shapes_dataset(40, spurious=False, seed=11)
    std_net, _ = V.train_cnn(spurious=False, seed=0, epochs=18, n_train=500)
    adv_net, _ = R.adversarial_train(seed=0, epochs=10, n_train=400,
                                     epsilon=0.15, pgd_steps=4)
    eps = 0.20
    std_robust = 1 - R.attack_success_rate(std_net, Xt, yt, eps, "pgd", 10)
    adv_robust = 1 - R.attack_success_rate(adv_net, Xt, yt, eps, "pgd", 10)
    assert adv_robust > std_robust      # hardened model resists better


def test_randomized_smoothing_certifies_clean_image():
    net, _ = _trained()
    X, y, _ = V.make_shapes_dataset(6, spurious=False, seed=13)
    cert = R.randomized_smoothing(net, X[0:1], sigma=0.25, n=200, seed=0)
    assert cert["prediction"] in (0, 1)
    assert 0.0 <= cert["p_a_lower"] <= 1.0
    assert cert["radius"] >= 0.0
    assert sum(cert["votes"]) == 200


def test_jailbreak_rules_are_deterministic():
    assert R.jailbreak_attempt("direct") == (False, "refuse")
    assert R.jailbreak_attempt("authority") == (False, "refuse")
    assert R.jailbreak_attempt("roleplay")[0] is True
    assert R.jailbreak_attempt("acrostic")[0] is True
