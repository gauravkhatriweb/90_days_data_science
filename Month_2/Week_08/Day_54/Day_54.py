"""
Day 54 — Small samples, sharpshooters, and a real A/B test
===========================================================
Exercises 4 and 6 are the ones that will change how you read other people's
results -- and how you audit your own.

Exercise 12 is the deliverable: the artefact an analyst actually produces.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)


# =============================================================================
# THE t-DISTRIBUTION
# =============================================================================

# 1 -- t at df = 1, 5, 30 against the normal. Watch the tails converge.
def ex_01():
    x = np.linspace(-5, 5, 500)
    fig, ax = plt.subplots(figsize=(9, 5))
    for df in (1, 5, 30):
        ax.plot(x, stats.t.pdf(x, df), label=f"t (df={df})")
    ax.plot(x, stats.norm.pdf(x), "k--", label="normal")
    ax.set_title("The t-distribution has fatter tails — because sigma is also estimated")
    ax.legend(); fig.tight_layout()


# 2 -- t vs z interval widths at n = 5, 10, 30, 100
def ex_02():
    for n in (5, 10, 30, 100):
        t_crit = stats.t.ppf(0.975, df=n - 1)
        z_crit = stats.norm.ppf(0.975)
        print(f"  n={n:>4}   t={t_crit:.3f}  z={z_crit:.3f}   t is {(t_crit/z_crit-1)*100:5.1f}% wider")


# 3 -- THE COST OF GETTING IT WRONG.
#      Use z on small samples. What is the REAL coverage of a "95%" interval?
#      ACTUAL COVERAGE at n=5: ____%
#      WHAT DOES THAT MEAN FOR A "95%" INTERVAL?
def ex_03(n=5, n_sims=20_000, true_mean=100, sd=15):
    z_hits = t_hits = 0
    for _ in range(n_sims):
        s = rng.normal(true_mean, sd, n)
        sem = stats.sem(s)
        zl, zh = stats.norm.interval(0.95, loc=s.mean(), scale=sem)
        tl, th = stats.t.interval(0.95, df=n - 1, loc=s.mean(), scale=sem)
        z_hits += zl <= true_mean <= zh
        t_hits += tl <= true_mean <= th
    print(f"  using z: {z_hits/n_sims:.1%} coverage   <- claimed 95%")
    print(f"  using t: {t_hits/n_sims:.1%} coverage")


# =============================================================================
# THE TEXAS SHARPSHOOTER
# =============================================================================

# 4 -- SUBGROUP HUNTING. No real effect. Split by five random variables.
#      HOW MANY SUBGROUPS BEFORE I FOUND SIGNIFICANCE? ____
#      WOULD I HAVE NOTICED MYSELF DOING THIS IN REAL WORK?
def ex_04(n=400):
    outcome = rng.normal(0, 1, n)
    group = rng.integers(0, 2, n)                  # A/B, genuinely random
    print(f"  overall: p = {stats.ttest_ind(outcome[group==0], outcome[group==1]).pvalue:.4f}")
    for name in ["age_band", "city", "device", "channel", "tenure"]:
        sub = rng.integers(0, 3, n)                # a random subgroup variable
        for level in range(3):
            m = sub == level
            if m.sum() > 30:
                p = stats.ttest_ind(outcome[m & (group == 0)], outcome[m & (group == 1)]).pvalue
                flag = "  <- 'SIGNIFICANT'" if p < 0.05 else ""
                print(f"    {name}={level}: p={p:.4f}{flag}")


# 5 -- Bonferroni on ex_04. How many survive?  ____
def ex_05(): pass


# 6 -- FLEXIBLE STOPPING. Check daily, stop at p < 0.05.
#      FALSE POSITIVE RATE: ____%   (should be 5%)
#      WHY DOES PEEKING INFLATE IT?
def ex_06(n_sims=2000, days=20, per_day=25):
    false_positives = 0
    for _ in range(n_sims):
        a, b = [], []
        for _ in range(days):
            a.extend(rng.normal(100, 15, per_day))
            b.extend(rng.normal(100, 15, per_day))      # NO real difference
            if len(a) > 30 and stats.ttest_ind(a, b).pvalue < 0.05:
                false_positives += 1
                break
    print(f"  false positive rate with daily peeking: {false_positives/n_sims:.1%}")
    print("  the honest rate, testing once at the end, is 5%.")


# 7 -- BUILD A SIMPSON'S PARADOX from scratch.
#      Then: could anything in MY data produce one?
#      WHICH VARIABLE, AND WHY:
def ex_07(): pass


# =============================================================================
# THE A/B TEST  -- exercises 8-12
# =============================================================================

# 8 -- PRE-REGISTRATION. Fill this in BEFORE generating or looking at any data.
#      Date:
#      PRIMARY METRIC (one):
#      MINIMUM EFFECT WORTH DETECTING:      and why that number:
#      SAMPLE SIZE (from ex_09):
#      DURATION:                            (at least one full week -- why?)
#      STOPPING RULE:                       (NOT "when p < 0.05")
#      GUARDRAIL METRICS:

# 9 -- power calculation for the effect size above
def ex_09(): pass

# 10 -- generate/collect data, then CHECK THE GROUPS ARE BALANCED
#       on things you did NOT manipulate
def ex_10(): pass

# 11 -- analyse IN THIS ORDER: effect size -> CI -> p-value -> guardrails
def ex_11(): pass

# 12 -- THE RECOMMENDATION. One page.
#       WHAT I FOUND:
#       HOW CONFIDENT (effect size + CI):
#       WHAT IT COSTS:
#       WHAT I RECOMMEND:
#       WHAT WOULD CHANGE MY MIND:


if __name__ == "__main__":
    print("--- ex_02 t vs z ---");              ex_02()
    print("--- ex_03 real coverage ---");       ex_03()
    print("--- ex_04 subgroup hunting ---");    ex_04()
    print("--- ex_06 flexible stopping ---");   ex_06()
    plt.show()
