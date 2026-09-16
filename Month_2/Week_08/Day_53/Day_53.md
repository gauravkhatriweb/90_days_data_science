# Day 53 — P-Values and Hypothesis Testing

|  |  |
|:--|:--|
| **Date** | Saturday, 7 November 2026 |
| **Position** | Week 8 · Month 2 · Phase 3 |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_53.py` |
| **Reading** | 📐 **Essential Math Ch. 3, pp. 95–104** |

> **The most misunderstood concept in applied statistics.** A p-value is misdefined in most business meetings, most news articles, and a large fraction of published papers. Today's objective is not to be able to compute one — `scipy` does that — but to be able to **say what it is and is not**, which is a genuinely uncommon skill and one that gets noticed in interviews.

---

## 🎯 Objective

State correctly what a p-value is, run the right test for a question, and know the specific ways hypothesis testing is misused.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 3, pp. 95–104** | **PRIMARY** · reading + code | 45 min | P-values, hypothesis testing, the t-distribution |
| [StatQuest — Hypothesis Testing and the Null](https://www.youtube.com/watch?v=0oc49DyA3hU) | **REINFORCEMENT** | 10 min | The framing |
| [StatQuest — p-values: what they are](https://www.youtube.com/watch?v=vemZtEM63GY) | **REINFORCEMENT** | 12 min | The intuition |
| The misuse section below | REFERENCE | 20 min | **The part that matters most** |

---

## 🧠 Core Concepts

### The logic — proof by contradiction, with uncertainty

1. Assume nothing is happening — the **null hypothesis (H₀)**
2. Ask: **if that were true**, how likely is data at least as extreme as mine?
3. That likelihood is the **p-value**
4. If it is small enough, conclude the assumption is implausible

**Note what step 4 does not say.** You never prove the alternative. You only find the null implausible. It is the statistical form of "this would be a remarkable coincidence" — not "this proves my theory".

### The definition, precisely

> **A p-value is the probability of observing data at least as extreme as yours, *assuming the null hypothesis is true*.**

Every word of "assuming the null hypothesis is true" carries weight. The p-value is computed **inside a world where there is no effect**. That is why it cannot tell you the probability that there is one.

### What it is NOT — the five errors

| Wrong claim | Why |
|:------------|:----|
| "p = 0.03 means a 3% chance the null is true" | **`P(data \| H₀)` is not `P(H₀ \| data)`.** Day 46's disease test, exactly. |
| "p = 0.03 means a 97% chance my hypothesis is right" | Same confusion, restated |
| "p > 0.05 means there is no effect" | **Absence of evidence is not evidence of absence.** A small sample cannot detect a real effect. |
| "p = 0.001 means a large effect" | It means *detectable*. With 10 million rows, a meaningless difference gets p < 0.001. |
| "p = 0.049 and p = 0.051 are different findings" | 0.05 is a convention, chosen arbitrarily, and treating it as a cliff is the source of a great deal of bad science. |

**The fourth is the one that will affect your working life.** At large n, everything is "significant". **Statistical significance is not practical significance** — always report the effect size alongside the p-value, and let the reader judge whether it matters.

### Choosing a test

| Question | Test | `scipy` |
|:---------|:-----|:--------|
| One mean vs a claimed value | One-sample t | `ttest_1samp` |
| Two independent group means | Two-sample t | `ttest_ind` |
| Before and after, same subjects | **Paired** t | `ttest_rel` |
| Two proportions | Two-proportion z | `proportions_ztest` |
| Categorical association | Chi-square | `chi2_contingency` |
| Three or more group means | ANOVA | `f_oneway` |
| Non-normal, small sample | Mann-Whitney U | `mannwhitneyu` |

**The paired-versus-independent distinction is the one people get wrong.** Measuring the same 30 shops before and after a policy is *paired* — using the independent test throws away the pairing and makes it much harder to detect a real effect.

### Two errors, and the trade-off

| | Truth: no effect | Truth: effect exists |
|:--|:--|:--|
| **You say "effect"** | **Type I** — false positive (α) | correct |
| **You say "no effect"** | correct | **Type II** — false negative (β) |

α = 0.05 means you accept a 5% false-positive rate. **Lowering α raises β** — being more careful about false alarms means missing more real effects. There is no setting that avoids both, and choosing depends on which error is more costly. Screening for a treatable disease and deciding whether to repaint a website button should not use the same threshold.

**Power = 1 − β** is your ability to detect a real effect. It rises with sample size and with effect size. **An underpowered study that finds nothing has found nothing** — it has not shown there is nothing.

### One-tailed versus two-tailed

Two-tailed asks "is it different?"; one-tailed asks "is it bigger?" One-tailed has more power — and switching to it *after* seeing your data which way it went is a form of cheating that roughly doubles your false-positive rate. **Decide before you look.**

---

## 💻 Code

`Day_53.py` — eleven exercises.

**The logic (1–3)**
1. **Simulate the null.** Generate data with no real effect, run 10,000 tests, and plot the p-value distribution. **It is uniform.** Understanding why is understanding p-values.
2. From exercise 1: how many gave p < 0.05 when there was genuinely no effect? Is it 5%?
3. Now simulate a real effect. How does the p-value distribution change?

**Running tests (4–7)**
4. One-sample t-test: does your PBS data's mean differ from a claimed value?
5. Two-sample t-test on two groups from your data
6. **Paired vs independent on the same data.** Run both. **Which has the smaller p-value, and why?**
7. Chi-square on a contingency table from your data

**The misuses (8–10)**
8. **The large-n demonstration.** A difference of 0.1% between two groups. Test at n = 100, 1,000, 10,000, 1,000,000. **Watch p collapse while the effect stays trivial.** Report effect size alongside.
9. **P-hacking, live.** Test 20 random variables against an outcome with no real relationship. **Count the "significant" results.** You will find one.
10. **Power:** simulate a real effect of a fixed size. What sample size do you need for 80% power? What happens at half that?

**Applying it (11)**
11. Formulate and run one real test on your Project 1 data. Write: the hypotheses, the test chosen and why, the p-value, **the effect size**, and the conclusion in plain English.

---

## 🔬 Understanding Check

1. **Definition.** State what a p-value is, in one sentence, precisely.
2. **Reasoning.** Exercise 1: why is the p-value distribution uniform under the null? *(This is the deepest question today.)*
3. **Debugging.** A colleague says "p = 0.03, so there is a 3% chance we are wrong." Correct them in two sentences.
4. **Judgement.** Exercise 8: at n = 1,000,000 the p-value is tiny and the effect is 0.1%. What do you report?
5. **Reasoning.** Exercise 9: how many false positives did you find in 20 tests? What does that mean for someone who explores until something is significant?
6. **Application.** Exercise 6: which test had more power, and why?
7. **Judgement.** Your test returns p = 0.08 on n = 25. What can you conclude? What can you not?
8. **Interview.** "Explain a p-value to a non-technical stakeholder." 60 seconds, no jargon.

---

## 🎯 Expected Outcome

- [ ] Define a p-value correctly and spot the five misuses
- [ ] Choose the right test for a question
- [ ] Always report an effect size alongside a p-value
- [ ] Explain why p > 0.05 does not mean "no effect"

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 95–104 | 45 min |
| StatQuest ×2 | 22 min |
| The misuses | 20 min |
| Eleven exercises | 80 min |
| Daily review | 13 min |
| **Total** | **~180 min** |

---

## 🧪 Mini Assessment

Ten minutes, closed book. A manager reports: *"We tested 8 changes to the checkout. One increased conversion by 2% with p = 0.04. Let's ship it."*

Write your response. Address: the multiple comparisons, what p = 0.04 means here, what you would need to believe it, and what you would actually recommend.

---

## 🔁 Daily Review

1. Exercise 1: why is the null p-value distribution uniform? Can I explain it?
2. Exercise 9: how many false positives in 20 tests?
3. Exercise 8: at what n did a trivial difference become "significant"?
4. Can I explain a p-value in 60 seconds without jargon? Try it out loud.

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 95–104 read, both StatQuest videos watched
- [ ] The uniform null distribution simulated and understood
- [ ] Paired vs independent compared on the same data
- [ ] The large-n demonstration run, with effect sizes recorded
- [ ] The p-hacking demonstration run, false positives counted
- [ ] One real test on Project 1 data, fully written up
- [ ] Committed to git

---

**[← Day 52](../Day_52/Day_52.md)** · **[Day 54 →](../Day_54/Day_54.md)** · [README](../../../README.md)
