# Day 81 — Project 3: Features and First Models

|  |  |
|:--|:--|
| **Date** | Saturday, 5 December 2026 |
| **Position** | Week 12 · Month 3 · Phase 6 |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `project_3/src/features.py`, `src/models.py` |

> **Explore the training set only.** That is not a formality — every look at the test set is a comparison you have made, and after a few of them it stops measuring anything. Day 54's Texas sharpshooter, enforced by discipline rather than hope.
>
> **The order today matters:** explore, then features, then the simplest model that could work, then more complex ones. Starting with a random forest and working backwards teaches you nothing about what the features are doing.

---

## 🎯 Objective

Build features from evidence in the training data, fit a simple model first, and establish honestly whether complexity is buying anything.

---

## 💻 The Work

### 🔴 MUST DO — explore the training set (35 min)

1. Target distribution. **Is it imbalanced?** By how much?
2. Each candidate feature against the target — box plots for numeric, rates for categorical
3. **Which features separate the classes?** Rank them by what you see, and write your predictions down.
4. Missing-data pattern. **Is missingness itself informative?** *(Day 33's MNAR — an order with no delivery date is a different kind of order.)*
5. `cond(X)` on the numeric features *(Day 67)* — anything above 1,000?

**Write the five things you learned.** These are what the feature work is based on.

### 🔴 MUST DO — features (45 min)

6. Build the five features from Day 79, plus anything exercise 3 suggested
7. **The aggregate feature, safely** — earlier rows only
8. Each feature, individually: does it separate the target? Drop anything that does nothing.
9. **Re-run the availability test** on every new feature. Engineered features leak more easily than raw ones, because the engineering can quietly reach forward in time.
10. Save the feature-building as a function, so it can run identically on the test set

### 🔴 MUST DO — models, simplest first (70 min)

11. **The baseline model** — a single rule, or `DummyClassifier`. Record it.
12. **Logistic regression or linear regression** on the five features, in the Day 79 pipeline. Cross-validate. **Compare with the baseline.**
13. Add the remaining features. Did it help?
14. **A single decision tree**, depth-limited. Print it. **Are the rules sensible?** *(This is a data check as much as a model — nonsense rules mean a feature problem.)*
15. A random forest. Cross-validate.
16. **The comparison table:** every model, its cross-validation mean and spread, and the time it took to fit.

### 🔴 MUST DO — the honesty check (15 min)

17. **Is any model beating the baseline by enough to matter?** Use Day 80's stated threshold.
18. **Is any score suspiciously good?** If the first model gets 0.97, stop and look for the leak *before* going further.
19. Record everything in `NOTES.md`, including what did not work.

---

## 🔬 Understanding Check

1. **Data.** Is the target imbalanced? What does that mean for your metric and your threshold?
2. **Features.** Which feature separated best? Did you predict it in exercise 3?
3. **Missingness.** Is missingness informative in this data? How did you handle it?
4. **Simplicity.** How much did the complex model beat the simple one? Is that worth the interpretability cost?
5. **Sanity.** Exercise 14: were the tree's rules sensible? If not, what does that say about the features?
6. **Honesty.** Is anything suspiciously good? What did you check?
7. **Judgement.** If no model clearly beats the baseline — what does that mean, and is it a failure?

> **On that last question:** it is not a failure. "These features do not predict this outcome" is a real finding, honestly arrived at, and writing it up well is a stronger portfolio piece than a model that beats the baseline by 1% and is presented as a success.

---

## 🎯 Expected Outcome

- [ ] An exploration of the training set only, with five written findings
- [ ] Features built from evidence, each justified
- [ ] Four models compared, simplest first
- [ ] A clear answer on whether complexity is buying anything
- [ ] Nothing suspiciously good left unchecked

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Explore the training set | 35 min |
| Feature engineering | 45 min |
| Models, simplest first | 70 min |
| The honesty check | 15 min |
| Daily review | 10 min |
| **Total** | **~175 min** |

---

## 🧪 Mini Assessment

The comparison table. It passes when it shows, for each model: the cross-validation mean, the spread across folds, the fit time, and **the gap to the baseline.** Anyone reading it should be able to say which model they would ship.

---

## 🔁 Daily Review

1. Five things I learned from the training data.
2. Which feature separated best? Did I predict it?
3. Best model, and its margin over the baseline.
4. Anything suspiciously good? What did I check?
5. **Did I look at the test set?** Answer honestly. If yes, that is worth knowing about yourself.

---

## 📦 Completion Criteria

- [ ] Training-set exploration complete, five findings written
- [ ] Features built, each justified, availability-tested
- [ ] Feature building saved as a reusable function
- [ ] Four models cross-validated, simplest first
- [ ] Comparison table with means, spreads and fit times
- [ ] The honesty check done, any suspicious score investigated
- [ ] **Test set still untouched**
- [ ] Committed to git

---

**[← Day 80](../Day_80/Day_80.md)** · **[Day 82 →](../Day_82/Day_82.md)** · [README](../../../README.md)
