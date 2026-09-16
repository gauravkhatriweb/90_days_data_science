# Week 6 Review — Joins, Reshaping, Visualisation, EDA

|  |  |
|:--|:--|
| **Covers** | Days 36–42 · 21–27 October 2026 |
| **Topics** | Joins · long/wide · Matplotlib · Seaborn · the EDA method · cleaning pipelines · SQL subqueries |
| **Budget** | 45–60 min |

---

## ⏸️ Catch-Up Rights

| Day | Done? | MUST DO only |
|:---:|:-----:|:-------------|
| 36 · Joins | ☐ | Exercises 2, 5, 6 — row counts and `validate` |
| 37 · Reshaping | ☐ | Exercises 2, 3, 9 |
| 38 · Charts | ☐ | Charts 1, 3, 9, 10 |
| 39 · Seaborn + P1 first look | ☐ | **The project pass.** Everything after depends on it. |
| 40 · EDA method | ☐ | The loop, plus exercise 4 |
| 41 · Cleaning pipeline | ☐ | `clean()` running end to end |
| 42 · Consolidation | ☐ | The three-day test |

---

## 📝 Part 1 — Knowledge (closed book, 15 min)

1. Why is `left` the usual default join in analysis?
2. Your revenue doubled after a join. What happened, and what would have caught it?
3. When is long better than wide? Name two consumers of each.
4. Why is `pivot`'s duplicate error more useful than `pivot_table`'s silence?
5. Name three of the seven chart-readability rules, and say why each matters.
6. Why are dual y-axes dangerous?
7. Figure-level vs axes-level in Seaborn — what is the practical difference?
8. Why correlate percentage changes rather than price levels in an inflationary period?
9. Why does missing-value handling come last in a cleaning pipeline?
10. What makes a subquery correlated, and why is that usually slower?

**Score: ___ / 10**

---

## 💻 Part 2 — Coding (closed book, 20 min)

**A — 5 min.** Left join with `validate` and `indicator`; report matched and unmatched counts.
**B — 5 min.** Wide to long and back; verify nothing was lost.
**C — 5 min.** A chart meeting all seven readability rules, with an annotation.
**D — 5 min.** A cleaning step returning `(df, count)`, plus one test for the empty case.

**Score: ___ / 4**

---

## 🧩 Part 3 — Problem Solving (open book, 10 min)

> You are handed a dataset of 200 products across 3 years and asked: *"Which products should we stop stocking?"*
>
> Write the plan. What do you compute, what do you plot, what could mislead you, and **what would you need to know that is not in the data?**
>
> The last part is the exercise. A good analyst says what the data cannot answer.

---

## 🔁 Part 4 — Retention Check

- [ ] I predict and verify row counts on every join
- [ ] I use `validate=` by habit
- [ ] I can melt and pivot without looking it up
- [ ] I write the finding before drawing the chart
- [ ] I title charts with the finding, not the contents
- [ ] I predict before I compute
- [ ] I classify outliers rather than deleting them
- [ ] My cleaning is a module, not notebook cells

> Weak this week: ______________________________________________

---

## 📊 Part 5 — Project 1 Status

| | Status |
|:--|:--|
| Cleaning pipeline runs end to end | ☐ |
| `data/processed/` regenerable from scratch | ☐ |
| Question one answered with evidence | ☐ |
| Three charts worth keeping | ☐ |
| Outlier and missing-data decisions recorded with counts | ☐ |
| `NOTES.md` readable by someone who has not seen the data | ☐ |

**Scope after the Day 42 decision:** ______________________________________________

**The one-sentence conclusion, as it stands:**

> ______________________________________________

**Ships Day 45. Three working days left. Is that realistic?** ☐ Yes ☐ Narrow further

---

## 🗄️ Part 6 — SQL Track

| | |
|:--|:--|
| SQLBolt lessons | ___ / 18 |
| `JOIN` from memory | ☐ |
| `GROUP BY` + `HAVING` from memory | ☐ |
| Subqueries from memory | ☐ |
| `LEFT JOIN … IS NULL` pattern | ☐ |

Next up: window functions on Day 52, then the SQL deep day on Day 55 and Project 2 from Day 58.

---

## 🎓 Part 7 — University

- Mid-semester exams: dates known yet? If so, mark them and pick the review day to convert into a pause.
- **CIS 105** overlaps this week's visualisation material. Anything transferable in either direction?
- Budget holding? ☐

---

## 🔮 Part 8 — The Decision

| If… | Then… |
|:----|:------|
| Part 1 ≥ 7, project on track | ✅ Continue. Statistics begins Day 46. |
| Project behind | 🔧 Narrow it. Days 43–45 hold; cut questions, not quality. |
| Part 2 ≤ 2 | ⚠️ Add a 15-minute Pandas warm-up to Days 43–45. |
| Exams landing in Weeks 7–8 | 🛑 **Plan the pause now.** Statistics is the worst block to do distracted — it is the one that needs attention. Push it rather than skim it. |

**My decision:**

> ______________________________________________

---

## 📊 Week 6 Scorecard

| Measure | Result |
|:--------|:-------|
| Days completed | ___ / 7 |
| Part 1 | ___ / 10 |
| Part 2 | ___ / 4 |
| Day 42 retrieval | ___ / 10 |
| Retention boxes | ___ / 8 |
| P1 on track | ☐ |
| Honest hours | ___ h |
| **Biggest weakness** | |
| **Biggest win** | |

---

**[← Day 42](./Day_42/Day_42.md)** · **[Day 43 →](../Week_07/Day_43/Day_43.md)** · [README](../../README.md)
