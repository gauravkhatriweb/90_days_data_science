# Day 76 — Why Accuracy Lies

|  |  |
|:--|:--|
| **Date** | Monday, 30 November 2026 |
| **Position** | Week 11 · Month 3 · Phase 6 |
| **Budget** | **~75 min** |
| **Code file** | `Day_76.py` |
| **Reading** | 📐 **Essential Math Ch. 6, pp. 211–223** |

> **Day 46's disease test, arriving where it was always heading.** A 99%-accurate test for a rare disease gives a 9% chance of actually having it — and **precision is exactly `P(actually positive | predicted positive)`.** The maths you did on Day 46 *is* today's metric.
>
> **The practical outcome:** you will stop reporting accuracy, and start asking which of the two mistakes costs more. That question is the whole of classification evaluation, and it is a business question rather than a technical one.

---

## 🎯 Objective

Read a confusion matrix, choose the right metric for the cost structure, and know why accuracy is nearly useless on imbalanced data.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 6, pp. 211–223** | **PRIMARY** · reading + code | 30 min | R² and p-values for logistic · train/test · confusion matrices · Bayes and classification |
| [StatQuest — The Confusion Matrix](https://www.youtube.com/watch?v=Kdsp6soqA7o) | **REINFORCEMENT** | 7 min | The layout, clearly |
| The metric-choice section below | REFERENCE | 20 min | The decision |

---

## 🧠 Core Concepts

### The confusion matrix

|  | Predicted negative | Predicted positive |
|:--|:--|:--|
| **Actually negative** | True negative (TN) | **False positive (FP)** — a false alarm |
| **Actually positive** | **False negative (FN)** — a miss | True positive (TP) |

**Everything else is arithmetic on these four numbers.** Learn the layout once — and note that scikit-learn puts actuals on rows and predictions on columns, while many textbooks do the opposite. Check before reading anyone's matrix.

### The metrics, and the question each answers

| Metric | Formula | Asks |
|:-------|:--------|:-----|
| **Accuracy** | (TP+TN) / all | "How often am I right?" — **almost always the wrong question** |
| **Precision** | TP / (TP+FP) | "When I say yes, how often am I right?" |
| **Recall** | TP / (TP+FN) | "Of the real cases, how many did I catch?" |
| **F1** | harmonic mean of the two | A single number when both matter equally |
| **Specificity** | TN / (TN+FP) | "Of the real negatives, how many did I clear?" |

**Precision is `P(actually positive | predicted positive)`** — Day 46's `P(disease | positive test)`, with new words on it.

### Why accuracy lies

Fraud is 1% of transactions. A model that predicts "not fraud" for everything scores **99% accuracy** and catches nothing.

**That is the baseline from Day 69.** Any accuracy number must be read against the majority-class rate, and a model that does not clearly beat it has learned nothing.

**The rule:** never report accuracy on imbalanced data without the class balance next to it. "94% accurate" where 94% is the majority class is not a result.

### The trade-off, and how to decide

Precision and recall move against each other. Lowering the threshold catches more real cases (recall up) and produces more false alarms (precision down).

**The question is not "which metric is better" but "which mistake costs more":**

| Situation | Worse mistake | Optimise |
|:----------|:--------------|:---------|
| Screening for a treatable cancer | Missing a case | **Recall** |
| Blocking a transaction as fraud | Blocking a real customer | **Precision** |
| Spam filter | A real email in the spam folder | **Precision** |
| Predicting machine failure | Missing a failure | **Recall** |
| Sending a retention offer | Depends on the offer's cost vs the customer's value | **Compute it** |

**The last row is the honest general case.** If a retention offer costs PKR 500 and an average retained customer is worth PKR 8,000, a false positive costs 500 and a false negative costs 8,000 — so a false negative is sixteen times worse, and the threshold should be set accordingly. **That arithmetic, not a metric name, is the answer.**

### The imbalance problem, and the honest options

| Approach | Does | Risk |
|:---------|:-----|:-----|
| **Nothing** | Use the right metric and threshold instead | Often the correct choice |
| `class_weight="balanced"` | Weights the rare class in the loss | Simple, usually effective |
| Undersampling | Drops majority rows | Throws away data |
| Oversampling / SMOTE | Duplicates or synthesises minority rows | **Must be inside the training fold only** — otherwise it is Day 74's leakage |

**Most imbalance "problems" are metric problems.** Before resampling anything, try: use precision and recall, set the threshold from costs, and check whether you beat the baseline. That solves it more often than resampling does.

### Multi-class, briefly

With more than two classes, precision and recall are computed per class and then averaged:

| Averaging | Behaviour |
|:----------|:----------|
| `macro` | Every class counts equally — **use when rare classes matter** |
| `weighted` | Classes counted by frequency — hides poor performance on rare classes |
| `micro` | Pools all decisions — equals accuracy in the single-label case |

---

## 💻 Code

`Day_76.py` — ten exercises.

**The matrix (1–3)**
1. Build a confusion matrix by hand from predictions; match `sklearn.confusion_matrix`
2. Compute all five metrics from the four cells, by hand; match `classification_report`
3. **Know your layout:** print sklearn's matrix and label every cell explicitly

**Why accuracy lies (4–6)**
4. **The 99% model.** On 1% fraud data, predict "no" always. Report the accuracy. Then report precision and recall.
5. Compare three models — a real one, an always-negative one, and a random one — on all five metrics. **Which metric separates them?**
6. **The Day 46 connection.** Compute precision on a rare-class problem and show it is the same calculation as `P(disease | positive test)`.

**The trade-off (7–8)**
7. **Sweep the threshold** from 0.01 to 0.99. Plot precision and recall on one chart. **Find where they cross.**
8. **The cost-based threshold.** Given FP cost 500 and FN cost 8,000, compute total cost at each threshold and **find the minimum.** Compare with F1's choice — they will differ.

**Imbalance (9–10)**
9. Compare `class_weight=None` against `"balanced"` on imbalanced data. What changes, and what does not?
10. **Apply to your own problem.** Build a confusion matrix for Project 3 or for Olist's late-delivery question. **Write the cost of each error type in words**, then choose the metric and threshold.

---

## 🔬 Understanding Check

1. **Reasoning.** Why is accuracy misleading on imbalanced data? Give a concrete example with numbers.
2. **Connection.** How is precision the same thing as Day 46's `P(disease | positive test)`?
3. **Application.** Exercise 7: where did precision and recall cross? What does that point mean?
4. **Judgement.** Exercise 8: did the cost-minimising threshold match F1's? Which would you use, and why?
5. **Reasoning.** For your Project 3 problem, which error costs more? Put numbers on both.
6. **Comparison.** When is `macro` averaging right and `weighted` misleading?
7. **Judgement.** When is the correct response to class imbalance to do nothing about it?

---

## 🎯 Expected Outcome

- [ ] Read a confusion matrix and compute every metric from it
- [ ] Explain why accuracy is nearly useless on imbalanced data
- [ ] Choose a threshold from the cost of each error
- [ ] Say when imbalance needs no special handling

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 211–223 | 30 min |
| StatQuest confusion matrix | 7 min |
| Metric choice | 20 min |
| Ten exercises | 30 min |
| Daily review | 5 min |
| **Total** | **~92 min** |

---

## 🧪 Mini Assessment

Six minutes. A model flags 200 transactions as fraud. 30 are genuinely fraudulent. There were 50 fraudulent transactions in total, out of 10,000.

1. Build the confusion matrix
2. Accuracy, precision, recall
3. **Is this model useful?** Answer with the costs, not the metrics.

---

## 🔁 Daily Review

1. Exercise 4: what accuracy did the always-negative model get?
2. Exercise 8: how far apart were the cost-minimising and F1 thresholds?
3. For Project 3, which error costs more, and by roughly how much?
4. Can I explain to a manager why "94% accurate" might mean nothing?

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 211–223 read, StatQuest watched
- [ ] Confusion matrix built by hand and matched
- [ ] The always-negative model's accuracy reported alongside its recall
- [ ] Precision shown to be the Day 46 calculation
- [ ] Precision–recall curves plotted, crossing point found
- [ ] A cost-minimising threshold computed and compared with F1
- [ ] Project 3 error costs written in words and numbers
- [ ] Committed to git

---

**[← Day 75](../Day_75/Day_75.md)** · **[Day 77 →](../Day_77/Day_77.md)** · [README](../../../README.md)
