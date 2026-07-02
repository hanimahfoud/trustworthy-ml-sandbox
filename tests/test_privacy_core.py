"""Unit tests for the privacy / poisoning / federated engine."""
import numpy as np

from core import vision_core as V
from core import privacy_core as PV


def test_trigger_stamps_corner():
    X, y, _ = V.make_shapes_dataset(4, spurious=False, seed=1)
    Xt = PV.stamp_trigger(X)
    assert np.allclose(Xt[:, :, :PV.TRIGGER_SIZE, :PV.TRIGGER_SIZE], 1.0)
    # rest of the image untouched
    assert np.allclose(Xt[:, :, PV.TRIGGER_SIZE:, PV.TRIGGER_SIZE:],
                       X[:, :, PV.TRIGGER_SIZE:, PV.TRIGGER_SIZE:])


def test_backdoor_high_clean_acc_and_trigger_flips():
    net, clean_acc, target = PV.make_backdoored_cnn(target=1, seed=0,
                                                    epochs=18, n_train=500,
                                                    poison_frac=0.35)
    Xc, yc, _ = V.make_shapes_dataset(60, spurious=False, seed=77)
    # behaves well on clean data...
    assert clean_acc > 0.85
    assert (net.predict(Xc) == yc).mean() > 0.75
    # ...but the trigger reliably forces the target class
    assert PV.backdoor_success_rate(net, Xc, target) > 0.95


def test_membership_inference_beats_chance():
    r = PV.membership_inference_demo(seed=0)
    # a real generalization gap drives the attack
    assert r["train_acc"] > r["test_acc"] + 0.1
    assert r["mean_members"] > r["mean_nonmembers"] + 0.05
    assert r["attack_accuracy"] > 0.65


def test_randomized_response_unbiased():
    rng = np.random.default_rng(0)
    bits = (rng.random(20000) < 0.15).astype(int)   # 15% true "yes"
    r = PV.randomized_response(bits, p_truth=0.5, seed=1)
    assert abs(r["estimated_true_rate"] - 0.15) < 0.03   # recovers the rate
    # individual answers are noisy (privacy): not equal to the truth
    assert not np.array_equal(r["reported"], bits)


def test_laplace_more_noise_at_small_epsilon():
    vals = np.zeros(4000)
    lo = PV.laplace_mechanism(vals, epsilon=10.0, sensitivity=1.0, seed=0)
    hi = PV.laplace_mechanism(vals, epsilon=0.1, sensitivity=1.0, seed=0)
    assert hi.std() > lo.std() * 5           # smaller epsilon -> much more noise


def test_dp_histogram_preserves_shape_but_perturbs():
    rng = np.random.default_rng(0)
    salaries = rng.normal(5000, 1200, 2000)
    bins = np.linspace(salaries.min(), salaries.max(), 12)
    true_c, noisy_c, _ = PV.dp_histogram(salaries, bins, epsilon=0.2, seed=0)
    assert len(true_c) == len(noisy_c)
    assert not np.allclose(true_c, noisy_c)   # noise actually added
    assert (noisy_c >= 0).all()


def test_gradient_leakage_reconstructs_input():
    rng = np.random.default_rng(0)
    x = rng.random(24 * 24)                   # a flattened "image"
    r = PV.gradient_leakage_linear(x, y_true=2, n_classes=4, seed=0)
    assert r["rel_error"] < 1e-6              # gradient exactly reveals x
