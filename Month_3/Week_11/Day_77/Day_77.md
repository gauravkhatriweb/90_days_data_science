# Day 77 — ROC, AUC, and Week 11 Consolidation

|  |  |
|:--|:--|
| **Date** | Tuesday, 1 December 2026 |
| **Position** | Week 11 · Month 3 · Phase 6 |
| **Budget** | **~60 min** |
| **Code file** | `Day_77.py` |
| **Reading** | 📐 **Essential Math Ch. 6, pp. 223–226 + exercises** |
| **Also today** | ✍️ **[Week 11 Review](../Week_11_Review.md)** |

> **Chapter 6 finishes today**, and with it the core machine learning theory. ROC and AUC are the last pieces, and they are worth getting right because AUC is the number most often quoted and most often misunderstood.

---

## 🎯 Objective

Read an ROC curve, know what AUC does and does not tell you, and consolidate Week 11.

---

## 📚 Learn — ROC and AUC (25 min)

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 6, pp. 223–226** | **PRIMARY** | 12 min | ROC/AUC · class imbalance |
| [StatQuest — ROC and AUC](https://www.youtube.com/watch?v=4jRBRDbJemM) | **REINFORCEMENT** | 16 min | The construction, step by step |
| **Chapter 6 exercises, p. 226** | PRACTICE | 15 min | Answers in Appendix B |

### What the curve is

For every threshold from 0 to 1, plot **true positive rate (recall)** against **false positive rate**. That traces a curve, and the **area under it is the AUC.**

| AUC | Means |
|:---:|:------|
| 0.5 | No better than random — the diagonal |
| 0.7 | Modest |
| 0.8–0.9 | Good |
| 1.0 | Perfect separation |
| **< 0.5** | Worse than random — **your labels are probably flipped** |

**The interpretation worth remembering:** AUC is the probability that a randomly chosen positive case is scored higher than a randomly chosen negative one. It measures **ranking quality**, independent of any threshold.

### What AUC does not tell you

| Limitation | |
|:-----------|:|
| **It ignores calibration** | A model can rank perfectly and output probabilities that are all wrong |
| **It is optimistic on imbalanced data** | The false-positive rate has a huge denominator, so a lot of false alarms barely move it |
| **It does not pick a threshold** | You still need Day 76's cost arithmetic |
| **It hides where the model is good** | Two models with the same AUC can be good in completely different regions |

**On imbalanced data, use a precision–recall curve instead.** With 1% positives, a model producing 900 false positives out of 99,000 negatives moves the FPR by less than 1% — so the ROC curve barely notices a model that is useless in practice. The PR curve makes the same failure obvious.

**The rule:** balanced classes → ROC/AUC. Imbalanced classes → precision–recall, and report average precision rather than AUC.

---

## 💻 Code

### 🔴 MUST DO — ROC and AUC (25 min)

1. **Build an ROC curve by hand** — sweep the threshold, compute TPR and FPR at each, plot. Match `sklearn.roc_curve`.
2. Compute AUC by hand with the trapezoidal rule; match `roc_auc_score`
3. **Verify the interpretation:** sample many random positive–negative pairs and count how often the positive scores higher. **It should equal the AUC.**
4. **The imbalance demonstration:** on 1% positive data, plot ROC and precision–recall side by side for the same model. **The ROC looks good and the PR curve does not.**
5. **Same AUC, different shapes:** construct two models with equal AUC but different curves. Which would you deploy?

### 🔴 MUST DO — retrieval (25 min)

Closed book, 3 minutes each.

| # | From | Task |
|:-:|:-----|:-----|
| 1 | 71 | Why square residuals? Name one cost |
| 2 | 72 | Write gradient descent in five lines from memory |
| 3 | 72 | Why do gradient methods need scaled features? |
| 4 | 73 | Why can R² only rise when you add features? |
| 5 | 74 | Name four leakage forms and the test that catches most of them |
| 6 | 74 | Why is scaling before splitting a leak? |
| 7 | 75 | Interpret a logistic coefficient of 0.69, correctly |
| 8 | 76 | Why does accuracy lie on imbalanced data? |

**Score: ___ / 8**

---

## 🔬 Understanding Check

1. **Understanding.** What does AUC measure, in one sentence?
2. **Application.** Exercise 3: did the sampling verification match the AUC?
3. **Judgement.** Exercise 4: what did the ROC show that the PR curve did not?
4. **Reasoning.** Why is ROC optimistic on imbalanced data? Answer with the denominator.
5. **Judgement.** Exercise 5: same AUC, different curves — which would you deploy, and why?
6. **Integration.** Week 11 in one paragraph: what is a model, how is it fitted, and how do you know whether to believe it?

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 223–226 + StatQuest | 25 min |
| ROC exercises 1–5 | 20 min |
| Retrieval, closed book | 20 min |
| Ch. 6 exercises | 15 min |
| **Total** | **~80 min** · then the Week 11 Review |

---

## 🔁 Daily Review

1. Retrieval score: ___ / 8. Weakest?
2. Exercise 4: how different were the ROC and PR pictures?
3. **Chapter 6 exercise score: ___ / ___**
4. **Project 3 starts in three days.** Is the brief still right, or did this week change it?

---

## 📦 Completion Criteria

- [ ] ROC built by hand and matched against sklearn
- [ ] AUC computed by hand and verified by pair sampling
- [ ] The ROC-vs-PR imbalance demonstration produced
- [ ] Eight retrieval tasks attempted closed-book
- [ ] **Chapter 6 exercises complete and checked**
- [ ] **[Week 11 Review](../Week_11_Review.md) completed**
- [ ] Committed to git

---

**[← Day 76](../Day_76/Day_76.md)** · **[Week 11 Review →](../Week_11_Review.md)** · [README](../../../README.md)
