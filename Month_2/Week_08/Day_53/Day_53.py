"""
Day 53 — P-values and hypothesis testing
=========================================
A p-value is P(data at least this extreme | THE NULL IS TRUE).

It is NOT P(the null is true | data). That is Day 46's disease test again,
and it is the single most consequential confusion in applied statistics.

Exercises 1, 8 and 9 are the ones that change how you read other people's work.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)


# =============================================================================
# 1 -- SIMULATE THE NULL. No real effect. 10,000 tests.
#      The p-value distribution is UNIFORM.
#      WHY?  (this is the deepest question today)
#      ANSWER:
# =============================================================================
def ex_01(n_tests=10_000, n=30):
    ps = []
    for _ in range(n_tests):
        a = rng.normal(100, 15, n)
        b = rng.normal(100, 15, n)          # SAME distribution -- no effect
        ps.append(stats.ttest_ind(a, b).pvalue)
    ps = np.array(ps)

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.hist(ps, bins=50)
    ax.set_title("p-values when there is genuinely NO effect — uniform, by construction")
    ax.set_xlabel("p-value"); fig.tight_layout()

    print(f"  p < 0.05 in {(ps < 0.05).mean():.4f} of tests   <- should be ~0.05")
    print(f"  p < 0.01 in {(ps < 0.01).mean():.4f} of tests   <- should be ~0.01")


# 2 -- From ex_01: how many "significant" results with NO effect?
#      COUNT: ____ of 10,000.   IS IT 5%?


# 3 -- Now simulate a REAL effect. How does the distribution change?
def ex_03(n_tests=10_000, n=30, effect=5):
    pass


# =============================================================================
# RUNNING TESTS
# =============================================================================

# 4 -- one-sample t: does the mean differ from a claimed value?
def ex_04(data, claimed): pass

# 5 -- two-sample t on two real groups
def ex_05(a, b): pass


# 6 -- PAIRED vs INDEPENDENT on the SAME data.
#      WHICH HAS THE SMALLER p? WHY?
#      WHAT DOES THE INDEPENDENT TEST THROW AWAY?
def ex_06(n=30):
    before = rng.normal(100, 15, n)
    after = before + rng.normal(3, 4, n)          # a real, consistent +3 effect
    print(f"  independent: p = {stats.ttest_ind(before, after).pvalue:.4f}")
    print(f"  paired     : p = {stats.ttest_rel(before, after).pvalue:.4f}")


# 7 -- chi-square on a contingency table from your data
def ex_07(df): pass


# =============================================================================
# THE MISUSES
# =============================================================================

# 8 -- THE LARGE-n DEMONSTRATION.
#      A 0.1% difference. Test at increasing n. Watch p collapse.
#      AT WHAT n DID A TRIVIAL DIFFERENCE BECOME "SIGNIFICANT"? ____
#      WHAT WOULD I REPORT AT n = 1,000,000?
def ex_08():
    for n in (100, 1_000, 10_000, 100_000, 1_000_000):
        a = rng.normal(100.0, 15, n)
        b = rng.normal(100.1, 15, n)              # a 0.1% difference
        p = stats.ttest_ind(a, b).pvalue
        cohens_d = (b.mean() - a.mean()) / np.sqrt((a.var() + b.var()) / 2)
        print(f"  n={n:>9,}   p={p:<12.2e}  effect size (d)={cohens_d:.4f}  <- trivial")


# 9 -- P-HACKING, LIVE. 20 random variables, no real relationship.
#      HOW MANY CAME OUT "SIGNIFICANT"? ____
#      WHAT DOES THAT MEAN FOR SOMEONE WHO EXPLORES UNTIL SOMETHING IS SIGNIFICANT?
def ex_09(n_vars=20, n=100):
    outcome = rng.normal(0, 1, n)
    hits = []
    for i in range(n_vars):
        noise = rng.normal(0, 1, n)              # pure noise
        r, p = stats.pearsonr(noise, outcome)
        if p < 0.05:
            hits.append((i, round(r, 3), round(p, 4)))
    print(f"  tested {n_vars} pure-noise variables")
    print(f"  'significant' at p<0.05: {len(hits)}  -> {hits}")
    print("  every one of these is a false positive.")


# 10 -- POWER. What n gives 80% power for a given effect?
#       n for 80% power: ____
#       power at HALF that n: ____
#       WHAT DOES AN UNDERPOWERED NULL RESULT ACTUALLY TELL ME?
def ex_10(effect=3, sd=15, alpha=0.05):
    for n in (10, 20, 40, 80, 160, 320):
        sig = sum(stats.ttest_ind(rng.normal(100, sd, n),
                                  rng.normal(100 + effect, sd, n)).pvalue < alpha
                  for _ in range(2000))
        print(f"  n={n:>4}   power = {sig / 2000:.3f}")


# =============================================================================
# 11 -- ONE REAL TEST ON PROJECT 1 DATA. Write it up fully.
# =============================================================================
#   H0:
#   H1:
#   TEST CHOSEN:                   WHY:
#   ONE-TAILED OR TWO? DECIDED BEFORE LOOKING?
#   p-value:          EFFECT SIZE:
#   CONCLUSION IN PLAIN ENGLISH:
#   WHAT I AM *NOT* CLAIMING:


# MINI ASSESSMENT -- 10 minutes, closed book
#   "We tested 8 checkout changes. One gave +2% conversion, p=0.04. Ship it."
#   MY RESPONSE:
#     on the multiple comparisons:
#     on what p=0.04 means here:
#     what I would need to believe it:
#     what I actually recommend:


if __name__ == "__main__":
    print("--- ex_01: p-values under the null ---"); ex_01()
    print("--- ex_06: paired vs independent ---");   ex_06()
    print("--- ex_08: large n ---");                 ex_08()
    print("--- ex_09: p-hacking ---");               ex_09()
    print("--- ex_10: power ---");                   ex_10()
    plt.show()
