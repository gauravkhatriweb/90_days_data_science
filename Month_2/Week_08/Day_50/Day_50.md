# Day 50 — The Normal Distribution and Z-Scores

|  |  |
|:--|:--|
| **Date** | Wednesday, 4 November 2026 |
| **Position** | Week 8 · Month 2 · Phase 3 — Statistics |
| **Budget** | **~75 min** |
| **Code file** | `Day_50.py` |
| **Reading** | 📐 **Essential Math Ch. 3, pp. 78–89** |

> **This week is the densest conceptual stretch of the ninety days.** Normal distribution today, the Central Limit Theorem tomorrow, confidence intervals on Friday, p-values and hypothesis testing at the weekend. Everything in Month 3 — every model evaluation, every "is this difference real?" — rests on these five days.
>
> **If a day here needs two attempts, take two attempts.** Falling behind on this material is much cheaper than carrying a misunderstanding into machine learning.

---

## 🎯 Objective

Understand what makes the normal distribution special, use the CDF to answer real probability questions, and use z-scores to compare things measured on different scales.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 3, pp. 78–89** | **PRIMARY** · reading + code | 40 min | Normal distribution · CDF · inverse CDF · z-scores |
| The sections below | REFERENCE | 15 min | Why it appears everywhere, and where it does not |

---

## 🧠 Core Concepts

### The shape, and its two parameters

The normal distribution is fully described by **mean (μ)** and **standard deviation (σ)**. Two numbers, and the entire curve is determined.

```
μ ± 1σ  ≈ 68%
μ ± 2σ  ≈ 95%
μ ± 3σ  ≈ 99.7%
```

**Memorise 68–95–99.7.** It converts a standard deviation into an intuition: if average delivery time is 4 days with σ = 1, then 95% of deliveries land between 2 and 6 days, and an 8-day delivery is a genuine outlier rather than bad luck.

### Density is not probability

The y-axis of a normal curve is **density**, not probability, and it can exceed 1. `P(X = exactly 5.0)` is zero for a continuous variable — there are infinitely many values, so no single one has positive probability.

**Probability is area.** That is why Day 25's integrals were in Chapter 1: the probability of landing between two points *is* the area under the curve between them.

You never integrate by hand. You use the CDF.

### CDF and inverse CDF — the two questions

```python
from scipy.stats import norm

norm.cdf(x, loc=mu, scale=sigma)       # P(X <= x)  -- "what fraction is below?"
norm.ppf(q, loc=mu, scale=sigma)       # the inverse -- "below what value is q?"
```

| Question | Tool |
|:---------|:-----|
| What proportion of deliveries take more than 6 days? | `1 - norm.cdf(6, 4, 1)` |
| What fraction take between 3 and 5 days? | `norm.cdf(5,4,1) - norm.cdf(3,4,1)` |
| 90% of deliveries arrive within how many days? | `norm.ppf(0.90, 4, 1)` |

**`ppf` is the one people forget exists**, and it answers the business question directly. "What should we promise customers?" is a `ppf` question, not a mean question — and the answer to "95% of orders arrive within N days" is `norm.ppf(0.95, ...)`.

### Z-scores — a common currency

```
z = (x − μ) / σ
```

**"How many standard deviations from the mean is this?"** Converting to z removes the units, which lets you compare things that are otherwise incomparable:

- A student 1.8σ above their class mean in maths and 0.4σ above in English is much better at maths, regardless of the raw marks
- A price 3σ above its own history is unusual, whether it is tea at 1,250 or salt at 60

| z | Roughly |
|:--|:--|
| 0 | at the mean |
| ±1 | ~68% of data inside |
| ±2 | ~95% inside — often called "unusual" |
| ±3 | ~99.7% inside — genuinely rare |

**Two places this returns:** Day 40's z-score outlier detection was this, and Day 79's feature scaling (`StandardScaler`) is literally this formula applied to every column.

### Where the normal distribution does *not* apply

This is the part that gets skipped and it matters.

