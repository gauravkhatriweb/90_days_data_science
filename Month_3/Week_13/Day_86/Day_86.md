# Day 86 — Finding Structure Without Labels

|  |  |
|:--|:--|
| **Date** | Thursday, 10 December 2026 |
| **Position** | Week 13 · Month 3 · Phase 7 |
| **Budget** | **~75 min** |
| **Code file** | `Day_86.py` |

> **This is the cut day.** If Project 3 needed another day, or exams are pressing, **take it from here** — it is the only remaining day with no downstream dependency. Nothing on Days 87–90 relies on it.
>
> **If you do have the time**, it closes a real gap: everything since Day 69 has been supervised, and there is a whole class of question where nobody has labelled the answer. It is also where Day 68's eigenvectors finally get used.

---

## 🎯 Objective

Cluster data without labels, apply PCA in practice, and — most importantly — know when both are the wrong tool.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [StatQuest — K-means clustering](https://www.youtube.com/watch?v=4b5d3muPQmA) | **PRIMARY** | 9 min | The algorithm |
| [StatQuest — PCA, Step-by-Step](https://www.youtube.com/watch?v=FgakZw6K1QQ) | **REINFORCEMENT** | 22 min | The practical view, after Day 68's mathematical one |
| The sections below | REFERENCE | 15 min | The honest limits |

---

## 🧠 Core Concepts

### K-means

1. Pick k random centres
2. Assign each point to its nearest centre
3. Move each centre to the mean of its points
4. Repeat until nothing moves

**Simple, fast, and it always returns an answer** — which is its main danger. **K-means will cluster pure noise into k tidy groups and report a result.** It never tells you there is no structure.

**The four assumptions**, all of which are frequently false:

| Assumes | Fails when |
|:--------|:-----------|
| Spherical clusters | Clusters are elongated or curved |
| Similar sizes | One group is much larger |
| Similar densities | Density varies |
| **You know k** | You almost never do |

### Choosing k — and why neither method is authoritative

| Method | Gives |
|:-------|:------|
| **Elbow** | Plot within-cluster variance against k; look for the bend | Often there is no clear bend |
| **Silhouette** | How well-separated the clusters are | More principled, still not definitive |
| **Domain knowledge** | "The business wants four segments" | **Usually the real answer** |

**The honest position:** k is a business decision informed by the data, not a number the data determines. Four segments a team can act on beat seven that are statistically tidier and operationally useless.

### Scaling is mandatory

K-means uses Euclidean distance — Day 65. Unscaled, the feature with the largest units *is* the clustering. **Always scale**, and this is not a preference.

### PCA in practice

Day 68 gave you the mathematics. The practical uses:

| Use | Note |
|:----|:-----|
| **Visualising high-dimensional data in 2D** | The most honest use |
| Reducing dimensions before a distance-based model | Can genuinely help |
| Removing multicollinearity | Works, and costs interpretability |
| Compression | Rarely the point in analytics |

**And the costs, again:** it needs scaling, it only finds linear structure, and **the components have no meaning to a business.** Never present a principal component to a stakeholder as though it were a variable they can act on.

### When to reach for neither

- **You have labels.** Use them. Supervised beats unsupervised whenever the answer exists.
- **The business already has segments.** Test those before inventing new ones.
- **Fewer than about six features.** PCA buys little and costs interpretability.
- **You want an explanation.** Clusters describe; they do not explain.

**Clustering produces a hypothesis, not a finding.** "There appear to be four groups" is worth testing — it is not worth acting on until you have checked whether the groups behave differently in something you care about.

---

## 💻 Code

`Day_86.py` — nine exercises.

**K-means (1–4)**
1. Run it on obviously clustered 2D data; plot the assignments and the centres
2. **The elbow plot** and **the silhouette plot** for k from 2 to 10. **Do they agree?**
3. **The noise demonstration:** run k-means on uniform random data with k=4. **It produces four tidy clusters.** Plot them. *(This is the lesson.)*
4. **The assumption failures:** elongated clusters, unequal sizes, unequal densities. Watch k-means get each one wrong.

**Scaling and PCA (5–7)**
5. Cluster unscaled versus scaled. **Are they the same clustering?**
6. PCA to 2D for visualisation; colour by cluster
7. PCA before k-means versus k-means on raw features — same groups?

**Applied (8–9)**
8. **Cluster your Olist customers** on RFM features. Compare with Day 62's rule-based RFM segments. **Which is more useful to a business, and why?**
9. **The honest check:** for each cluster, compute a business metric that was *not* used in the clustering. **Do the clusters differ on it?** If not, they may be an artefact rather than a finding.

Exercise 9 is what turns clustering from a picture into evidence, and almost nobody does it.

---

## 🔬 Understanding Check

1. **Reasoning.** Why is it dangerous that k-means always returns an answer?
2. **Application.** Exercise 3: what did k-means do with pure noise? How would you have known without knowing the truth?
3. **Judgement.** Exercise 2: did the elbow and silhouette agree? What would you do if they disagreed?
4. **Reasoning.** Why must you scale before k-means? Connect it to Day 65.
5. **Comparison.** Exercise 8: rule-based RFM or k-means clusters — which would a shop owner act on?
6. **Validation.** Exercise 9: did the clusters differ on an unused metric? What does each answer mean?
7. **Judgement.** When would you use neither clustering nor PCA?

---

## 🎯 Expected Outcome

- [ ] Run k-means and choose k with reasoning rather than a rule
- [ ] Recognise when its assumptions fail
- [ ] Use PCA for visualisation, and know what it costs
- [ ] Validate clusters against something they were not built from

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| StatQuest k-means + PCA | 31 min |
| Limits and honesty | 15 min |
| Nine exercises | 25 min |
| Daily review | 5 min |
| **Total** | **~76 min** |

---

## 🧪 Mini Assessment

Five minutes. A manager says: *"Segment our customers with machine learning."*

Write: the three questions you would ask first, the method you would try, and **how you would know whether the segments are real.**

---

## 🔁 Daily Review

1. Exercise 3: what did k-means produce on pure noise?
2. Did elbow and silhouette agree?
3. Exercise 9: did the clusters differ on an unused metric?
4. Rule-based RFM or k-means — which would I give a shop owner?

---

## 📦 Completion Criteria

- [ ] K-means run, elbow and silhouette compared
- [ ] The pure-noise demonstration produced
- [ ] Three assumption failures shown
- [ ] Scaled vs unscaled clustering compared
- [ ] PCA used for 2D visualisation
- [ ] Clusters validated against an unused business metric
- [ ] Committed to git

---

**[← Day 85](../Day_85/Day_85.md)** · **[Day 87 →](../Day_87/Day_87.md)** · [README](../../../README.md)
