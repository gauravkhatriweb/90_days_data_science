# Day 43 — The Three Questions

|  |  |
|:--|:--|
| **Date** | Wednesday, 28 October 2026 |
| **Position** | Week 7 · Month 2 · Phase 2 |
| **Budget** | **~75 min** |
| **Code file** | `project_1/notebooks/03_analysis.ipynb` |
| **Project** | 📊 **P1 — final analysis** |

> **Why today is about narrowing, not exploring.** Days 39 and 40 opened the data up. Today closes it down. A portfolio project that answers **one question convincingly** is far stronger than one that gestures at five — because a reviewer reads depth as competence and breadth as inability to choose.

---

## 🎯 Objective

Settle on the questions this project answers, produce the final numbers, and know exactly where each one is vulnerable.

---

## 📚 Learn — the structure of a finding (20 min)

### 🔴 MUST DO

**A finding has four parts:**

| Part | Example |
|:-----|:--------|
| **The claim** | "Cooking oil rose 47% between January and September 2026" |
| **The evidence** | "Weekly SPI, 38 observations, from 312 to 459 PKR/litre" |
| **The comparison** | "Against overall SPI inflation of 11% over the same period" |
| **The limitation** | "SPI tracks one grade in urban markets; rural and brand variation are not captured" |

**Most beginners produce only the first.** The comparison is what turns a number into a finding — 47% means nothing until you know what else was doing. And the limitation is what makes the whole thing credible: an analyst who states their own weaknesses is one you can trust on the rest.

### The comparison is the analysis

A number alone is not interesting. A number **against something** is:

- against the overall average — is this item unusual?
- against its own history — is this fast for this item?
- against a related item — did the whole category move?
- against a different group — urban versus rural
- against expectation — what would you have guessed?

### The anti-pattern: conclusions your data cannot support

| Do not write | Because |
|:-------------|:--------|
| "Oil prices rose **because** of the fuel levy" | You have prices. You have no causal evidence. |
| "Prices will reach X by December" | You did no forecasting and have no interval |
| "This proves the official figure is wrong" | It measures a different basket; different is not wrong |
| "Inflation hit the poor hardest" | You would need household expenditure data to say that |

**What you can honestly write** is *what happened* and *how it compares* — which is a complete, useful analysis. Claiming causation from an observational time series is the single most common way a promising portfolio project loses credibility with someone who knows the field.

---

## 💻 Code

### 🔴 MUST DO — `03_analysis.ipynb` (50 min)

**1. Fix the questions (10 min).** Write the final one, two or three. For each: the claim you expect, the comparison you will make, and what would falsify it.

**2. The headline number (15 min).** One number this project is *about*. Compute it, sanity-check it against the raw data by hand, and write down its precise definition — *"percentage change in the weekly SPI price of cooking oil, first week of January to last week of September 2026, urban average"*. Vagueness here is where analyses get quietly wrong.

**3. The comparisons (15 min).** Compute the same number for the overall index, for the related category, and for the same period a year earlier if you have it.

**4. The robustness check (10 min).** Does the finding survive?
- Excluding the outliers you found on Day 40?
- A different start date — is it an artefact of one unusual week?
- Median instead of mean?

**If the finding does not survive, that is the finding** — and saying so is a stronger result than a fragile claim. Write down what you tried either way; it goes in the README.

### 🟢 IF TIME

- One secondary question, answered to the same standard.

---

## 🔬 Understanding Check

1. **Structure.** Write your headline finding in all four parts.
2. **Reasoning.** Why is the comparison the part that makes a number a finding?
3. **Judgement.** Name one conclusion you are tempted to draw that the data does not support. Why is it tempting?
4. **Robustness.** Did your finding survive all three checks? Which was closest to breaking it?
5. **Precision.** Write the exact definition of your headline number. Could someone else reproduce it from that sentence alone?
6. **Application.** If a journalist asked "so what does this mean for a family in Hyderabad?" — what could you honestly say, and what would you have to decline to say?

---

## 🎯 Expected Outcome

- [ ] One to three final questions, fixed
- [ ] A headline number, precisely defined and hand-verified
- [ ] At least two comparisons
- [ ] A robustness check with the results recorded
- [ ] A written list of conclusions the data cannot support

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| The structure of a finding | 20 min |
| Analysis (1–4) | 50 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

State your finding in **four sentences** — claim, evidence, comparison, limitation. Then say it out loud to someone who does not work with data. If they ask "so what?", the comparison is missing.

---

## 🔁 Daily Review

1. My headline finding, in four parts.
2. Did it survive the robustness checks? Which nearly broke it?
3. What am I tempted to claim that I cannot?
4. Two days to ship. What is left?

---

## 📦 Completion Criteria

- [ ] Final questions fixed and written in `NOTES.md`
- [ ] Headline number computed and hand-verified against raw data
- [ ] Two or more comparisons computed
- [ ] Three robustness checks run and recorded
- [ ] Unsupportable conclusions listed explicitly
- [ ] Committed to git

---

**[← Week 6 Review](../../Week_06/Week_06_Review.md)** · **[Day 44 →](../Day_44/Day_44.md)** · [README](../../../README.md)
