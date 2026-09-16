# Day 64 — Project 2: The Recommendation

|  |  |
|:--|:--|
| **Date** | Wednesday, 18 November 2026 |
| **Position** | Week 10 · Month 3 · Phase 4 |
| **Budget** | **~75 min** |
| **Code file** | `project_2/RECOMMENDATION.md` · `project_2/README.md` |
| **Project** | 🛒 **P2 ships today** |

> **No new analysis today.** If a question is unanswered, it stays unanswered — that is the scope decision from Day 63 taking effect. Today is the write-up, and the write-up is the deliverable.
>
> **Why this project's memo matters more than Project 1's README.** Project 1 was an analysis. Project 2 is an analysis *for someone* — its whole framing is a business that has to decide something. **That document is the thing that distinguishes an analyst from someone who writes queries**, and it is the artefact most missing from junior portfolios.

---

## 🎯 Objective

Turn queries into a decision document a non-technical person could act on, and ship the repository.

---

## 📚 Learn — the recommendation memo (15 min)

### The structure

```markdown
# One line: the recommendation itself

## The situation
Two sentences of context. Why are we looking at this?

## What the data shows
2–4 findings. Each with a number. Each with a comparison.

## What I recommend
The action. Specific enough to assign to someone.

## What it is worth
The size of the prize, in money or in risk.

## What I am not certain about
The limitations, and what would change the recommendation.

## What I would do next
The obvious follow-up question.
```

### Four rules

**1. The recommendation is the title.** Not "Customer Retention Analysis" — "Contact the 340 at-risk customers who represent 18% of historical revenue". Someone reading only the title should know what you are asking for.

**2. Numbers, always with a comparison.** "Retention is 22%" is a fact. "Month-1 retention is 22%, and it has fallen from 31% for cohorts a year ago" is a reason to act.

**3. Size the prize.** *"340 at-risk customers × PKR 4,200 average historical spend = PKR 1.4 million of at-risk revenue."* Even a rough number changes the conversation from "interesting" to "how much would it cost to keep them?"

**4. State what would change your mind.** This is the rule people skip, and it is the one that buys trust. *"If the at-risk group turns out to be mostly one-off gift purchasers, retention spend on them is wasted — the next thing to check is purchase context."*

### What not to do

| Do not | Because |
|:-------|:--------|
| Bury the finding in paragraph four | Nobody gets there |
| Include a chart because it is pretty | Every chart must earn its place |
| Recommend "further analysis" as the main action | That is a way of not deciding |
| Claim causation from observational data | **The most common credibility failure.** You have correlations. |
| Present five equal options | You are being paid for a view. Give one, with alternatives noted. |

---

## 💻 The Work

### 🔴 MUST DO — the memo (35 min)

1. Write the recommendation as the title
2. Two sentences of situation
3. Two to four findings, each with a number and a comparison
4. **One specific recommendation**, assignable to a person
5. **Size the prize** — do the arithmetic, however rough, and show it
6. The limitations — at least three, specific
7. What would change your mind
8. The obvious next question
9. **The read-aloud test:** read it to someone non-technical. Can they say what you are asking for, and why?

### 🔴 MUST DO — ship (25 min)

10. `README.md` — the finding, the data, the method, how to reproduce, the layout
11. Every query commented, with a header saying what question it answers
12. `schema.md` — tables, relationships, grains
13. Reproduction instructions: build the database, run the queries. **Test them.**
14. `.gitignore` the raw CSVs *(they are large)*, but `SOURCES.md` must say exactly how to get them
15. Check for absolute paths
16. Commit and push
17. Add to the career-pillar portfolio tracker

---

## 🔬 Understanding Check

1. **Communication.** Why is the recommendation the title?
2. **Judgement.** What is your prize number, and how rough is the arithmetic? Is it defensible?
3. **Reasoning.** Why does "what would change my mind" build trust rather than undermine it?
4. **Application.** Exercise 9: did your reader understand the ask? What did they misread?
5. **Honesty.** Name one causal claim you were tempted to make. What could you say instead that is true?
6. **Comparison.** Project 1 was an analysis; Project 2 is a decision document. Which was harder, and which do you think employers value more?
7. **Career.** In one sentence, what does Project 2 prove that Project 1 does not?

---

## 🎯 Expected Outcome

- [ ] A one-page memo a non-technical reader can act on
- [ ] A quantified business case
- [ ] A shipped, reproducible repository
- [ ] Two portfolio projects

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| The memo structure | 15 min |
| Write it (1–9) | 35 min |
| Ship (10–17) | 20 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

The read-aloud test. Read the memo to someone with no context. **They should be able to say what you are recommending and roughly what it is worth.** If they cannot, the structure is wrong, not their attention.

---

## 🔁 Daily Review

1. What did my reader misunderstand?
2. What is the prize number, and would I defend it in a meeting?
3. What causal claim did I want to make, and what did I write instead?
4. **Two projects shipped.** What does the second prove that the first did not?

---

## 📦 Completion Criteria

- [ ] `RECOMMENDATION.md` complete, with the recommendation as the title
- [ ] The business case quantified with visible arithmetic
- [ ] Three or more specific limitations
- [ ] "What would change my mind" written
- [ ] Read-aloud test done with a real person
- [ ] README, schema doc, commented queries
- [ ] Reproduction instructions tested
- [ ] **Project 2 shipped** 🎉

---

**[← Week 9 Review](../../Week_09/Week_09_Review.md)** · **[Day 65 →](../Day_65/Day_65.md)** · [README](../../../README.md)
