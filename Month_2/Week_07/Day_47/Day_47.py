"""
Day 47 — Binomial and beta
===========================
BINOMIAL: known rate -> what outcomes should I expect?
BETA:     observed outcomes -> what rates are plausible?

Exercise 4 is the lesson. One chart, three curves, and you will never
again report a percentage without asking how many trials it came from.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta, binom

rng = np.random.default_rng(42)


# 1 -- binomial PMF for n=10, p=0.9. Exact, at-most, at-least.
def ex_01():
    n, p = 10, 0.9
    k = np.arange(n + 1)
    print(f"  P(exactly 8)   = {binom.pmf(8, n, p):.4f}")
    print(f"  P(8 or fewer)  = {binom.cdf(8, n, p):.4f}")
    print(f"  P(more than 8) = {1 - binom.cdf(8, n, p):.4f}")
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(k, binom.pmf(k, n, p))
    ax.set_title(f"Binomial(n={n}, p={p}) — the outcomes to expect from a known rate")
    ax.set_xlabel("successes"); ax.set_ylabel("probability")
    fig.tight_layout()


# 2 -- verify by simulation. 100,000 runs of 10 trials.
#      analytic: ____   simulated: ____
def ex_02(n_sims=100_000):
    pass


# 3 -- BREAK AN ASSUMPTION. Simulate DEPENDENT trials.
#      HOW FAR OFF IS THE BINOMIAL?
#      WHERE DOES DEPENDENCE HAPPEN IN REAL DATA?
def ex_03():
    pass


# 4 -- THE LESSON. Three betas, same 80% rate, different sample sizes.
def ex_04():
    fig, ax = plt.subplots(figsize=(9, 5))
    x = np.linspace(0, 1, 500)
    for succ, fail, label in [(8, 2, "8 / 10"), (80, 20, "80 / 100"), (800, 200, "800 / 1000")]:
        ax.plot(x, beta.pdf(x, succ, fail), label=f"{label}  (80%)")
    ax.axvline(0.8, ls="--", lw=1, color="grey")
    ax.set_title("Same 80% — three completely different claims")
    ax.set_xlabel("true underlying rate"); ax.set_ylabel("density")
    ax.legend(); fig.tight_layout()
    # DESCRIBE WHAT HAPPENS TO THE CURVE AS n GROWS, AND WHY:


# 5 -- P(true rate > 0.9) for all three. Put the numbers side by side.
def ex_05():
    for a, b, label in [(8, 2, "8/10"), (80, 20, "80/100"), (800, 200, "800/1000")]:
        print(f"  {label:<11} P(rate > 0.90) = {1 - beta.cdf(0.90, a, b):.4f}")
    # ALL THREE ARE "80%". WHY ARE THESE NUMBERS SO DIFFERENT?


# 6 -- 95% credible intervals for all three. Record the widths.
#      8/10:      [____, ____]  width ____
#      80/100:    [____, ____]  width ____
#      800/1000:  [____, ____]  width ____
def ex_06():
    pass


# 7 -- THE A/B TEST, FROM FIRST PRINCIPLES.
#      A: 30/500    B: 45/500
#      Sample from both betas. Compute P(B > A).
#      P(B > A) = ____
#      WHAT WOULD I TELL A PRODUCT MANAGER?
def ex_07(n_samples=200_000):
    a_samples = rng.beta(30, 470, n_samples)
    b_samples = rng.beta(45, 455, n_samples)
    print(f"  P(B > A) = {(b_samples > a_samples).mean():.4f}")
    print(f"  median lift = {np.median(b_samples - a_samples):.4f}")


# 8 -- Chapter 2 exercises, p. 61. Check against Appendix B.
#      SCORE: ___ / ___     WRONG ONES, AND WHY:


# 9 -- APPLY IT. A rate from Project 1 -- e.g. share of weeks an item rose.
#      point estimate: ____   95% interval: [____, ____]
#      SHOULD THIS HAVE BEEN IN MY PROJECT 1 README?
def ex_09(df):
    pass


# MINI ASSESSMENT -- 8 minutes, closed book
#   Churn model got 47 of 52 right.
#     1. point estimate       = ____
#     2. 95% credible interval= [____, ____]
#     3. P(accuracy > 0.85)   = ____
#     4. ONE SENTENCE TO MY MANAGER:


if __name__ == "__main__":
    print("--- ex_01 binomial ---"); ex_01()
    print("--- ex_04 the lesson ---"); ex_04()
    print("--- ex_05 ---"); ex_05()
    print("--- ex_07 A/B ---"); ex_07()
    plt.show()
