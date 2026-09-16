# Day 57 — Metric Design Workbook

> No code today. The work is thinking clearly and writing precisely.

---

## 1. Ten bad metrics

Real ones — from your LifeOS dashboards, a product you use, a news article.

| # | The metric | Where I saw it | What is wrong | How I would fix it |
|:-:|:-----------|:---------------|:--------------|:-------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |

---

## 2. Five fixed definitions

Precise enough that two analysts working independently get the same number.

**Metric 1**
- Formula:
- Time window:
- Who is included:
- Who is excluded, and why:
- Edge cases *(refunds, test accounts, same-day repeats)*:
- Guardrail metric:

*(repeat for 2–5)*

---

## 3. KPI tree — a kiryana shop using SwiftBase

Start from a real goal. Break down until every leaf is a query.

```text
GOAL:
├──
│   ├──            <- queryable?
│   └──            <- queryable?
├──
│   ├──
│   └──
└──
    ├──
    └──
```

**Which leaves could I actually compute from SwiftBase's data?**

**Which would need data that does not exist yet?** *(That is a product requirement, and noticing it is a contribution.)*

---

## 4. Five precise metrics for that shop

| Metric | Formula | Window | Guardrail | Why it is actionable |
|:-------|:--------|:-------|:----------|:---------------------|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

---

## 5. A leading indicator

**The lagging outcome:** the shop is still using SwiftBase in six months.

**My hypothesis — the early behaviour that predicts it:**

>

**Why I believe it:**

>

**How I would test it:**

>

**What would falsify it:**

>

---

## 6. Goodhart's test

For three metrics: how would a motivated person game it? Then redesign.

| Metric | How it gets gamed | Redesigned |
|:-------|:------------------|:-----------|
| | | |
| | | |
| | | |

**Did redesigning actually make gaming harder, or just less obvious?**

---

## 7. Project 1, rewritten as a decision

**FINDING** — what the data says

>

**SO WHAT** — why it matters, in money or risk

>

**RECOMMENDATION** — what to do

>

**CONFIDENCE** — how sure, and what would change my mind

>

**COST** — what the recommendation takes

>

**Is this better than what is in my Project 1 README? Should I update it?**

---

## Mini assessment

*"I want more sales."*

| Metric | Formula | Guardrail |
|:-------|:--------|:----------|
| 1 | | |
| 2 | | |
| 3 | | |

**The one question I would ask them first:**

>

**Why that question and not another:**

>
