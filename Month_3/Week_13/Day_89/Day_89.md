# Day 89 — Can You Explain It?

|  |  |
|:--|:--|
| **Date** | Sunday, 13 December 2026 |
| **Position** | Week 13 · Month 3 · Phase 7 |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_89.py` |
| **Reading** | 📐 **Essential Math Ch. 8 — Career Advice and the Path Forward** |

> **Ninety days of building, and today is the first day about explaining.** That ordering is deliberate: interview preparation without skills is theatre. You now have the skills, and the gap between knowing something and being able to say it under mild pressure is real and closes with practice.
>
> **You are not applying for jobs yet** — you are a first-semester undergraduate, and applications are a 2027 activity. Today exists to find out **what you can and cannot explain**, which tells you what the next ninety days should contain.

---

## 🎯 Objective

Test whether you can explain what you know, out loud, without notes — and finish Essential Math with its career chapter.

---

## 📚 Learn — Essential Math Chapter 8 (40 min)

**Read pp. 257–285.** Nield's closing chapter is unusually honest about the field, and worth reading properly rather than skimming.

**The parts that matter for you:**

| Section | Why |
|:--------|:----|
| **Redefining Data Science** | The title means different things at different companies — which is why job descriptions vary so wildly |
| **Finding Your Edge — SQL Proficiency** | He puts SQL first, which is the same conclusion this plan reached from job postings |
| **Programming Proficiency** | Writing software, not just scripts — which is why `src/` and tests mattered on Day 88 |
| **Knowing Your Industry** | **Domain knowledge is a differentiator.** Pakistani retail and SME operations is a domain you genuinely know. |
| **Practitioner vs Advisor** | Two different career shapes. Worth knowing which you are drawn to. |
| **What to Watch Out For** | Role definition, organisational buy-in, unrealistic objectives — read this before your first internship, not after |

**Write three things this chapter told you that you did not already believe.** If there are none, you skimmed it.

---

## 💻 The Work

### 🔴 MUST DO — the explanation drills (60 min)

**Out loud. Timed. No notes.** Record yourself if you can — hearing your own hesitation is diagnostic in a way that self-assessment is not.

**Round 1 — concepts (30 min, 90 seconds each)**

| # | Question |
|:-:|:---------|
| 1 | What is a p-value? Explain to a non-technical manager. |
| 2 | Why does a train–test split matter? |
| 3 | What is data leakage? Give an example you have built. |
| 4 | Explain overfitting using something other than a model. |
| 5 | Why is accuracy a bad metric? When is it fine? |
| 6 | Difference between correlation and causation — with an example from your own work. |
| 7 | How would you handle missing data? |
| 8 | What is the Central Limit Theorem, and why does it matter? |
| 9 | Explain gradient descent to someone who knows what a slope is. |
| 10 | When would you use a linear model over a random forest? |

**Round 2 — your projects (20 min, 2 minutes each)**

| # | Question |
|:-:|:---------|
| 11 | Walk me through Project 1. |
| 12 | Walk me through Project 3. What would you do differently? |
| 13 | Tell me about a bug that took a long time to find. |
| 14 | Tell me about something you got wrong. |

**Question 14 is the one people fail.** Not because they have nothing, but because they try to make the answer flattering. A real mistake, described plainly, with what you changed, is a strong answer.

**Round 3 — cases (10 min)**

15. *"Our conversion rate dropped 15% last month. How would you investigate?"*
16. *"How would you design an A/B test for a new checkout flow?"*

### 🔴 MUST DO — technical drills (60 min)

**SQL — 25 min, closed book, timed.** The Day 55 patterns, on new data:
- Top N per group · period-on-period change · running total · cohort month index · the gap pattern · deduplicate keeping latest

**Python — 20 min, closed book:**
- Group and aggregate a list of dicts, no libraries
- A class with a cached property and a mutator that invalidates it
- Clean a messy column with `.str` methods
- `groupby().agg()` with named outputs and a `transform`

**Statistics and ML — 15 min, written:**
- Compute a confidence interval and interpret it correctly
- Read a confusion matrix and choose a metric for a stated cost structure
- Explain what a coefficient means, correctly
- Name four leakage forms

### 🔴 MUST DO — the honest audit (20 min)

17. **Score each drill.** Where did you hesitate? Where did you get it wrong?
18. **List every question you could not answer well.** That list is the next ninety days' input.
19. **Search five real job postings** — data analyst or data science intern, Pakistan or remote. For each: which requirements can you meet now, and which cannot you? **Be honest; this is calibration, not judgement.**

---

## 🔬 Understanding Check

1. **Self-assessment.** Which three concept questions were weakest?
2. **Projects.** Could you talk about Project 3 for two minutes without hesitating?
3. **Honesty.** What was your answer to "tell me about something you got wrong"? Was it a real mistake?
4. **SQL.** How many of the six patterns did you write inside the time?
5. **Calibration.** From the five job postings — what fraction of requirements can you meet now?
6. **Direction.** Nield's practitioner-versus-advisor distinction — which are you drawn to, and what does that change?
7. **Domain.** What domain do you know that most data scientists do not?

---

## 🎯 Expected Outcome

- [ ] Every concept explained out loud, timed
- [ ] Both projects narrated in two minutes each
- [ ] SQL and Python drills under time
- [ ] A specific list of what you cannot yet explain
- [ ] **Essential Math complete** *(Chapters 1–6 and 8)*

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math Ch. 8 | 40 min |
| Explanation drills | 60 min |
| Technical drills | 60 min |
| The honest audit | 20 min |
| **Total** | **~180 min** |

---

## 🧪 Mini Assessment

**Two minutes on Project 3**, out loud, to a real person: the question, the approach, the result, the limitation, what you would do differently.

**If they ask a follow-up you cannot answer, that is the assessment result** — and it is more useful than the two minutes.

---

## 🔁 Daily Review

1. Three weakest concept questions.
2. What I said to "tell me about something you got wrong". Was it honest?
3. SQL patterns inside time: ___ / 6.
4. From five job postings: what I can meet, and what I cannot.
5. **Essential Math is finished.** Which chapter changed the most about how I work?

---

## 📦 Completion Criteria

- [ ] Essential Math Chapter 8 read, three new things written down
- [ ] Sixteen explanation drills done out loud and timed
- [ ] SQL, Python and statistics drills completed closed-book
- [ ] Every drill scored
- [ ] **The "cannot explain" list written** — this is Day 90's input
- [ ] Five real job postings read and assessed
- [ ] Committed to git

---

**[← Day 88](../Day_88/Day_88.md)** · **[Day 90 →](../Day_90/Day_90.md)** · [README](../../../README.md)
