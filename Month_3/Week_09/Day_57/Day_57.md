# Day 57 — Metrics: What to Measure, and Why It Is Hard

|  |  |
|:--|:--|
| **Date** | Wednesday, 11 November 2026 |
| **Position** | Week 9 · **Month 3 begins** · Phase 4 — Business analytics |
| **Budget** | **~75 min** |
| **Code file** | **None.** Today is thinking and writing. |

> **Why business analytics gets one day and not a month.** You said it yourself: you already have a business reading system, six business books, and a startup with a customer-discovery framework you wrote. **Business thinking is one of your strengths, not a gap.** Turning this challenge into an entrepreneurship curriculum would waste that.
>
> What you have *not* done is connect business thinking to data rigorously. So business analytics appears here as **one day of metric design**, and then as a lens applied to every project — Project 2 is entirely business analytics, and every project ends with a recommendation.
>
> **Today's real value:** most analysts can compute anything and cannot say what should be computed. That gap is where careers stall, and you are unusually well placed to close it.

---

## 🎯 Objective

Define metrics that survive contact with the people who will be measured by them, and build a KPI tree that connects a business goal to something you can query.

---

## 📚 Learn

### 🔴 MUST DO — read and then write

### What makes a metric bad

| Problem | Example | Why it fails |
|:--------|:--------|:-------------|
| **Vanity** | Total registered users | Only ever goes up. Tells you nothing. |
| **Gameable** | Tickets closed per agent | Agents close tickets without solving them |
| **Lagging only** | Quarterly revenue | You find out when it is too late to act |
| **Unactionable** | "Brand sentiment" | Nobody knows what to do differently on Monday |
| **Ambiguously defined** | "Active users" | Active how? Opened the app? Made a purchase? Over what window? |
| **Averaged over a mixture** | Average order value across all segments | A rise could mean rich customers spending more, or poor ones leaving |

**Goodhart's law:** *when a measure becomes a target, it ceases to be a good measure.* Any metric you set will be optimised — including in ways you did not intend. **Design metrics assuming someone will try to game them**, because someone will, usually without meaning to.

### What makes a metric good

1. **Actionable** — a named person can do something differently because of it
2. **Unambiguous** — two analysts computing it independently get the same number
3. **Ratio or rate, not a raw count** — revenue *per customer* survives growth; total revenue does not tell you whether anything improved
4. **Paired with a guardrail** — optimise conversion, watch refund rate; optimise speed, watch error rate
5. **Sensitive on a useful timescale** — if it only moves quarterly, it cannot guide weekly decisions

### Leading and lagging

| Lagging | Leading |
|:--------|:--------|
| Revenue, churn, profit | Trial signups, support tickets, time-to-first-order |
| What happened | What is about to happen |
| Cannot be influenced now | Can be influenced now |
| Easy to define | Hard to find, and requires a hypothesis |

**Finding a leading indicator is a genuine analytical contribution.** "Customers who do X in week 1 are three times more likely to still be here in month 6" is worth more than any dashboard — and it is a testable claim, which means it can be wrong, which is what makes it valuable.

### The KPI tree

Break a goal down until you reach something a query can return.

```
Increase monthly revenue
├── More customers
│   ├── More visitors           ← marketing
│   └── Better conversion       ← product
│       ├── Fewer cart abandons
│       └── Fewer failed payments
├── Higher spend per customer
│   ├── Larger basket
│   └── More frequent purchases
└── Better retention
    ├── Lower churn
    └── More reactivations
```

**Every leaf is a SQL query.** The tree is what makes an analysis relevant rather than merely correct — it connects "here is a number" to "here is why you should care".

**Build one for SwiftBase's target customer** in today's exercises. You know that domain better than any textbook example, and the tree will be better for it.

### The metrics you will meet everywhere

| Metric | Is | The trap |
|:-------|:---|:---------|
| **Conversion rate** | Completed ÷ started | Which start, and over what window? |
| **Churn** | Lost ÷ total at start | "Lost" needs a definition for a business with no subscription |
| **Retention (cohort)** | Still active after N periods | Only meaningful within a cohort |
| **AOV** | Revenue ÷ orders | Moves when the customer mix changes, not just when behaviour does |
| **CLV** | Expected total value per customer | Depends on a churn forecast — treat with suspicion |
| **CAC** | Acquisition spend ÷ new customers | Which costs count? |
| **RFM** | Recency, frequency, monetary | The most practical segmentation there is |

