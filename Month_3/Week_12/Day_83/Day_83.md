# Day 83 — Project 3: What It Means, and What It Cannot Do

|  |  |
|:--|:--|
| **Date** | Monday, 7 December 2026 |
| **Position** | Week 12 · Month 3 · Phase 6 |
| **Budget** | **~75 min** |
| **Code file** | `project_3/RECOMMENDATION.md` |

> **The model is finished. The project is not.** A model with no interpretation and no stated limits is a number in a notebook. Today turns it into something a person can act on — and, just as importantly, something they will not over-trust.
>
> **The limitations section is the one that earns credibility.** Anyone experienced will find the weaknesses within minutes. Finding them already written, in your own words, is the difference between "careful" and "did not think about it".

---

## 🎯 Objective

Explain what the model learned, state what it cannot do, and write a recommendation someone could act on tomorrow.

---

## 📚 Learn — interpretation, honestly (20 min)

### What you can and cannot say

| | Can say | Cannot say |
|:--|:--|:--|
| **Linear coefficient** | "Associated with a change of β, holding others constant" | "Causes" |
| **Odds ratio** | "The odds multiply by e^β" | "The probability doubles" *(Day 75)* |
| **Feature importance** | "The model relies on this for splitting" | "This drives the outcome" *(Day 78)* |
| **A prediction** | "Given these inputs, the model estimates p" | "This will happen" |
| **A score** | "On this test set, of this size" | "In production" |

**Every row's left column is a claim about the model. Every right column is a claim about the world.** Confusing the two is the most common way a technically competent project loses credibility.

### The tools worth using

| Tool | Gives |
|:-----|:------|
| Coefficients and odds ratios | Direct interpretation for linear models |
| **Permutation importance** | What the model actually relies on, on held-out data — Day 78 |
| Partial dependence | The average effect of one feature across its range |
| Individual explanations | Why *this* prediction — useful when a person must act on a single case |

**Start with the simplest that answers the question.** A coefficient table often does, and needs no extra library.

### The limitations to state

Six categories. Aim for at least four, specific:

1. **Data** — what the data does not cover; who or what is missing
2. **Time** — the period it was trained on, and what would make it stale
3. **Population** — who it applies to, and who it does not
4. **The failure mode** — Day 82's sentence
5. **Causality** — what it cannot tell you about interventions
6. **Deployment** — what would have to be true for it to be used

**Category 5 is the one that matters most for how the model would be used.** A model predicting churn from support tickets does not tell you that reducing tickets reduces churn — and someone *will* read it that way unless you say otherwise, in the document, in plain words.

### The recommendation structure

Day 64's memo, adapted:

```
# The recommendation itself, as the title

## The situation
## What the model does, and how well
## What it cannot do          <- prominent, not buried
## What I recommend
## What it is worth
## What would change my mind
## What I would do next
```

---

## 💻 The Work

### 🔴 MUST DO — interpretation (30 min)

1. Coefficient table with odds ratios, if linear — with a plain sentence for each
2. **Permutation importance** on the test set; compare with built-in if a forest
3. Partial dependence for the top two features. **Is the shape sensible?**
4. Pick **three individual predictions** — one confident and right, one confident and wrong, one uncertain — and explain each in a sentence
5. **Write what the model learned, in one paragraph, for a non-technical reader**

### 🔴 MUST DO — the recommendation (35 min)

6. Title it with the recommendation
7. Two sentences of situation
8. What the model does, with the number and its interval
9. **Limitations — at least four, from at least three of the six categories**
10. **The causality paragraph.** Write explicitly what this does not prove.
11. The recommendation itself, specific and assignable
12. What it is worth — the arithmetic, however rough
13. What would change your mind
14. **The read-aloud test**, with a real person

### 🟢 IF TIME

- SHAP values for individual explanations. Useful, and not required — a coefficient table plus permutation importance usually answers the question.

---

## 🔬 Understanding Check

1. **Interpretation.** Write your best feature's effect in a sentence that is true, then in the tempting sentence that is false.
2. **Importance.** Did permutation importance agree with the built-in? Which do you report?
3. **Sanity.** Exercise 3: was the partial dependence shape sensible? What would a nonsensical shape have meant?
4. **Individuals.** Exercise 4: what made the confident-and-wrong case wrong?
5. **Causality.** What is the causal claim someone will wrongly take from this? Write the sentence that prevents it.
6. **Limits.** Which of your four limitations is the most serious? Would you still recommend deploying?
7. **Communication.** Exercise 14: what did your reader take away? Was it what you meant?

---

## 🎯 Expected Outcome

- [ ] The model's behaviour explained in plain language
- [ ] Permutation importance computed on held-out data
- [ ] Four or more specific limitations across several categories
- [ ] An explicit statement of what cannot be concluded
- [ ] A recommendation someone could act on

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Interpretation, honestly | 20 min |
| Interpretation work (1–5) | 25 min |
| The recommendation (6–14) | 25 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

**The causality paragraph.** One paragraph stating what this model does *not* prove, written so that a manager who reads only that paragraph would not misuse the result.

If you can write that well, you can be trusted with a model.

---

## 🔁 Daily Review

1. The true sentence and the tempting false one, side by side.
2. What made the confident-and-wrong prediction wrong?
3. My most serious limitation — and would I still deploy?
4. What did my reader take away?

---

## 📦 Completion Criteria

- [ ] Coefficients or importances interpreted with plain sentences
- [ ] Permutation importance computed on the test set
- [ ] Partial dependence checked for sensibility
- [ ] Three individual predictions explained
- [ ] `RECOMMENDATION.md` complete, recommendation as the title
- [ ] Four or more limitations, across several categories
- [ ] **The causality paragraph written**
- [ ] Read-aloud test done
- [ ] Committed to git

---

**[← Day 82](../Day_82/Day_82.md)** · **[Day 84 →](../Day_84/Day_84.md)** · [README](../../../README.md)
