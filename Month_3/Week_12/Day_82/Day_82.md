# Day 82 — Project 3: Where the Model Fails

|  |  |
|:--|:--|
| **Date** | Sunday, 6 December 2026 |
| **Position** | Week 12 · Month 3 · Phase 6 |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `project_3/src/evaluate.py` |

> **Error analysis is the most valuable and least practised skill in machine learning.** Anyone can report a score. Very few can say *on which kind of case the model is wrong, and why* — and that is the part a business actually needs, because it determines whether the model can be trusted in the cases that matter.
>
> **Today you also touch the test set. Once.** Everything before this has been cross-validation on the training data. After today's evaluation, no more tuning — because a test set you have tuned against is a training set.

---

## 🎯 Objective

Tune honestly, evaluate once on held-out data, and understand where and why the model fails.

---

## 💻 The Work

### 🔴 MUST DO — tuning, on training data only (45 min)

1. `GridSearchCV` or `RandomizedSearchCV` on your best two models. **Note that the search runs inside the cross-validation**, so the pipeline refits each fold — that is why Day 79 mattered.
2. **Record how much tuning actually bought.** It is usually less than expected, and that is worth knowing.
3. The threshold, from Day 76's cost arithmetic — **not from accuracy or F1**
4. **Check the learning curve** *(Day 74, exercise 5)*: would more data help, or is the model the limit?

### 🔴 MUST DO — the test set, once (25 min)

5. **Fit the final pipeline on all the training data. Predict on the test set. Once.**
6. Report: the primary metric, a confidence interval on it *(Day 52 — it is a sample statistic)*, and the gap to baseline
7. **Compare with the cross-validation estimate.** A large gap means something went wrong — investigate rather than explain it away.
8. **Write the number in the README now**, before any further work, so it cannot drift.

### 🔴 MUST DO — error analysis (80 min)

This is the day's real work.

9. **Pull the worst errors.** The most confident wrong predictions, both directions.
10. **Read them.** Actually read twenty rows. **What do they have in common?**
11. Error rate by segment — by category, region, time period, target value. **Where is the model worst?**
12. **The error distribution:** is the model wrong randomly, or systematically in one direction?
13. For regression: residuals against fitted values, and against each feature *(Day 71)*. For classification: the confusion matrix, and the probability distribution for each true class.
14. **Find one concrete failure mode** — a describable kind of case the model handles badly. Write it in one sentence.
15. **Ask whether it is fixable.** More data? A better feature? Or is it genuinely unpredictable?

### 🔴 MUST DO — record it (15 min)

16. Write results and error analysis into the README
17. **Including what did not work.** A README that only lists successes reads as incomplete to anyone experienced.

---

## 🔬 Understanding Check

1. **Tuning.** How much did tuning buy? Was it worth the compute?
2. **Honesty.** How close was the test score to the cross-validation estimate? What would a large gap have meant?
3. **Uncertainty.** What is the confidence interval on your test score? How wide, given the test-set size?
4. **Errors.** What do the worst errors have in common? Read them before answering.
5. **Segments.** Which segment is the model worst on? Does that matter for the decision it informs?
6. **Systematic bias.** Is the model wrong in one direction? What would cause that?
7. **The failure mode.** State it in one sentence. Is it fixable?
8. **Deployment.** Would you deploy this? What would have to be true first?

---

## 🎯 Expected Outcome

- [ ] A tuned model, with the gain from tuning recorded
- [ ] A single, honest test-set evaluation with a confidence interval
- [ ] Twenty errors actually read
- [ ] Error rates by segment
- [ ] One named, described failure mode

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Tuning, training data only | 45 min |
| The test set, once | 25 min |
| **Error analysis** | 80 min |
| Writing it up | 15 min |
| Daily review | 10 min |
| **Total** | **~175 min** |

---

## 🧪 Mini Assessment

**One sentence describing a failure mode**, specific enough that someone could act on it.

> e.g. *"The model systematically under-predicts delay for orders shipped from sellers in states more than 2,000 km from the customer, because only 3% of training orders were long-distance and the distance feature is effectively unused below that threshold."*

That sentence is worth more than the accuracy number.

---

## 🔁 Daily Review

1. Test score, and how far from the cross-validation estimate?
2. What did the twenty worst errors have in common?
3. My one-sentence failure mode.
4. Would I deploy this? What would have to be true first?
5. **Did I resist touching the test set more than once?**

---

## 📦 Completion Criteria

- [ ] Tuning done inside cross-validation, gain recorded
- [ ] Threshold set from costs
- [ ] Learning curve checked
- [ ] **Test set evaluated once**, with a confidence interval
- [ ] Cross-validation vs test gap noted
- [ ] Twenty errors read individually
- [ ] Error rates computed by segment
- [ ] One failure mode named and described
- [ ] Results and failures written into the README
- [ ] Committed to git

---

**[← Day 81](../Day_81/Day_81.md)** · **[Day 83 →](../Day_83/Day_83.md)** · [README](../../../README.md)