**Cohort retention and RFM are Project 2.** You will compute both in SQL from Day 58.

### Turning analysis into a decision

The structure that works:

> **Finding** — what the data says
> **So what** — why it matters, in money or risk
> **Recommendation** — what to do
> **Confidence** — how sure you are, and what would change your mind
> **Cost** — what the recommendation takes

**Most analysts stop at "finding".** The gap between finding and recommendation is where analysts become valued — and it is mostly a writing skill, which is something you already have.

---

## 💻 The Work

### 🔴 MUST DO — write, in `Day_57_metrics.md`

1. **Ten bad metrics.** Real ones you have seen — in your own LifeOS dashboards, in a product, in a news article. For each: what is wrong with it, and how you would fix it.
2. **Fix five of them.** Write the improved definition, unambiguously enough that two analysts would agree.
3. **A KPI tree for a SwiftBase customer** — a kiryana shop. Start from a real business goal. Break it down until every leaf is something you could query.
4. **Define five metrics precisely** for that shop. Each needs: the formula, the time window, the inclusion rule, the edge cases, and the guardrail metric that goes with it.
5. **Find a leading indicator.** For the goal "the shop is still using SwiftBase in six months", what early behaviour might predict it? State it as a testable hypothesis.
6. **Goodhart's test.** Take three of your metrics and describe exactly how a motivated person would game each one. Then redesign to make gaming harder.
7. **The recommendation exercise.** Take your Project 1 finding and rewrite it in the five-part structure: finding, so what, recommendation, confidence, cost.

Exercise 6 is the one that most improves your metrics, and exercise 7 is the one that most improves your Project 1 README.

---

## 🔬 Understanding Check

1. **Reasoning.** Why is a ratio usually better than a count?
2. **Application.** Exercise 6: how would someone game your best metric? Did redesigning it work?
3. **Judgement.** "Active users" is ambiguous. Write a definition two analysts would agree on — and say what your definition deliberately excludes.
4. **Reasoning.** Why is finding a leading indicator harder than measuring a lagging one? What do you need that you do not need for the lagging version?
5. **Application.** Average order value rose 12%. Name three completely different explanations, and say what you would check first.
6. **Understanding.** Why does every metric need a guardrail? Give an example where optimising one metric wrecked something else.
7. **Career.** What is the difference between an analyst who reports numbers and one who influences decisions? Answer using the five-part structure.

---

## 🎯 Expected Outcome

- [ ] Recognise a bad metric on sight and say what is wrong
- [ ] Define a metric unambiguously enough to be reproduced
- [ ] Build a KPI tree from a goal down to queryable leaves
- [ ] Write a finding as a decision, not as a number

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Read the sections above | 25 min |
| Exercises 1–5 | 30 min |
| Exercises 6–7 | 15 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Ten minutes. A shop owner says: *"I want more sales."*

Turn it into three specific, measurable, actionable metrics with guardrails — and **one question you would need to ask them before any of it means anything.**

That last part is the assessment. Analysts who ask it are the ones who get asked back.

---

## 🔁 Daily Review

1. Which bad metric was the hardest to fix, and why?
2. Exercise 6: how would someone game my best metric?
3. What leading indicator did I propose? How would I test it?
4. Did the five-part rewrite improve my Project 1 finding? Should the README change?

---

## 📦 Completion Criteria

- [ ] Ten bad metrics identified with fixes
- [ ] A complete KPI tree with queryable leaves
- [ ] Five metrics defined precisely, with guardrails
- [ ] A leading-indicator hypothesis written
- [ ] Three metrics gamed and redesigned
- [ ] The Project 1 finding rewritten as a recommendation
- [ ] Committed to git

---

**[← Month 2 Review](../../../Month_2/Month_2_Review.md)** · **[Day 58 →](../Day_58/Day_58.md)** · [README](../../../README.md)
