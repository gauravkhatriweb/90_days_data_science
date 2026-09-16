# Week 10 Review — Project 2 Shipped, Linear Algebra Done

|  |  |
|:--|:--|
| **Covers** | Days 64–70 · 18–24 November 2026 |
| **Topics** | Recommendation memos · vectors · transformations · determinants · eigenvectors · ML framing |
| **Budget** | 45–60 min |
| **Milestone** | 🎉 **Project 2 shipped on Day 64** — two portfolio pieces |

---

## ⏸️ Catch-Up Rights

| Day | Done? | MUST DO only |
|:---:|:-----:|:-------------|
| 64 · P2 ship | ☐ | **The memo. Ship it.** |
| 65 · Vectors | ☐ | The span demo + the multicollinearity build |
| 66 · Transformations | ☐ | Read the columns + the collapse |
| 67 · Determinants, inverses | ☐ | **Exercise 10 — regression with `solve`** |
| 68 · Eigenvectors, PCA | ☐ | The PCA-from-covariance build |
| 69 · ML framing | ☐ | **The Project 3 brief.** Everything from Day 80 depends on it. |
| 70 · Consolidation | ☐ | The ten tasks |

---

## 📝 Part 1 — Knowledge (closed book, 15 min)

1. Why is the recommendation the title of a memo?
2. What is a row of your dataset, in linear-algebra terms?
3. Explain linear dependence geometrically, without saying "correlated".
4. What do the columns of a matrix tell you?
5. What does the determinant measure? What does `det = 0` mean?
6. State the four equivalent statements and why they are one idea.
7. What is an eigenvector, geometrically?
8. Why are the covariance matrix's eigenvectors the principal components?
9. Define machine learning in terms of vectors, matrices and optimisation.
10. What is data leakage? Give two forms and the test that catches both.

**Score: ___ / 10**

---

## 💻 Part 2 — Coding (closed book, 20 min)

**A — 6 min.** Fit a linear regression with `solve(X.T @ X, X.T @ y)` and verify against sklearn.
**B — 5 min.** Build a collinear feature matrix; show the determinant and condition number.
**C — 5 min.** PCA from the covariance matrix; report explained variance.
**D — 4 min.** Compute the regression and classification baselines on a dataset.

**Score: ___ / 4**

---

## 🧩 Part 3 — Problem Solving (open book, 10 min)

> You are handed a model that predicts late delivery with **98% accuracy**. The team is delighted.
>
> Write the five questions you would ask before believing it. For each, say what answer would worry you.

**98% is a bug report until proven otherwise.** This is the instinct Days 69 and 74 exist to build.

---

## 🔁 Part 4 — Retention Check

- [ ] I see a dataset as a cloud of points in feature-space
- [ ] I can read a matrix as "where the basis vectors land"
- [ ] I check `cond(X)` before interpreting a coefficient
- [ ] I use `solve`, never `inv @ b`
- [ ] I can explain PCA without matrices
- [ ] I compute a baseline before any model
- [ ] I apply the availability test to every feature
- [ ] I treat a suspiciously high score as a bug

> Weak this week: ______________________________________________

---

## 🎉 Part 5 — Project 2 Retrospective

| | |
|:--|:--|
| Shipped | ☐ |
| Reproduction tested | ☐ |
| Read-aloud test passed | ☐ |
| The prize quantified | ☐ |

**The 30-second pitch:**

> ______________________________________________

**What Project 2 proves that Project 1 does not:**

> ______________________________________________

**Two projects. Which would you lead with in an interview, and why?**

> ______________________________________________

---

## 📐 Part 6 — Mathematics

**Essential Math Chapter 4 complete?** ☐  ·  Exercise score: ___ / ___

| Concept | Explain it? | Where it returns |
|:--------|:-----------:|:-----------------|
| Vectors as observations | | Every model |
| Span, linear dependence | | **Day 73** — unstable coefficients |
| Matrices as transformations | | Day 66 → every `X @ W` |
| Determinant, rank, invertibility | | **Day 73** — why a fit fails |
| Solving `Ax = b` | | **Day 71** — the closed-form regression |
| Eigenvectors | | **Day 86** — PCA |
| Condition number | | Day 73 — whether to trust a coefficient |

**Chapters 1–4 done. Remaining: Ch. 5 (Days 71–73), Ch. 6 (Days 75–77), Ch. 8 (Day 89).**

---

## 🤖 Part 7 — Project 3 Scoping

Project 3 starts Day 80. **The brief was Day 69's exercise 7.**

| | |
|:--|:--|
| Question chosen | ☐ |
| Target precisely defined | ☐ |
| Data identified and accessible | ☐ |
| Features listed, availability-tested | ☐ |
| Baseline known | ☐ |
| Worth stated in money or risk | ☐ |

**If any box is unticked, fix it this week, not on Day 80.** Ten days of ML study are much more useful when you know what you are going to build.

**My Project 3 question:**

> ______________________________________________

---

## 🎓 Part 8 — University

- Ten weeks of semester in. Final exams come after Day 90 — when does revision start?
- **Days 80–85 are Project 3.** If December coursework will collide, plan it now.
- Budget holding? ☐

---

## 🔮 Part 9 — The Decision

| If… | Then… |
|:----|:------|
| Part 1 ≥ 7, Day 70 ≥ 7, P3 scoped | ✅ Continue. Regression starts Day 71. |
| Day 70 < 7 | ⚠️ Rewatch the four 3Blue1Brown chapters in Week 11's IF TIME — 50 minutes, high return. |
| P3 not scoped | 🛑 **Scope it this week.** Do not arrive at Day 80 undecided. |
| Behind overall | 🔧 Follow the Month 2 Review's cut order: protect Project 3 and the evaluation days (74, 76, 77). Cut trees and PCA first. |

**My decision:**

> ______________________________________________

---

## 📊 Week 10 Scorecard

| Measure | Result |
|:--------|:-------|
| Days completed | ___ / 7 |
| Part 1 | ___ / 10 |
| Part 2 | ___ / 4 |
| Day 70 retrieval | ___ / 10 |
| Retention boxes | ___ / 8 |
| Ch. 4 exercises | ___ / ___ |
| **Project 2 shipped** | ☐ |
| **Project 3 scoped** | ☐ |
| Honest hours | ___ h |
| **Biggest win** | |
| **Biggest gap** | |

---

**[← Day 70](./Day_70/Day_70.md)** · **[Day 71 →](../Week_11/Day_71/Day_71.md)** · [README](../../README.md)
