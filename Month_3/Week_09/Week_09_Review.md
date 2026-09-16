# Week 9 Review — Metrics, SQL Analytics, and a Hackathon

|  |  |
|:--|:--|
| **Covers** | Days 57–63 · 11–17 November 2026 |
| **Topics** | Metric design · KPI trees · cohort retention · RFM · funnels |
| **Budget** | 45 min — a short week |
| **Note** | ⚫ Days 60–61 were the NASA Space Apps hackathon — **planned zeros, not missed days** |

---

## ⏸️ Catch-Up Rights

| Day | Done? | MUST DO only |
|:---:|:-----:|:-------------|
| 57 · Metrics | ☐ | The KPI tree + five precise definitions |
| 58 · P2 setup | ☐ | Database + schema + three questions |
| 59 · Cohort retention | ☐ | The query working, five decisions recorded |
| 60–61 | ⚫ | **Nothing to catch up. Planned.** |
| 62 · RFM + funnel | ☐ | RFM segments + the at-risk number |
| 63 · Consolidation | ☐ | Six SQL patterns |

---

## 📝 Part 1 — Knowledge (closed book, 12 min)

1. Name four things that make a metric bad, with an example each.
2. What is Goodhart's law, and how do you design against it?
3. Why is a ratio usually better than a count?
4. Why does aggregate retention mislead in a growing business?
5. What are the five definitional decisions in a cohort analysis?
6. Why `NTILE` rather than fixed thresholds in RFM?
7. Which RFM segment is usually the most valuable to act on, and why?
8. Why must you exclude recent orders from a funnel?

**Score: ___ / 8**

---

## 💻 Part 2 — Coding (closed book, 20 min)

**A — 6 min.** A cohort month index from a first-purchase date.
**B — 5 min.** `NTILE(5)` scoring with the ordering correct for recency.
**C — 5 min.** Funnel step rates with conditional aggregation.
**D — 4 min.** Top 3 per group with `ROW_NUMBER` in a CTE.

**Score: ___ / 4**

---

## 🧩 Part 3 — Problem Solving (open book, 10 min)

> A shop owner says: *"Business is fine, revenue is flat."*
>
> Flat revenue could be: stable customers spending the same · losing customers but each spending more · gaining customers who spend less · a mix that hides both.
>
> Which analyses would tell them apart? Write the queries you would run, in order, and say what each result would rule out.

**This is the question cohort analysis exists to answer**, and it is a common interview case.

---

## 🔁 Part 4 — Retention Check

- [ ] I define a metric with a window, an inclusion rule and a guardrail
- [ ] I write the definitional decisions before running a cohort query
- [ ] I can write a window function without reference
- [ ] I check whether my NTILE ordering is reversed
- [ ] I segment a funnel rather than reporting the average
- [ ] I end an analysis with a recommendation, not a number

> Weak this week: ______________________________________________

---

## 🛒 Part 5 — Project 2 Status

| | |
|:--|:--|
| Database built, schema documented | ☐ |
| Questions answered | ___ / 3 |
| Queries readable and commented | ☐ |
| Business case quantified | ☐ |
| Ships tomorrow — realistic? | ☐ |

**The at-risk number:** ______________________________________________

**The one finding I would lead the memo with:**

> ______________________________________________

---

## 🚀 Part 6 — The Hackathon

1. What we built:
2. What I contributed:
3. **What I could not do:**
4. Is that gap covered by the remaining 27 days, or is it a 2027 item?

---

## 🎓 Part 7 — University

- Nine weeks of semester in. Budget holding? ☐
- Final exams start after Day 90 — is the December workload going to affect Days 78–90?
- **Plan it now.** Days 80–85 are Project 3, and that is the piece you most need to protect.

---

## 🔮 Part 8 — The Decision

**Week 10 is linear algebra**, then machine learning begins on Day 69.

| If… | Then… |
|:----|:------|
| Part 1 ≥ 6, P2 nearly done | ✅ Continue. |
| P2 behind | 🔧 Cut to two questions. Ship Day 64 regardless. |
| Statistics from Month 2 still shaky | ⚠️ **Re-read Ch. 3, pp. 89–107 in Week 10's IF TIME.** ML evaluation is statistics. |
| Very behind overall | 🔧 **Compress linear algebra to two days** (3Blue1Brown only, skip the EMDS computation) and give the days to Project 3. Follow the Month 2 Review's cut order. |

**My decision:**

> ______________________________________________

---

## 📊 Week 9 Scorecard

| Measure | Result |
|:--------|:-------|
| Days completed | ___ / 5 *(excluding the two planned zeros)* |
| Part 1 | ___ / 8 |
| Part 2 | ___ / 4 |
| SQL patterns (Day 63) | ___ / 6 |
| Retention boxes | ___ / 6 |
| Honest hours | ___ h |
| **Biggest win** | |
| **Biggest gap** | |

---

**[← Day 63](./Day_63/Day_63.md)** · **[Day 64 →](../Week_10/Day_64/Day_64.md)** · [README](../../README.md)
