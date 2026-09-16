# Day 35 — Consolidation: From Arrays to Tables

|  |  |
|:--|:--|
| **Date** | Tuesday, 20 October 2026 |
| **Position** | Week 5 · Month 2 · Phase 2 |
| **Budget** | **~60 min** |
| **Code file** | `Day_35.py` |
| **Also today** | ✍️ **[Week 5 Review](../Week_05_Review.md)** |

> Retrieval, not new material. Week 5 covered NumPy in three days and the core of Pandas in three more — a lot of API in a short time. Today checks what stuck before Week 6 adds joins, reshaping and visualisation on top of it.

---

## 🎯 Objective

Retrieve Days 29–34 from memory and find what has already faded.

---

## 💻 Code

### 🔴 MUST DO — the retrieval set (40 min)

`Day_35.py` — twelve tasks, **closed book**, 3 minutes each. Mark 0 / 0.5 / 1.

| # | From | Task |
|:-:|:-----|:-----|
| 1 | 29 | Why is an array faster than a list? *(Written answer, in memory terms.)* |
| 2 | 29 | Slice an array, modify the slice, and predict the original |
| 3 | 30 | State the axis rule and apply it to a `(4,6)` array |
| 4 | 30 | Predict whether `(3,4)` and `(3,)` broadcast, and fix it if not |
| 5 | 30 | Replace a loop-with-an-`if` with `np.where` |
| 6 | 31 | Compute a mean over data containing NaN, correctly |
| 7 | 31 | Compound boolean mask, correct precedence |
| 8 | 32 | The five-line inspection ritual, from memory |
| 9 | 32 | `loc` vs `iloc` — same selection both ways, and the slice-end difference |
| 10 | 33 | `to_numeric(errors="coerce")` and count what it caught |
| 11 | 34 | `groupby().agg()` with named outputs |
| 12 | 34 | `transform` to compare each row to its group's mean |

### 🔴 MUST DO — integration (15 min)

13. **One question, three tools.** *"What is the average price per item, for items seen more than 20 times?"* — answer it in pure Python (Day 12 style), Pandas, and SQL. Compare the line counts and say which you would choose for 1,000 rows, and for 50 million.

This is the most useful exercise of the week. Three tools, one question — and the differences between them become obvious rather than theoretical.

---

## 🔬 Understanding Check

1. **Integration.** You get a 500 MB CSV with mixed types, 5% missing values and inconsistent item names. Describe the full pipeline from load to grouped summary, naming the method at each step.
2. **Reasoning.** Which Week 5 concept will matter most for Project 1, and which least?
3. **Comparison.** Exercise 13: what did the three implementations reveal?
4. **Self-assessment.** Which task failed? That is next week's warm-up.

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Twelve retrieval tasks | 36 min |
| Integration exercise | 15 min |
| Score + notes | 9 min |
| **Total** | **~60 min** · then the Week 5 Review |

---

## 🔁 Daily Review

1. Score: ___ / 12. Weakest three?
2. Exercise 13: which tool felt most natural? Is that the right one for the job?
3. Is my Project 1 data in a state where Day 39's EDA can start?

---

## 📦 Completion Criteria

- [ ] Twelve tasks attempted closed-book and scored
- [ ] The three-tool comparison written with line counts
- [ ] **[Week 5 Review](../Week_05_Review.md) completed**
- [ ] Committed to git

---

**[← Day 34](../Day_34/Day_34.md)** · **[Week 5 Review →](../Week_05_Review.md)** · [README](../../../README.md)
