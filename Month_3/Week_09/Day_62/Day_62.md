# Day 62 — RFM Segmentation and the Funnel

|  |  |
|:--|:--|
| **Date** | Monday, 16 November 2026 |
| **Position** | Week 9 · Month 3 · Phase 4 |
| **Budget** | **~75 min** |
| **Code file** | `project_2/queries/02_rfm.sql`, `03_funnel.sql` |

> **Back from the hackathon. No catch-up.** Days 60–61 were planned zeros. Start here.
>
> **Why RFM and the funnel together.** They are the two most practically useful segmentations in retail, and they are opposite in nature: RFM sorts *people*, the funnel sorts *steps*. Both are one good query, and both produce something a business can act on the same week.

---

## 🎯 Objective

Segment customers by behaviour and find where the order journey breaks — both in SQL, both ending in something actionable.

---

## 📚 Learn (20 min)

### RFM

Three numbers per customer:

| | | Signals |
|:--|:--|:--|
| **R** — recency | Days since their last order | Are they still around? |
| **F** — frequency | How many orders | Is this a habit? |
| **M** — monetary | Total spent | How much are they worth? |

Score each 1–5 with `NTILE(5)`, then combine:

| Segment | Pattern | Action |
|:--------|:--------|:-------|
| **Champions** | R5 F5 M5 | Keep. Reward. Ask them why they stay. |
| **Loyal** | R4–5 F4–5 | Grow basket size |
| **At risk** | R1–2, F4–5, M4–5 | **Highest-value action.** Valuable customers who have gone quiet. |
| **New** | R5 F1 | Onboard well — this is where retention is won |
| **Hibernating** | R1 F1 M1 | Cheap to ignore |
| **Big spender, one purchase** | R?, F1, M5 | Why did they not come back? |

**"At risk" is the segment that pays for the analysis.** Losing a customer who has bought five times costs far more than failing to convert a browser, and they are identifiable *before* they are gone — which is what makes RFM actionable rather than descriptive.

**Why `NTILE` rather than fixed thresholds:** quintiles adapt to your data. "Spent over PKR 10,000" stops meaning anything after a year of inflation; "top 20% of spenders" does not.

**The one reversal to get right:** for recency, **lower is better**. Sort ascending for R and descending for F and M, or your champions will be your hibernators.

### The funnel

Count how many orders reach each stage, and where they stop.

```
placed → approved → shipped → delivered
                 └→ cancelled / unavailable
```

```sql
SELECT
    COUNT(*)                                                          AS placed,
    SUM(CASE WHEN order_approved_at IS NOT NULL THEN 1 ELSE 0 END)    AS approved,
    SUM(CASE WHEN order_delivered_carrier_date IS NOT NULL THEN 1 ELSE 0 END) AS shipped,
    SUM(CASE WHEN order_delivered_customer_date IS NOT NULL THEN 1 ELSE 0 END) AS delivered
FROM orders;
```

**Two things that make a funnel useful rather than decorative:**

1. **The step conversion rate, not just the total.** Losing 40% between approved and shipped is a different problem from losing 40% between placed and approved, and they belong to different teams.
2. **Segment it.** A funnel for everyone is an average. The same funnel split by state, category, or seller size shows you *where* the problem is — and that is the difference between "we lose 12%" and "we lose 12%, and almost all of it is one region".

**Beware survivorship in a funnel:** an order placed yesterday has not had time to be delivered. Restrict to orders old enough to have completed the journey, or your last month will look catastrophic.

---

## 💻 Code

### 🔴 MUST DO — RFM (35 min)

1. Compute R, F and M per `customer_unique_id`
2. `NTILE(5)` each — **watch the recency reversal**
3. Combine into a three-digit RFM score
4. Map scores to named segments with `CASE`
5. Count customers and total revenue per segment
6. **Sanity-check:** do the segment revenue shares look plausible? Do champions hold a disproportionate share? *(They should — if not, something is reversed.)*
7. **Find the "at risk" customers.** How many, and how much revenue do they represent? **That number is the business case for the whole analysis.**

### 🔴 MUST DO — the funnel (25 min)

8. Overall counts at each stage
9. **Step-to-step conversion rates**, not just totals
10. Exclude orders too recent to have completed
11. Segment the funnel by one dimension — state, category, or seller
12. **Find the worst-performing segment at the worst step.** That is the finding.

### 🟢 IF TIME

- Cross the two: what does the funnel look like for champions versus new customers?

---

## 🔬 Understanding Check

1. **Reasoning.** Why `NTILE` rather than fixed thresholds?
2. **Debugging.** Your champions have the worst recency. What went wrong?
3. **Business.** Exercise 7: how much revenue is "at risk"? What would you recommend, and what would it cost?
4. **Reasoning.** Why segment a funnel? What does the aggregate hide?
5. **Judgement.** Why exclude recent orders from a funnel? What would including them do to your conclusion?
6. **Application.** Which single segment would you act on first, and why that one?
7. **Interview.** "How would you segment our customers?" 60 seconds, with RFM and why it is actionable.

---

## 🎯 Expected Outcome

- [ ] A working RFM segmentation with named segments and revenue per segment
- [ ] A funnel with step-to-step rates, correctly time-restricted
- [ ] A segmented funnel showing where the problem actually is
- [ ] A quantified business case for one recommendation

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| RFM and funnel concepts | 20 min |
| RFM (1–7) | 30 min |
| Funnel (8–12) | 20 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

One sentence with a number: **"There are ___ at-risk customers representing PKR ___ of historical revenue, and they have not ordered in ___ days."**

That sentence is a business case. Everything else today was the work to earn it.

---

## 🔁 Daily Review

1. Did I hit the recency reversal?
2. How much revenue is at risk?
3. Which funnel segment is worst, and at which step?
4. Project 2 ships in two days. What is left?

---

## 📦 Completion Criteria

- [ ] RFM working, with named segments
- [ ] Revenue per segment, sanity-checked
- [ ] The at-risk number computed
- [ ] Funnel with step rates and a time restriction
- [ ] Funnel segmented, worst segment identified
- [ ] Committed to git

---

**[← Day 61](../Day_61/Day_61.md)** · **[Day 63 →](../Day_63/Day_63.md)** · [README](../../../README.md)
