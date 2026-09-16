"""
Day 52 — Confidence intervals
==============================
A point estimate is a guess presented as a fact.
An interval is an honest statement of what you know.

CORRECT: "my method captures the truth 95% of the time, and this is one of them"
WRONG:   "there is a 95% probability the truth is in THIS interval"
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)


# 1 -- CI at 90 / 95 / 99 on PBS prices. Record the widths.
#      90%: [____, ____]  width ____
#      95%: [____, ____]  width ____
#      99%: [____, ____]  width ____
def ex_01(data): pass


# 2 -- THE EMPIRICAL PROOF. 1,000 samples, 1,000 intervals.
#      HOW MANY CONTAIN THE TRUE MEAN? (should be ~950)
#      COUNT: ____
#      DID THIS MAKE THE DEFINITION CONCRETE?
def ex_02(n_sims=1000, n=40, true_mean=100, true_sd=15):
    contains = 0
    for _ in range(n_sims):
        s = rng.normal(true_mean, true_sd, n)
        lo, hi = stats.t.interval(0.95, df=n - 1,
                                  loc=s.mean(), scale=stats.sem(s))
        contains += lo <= true_mean <= hi
    print(f"  {contains} of {n_sims} intervals contained the true mean")
    print(f"  = {contains / n_sims:.1%}    <- THIS is what '95% confidence' means")


# 3 -- width vs n at 10, 50, 200, 1000. Plot it.
def ex_03(): pass


# 4 -- norm.interval vs t.interval at n=10 and n=1000.
#      WHEN DOES THE DIFFERENCE MATTER?
def ex_04(true_mean=100, true_sd=15):
    for n in (10, 1000):
        s = rng.normal(true_mean, true_sd, n)
        sem = stats.sem(s)
        z_lo, z_hi = stats.norm.interval(0.95, loc=s.mean(), scale=sem)
        t_lo, t_hi = stats.t.interval(0.95, df=n - 1, loc=s.mean(), scale=sem)
        print(f"  n={n:>5}  z-width {z_hi - z_lo:7.3f}   t-width {t_hi - t_lo:7.3f}")


# 5 -- THE OVERLAP CHECK on two real groups from your data.
#      group A CI: [____, ____]
#      group B CI: [____, ____]
#      OVERLAP?  ____
#      WHAT CAN I CLAIM?  WHAT CAN I NOT?
def ex_05(df): pass


# 6 -- WRITE THE INTERPRETATION.
#      CORRECT VERSION:
#
#      COMMON WRONG VERSION:
#
#      WHAT IS WRONG WITH IT:


# 7 -- Add a CI to one number in the Project 1 README.
#      DID IT CHANGE THE CLAIM?   SHOULD I UPDATE THE README?
def ex_07(df): pass


# MINI ASSESSMENT -- 6 minutes, closed book
#   Shop A: mean 2400, n=40, SD 900
#   Shop B: mean 2650, n=35, SD 1100
#     1. CI for each
#     2. do they overlap?
#     3. THE EXACT SENTENCE I WOULD PUT IN A REPORT:


if __name__ == "__main__":
    print("--- ex_02: what 95% actually means ---"); ex_02()
    print("--- ex_04: z vs t ---");                  ex_04()
