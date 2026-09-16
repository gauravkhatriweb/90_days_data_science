# Day 54 — Small Samples, Sharpshooters, and a Real A/B Test

|  |  |
|:--|:--|
| **Date** | Sunday, 8 November 2026 |
| **Position** | Week 8 · Month 2 · Phase 3 |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_54.py` |
| **Reading** | 📐 **Essential Math Ch. 3, pp. 104–107 + exercises** |

> **Chapter 3 finishes today**, and it finishes with the two things that make the difference between someone who runs tests and someone who can be trusted with the results: **handling small samples honestly**, and **recognising the Texas sharpshooter fallacy** — drawing the target after firing at the barn.
>
> Then you do the thing everything so far has been building towards: **a complete A/B test analysis, end to end, written up.** This is a genuine job task at almost every company with a product, and it is the most commonly asked case question in analytics interviews.

---

## 🎯 Objective

Handle small samples correctly, recognise conclusions drawn after the fact, and produce a complete, honest experiment analysis.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 3, pp. 104–107** | **PRIMARY** · reading | 20 min | The t-distribution · big data and the Texas sharpshooter |
| **Chapter 3 exercises, p. 107** | **PRACTICE** | 30 min | Answers in Appendix B |
| The sections below | REFERENCE | 20 min | The A/B framework |

---

## 🧠 Core Concepts

### The t-distribution — honesty about small samples

The normal distribution assumes you know σ. You do not — you estimated it from the same small sample you are testing.

**With a small sample, your σ estimate is itself uncertain**, and sometimes it comes out too small, which would make your interval look narrower than it should. The t-distribution has fatter tails to account for exactly that.

| n | t critical (95%) | z critical |
|:--:|:--:|:--:|
| 5 | 2.776 | 1.960 |
| 10 | 2.262 | 1.960 |
| 30 | 2.045 | 1.960 |
| 100 | 1.984 | 1.960 |
| ∞ | 1.960 | 1.960 |

At n=5 the t interval is **42% wider**. At n=100 the difference is 1%. **Use t by default** — it converges to z when n is large, so you lose nothing, and it protects you when n is small.

Degrees of freedom is `n − 1`, for the same reason as Day 48's divisor: one degree was spent estimating the mean.

### The Texas sharpshooter

> A man fires at a barn, then paints a target around the tightest cluster of holes and claims to be a marksman.

In analysis: **explore the data, find a pattern, then report it as though you had predicted it.**

| Form | What it looks like |
|:-----|:-------------------|
| **Subgroup hunting** | No overall effect, but "it worked for users aged 25–34 in Lahore on mobile" |
| **Outcome switching** | Measured conversion, it did not move, so you report time-on-site instead |
| **Flexible stopping** | Checking the test daily and stopping the moment p dips under 0.05 |
| **The garden of forking paths** | Hundreds of small analysis choices, each reasonable, all nudging towards the result you hoped for |

**None of these require dishonesty.** They happen to careful people who genuinely want to know the answer. That is what makes them dangerous.

**The defences:**
1. **Write down the hypothesis and the metric before looking.** In the file. With a date.
2. **Decide the sample size in advance** and do not peek.
3. **Correct for multiple comparisons** — Bonferroni divides α by the number of tests; crude but honest.
4. **Treat anything found by exploration as a hypothesis, not a finding.** It needs fresh data to become a result.

**Big data makes this worse, not better.** With millions of rows, some subgroup will always show a "significant" pattern. More data is not a defence against looking in more places.

### The A/B test framework

**Before**
1. One primary metric. Named, in writing.
2. The minimum effect worth detecting — *"a 1% lift would not justify the engineering cost; 3% would"*
3. Sample size, from a power calculation, **before starting**
4. How long it runs — at least one full week, to cover the weekly cycle
5. What would make you stop early — and it is not "p < 0.05"

**During**
6. Check the randomisation worked: are the groups balanced on things you did not manipulate?
7. **Do not peek at the result.** Every peek is another comparison.

**After**
8. Effect size with a confidence interval — **before** the p-value
9. The p-value, in context
10. Check the guardrail metrics did not get worse
11. A recommendation that includes cost, not just significance

**Step 8's ordering is not a formality.** "B converted 2.1% better, 95% CI [0.4%, 3.8%]" tells a decision-maker what they need. "p = 0.03" tells them nothing about whether it is worth doing.

### Simpson's paradox — worth twenty minutes of your life

A trend that appears in every subgroup can **reverse** when the groups are combined.

> A treatment has a higher success rate than the control among mild cases *and* among severe cases — yet a lower rate overall. This happens when the treatment group has more severe cases.

It is not a trick; it is arithmetic. **It means an aggregate number can be the opposite of the truth**, and the only defence is to check whether an important variable is distributed unevenly across your groups. Exercise 7 makes you build one.

---

## 💻 Code

`Day_54.py` — twelve exercises.

**The t-distribution (1–3)**
1. Plot t at df = 1, 5, 30, ∞ against the normal. Watch the tails converge.
2. Compare t and z intervals at n = 5, 10, 30, 100. Record the width difference.
3. **The cost of getting it wrong:** simulate small-sample intervals using z instead of t. **What is the real coverage?** *(It will not be 95%.)*

**The sharpshooter (4–7)**
4. **Subgroup hunting:** generate data with no effect, split it by five random variables, and hunt for a "significant" subgroup. **You will find one.**
5. Apply a Bonferroni correction to exercise 4. How many survive?
6. **Flexible stopping:** simulate checking daily and stopping at p < 0.05. **What is the false-positive rate?** *(Far above 5%.)*
7. **Build a Simpson's paradox** from scratch. Then find whether anything in your own data could produce one.

**The A/B test (8–12)**
8. Write the pre-registration: metric, minimum detectable effect, sample size, duration, stopping rule. **Before generating any data.**
9. Power calculation for your chosen effect size
10. Generate or use real data; check the groups are balanced
11. Analyse: effect size, CI, then p-value, then guardrails — **in that order**
12. **Write the recommendation.** One page. What you found, how confident you are, what it costs, what you recommend, and what would change your mind.

Exercise 12 is the deliverable. It is the artefact an analyst actually produces, and it is what an interview case question is asking for.

---

## 🔬 Understanding Check

1. **Reasoning.** Why does the t-distribution have fatter tails? What is it accounting for?
2. **Application.** Exercise 3: what was the actual coverage when you used z on small samples? What does that mean for a "95%" interval?
3. **Judgement.** Exercise 4: how many subgroups did you have to try before finding significance? Would you have noticed yourself doing this in real work?
4. **Reasoning.** Exercise 6: what was the false-positive rate with flexible stopping? Why does peeking inflate it?
5. **Understanding.** Explain Simpson's paradox to someone without statistics training, using a concrete example.
6. **Application.** Why report effect size and CI *before* the p-value?
7. **Judgement.** Your A/B test shows a 0.3% lift, p = 0.02, on 2 million users. Engineering cost is three weeks. What do you recommend?
8. **Interview.** "How would you design an A/B test for a new checkout flow?" Answer in 90 seconds using your framework.

---

## 🎯 Expected Outcome

- [ ] Use the t-distribution correctly and know why
- [ ] Recognise post-hoc pattern-finding in your own work and others'
- [ ] Run a complete experiment analysis in the right order
- [ ] Write a recommendation that a decision-maker could act on

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 104–107 | 20 min |
| The A/B framework + Simpson's | 20 min |
| Exercises 1–7 | 55 min |
| **The A/B analysis (8–12)** | 55 min |
| **Chapter 3 exercises + checking** | 30 min |
| **Total** | **~180 min** |

---

## 🧪 Mini Assessment

The one-page recommendation from exercise 12. It passes when someone non-technical could read it and make a decision, and when someone technical could not find an obvious hole.

---

## 🔁 Daily Review

1. Exercise 3: what was the real coverage of a "95%" z-interval on n=5?
2. Exercise 4: how many subgroups before I found significance?
3. Exercise 6: what was the false-positive rate with peeking?
4. **Chapter 3 is done.** Which concept from Days 46–54 do I most expect to forget, and where will it bite me?

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 104–107 read
- [ ] **Chapter 3 exercises complete and checked against Appendix B**
- [ ] The t-vs-z coverage simulation run
- [ ] Subgroup hunting and flexible stopping both demonstrated with rates
- [ ] A Simpson's paradox built from scratch
- [ ] A full A/B analysis with pre-registration written first
- [ ] The one-page recommendation written
- [ ] Committed to git

---

**[← Day 53](../Day_53/Day_53.md)** · **[Day 55 →](../Day_55/Day_55.md)** · [README](../../../README.md)
