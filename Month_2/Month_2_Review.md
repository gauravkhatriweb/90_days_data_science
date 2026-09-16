# Month 2 Review — From Arrays to Answers

|  |  |
|:--|:--|
| **Covers** | Days 29–56 · 14 October – 10 November 2026 |
| **Phase** | NumPy · Pandas · cleaning · EDA · visualisation · **Project 1** · probability · statistics · SQL |
| **Budget** | ~90 min |
| **Milestone** | 🎉 Project 1 shipped on Day 45 |

> A capability audit. Every finding needs evidence. The month ends with a scope decision for Month 3 — which contains the final project and all the portfolio work.

---

## 📍 Part 1 — The Capability Test (25 min)

Not a quiz. A working session. **Open a dataset you have never used** — Kaggle, or a second PBS file you did not use in Project 1 — and give yourself 25 minutes to:

1. Load it and run the inspection ritual
2. Identify and diagnose the missing data
3. Fix the dtypes
4. Produce one grouped summary
5. Produce one chart with a finding-title
6. Compute one confidence interval
7. State one thing you cannot conclude from it

**This is the Month 2 exam.** If you can do all seven in 25 minutes, Month 2 worked.

| Step | Done? | Time |
|:--|:--:|:--|
| 1 · Load and inspect | ☐ | |
| 2 · Diagnose missing | ☐ | |
| 3 · Fix dtypes | ☐ | |
| 4 · Grouped summary | ☐ | |
| 5 · Chart with a finding | ☐ | |
| 6 · Confidence interval | ☐ | |
| 7 · A stated limitation | ☐ | |

**Score: ___ / 7 in 25 minutes**

---

## 🧠 Part 2 — Knowledge Audit

✅ can explain and use · 🟡 can use, cannot explain · ❌ neither

| Topic | Day | Status | Evidence |
|:------|:---:|:------:|:---------|
| Why arrays beat lists | 29 | | |
| View vs copy | 29 | | |
| Vectorisation, the axis rule | 30 | | |
| Broadcasting rules | 30 | | |
| NaN handling, boolean masks | 31 | | |
| DataFrames, index alignment, `loc`/`iloc` | 32 | | |
| Missing-data diagnosis (MCAR/MAR/MNAR) | 33 | | |
| Dtype coercion | 33 | | |
| `groupby` — `agg`/`transform`/`filter` | 34 | | |
| Joins, row-count discipline | 36 | | |
| Long vs wide, tidy data | 37 | | |
| Chart choice and readability | 38 | | |
| Seaborn, figure vs axes | 39 | | |
| **The EDA loop** | 40 | | |
| Outlier classification | 40 | | |
| Confounded correlation | 40 | | |
| Cleaning pipelines | 41 | | |
| The structure of a finding | 43 | | |
| **Probability: joint, union, conditional** | 46 | | |
| **Bayes and base rates** | 46 | | |
| Binomial vs beta | 47 | | |
| Population vs sample, `n−1` | 48 | | |
| Normal distribution, z-scores, `ppf` | 50 | | |
| **The Central Limit Theorem** | 51 | | |
| **Confidence intervals** | 52 | | |
| **P-values — and what they are not** | 53 | | |
| Test selection, Type I/II, power | 53 | | |
| t-distribution, Texas sharpshooter | 54 | | |
| SQL: joins, groups, windows, CTEs | 33–55 | | |

**🟡 count: ___** — the dangerous ones. Something you can use but cannot explain fails in an interview and in any situation slightly unlike the one you learned it in.

**The five in bold are load-bearing for Month 3.** If any is 🟡 or ❌, fix it in Week 9's IF TIME before machine learning starts.

---

## 💻 Part 3 — Practical Audit

| | Evidence |
|:--|:--|
| Clean a messy real dataset end to end | Project 1 pipeline runs? ☐ |
| Produce a defensible finding | Four-part finding written? ☐ |
| Build charts a stranger understands | Passed the ten-second test? ☐ |
| Write a reproducible project | Fresh-clone test passed? ☐ |
| Reason about uncertainty | CIs computed and interpreted? ☐ |
| Run and interpret a hypothesis test | Day 53 exercise 11? ☐ |
| Write multi-step SQL | Day 55 score: ___ / 5 |

**The honest question:** handed a new business question and a new dataset tomorrow, could you go from raw file to a written recommendation **without help**? **Yes / Mostly / No.**

---

## 📐 Part 4 — Mathematics Audit

Essential Math **Chapters 1, 2 and 3** — complete? ☐ ☐ ☐

| Concept | Explain it? | Where it returns |
|:--------|:-----------:|:-----------------|
| Bayes and base rates | | **Day 76** — precision with imbalanced classes |
| Beta / sample size and confidence | | Day 76 — accuracy needs an n |
| `n−1` and sample vs population | | Everywhere |
| Normal distribution, z-scores | | **Day 79** — `StandardScaler` |
| **Central Limit Theorem** | | Every interval and test you will ever run |
| Confidence intervals | | Day 76 — model metrics |
| P-values and their misuses | | Day 73 — coefficient significance |
| Power and sample size | | Any experiment |
| Texas sharpshooter | | **Day 74** — the reason for a held-out test set |