| Data | Distribution | Why not normal |
|:-----|:-------------|:---------------|
| Income, wealth | Right-skewed, often log-normal | A floor at zero, no ceiling |
| Counts of rare events | Poisson | Discrete, non-negative |
| Time until an event | Exponential | Non-negative, memoryless |
| Prices over time | Often log-normal on levels | Multiplicative growth, floor at zero |
| Website session length | Heavy-tailed | A few very long sessions |

**Your PBS price data is probably not normally distributed.** Check before assuming — `.hist()`, a Q-Q plot, and `scipy.stats.shapiro`. Applying normal-based methods to skewed data produces confident, wrong answers, and it is one of the most common errors in applied work.

**The good news arrives tomorrow:** the Central Limit Theorem says that *sample means* tend towards normal even when the data is not — which is why normal-based methods work far more often than they have any right to.

---

## 💻 Code

`Day_50.py` — nine exercises.

**The shape (1–3)**
1. Plot normal curves at three different σ; verify 68–95–99.7 by integrating the CDF
2. **Density is not probability:** show the PDF exceeding 1 for a small σ, and explain why that is fine
3. `cdf` vs `pdf` on the same values — state what each returns

**Real questions (4–6)**
4. Delivery times, μ=4, σ=1 — answer four business questions with `cdf` and `ppf`
5. `ppf`: what delivery promise can you make at 90%, 95% and 99%? **Which would you actually promise, and why not the highest?**
6. Apply it to your PBS data: what is the probability of a week-on-week rise above 5%, assuming normal? **Then check whether that assumption holds.**

**Z-scores (7–8)**
7. Convert a price series to z-scores; find everything beyond ±2 and ±3
8. Compare two items on completely different price scales using z — which had the more unusual move?

**The check (9)**
9. **Is your data normal?** Histogram, Q-Q plot, and a Shapiro-Wilk test. Then answer: **what would you have got wrong if you had assumed normality?**

---

## 🔬 Understanding Check

1. **Understanding.** Why can a probability density exceed 1 when a probability cannot?
2. **Application.** Exercise 5: which delivery promise would you make, and why not the 99% one?
3. **Reasoning.** Why does converting to z-scores let you compare a maths mark with an English mark?
4. **Comparison.** `cdf` vs `ppf` — state the question each answers.
5. **Judgement.** Exercise 9: is your data normal? What specifically would you have got wrong by assuming it was?
6. **Application.** Name three real quantities that are definitely *not* normal, and say what shape each has.
7. **Connection.** `StandardScaler` on Day 79 is the z-score formula. Why would a model need every feature on the same scale?

---

## 🎯 Expected Outcome

- [ ] Use `cdf` and `ppf` to answer real questions without hesitation
- [ ] Explain density versus probability
- [ ] Use z-scores to compare incomparable scales
- [ ] Check normality rather than assuming it

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 78–89, with code | 40 min |
| Where it does and does not apply | 15 min |
| Nine exercises | 25 min |
| Daily review | 5 min |
| **Total** | **~85 min** |

---

## 🧪 Mini Assessment

Six minutes, closed book. Exam marks are normal, μ=68, σ=12.

1. What fraction scored above 85?
2. What mark is the 90th percentile?
3. A student scored 44. How unusual, in z terms and in words?
4. The top 5% get a distinction. What is the cutoff?

---

## 🔁 Daily Review

1. Is my PBS data normal? What did the Q-Q plot show?
2. What would I have got wrong by assuming normality?
3. Can I state 68–95–99.7 and explain what it means to someone in one sentence?
4. Which delivery promise did I choose, and what was my reasoning?

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 78–89 read, code typed
- [ ] 68–95–99.7 verified by CDF integration
- [ ] Four business questions answered with `cdf` and `ppf`
- [ ] Z-score comparison across two different price scales
- [ ] Normality checked three ways on your own data
- [ ] Mini assessment done closed-book
- [ ] Committed to git

---

**[← Week 7 Review](../../Week_07/Week_07_Review.md)** · **[Day 51 →](../Day_51/Day_51.md)** · [README](../../../README.md)
