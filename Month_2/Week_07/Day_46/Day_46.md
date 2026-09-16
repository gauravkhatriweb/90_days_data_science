# Day 46 — Probability: Reasoning Under Uncertainty

|  |  |
|:--|:--|
| **Date** | Saturday, 31 October 2026 |
| **Position** | Week 7 · Month 2 · **Phase 3 — Statistics begins** |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_46.py` |
| **Reading** | 📐 **Essential Math Ch. 2, pp. 41–51** |

> **Why statistics comes before machine learning here, and not after.** Every roadmap in `Tem.txt` teaches `.fit()` first and statistics later, if at all. That order produces people who can train a model and cannot tell a good one from a lucky one. **A model's accuracy is a sample statistic**, and a sample statistic without an understanding of sampling variation is a number you cannot interpret.
>
> So: probability today, statistics through Day 54, and machine learning from Day 69 — by which point you will be able to ask "is that difference real?" rather than "is that number big?"
>
> Project 1 shipped yesterday. Month 2's second half is the part that makes Month 3 possible.

---

## 🎯 Objective

Reason correctly about probability — especially conditional probability, which is where nearly everyone's intuition fails.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 2, pp. 41–51** | **PRIMARY** · reading + code | 55 min | Probability vs statistics · joint · union · conditional · Bayes |
| The sections below | REFERENCE | 20 min | The intuition failures specifically |

### 🟢 IF TIME

- [StatQuest — Bayes' Theorem](https://www.youtube.com/results?search_query=statquest+bayes+theorem) · ~15 min, if Nield's treatment did not land.

---

## 🧠 Core Concepts

### Probability and statistics are opposite directions

| | Starts from | Asks |
|:--|:--|:--|
| **Probability** | A known model | What data would it produce? |
| **Statistics** | Observed data | What model could have produced it? |

Nield makes this distinction early because everything from Day 48 onward is the *statistics* direction — and it is harder, because the answer is never certain.

### The four operations

```
P(A)              probability of A
P(A and B)        JOINT     -- both happen
P(A or B)         UNION     -- at least one
P(A | B)          CONDITIONAL -- A, given that B happened
```

```
P(A and B) = P(A) × P(B)           if INDEPENDENT
P(A and B) = P(A|B) × P(B)         always
P(A or B)  = P(A) + P(B) − P(A and B)
```

**The subtraction in the union rule** is there because adding the two probabilities double-counts the overlap. Forgetting it is the most common arithmetic error in introductory probability, and it is also why "probability of at least one" problems are often easier as `1 − P(none)`.

### Conditional probability — where intuition fails

**`P(A|B)` and `P(B|A)` are not the same thing**, and confusing them is the single most consequential error in applied statistics.

- `P(positive test | has disease)` = 99% — the test is good
- `P(has disease | positive test)` = **maybe 9%** — depends entirely on how rare the disease is

Same test, wildly different numbers. The second is the one a patient cares about, and it is the one people get wrong.

### Bayes' theorem — the correction for base rates

```
P(A|B) = P(B|A) × P(A) / P(B)
```

Worked, with numbers, because the abstract form does not convince anyone:

> A disease affects **0.1%** of people. A test catches **99%** of those who have it, and gives a false positive **1%** of the time. You test positive. What is the probability you have the disease?

Out of 100,000 people:

| | Count |
|:--|--:|
| Actually have it | 100 |
| → test positive (true positives) | **99** |
| Do not have it | 99,900 |
| → test positive anyway (false positives) | **999** |
| **Total positives** | 1,098 |

`P(disease | positive) = 99 / 1,098 = **9%**`

**Nine percent, from a 99%-accurate test.** Because the disease is rare, most positives come from the much larger healthy group. Most people guess 95%+.

**Where this returns:** Day 76, classification with imbalanced classes. A fraud detector that flags 1,000 transactions when only 50 are fraudulent has exactly this problem — and precision is exactly `P(fraud | flagged)`. The maths you are doing today *is* the precision metric.

### Independence — and why it is usually assumed rather than true

`P(A and B) = P(A) × P(B)` **only if A and B are independent.** Two prices in the same inflationary economy are not independent. Two customers in the same city are not independent.

Assuming independence when it does not hold **understates uncertainty** — you think you have more information than you do. This is the core of Naive Bayes, which works despite the assumption being false, and it is worth understanding both facts.

---

## 💻 Code

`Day_46.py` — ten exercises. **Simulate everything** — Nield's approach, and it is the fastest way to know whether your reasoning is right.

**Foundations (1–3)**
1. Simulate 100,000 dice rolls; compare empirical to theoretical for six events
2. Joint and union probability from simulation; **verify the −P(A and B) term is needed** by computing it both ways
3. Simulate dependent vs independent events; show the multiplication rule failing for the dependent case

**Conditional and Bayes (4–7)**
4. Build a two-way contingency table; compute every conditional from it
5. **Demonstrate `P(A|B) ≠ P(B|A)`** with your own numbers and a sentence on what each means
6. **The disease test.** Write the function, verify 9%, then plot the answer as the base rate varies from 0.01% to 10%. **What shape is the curve?**
7. Apply Bayes to a realistic case: given a price rise above 10%, what is the probability the item is in the food category?

**From the `Tem.txt` question bank (8–10)** — lines 2083–2108
8. Ten of the twenty probability questions, solved by hand, then verified by simulation
9. Conditional versions: drawing without replacement
10. **The independence check:** are two of your PBS items independent? Test it, and say what your answer means for any analysis that assumed they were.

---

## 🔬 Understanding Check

1. **Understanding.** Probability and statistics start from opposite ends. Explain, with an example of each.
2. **Reasoning.** Why does the union rule subtract the joint probability?
3. **Application.** Exercise 6: why does a 99%-accurate test give a 9% answer? Explain it to someone without using Bayes' theorem.
4. **Comparison.** `P(spam | contains "free")` vs `P(contains "free" | spam)` — which does a spam filter need, and which is easier to measure?
5. **Judgement.** Exercise 6's plot: at what base rate does a positive test become more likely than not to be true? What does that say about screening rare conditions?
6. **Reasoning.** What goes wrong if you assume independence and the events are correlated? Which direction does the error go?
7. **Connection.** Precision is `P(actually positive | predicted positive)`. How does today's disease example predict what will happen on Day 76 with an imbalanced class?

---

## 🎯 Expected Outcome

- [ ] Compute joint, union and conditional probabilities correctly
- [ ] Explain why `P(A|B) ≠ P(B|A)` with a concrete case
- [ ] Apply Bayes' theorem and explain the base-rate effect without the formula
- [ ] Recognise when an independence assumption is unsafe

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 41–51, with code | 55 min |
| Intuition failures | 20 min |
| Ten exercises | 90 min |
| Daily review | 12 min |
| **Total** | **~180 min** |

---

## 🧪 Mini Assessment

Ten minutes, closed book. A shop's fraud check flags 5% of transactions. Of genuinely fraudulent transactions it flags 90%. Genuine fraud is 0.5% of all transactions.

1. What is the probability a flagged transaction is actually fraudulent?
2. What would the shop owner assume it is?
3. **What should you tell them?**

---

## 🔁 Daily Review

1. What did I guess for the disease problem before computing it?
2. Exercise 6's curve — what shape, and what does that mean for rare-condition screening?
3. Can I explain Bayes without the formula, using counts out of 100,000?
4. Which of my Day 40 analyses quietly assumed independence?

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 41–51 read, code typed
- [ ] Ten exercises done, all verified by simulation
- [ ] The disease problem computed and plotted across base rates
- [ ] `P(A|B) ≠ P(B|A)` demonstrated with your own numbers
- [ ] The fraud assessment completed closed-book
- [ ] Committed to git

---

**[← Day 45](../Day_45/Day_45.md)** · **[Day 47 →](../Day_47/Day_47.md)** · [README](../../../README.md)
