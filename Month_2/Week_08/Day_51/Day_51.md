# Day 51 — The Central Limit Theorem

|  |  |
|:--|:--|
| **Date** | Thursday, 5 November 2026 |
| **Position** | Week 8 · Month 2 · Phase 3 — Statistics |
| **Budget** | **~75 min** |
| **Code file** | `Day_51.py` |
| **Reading** | 📐 **Essential Math Ch. 3, pp. 89–92** |

> **This is the most important single idea in the ninety days.** Everything that follows — confidence intervals, p-values, hypothesis tests, model comparison, A/B tests — exists because of the Central Limit Theorem. It is what makes statistics possible at all.
>
> It is also, unusually, an idea you can *see*. Simulate it once and it stops being a theorem and becomes something obvious.

---

## 🎯 Objective

Understand, demonstrate and be able to explain why sample means are normally distributed even when the underlying data is not.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 3, pp. 89–92** | **PRIMARY** · reading + code | 20 min | The CLT and the standard error |
| [StatQuest — The Central Limit Theorem](https://www.youtube.com/watch?v=YAlJCEDH2uY) | **REINFORCEMENT** | 8 min | The picture. Watch it **after** reading. |
| The sections below | REFERENCE | 12 min | The consequences |

**Why both:** Nield gives you the formula and the code; Starmer gives you the picture. Read first so the video confirms something rather than introducing it — that ordering is worth more than either resource alone.

---

## 🧠 Core Concepts

### The statement

> Take samples of size *n* from **any** distribution with a finite mean and variance. The distribution of the **sample means** approaches normal as *n* grows — **regardless of the shape of the original distribution.**

Read that twice. **Regardless of shape.** Skewed, bimodal, uniform, a mess — the sample means still go normal.

### Why it is the foundation of everything

You have one sample. You compute one mean. That mean is one draw from a distribution of possible means you could have got.

The CLT tells you **what that distribution looks like** — and once you know its shape, you can say how far your one mean might plausibly be from the truth.

**That is the entire basis of inference.** Every confidence interval and every p-value from here to Day 90 is an application of this one fact.

### The standard error

The sample means have their own standard deviation, called the **standard error**:

```
SE = σ / √n
```

| n | SE, if σ = 15 |
|:--:|:--|
| 4 | 7.50 |
| 25 | 3.00 |
| 100 | 1.50 |
| 400 | 0.75 |
| 1,600 | 0.375 |

**The √n is the fact with real consequences.** To halve your uncertainty you need **four times** the data. To get ten times more precise you need **a hundred times** more data.

This is why "just collect more data" hits diminishing returns fast, why large studies are expensive, and why an A/B test that needs to detect a small effect needs an enormous sample.

### How large does n need to be?

The usual rule of thumb is n ≥ 30, and like most rules of thumb it is approximately right and often wrong:

| Original distribution | n needed |
|:----------------------|:---------|
| Already normal | 1 |
| Symmetric, light tails | ~10 |
| Moderately skewed | ~30 |
| Heavily skewed (income, prices) | **100+** |
| Very heavy-tailed | may fail in practice |

**Your PBS data is skewed** — you established that yesterday. So "n ≥ 30" may not be enough, and exercise 4 makes you find out for your own data rather than trusting the rule.

### The two things it does not say

**1. It does not say your data becomes normal.** Only the *means* do. A histogram of your raw prices will stay skewed no matter how much data you collect.

**2. It needs finite variance.** Some real distributions — certain financial returns, some network phenomena — have such heavy tails that the CLT does not usefully apply. Rare, but it is why the caveat exists.

---

## 💻 Code

`Day_51.py` — seven exercises. **This is a day where the simulation is the lesson.**

**Seeing it (1–3)**
1. **The demonstration.** Sample means from four very different distributions — uniform, exponential, bimodal, and your own PBS prices. Plot all four means distributions. **They all go normal.**
2. Vary *n*: 2, 5, 10, 30, 100. Watch the means distribution converge. At what *n* does each source look normal?
3. Overlay a fitted normal curve on each histogram of means to show how close it is

**The standard error (4–6)**
4. **Find the n your own data needs.** Use the Shapiro-Wilk test on the sample means at each *n*, and find where it stops rejecting normality. **Is 30 enough for your data?**
5. Verify `SE = σ/√n` empirically at five sample sizes
6. **The √n consequence:** plot SE against n. Mark the n needed to halve your current uncertainty, and the n needed to halve it again.

**Applying it (7)**
7. From one sample of your PBS prices, estimate the standard error of the mean, and state the range within which the true mean plausibly lies. **You have just built a confidence interval** — tomorrow gives it a name and a precise definition.

---

## 🔬 Understanding Check

1. **Understanding.** State the CLT in your own words. What exactly becomes normal?
2. **Reasoning.** Why does the CLT make inference possible at all? Answer in terms of having one sample.
3. **Application.** Exercise 4: what *n* does your data need? Was the rule of thumb right?
4. **Reasoning.** Why does SE shrink as `√n` and not as `n`? What is the practical consequence for data collection budgets?
5. **Debugging.** Someone says "my data is not normal so I cannot use these methods." What is wrong with that, and when would they be right?
6. **Judgement.** Exercise 6: how many more observations to halve your uncertainty? Is that realistic to collect?
7. **Connection.** You just estimated a range for the true mean. What is that called, and what does it *not* mean? *(Tomorrow.)*

---

## 🎯 Expected Outcome

- [ ] State and demonstrate the CLT
- [ ] Explain why it makes inference possible
- [ ] Compute and interpret a standard error
- [ ] Explain the √n consequence and why it matters commercially

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 89–92 | 20 min |
| StatQuest CLT | 8 min |
| Consequences | 12 min |
| Seven exercises | 30 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Five minutes, closed book. A sample of 64 customers spends a mean of PKR 2,400 with SD 800.

1. The standard error
2. The range containing the true mean about 95% of the time
3. How many customers would you need to halve that range?
4. **Explain to a shop owner, in one sentence, why you cannot just say "average spend is 2,400."**

---

## 🔁 Daily Review

1. Exercise 1: did seeing all four converge change my understanding, or confirm it?
2. What *n* does my own data need? Was 30 enough?
3. Can I explain the √n consequence to a non-technical person?
4. **This is the foundation of everything after it.** Is there anything still unclear? If yes, redo exercise 1 before Day 52.

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 89–92 read, StatQuest watched after
- [ ] The four-distribution demonstration produced as one figure
- [ ] The *n* your own data needs, found empirically
- [ ] `SE = σ/√n` verified at five sample sizes
- [ ] The √n consequence plotted with the doubling points marked
- [ ] A range for the true mean estimated from one sample
- [ ] Committed to git

---

**[← Day 50](../Day_50/Day_50.md)** · **[Day 52 →](../Day_52/Day_52.md)** · [README](../../../README.md)
