# Week 12 Review — Trees, Pipelines, and Project 3

|  |  |
|:--|:--|
| **Covers** | Days 78–84 · 2–8 December 2026 |
| **Topics** | Decision trees · random forests · feature engineering · pipelines · **Project 3 built** |
| **Budget** | 45–60 min |

---

## ⏸️ Catch-Up Rights

| Day | Done? | MUST DO only |
|:---:|:-----:|:-------------|
| 78 · Trees | ☐ | Depth curves + the cardinality-bias demonstration |
| 79 · Pipelines | ☐ | **The `ColumnTransformer` pipeline.** Project 3 needs it. |
| 80 · P3 setup | ☐ | **Split + baselines + protocol.** Non-negotiable. |
| 81 · P3 features and models | ☐ | The comparison table |
| 82 · P3 evaluation | ☐ | **The test evaluation + twenty errors read** |
| 83 · P3 interpretation | ☐ | The limitations + the causality paragraph |
| 84 · Consolidation | ☐ | The endgame decision |

---

## 📝 Part 1 — Knowledge (closed book, 12 min)

1. How does a decision tree choose a split?
2. Why does bagging reduce variance?
3. Two reasons to distrust built-in feature importance.
4. Why does a `Pipeline` make preprocessing leakage structurally impossible?
5. Which models need scaling, and why those specifically?
6. Why compute the baseline before any model?
7. Why is the test set touched once?
8. Name four categories of limitation for a model write-up.

**Score: ___ / 8**

---

## 💻 Part 2 — Coding (closed book, 18 min)

**A — 6 min.** A `ColumnTransformer` + `Pipeline` with imputation, scaling and one-hot encoding, cross-validated.
**B — 5 min.** Permutation importance on a held-out set.
**C — 4 min.** A cost-based threshold from FP and FN costs.
**D — 3 min.** A confidence interval on a test-set accuracy.

**Score: ___ / 4**

---

## 🧩 Part 3 — Problem Solving (open book, 10 min)

> Your model's test score is **0.12 below** its cross-validation estimate.
>
> List the six things that could cause that, in the order you would check them, and say what each would look like.

---

## 🔁 Part 4 — Retention Check

- [ ] I build a `Pipeline` rather than transforming data by hand
- [ ] I compute a baseline before fitting anything
- [ ] I split before exploring
- [ ] I use permutation importance, not the built-in
- [ ] I read individual errors, not just aggregate metrics
- [ ] I state limitations before anyone asks
- [ ] I never write "causes" about an observational model

> Weak this week: ______________________________________________

---

## 🤖 Part 5 — Project 3 Status

| | |
|:--|:--|
| Problem statement and protocol written before modelling | ☐ |
| Leaks dropped in code with reasons | ☐ |
| Baselines recorded | ☐ |
| Models compared, simplest first | ☐ |
| **Test set evaluated once** | ☐ |
| Confidence interval on the score | ☐ |
| **Twenty errors read individually** | ☐ |
| A named failure mode | ☐ |
| Limitations and the causality paragraph | ☐ |
| Recommendation written | ☐ |

**Test score:** ___  ·  **Baseline:** ___  ·  **Gap:** ___

**Does it clear Day 80's stated threshold?** ☐

**My failure mode, in one sentence:**

> ______________________________________________

**The honest question:** is this a model worth deploying, or a project worth writing up as "these features do not predict this outcome"? **Both are good outcomes. Only one is a lie.**

> ______________________________________________

---

## 🎓 Part 6 — University

- Final exams are close. Days 85–90 are the portfolio and review — **lower cognitive load than Weeks 11–12**, which is deliberate.
- If exams collide, Day 84's priority order tells you what to protect.

---

## 🔮 Part 7 — The Decision

**Six days left.**

| If… | Then… |
|:----|:------|
| P3 ready, Part 1 ≥ 6 | ✅ Ship tomorrow, then the portfolio. |
| P3 needs another day | 🔧 **Take it from Day 86.** That is what the cut order is for. |
| Behind on everything | 🛑 **Ship P3, do Day 88, do Day 90.** Those three are the ones that matter. Move 86, 87 and 89 to January. |
| Comfortable | ⏩ Start Day 88's portfolio pass early — it always takes longer than expected. |

**My decision:**

> ______________________________________________

---

## 📊 Week 12 Scorecard

| Measure | Result |
|:--------|:-------|
| Days completed | ___ / 7 |
| Part 1 | ___ / 8 |
| Part 2 | ___ / 4 |
| Day 84 retrieval | ___ / 8 |
| Retention boxes | ___ / 7 |
| **Project 3 built** | ☐ |
| Honest hours | ___ h |
| **Biggest win** | |
| **Biggest gap** | |

---

**[← Day 84](./Day_84/Day_84.md)** · **[Day 85 →](../Week_13/Day_85/Day_85.md)** · [README](../../README.md)
