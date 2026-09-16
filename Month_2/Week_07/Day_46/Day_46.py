"""
Day 46 — Probability
=====================
SIMULATE EVERYTHING. It is the fastest way to find out whether your
reasoning was right, and Nield takes the same approach.

The one that matters: P(A|B) is NOT P(B|A).
"""
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)


# 1 -- 100,000 dice rolls. Empirical vs theoretical for six events.
def ex_01(n=100_000):
    rolls = rng.integers(1, 7, n)
    events = {
        "P(6)":            lambda r: r == 6,
        "P(even)":         lambda r: r % 2 == 0,
        "P(>4)":           lambda r: r > 4,
        "P(2 or 5)":       lambda r: (r == 2) | (r == 5),
        "P(not 1)":        lambda r: r != 1,
        "P(prime)":        lambda r: np.isin(r, [2, 3, 5]),
    }
    for name, fn in events.items():
        print(f"  {name:<12} empirical {fn(rolls).mean():.4f}")
    # THEORETICAL VALUES:


# 2 -- joint and union. VERIFY the -P(A and B) term is needed.
#      Compute the union both ways and compare.
#      WITHOUT subtraction: ____   WITH: ____   TRUE (simulated): ____
def ex_02(n=100_000):
    pass


# 3 -- dependent vs independent. Show the multiplication rule FAILING
#      for the dependent case.
#      P(A)*P(B) = ____   actual P(A and B) = ____   WHY THE GAP?
def ex_03(n=100_000):
    pass


# 4 -- two-way contingency table. Compute EVERY conditional from it.
def ex_04():
    pass


# 5 -- DEMONSTRATE P(A|B) != P(B|A) with your own numbers.
#      P(A|B) = ____  MEANS:
#      P(B|A) = ____  MEANS:
def ex_05():
    pass


# 6 -- THE DISEASE TEST. Verify 9%, then plot across base rates.
#      MY GUESS BEFORE COMPUTING: ____%
#      WHAT SHAPE IS THE CURVE?
#      AT WHAT BASE RATE DOES A POSITIVE BECOME MORE LIKELY TRUE THAN FALSE?
def bayes_positive(base_rate, sensitivity=0.99, false_positive=0.01):
    """P(disease | positive test)."""
    pass

def ex_06():
    print(f"  base 0.1%  -> {bayes_positive(0.001):.4f}")
    rates = np.logspace(-4, -1, 100)
    probs = [bayes_positive(r) for r in rates]
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.semilogx(rates * 100, np.array(probs) * 100)
    ax.axhline(50, ls="--", lw=1)
    ax.set_xlabel("Base rate in the population (%)")
    ax.set_ylabel("P(disease | positive test)  (%)")
    ax.set_title("A 99%-accurate test tells you almost nothing about a rare disease")
    fig.tight_layout()


# 7 -- Bayes on real data: given a price rise > 10%, P(item is food)?
def ex_07(df):
    pass


# 8 -- ten questions from Tem.txt lines 2083-2108.
#      Solve BY HAND first, then verify by simulation. Score yourself.
#      hand: ___ / 10   matched simulation: ___ / 10


# 9 -- drawing WITHOUT replacement (the conditional versions)
def ex_09(n=100_000):
    pass


# 10 -- THE INDEPENDENCE CHECK on two of your PBS items.
#       ARE THEY INDEPENDENT?  evidence:
#       WHAT DOES THAT MEAN FOR ANY ANALYSIS THAT ASSUMED THEY WERE?
def ex_10(df):
    pass


# MINI ASSESSMENT -- 10 minutes, closed book
#   Fraud check flags 5% of transactions.
#   Of genuinely fraudulent ones, it flags 90%.
#   Genuine fraud is 0.5% of all transactions.
#
#   1. P(actually fraud | flagged) = ____
#   2. What would the shop owner ASSUME it is? ____
#   3. WHAT SHOULD I TELL THEM?


if __name__ == "__main__":
    print("--- ex_01 ---"); ex_01()
    print("--- ex_06: the disease test ---"); ex_06()
    plt.show()
