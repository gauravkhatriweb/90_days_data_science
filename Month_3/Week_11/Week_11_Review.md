# Week 11 Review — Regression, Gradient Descent, Validation, Classification

|  |  |
|:--|:--|
| **Covers** | Days 71–77 · 25 November – 1 December 2026 |
| **Topics** | Linear regression · gradient descent · R² and significance · **validation and leakage** · logistic regression · classification metrics · ROC/AUC |
| **Budget** | 45–60 min |
| **Milestone** | 📐 **Essential Math Chapters 5 and 6 complete** |

> The densest week of Month 3. Everything in Project 3 depends on it.

---

## ⏸️ Catch-Up Rights

| Day | Done? | MUST DO only |
|:---:|:-----:|:-------------|
| 71 · Linear regression | ☐ | The closed-form fit + the residual plot |
| 72 · Gradient descent | ☐ | **Write it from scratch.** Non-negotiable. |
| 73 · R², significance | ☐ | The noise demonstration + multicollinearity |
| 74 · **Validation and leakage** | ☐ | **The four deliberate leaks. Keep this one above all.** |
| 75 · Logistic regression | ☐ | The fit + the doubling mistake |
| 76 · Classification metrics | ☐ | The 99% model + the cost-based threshold |
| 77 · ROC/AUC | ☐ | The imbalance demonstration |

---

## 📝 Part 1 — Knowledge (closed book, 15 min)

1. Why square residuals rather than take absolute values? Name a cost.
2. Write gradient descent in five lines from memory.
3. Why do gradient-based methods need scaled features? Answer with the error surface.
4. Why can R² only rise when features are added? What does adjusted R² do?
5. Name four leakage forms and the single test that catches most of them.
6. Why does scaling before splitting leak? What exactly crosses the boundary?
7. What is the difference between a confidence interval and a prediction interval?
8. Interpret a logistic coefficient of 0.69, correctly — and say what the common mistake is.
9. Why does accuracy lie on imbalanced data?
10. What does AUC measure? Name two things it does not tell you.

**Score: ___ / 10**

---

## 💻 Part 2 — Coding (closed book, 20 min)

**A — 6 min.** Gradient descent from scratch, converging to match the closed form.
**B — 5 min.** A correct pipeline: split → scale inside → cross-validate → test once.
**C — 5 min.** A confusion matrix and all five metrics, by hand.
**D — 4 min.** A cost-based threshold given FP and FN costs.

**Score: ___ / 4**

---

## 🧩 Part 3 — Problem Solving (open book, 10 min)

> A colleague shows you a churn model: **AUC 0.94**, accuracy 96%, and they want to deploy it tomorrow. Churn is 4% of customers.
>
> Write your review. Cover: what you would check, what the accuracy figure is worth, what AUC is hiding here, what could be leaking, and **what one question you would ask the business before any of it matters.**

---

## 🔁 Part 4 — Retention Check

- [ ] I plot residuals before trusting a fit
- [ ] I can write gradient descent without reference
- [ ] I check `cond(X)` before interpreting a coefficient
- [ ] I split before doing anything else
- [ ] I put preprocessing inside a `Pipeline`, always
- [ ] I treat a suspiciously good score as a bug report
- [ ] I read logistic coefficients as odds ratios, not probabilities
- [ ] I choose a threshold from costs, never from 0.5
- [ ] I use precision–recall instead of ROC on imbalanced data

> Weak this week: ______________________________________________

---

## 📐 Part 5 — Mathematics

**Chapters 5 and 6 complete?** ☐ ☐  ·  Exercise scores: Ch. 5 ___ / ___ · Ch. 6 ___ / ___

**Chapters 1–6 are now done. Only Chapter 8 (career) remains, on Day 89.** Chapter 7 (neural networks) is deliberately deferred — see [Resources & Decisions](../../Resources_and_Decisions.md).

**The honest question:** did the mathematics make the modelling clearer, or was it a detour? Answer specifically — which chapter earned its time, and which felt thin?

> ______________________________________________

---

## 🤖 Part 6 — Project 3 Readiness

**Starts Day 80. Three days away.**

| | |
|:--|:--|
| Question and target defined | ☐ |
| Data accessible | ☐ |
| Baseline computed | ☐ |
| **Leakage audit done (Day 74, ex 12)** | ☐ |
| Split strategy chosen, with a reason | ☐ |
| Metric chosen, with a reason | ☐ |
| Error costs estimated | ☐ |

**Any unticked box is a Day 78–79 job, not a Day 80 one.** Arriving at a project undecided costs a day you do not have.

**My metric and threshold reasoning:**

> ______________________________________________

---

## 🎓 Part 7 — University

- Final exams follow Day 90. When does revision start, and does it collide with Days 80–85?
- **Project 3 is the piece you most need to protect.** If December is heavy, decide now what gives — and it should not be Project 3.

---

## 🔮 Part 8 — The Decision

| If… | Then… |
|:----|:------|
| Part 1 ≥ 7, Day 74 done properly | ✅ Continue. Trees and feature engineering next. |
| Day 74 skipped or rushed | 🛑 **Do it before Day 80.** It is the difference between a real project and a tutorial. |
| Behind overall | 🔧 **Cut Day 78 (trees) and Day 86 (k-means, PCA).** Keep Days 79, 80–85. Follow the Month 2 Review's cut order. |
| Comfortable | ⏩ Read ahead on pipelines; start Project 3's data loading on Day 79. |

**My decision:**

> ______________________________________________

---

## 📊 Week 11 Scorecard

| Measure | Result |
|:--------|:-------|
| Days completed | ___ / 7 |
| Part 1 | ___ / 10 |
| Part 2 | ___ / 4 |
| Day 77 retrieval | ___ / 8 |
| Retention boxes | ___ / 9 |
| Ch. 5 exercises | ___ / ___ |
| Ch. 6 exercises | ___ / ___ |
| **Project 3 ready** | ___ / 7 boxes |
| Honest hours | ___ h |
| **Biggest win** | |
| **Biggest gap** | |

---

**[← Day 77](./Day_77/Day_77.md)** · **[Day 78 →](../Week_12/Day_78/Day_78.md)** · [README](../../README.md)
