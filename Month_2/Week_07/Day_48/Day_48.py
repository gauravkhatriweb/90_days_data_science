"""
Day 48 — Descriptive statistics, and why n-1
=============================================
YOU ALMOST NEVER HAVE A POPULATION. Everything you compute is an ESTIMATE
of something you cannot observe. That is why statistics exists.

Exercise 4 is the empirical proof of n-1. It is more convincing than the algebra.
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)


# 1 -- mean, median, mode on PBS prices. WHERE DO THEY DISAGREE?
#      WHAT DOES THE DISAGREEMENT TELL ME ABOUT THE DISTRIBUTION?
def ex_01(df): pass


# 2 -- THE OUTLIER DEMONSTRATION.
#      mean moved by: ____    median moved by: ____
#      WHEN IS THE MEAN'S SENSITIVITY A FEATURE RATHER THAN A BUG?
def ex_02():
    data = np.array([50_000] * 100 + [500_000_000])
    clean = data[:-1]
    print(f"  without outlier: mean {clean.mean():>14,.0f}  median {np.median(clean):>12,.0f}")
    print(f"  with outlier   : mean {data.mean():>14,.0f}  median {np.median(data):>12,.0f}")


# 3 -- variance from scratch, both divisors. Match against SciPy.
def ex_03(data):
    pass


# 4 -- THE n-1 PROOF. 10,000 samples of size 5 from a KNOWN population.
#      Which divisor averages to the TRUE variance?
#      TRUE VARIANCE: ____
#      mean of /n   estimates: ____
#      mean of /n-1 estimates: ____
#      WHICH ONE IS UNBIASED?
#      DID THE SIMULATION CONVINCE ME MORE THAN THE ARGUMENT?
def ex_04(n_sims=10_000, sample_size=5):
    population = rng.normal(100, 15, 1_000_000)
    true_var = population.var()

    var_n, var_n1 = [], []
    for _ in range(n_sims):
        s = rng.choice(population, sample_size, replace=False)
        var_n.append(s.var(ddof=0))
        var_n1.append(s.var(ddof=1))

    print(f"  true population variance : {true_var:8.2f}")
    print(f"  mean of  /n   estimates  : {np.mean(var_n):8.2f}   (too small)")
    print(f"  mean of  /n-1 estimates  : {np.mean(var_n1):8.2f}")


# 5 -- np.std vs df.std(). They DISAGREE by default.
#      WHY? WHICH DO I ACTUALLY WANT?
def ex_05():
    data = [12, 15, 19, 22, 30]
    print(f"  np.std(data)            = {np.std(data):.4f}   (ddof=0, POPULATION)")
    print(f"  np.std(data, ddof=1)    = {np.std(data, ddof=1):.4f}   (ddof=1, SAMPLE)")
    print(f"  pd.Series(data).std()   = {pd.Series(data).std():.4f}   (ddof=1 by default)")


# 6 -- weighted vs unweighted mean on your SPI items. HOW DIFFERENT?
#      unweighted: ____   weighted: ____
#      WHAT DOES THE UNWEIGHTED VERSION ACTUALLY MEASURE?
def ex_06(df): pass


# 7 -- range, IQR, SD on the same data. WHEN WOULD EACH MISLEAD?
#      range:
#      IQR:
#      SD:
def ex_07(s): pass


# 8 -- THE BIAS IN MY OWN DATA.
#      WHICH BIAS: selection / self-selection / survivorship / confirmation
#      WHY:
#      WHAT DOES IT DO TO MY PROJECT 1 CONCLUSION:
#      DID I MENTION IT IN THE README?


# MINI ASSESSMENT -- 6 minutes, closed book
#   40 salaries, one is 10x the others.
#     1. measure of centre, and why:
#     2. measure of spread, and why:
#     3. sample SD (correct divisor): ____
#     4. one sentence for the report about that one value:


if __name__ == "__main__":
    print("--- ex_02 the outlier ---"); ex_02()
    print("--- ex_04 the n-1 proof ---"); ex_04()
    print("--- ex_05 the defaults ---"); ex_05()
