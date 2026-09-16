"""
Day 51 — The Central Limit Theorem
===================================
The most important idea in the ninety days. Everything after it --
confidence intervals, p-values, hypothesis tests, model comparison --
is an application of this one fact.

Exercise 1 is the lesson. Run it before reading anything else.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)


# =============================================================================
# 1 -- THE DEMONSTRATION. Four very different sources. All means go normal.
# =============================================================================
def ex_01(n=30, n_samples=5_000):
    sources = {
        "uniform":     lambda k: rng.uniform(0, 100, k),
        "exponential": lambda k: rng.exponential(10, k),          # heavily skewed
        "bimodal":     lambda k: np.concatenate([rng.normal(20, 5, k // 2),
                                                 rng.normal(80, 5, k - k // 2)]),
        "your prices": lambda k: rng.lognormal(6, 1, k),          # replace with real PBS data
    }

    fig, axes = plt.subplots(2, 4, figsize=(16, 7))
    for col, (name, draw) in enumerate(sources.items()):
        raw = draw(50_000)
        axes[0, col].hist(raw, bins=60)
        axes[0, col].set_title(f"{name}\n(the raw data)")

        means = [draw(n).mean() for _ in range(n_samples)]
        axes[1, col].hist(means, bins=60)
        p = stats.shapiro(means[:5000])[1]
        axes[1, col].set_title(f"means of n={n}\nShapiro p={p:.3f}")

    fig.suptitle("The data can be any shape. The SAMPLE MEANS go normal.", fontsize=14)
    fig.tight_layout()


# 2 -- Vary n: 2, 5, 10, 30, 100. At what n does EACH source look normal?
#      uniform: n=____   exponential: n=____   bimodal: n=____   prices: n=____
def ex_02(): pass


# 3 -- Overlay a fitted normal on each means-histogram. How close?
def ex_03(): pass


# =============================================================================
# THE STANDARD ERROR
# =============================================================================

# 4 -- FIND THE n YOUR OWN DATA NEEDS.
#      Shapiro on the sample means at each n. Where does it stop rejecting?
#      MY DATA NEEDS n >= ____
#      WAS THE "n >= 30" RULE RIGHT FOR MY DATA?
def ex_04(data):
    for n in (5, 10, 30, 50, 100, 200):
        means = [rng.choice(data, n).mean() for _ in range(2000)]
        p = stats.shapiro(means)[1]
        verdict = "normal" if p > 0.05 else "NOT normal"
        print(f"  n={n:>4}   Shapiro p={p:.4f}   {verdict}")


# 5 -- Verify SE = sigma / sqrt(n) empirically at five sample sizes.
def ex_05(sigma=15):
    for n in (4, 25, 100, 400, 1600):
        theoretical = sigma / np.sqrt(n)
        empirical = np.std([rng.normal(100, sigma, n).mean() for _ in range(5000)], ddof=1)
        print(f"  n={n:>5}   theory {theoretical:6.3f}   empirical {empirical:6.3f}")


# 6 -- THE sqrt(n) CONSEQUENCE. Plot SE vs n.
#      current n = ____   current SE = ____
#      n needed to HALVE it        = ____
#      n needed to halve it AGAIN  = ____
#      IS THAT REALISTIC TO COLLECT?
def ex_06(sigma=15):
    n = np.arange(1, 2001)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(n, sigma / np.sqrt(n))
    ax.set_xlabel("sample size"); ax.set_ylabel("standard error")
    ax.set_title("To halve your uncertainty you need FOUR times the data")
    fig.tight_layout()


# 7 -- From ONE sample: estimate the SE and the plausible range for the true mean.
#      YOU HAVE JUST BUILT A CONFIDENCE INTERVAL. Tomorrow names it.
def ex_07(sample):
    pass


# MINI ASSESSMENT -- 5 minutes, closed book
#   64 customers, mean spend 2400, SD 800.
#     1. SE = ____
#     2. ~95% range for the true mean = [____, ____]
#     3. n to halve that range = ____
#     4. ONE SENTENCE TO A SHOP OWNER on why "average spend is 2400" is not enough:


if __name__ == "__main__":
    print("--- ex_01: THE demonstration ---"); ex_01()
    print("--- ex_05: SE = sigma/sqrt(n) ---"); ex_05()
    print("--- ex_06: the sqrt(n) cost ---");   ex_06()
    plt.show()
