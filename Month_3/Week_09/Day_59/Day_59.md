# Day 59 — Cohort Retention

|  |  |
|:--|:--|
| **Date** | Friday, 13 November 2026 |
| **Position** | Week 9 · Month 3 · Phase 4 |
| **Budget** | **~75 min** |
| **Code file** | `project_2/queries/01_cohort_retention.sql` |
| **Note** | ⚠️ **Last working day before the hackathon.** Finish at a clean stopping point. |

> **Why cohort retention first.** It is the most valuable analytics question there is — *"do the customers we win stay?"* — and it is the hardest of the three to write, so it goes where you have the most energy. It is also the question most often asked in analytics interviews, and one most candidates cannot write under pressure.
>
> **Finish something today.** Days 60–61 are the hackathon. Leaving a half-written query to return to on Monday wastes the Monday warming up. Get one query working and one finding written down.

---

## 🎯 Objective

Build a cohort retention table in SQL and read what it says about the business.

---

## 📚 Learn — cohort analysis (20 min)

### The idea

Group customers by **when they first appeared**, then track each group forward. The cohort is fixed at entry and never changes.

|  Cohort | Size | M0 | M1 | M2 | M3 |
|:--------|-----:|---:|---:|---:|---:|
| 2017-01 | 1,240 | 100% | 18% | 11% | 8% |
| 2017-02 | 1,580 | 100% | 22% | 14% | 10% |
| 2017-03 | 1,890 | 100% | 24% | 16% | — |

**Read it two ways:**

- **Across a row** — how fast does a cohort decay? Where does the drop-off flatten?
- **Down a column** — is the business getting better at retaining? A rising M1 column means recent cohorts stay longer, which is the single best sign a product is improving.

**Why aggregate retention hides this.** "Overall repeat-purchase rate is 12%" mixes a cohort acquired last month with one acquired two years ago. If you are growing, the newest cohort dominates the average and makes retention look worse than it is. **Cohorts are the fix for that confound** — the same reasoning as Day 40's detrending.

### The construction

```sql
WITH first_order AS (
    SELECT customer_unique_id,
           MIN(DATE(order_purchase_timestamp)) AS first_date
    FROM orders o JOIN customers c USING (customer_id)
    WHERE order_status = 'delivered'
    GROUP BY customer_unique_id
),
activity AS (
    SELECT f.customer_unique_id,
           strftime('%Y-%m', f.first_date) AS cohort,
           (strftime('%Y', o.order_purchase_timestamp) - strftime('%Y', f.first_date)) * 12
         + (strftime('%m', o.order_purchase_timestamp) - strftime('%m', f.first_date)) AS month_index
    FROM first_order f
    JOIN customers c USING (customer_unique_id)
    JOIN orders o    USING (customer_id)
    WHERE o.order_status = 'delivered'
)
SELECT cohort,
       month_index,
       COUNT(DISTINCT customer_unique_id) AS customers
FROM activity
GROUP BY cohort, month_index
ORDER BY cohort, month_index;
```

Then divide each row by its `month_index = 0` value to get percentages.

### The five decisions that change the answer

| Decision | Options | Why it matters |
|:---------|:--------|:---------------|
| What counts as "active" | Any order · a delivered order · an order above a threshold | Changes every number |
| Which customer id | `customer_id` or `customer_unique_id` | **In Olist, `customer_id` is per-order.** Using it makes retention look like zero. |
| Period | Month, week, quarter | Monthly for most retail |
| Incomplete cohorts | Include or exclude | The newest cohort has no M3 yet — showing it as 0% is a lie |
| Cancelled orders | Include or exclude | Must match your revenue definition |

**Write all five down before you run the query.** Two analysts making different choices get different retention curves for the same business — which is why "our retention is 22%" means nothing without the definitions.

**The `customer_unique_id` point is the specific trap in this dataset**, and getting it wrong produces a retention table of all zeros. If your first result looks like that, this is why.

---

## 💻 Code

### 🔴 MUST DO (50 min)

1. **Write the five decisions down first**, with reasons, in `NOTES.md`
2. Build a `first_order` CTE
3. Compute the month index from first purchase
4. Produce the cohort table as counts
5. Convert to percentages
6. **Sanity-check it:** does the M0 column sum to your total customer count? Does every row start at 100%?
7. **Exclude incomplete cohorts** — and say in a comment which ones and why
8. Export to Pandas and produce a readable heatmap
9. **Write three findings** — one from reading across, one from reading down, one you did not expect

### 🟢 IF TIME

- Revenue retention as well as customer retention. Do they tell the same story? *(They often do not, and the difference is interesting.)*

---

## 🔬 Understanding Check

1. **Reasoning.** Why does aggregate retention mislead in a growing business? Connect it to Day 40's confounding.
2. **Debugging.** Your retention table is all zeros after M0. What is the most likely cause in this dataset?
3. **Judgement.** Which of the five decisions would change your headline number the most?
4. **Application.** Reading down the M1 column — is this business improving? What else would you check before saying so?
5. **Reasoning.** Why must incomplete cohorts be excluded rather than shown as 0%?
6. **Business.** Your M1 retention is 18%. Is that good? **What would you need to know to answer?**
7. **Interview.** "How would you measure whether our customers are sticking around?" 60 seconds.

---

## 🎯 Expected Outcome

- [ ] A working cohort retention table in SQL
- [ ] The five definitional decisions written down with reasons
- [ ] A readable heatmap
- [ ] Three findings, one of them unexpected

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Cohort analysis concepts | 20 min |
| Build and verify the query | 40 min |
| Heatmap and findings | 10 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

The query runs, M0 is 100% for every cohort, incomplete cohorts are excluded, and **you can explain every number to someone who has not seen the data.**

---

## 🔁 Daily Review

1. Which of the five decisions did I have to think hardest about?
2. Did I hit the `customer_unique_id` trap?
3. My three findings — which was unexpected?
4. **Hackathon tomorrow.** Is this at a clean stopping point? Is the query committed and working?

---

## 📦 Completion Criteria

- [ ] Five decisions recorded with reasons **before** the query
- [ ] Cohort table working, as counts and percentages
- [ ] Sanity checks passed
- [ ] Incomplete cohorts excluded and documented
- [ ] Heatmap produced
- [ ] Three findings written
- [ ] **Committed** — leave nothing half-written over the weekend

---

**[← Day 58](../Day_58/Day_58.md)** · **[Day 60 →](../Day_60/Day_60.md)** · [README](../../../README.md)
