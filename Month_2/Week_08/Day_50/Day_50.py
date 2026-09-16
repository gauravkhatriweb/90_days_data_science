"""
Day 50 — The normal distribution and z-scores
==============================================
DENSITY IS NOT PROBABILITY. Probability is AREA. That is why Day 25
covered integrals -- and why you never integrate by hand: you use the CDF.

  cdf(x) -> "what fraction is below x?"
  ppf(q) -> "below what value is fraction q?"   <- the business question
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)


# 1 -- three curves at different sigma. VERIFY 68-95-99.7 via the CDF.
def ex_01():
    for sd in (1, 2, 5):
        inside_1 = stats.norm.cdf(1, 0, 1) - stats.norm.cdf(-1, 0, 1)
        inside_2 = stats.norm.cdf(2, 0, 1) - stats.norm.cdf(-2, 0, 1)
        inside_3 = stats.norm.cdf(3, 0, 1) - stats.norm.cdf(-3, 0, 1)
    print(f"  +/-1 sd: {inside_1:.4f}")
    print(f"  +/-2 sd: {inside_2:.4f}")
    print(f"  +/-3 sd: {inside_3:.4f}")


# 2 -- DENSITY IS NOT PROBABILITY. Show the PDF exceeding 1.
#      WHY IS THAT FINE?
def ex_02():
    print(f"  pdf(0) with sigma=0.1 : {stats.norm.pdf(0, 0, 0.1):.4f}   <- above 1")
    print(f"  total area            : {stats.norm.cdf(1e9, 0, 0.1):.4f}")


# 3 -- cdf vs pdf on the same values. WHAT DOES EACH RETURN?
def ex_03(): pass


# 4 -- FOUR BUSINESS QUESTIONS. Deliveries: mu=4 days, sigma=1.
def ex_04(mu=4, sd=1):
    print(f"  P(more than 6 days)      = {1 - stats.norm.cdf(6, mu, sd):.4f}")
    print(f"  P(between 3 and 5 days)  = {stats.norm.cdf(5, mu, sd) - stats.norm.cdf(3, mu, sd):.4f}")
    print(f"  90% arrive within        = {stats.norm.ppf(0.90, mu, sd):.2f} days")
    print(f"  99% arrive within        = {stats.norm.ppf(0.99, mu, sd):.2f} days")


# 5 -- ppf at 90 / 95 / 99.
#      WHICH WOULD I ACTUALLY PROMISE?
#      WHY NOT THE HIGHEST ONE?
def ex_05(): pass


# 6 -- On PBS data: P(week-on-week rise > 5%) ASSUMING normal.
#      THEN CHECK WHETHER THE ASSUMPTION HOLDS.
def ex_06(df): pass


# 7 -- z-scores on a price series. Everything beyond +/-2 and +/-3.
def ex_07(s): pass


# 8 -- Compare two items on DIFFERENT price scales using z.
#      WHICH HAD THE MORE UNUSUAL MOVE?  (raw change would give the wrong answer)
def ex_08(df): pass


# 9 -- IS MY DATA NORMAL? Three checks.
#      histogram shows:
#      Q-Q plot shows:
#      Shapiro-Wilk p = ____  ->  conclusion:
#      WHAT WOULD I HAVE GOT WRONG BY ASSUMING NORMALITY?
def ex_09(s):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    axes[0].hist(s, bins=30)
    axes[0].set_title("Distribution")
    stats.probplot(s, dist="norm", plot=axes[1])
    axes[1].set_title("Q-Q plot — straight line means normal")
    fig.tight_layout()
    stat, p = stats.shapiro(s.sample(min(len(s), 5000)))
    print(f"  Shapiro-Wilk p = {p:.6f}   -> {'not normal' if p < 0.05 else 'consistent with normal'}")


# MINI ASSESSMENT -- 6 minutes, closed book
#   Exam marks: mu=68, sigma=12
#     1. fraction above 85     = ____
#     2. the 90th percentile   = ____
#     3. a 44 is z = ____  -> in words: ____
#     4. top-5% distinction cutoff = ____


if __name__ == "__main__":
    print("--- ex_01 68-95-99.7 ---"); ex_01()
    print("--- ex_02 density > 1 ---"); ex_02()
    print("--- ex_04 business questions ---"); ex_04()