**Chapter exercise scores:** Ch. 2 ___ / ___ · Ch. 3 ___ / ___

**MAT 265 overlap so far:** ___% — is the maths track earning its time twice?

---

## 🎓 Part 5 — University Audit

| | |
|:--|:--|
| Mid-semester exams — done, upcoming, or unknown? | |
| **CSE 110** — ahead, level, or behind this plan? | |
| **MAT 265** — where is it now? | |
| **CIS 105** — overlap with visualisation and spreadsheets? | |
| Seven weeks of semester in — is the budget still holding? | |
| Days missed this month, and why | |

---

## 🛠️ Part 6 — Portfolio Audit

| Project | Status | Would you show it? |
|:--------|:-------|:-------------------|
| `shopsummary` (D12) | | No — a learning exercise |
| `lifelog` / P0 (D22–26) | | Shows design ability, not analysis |
| **Project 1** (D32–45) | | ☐ **Yes** |

**Project 1 retrospective, now that a few weeks have passed:**
- What still looks good:
- What now looks weak:
- Would you rewrite the README? What would change?

---

## 💼 Part 7 — Career Audit

Three specific, demonstrable things you can now claim:

> 1.
> 2.
> 3.

**The interview test.** Could you answer these right now?
- [ ] "Walk me through a data project you've built."
- [ ] "How do you handle missing data?"
- [ ] "What's a p-value?"
- [ ] "Write a query for the top 3 products per category."
- [ ] "How would you design an A/B test?"

**Any unticked box is a Month 3 practice item.** Day 89 drills all five.

---

## 🔮 Part 8 — Month 3 Decisions

Month 3 is Days 57–90: business metrics, **Project 2**, linear algebra, machine learning, **Project 3**, and the portfolio.

### A. The pace decision

| If Month 2 was… | Then Month 3… |
|:----------------|:--------------|
| **Comfortable. Part 1 ≥ 6/7, statistics solid** | As written. Consider adding depth to Project 3. |
| **Manageable. Part 1 4–5/7, some gaps** | As written, with IF TIME spent on the 🟡 topics. |
| **Hard. Statistics shaky** | ⚠️ **Spend Week 9's IF TIME re-reading Ch. 3, pp. 89–107.** The CLT, intervals and p-values are what make ML evaluation meaningful. |
| **Not sustainable** | 🔧 **Cut Project 2 to three days and protect Project 3.** One excellent ML project beats two rushed ones. |

**My pace decision:** ______________________________________________

### B. The scope decision — read this one carefully

Month 3 has two projects, four days of linear algebra and eleven days of machine learning in 34 days, minus two for the hackathon. **That is tight.** If anything must give, here is the order:

| Priority | Item | Why |
|:--------:|:-----|:----|
| 1 | **Project 3 + the portfolio pass** | This is what you can show anyone |
| 2 | **Validation, leakage, evaluation (D74, 76, 77)** | The part that separates real from tutorial |
| 3 | **Project 2** | Valuable, but cuttable to three days |
| 4 | Linear algebra depth (D65–68) | Compressible to two days with 3Blue1Brown only |
| 5 | Trees, k-means, PCA (D78, 86) | Nice to have. Cut first. |

**Cut from the bottom, never from the top.** A month that produces a strong Project 3 and honest evaluation skills beats one that covers more topics and ships nothing.

**My scope decision:** ______________________________________________

### C. Specific fixes

| Weakness | Fix | Which day's IF TIME |
|:---------|:----|:--------------------|
| | | |
| | | |
| | | |

### D. The one thing

If only one thing improves in Month 3:

> ______________________________________________

---

## 📊 Month 2 Scorecard

| Measure | Result |
|:--------|:-------|
| Days completed | ___ / 28 |
| Part 1 capability test | ___ / 7 in 25 min |
| Topics ✅ | ___ / 30 |
| Topics 🟡 (the risk) | ___ |
| Essential Math Ch. 1 ☐ Ch. 2 ☐ Ch. 3 ☐ | |
| Day 55 SQL interview problems | ___ / 5 |
| SQLBolt / pgexercises | ___ |
| **Project 1 shipped** | ☐ |
| Interview questions answerable | ___ / 5 |
| Total honest hours | ___ h |
| **Biggest win** | |
| **Biggest gap** | |
| **Am I on track for a real portfolio by Day 90?** | |

---

<div align="center">

**Month 1 made Python stop being the obstacle. Month 2 made data the subject.**
Month 3 is where it turns into evidence.

**[← Day 56](./Week_08/Day_56/Day_56.md)** · **[Day 57 →](../Month_3/Week_09/Day_57/Day_57.md)** · **[README](../README.md)**

</div>
