# Day 47 — Distributions: Binomial and Beta

|  |  |
|:--|:--|
| **Date** | Sunday, 1 November 2026 |
| **Position** | Week 7 · Month 2 · Phase 3 — Statistics |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_47.py` |
| **Reading** | 📐 **Essential Math Ch. 2, pp. 51–61 + exercises** |

> **Why these two distributions and not a catalogue of twelve.** Nield picks binomial and beta deliberately: the binomial answers *"given a known rate, what outcomes should I expect?"* and the beta answers *"given the outcomes I saw, what rates are plausible?"* — **the two directions of Day 46's probability-versus-statistics distinction**, made concrete.
>
> The beta in particular is where probability stops being about dice and starts being about your actual work: it is how you reason about a conversion rate from 8 successes in 10 trials, and how you know that "80%" from ten trials is a much weaker claim than "80%" from a thousand.

---

## 🎯 Objective

Use the binomial to predict outcomes from a known rate, and the beta to reason about an unknown rate from observed outcomes.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 2, pp. 51–61** | **PRIMARY** · reading + code | 45 min | Binomial and beta distributions |
| **Chapter 2 exercises, p. 61** | **PRACTICE** | 30 min | Answers in Appendix B — check yourself |
| The sections below | REFERENCE | 20 min | The interpretation |

---

## 🧠 Core Concepts

### The binomial — known rate, unknown outcome

*n* independent trials, each succeeding with probability *p*. How many successes?

```python
from scipy.stats import binom
binom.pmf(k=8, n=10, p=0.9)     # P(exactly 8 of 10)
binom.cdf(k=8, n=10, p=0.9)     # P(8 or fewer)
1 - binom.cdf(k=8, n=10, p=0.9) # P(more than 8)
```

**The requirements matter as much as the formula:** fixed *n*, two outcomes, constant *p*, independent trials. Break any one and it does not apply. The one that breaks most often in real data is independence — customers influence each other, and days are correlated.

### The beta — known outcome, unknown rate

This is the one that changes how you think.

> A drug worked on 8 of 10 patients. Is the true success rate really 80%?

The binomial cannot answer that — it needs *p* as an input. The beta gives you the **distribution of plausible values for *p*** given what you saw.

```python
from scipy.stats import beta
a, b = 8, 2                              # successes, failures
1 - beta.cdf(0.90, a, b)                 # P(true rate > 90%)
beta.cdf(0.90, a, b) - beta.cdf(0.80, a, b)   # P(between 80% and 90%)
beta.ppf([0.025, 0.975], a, b)           # a 95% credible interval
```

**The key property: more data narrows the distribution.**

| Observed | Same rate | 95% interval | |
|:---------|:---------:|:-------------|:--|
| 8 of 10 | 80% | roughly 0.49 – 0.94 | almost no information |
| 80 of 100 | 80% | roughly 0.71 – 0.87 | useful |
| 800 of 1,000 | 80% | roughly 0.77 – 0.83 | confident |

**Same point estimate. Completely different claims.** This is the entire idea behind confidence intervals, which you meet on Day 52, and behind why "our model is 94% accurate" is meaningless without knowing the test-set size.

### Where you will use this

| Situation | Distribution |
|:----------|:-------------|
| "Will more than 8 of the next 10 deliveries arrive on time?" | Binomial |
| "Our checkout converts at 3%. What should tomorrow look like?" | Binomial |
| "12 of 400 visitors converted. What is the true rate?" | Beta |
| "Version A: 30/500. Version B: 45/500. Is B better?" | Beta for each, compare — **and this is an A/B test** |
| "The model got 94 of 100 right. How good is it really?" | Beta |

That fourth row is Day 54's A/B test, and the fifth is why Day 76's accuracy number needs a sample size attached.

### The connection worth holding on to

**Beta is the answer to "how much should I trust this percentage?"** Every rate you will ever report — conversion, accuracy, defect rate, churn — is a sample, and the beta tells you how wide the plausible range is. A team that reports 80% from ten trials and 80% from a thousand as the same number is making a mistake this chapter prevents.

---

## 💻 Code

`Day_47.py` — nine exercises.

**Binomial (1–3)**
1. Plot the PMF for `n=10, p=0.9`; compute exact, at-most and at-least probabilities
2. Verify by simulation — 100,000 runs of 10 trials; compare with the analytic answer
3. **Break an assumption:** simulate *dependent* trials and compare against the binomial. How wrong does it get?

**Beta (4–7)**
4. Plot the beta for 8/10, 80/100 and 800/1,000. **One chart, three curves.** This picture is the lesson.
5. Compute `P(true rate > 0.9)` for all three. Put the numbers next to each other.
6. 95% credible intervals for all three; record how the width shrinks
7. **The A/B test, by hand:** A converts 30/500, B converts 45/500. Sample from both betas and compute `P(B > A)`. State what you would tell a product manager.

**Chapter exercises (8–9)**
8. All Chapter 2 exercises from p. 61; check against Appendix B and score yourself
9. **Apply it to your own work:** pick a rate from Project 1 — the share of weeks an item rose, say — and put a credible interval on it. **Should that have been in your README?**

---

## 🔬 Understanding Check

1. **Comparison.** Binomial and beta answer opposite questions. State both.
2. **Understanding.** Exercise 4's chart: what happens to the curve as n grows, and why?
3. **Reasoning.** 8/10 and 800/1,000 are both 80%. Why is the second a much stronger claim? Answer with numbers.
4. **Application.** Exercise 7: what would you tell a product manager who asks "is B better?"
5. **Judgement.** A colleague reports "our new feature converts at 25%" from 4 of 16 users. What do you say?
6. **Reasoning.** Exercise 3: how badly did dependence break the binomial? Where does that occur in real data?
7. **Connection.** How does today's beta distribution relate to a confidence interval? *(You get the frequentist version on Day 52 — predict the connection now.)*
8. **Project.** Exercise 9: should a credible interval have been in your Project 1 README?

---

## 🎯 Expected Outcome

- [ ] Use the binomial and know when its assumptions fail
- [ ] Use the beta to reason about an unknown rate
- [ ] Explain why sample size changes what a percentage means
- [ ] Run a simple A/B comparison from first principles

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 51–61, with code | 45 min |
| Binomial and beta, interpretation | 20 min |
| Exercises 1–7 | 70 min |
| **Chapter 2 exercises + checking** | 30 min |
| Daily review | 12 min |
| **Total** | **~180 min** |

---

## 🧪 Mini Assessment

Eight minutes, closed book. Your churn model correctly identified 47 of 52 customers who left.

1. Point estimate of accuracy
2. 95% credible interval
3. `P(true accuracy > 0.85)`
4. **What do you tell your manager, in one sentence?**

---

## 🔁 Daily Review

1. How much did the beta curve narrow from n=10 to n=1,000? Describe it in words.
2. Exercise 7: what is `P(B > A)`? Is it enough to ship?
3. Exercise 3: how far did dependence push the binomial off?
4. Chapter 2 exercise score: ___ / ___. Which did I get wrong, and why?

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 51–61 read, code typed
- [ ] The three-curve beta chart produced
- [ ] Credible intervals computed for all three sample sizes
- [ ] The A/B comparison done, with a recommendation in plain words
- [ ] **Chapter 2 exercises complete and checked against Appendix B**
- [ ] A credible interval computed on a real Project 1 rate
- [ ] Committed to git

---

**[← Day 46](../Day_46/Day_46.md)** · **[Day 48 →](../Day_48/Day_48.md)** · [README](../../../README.md)
