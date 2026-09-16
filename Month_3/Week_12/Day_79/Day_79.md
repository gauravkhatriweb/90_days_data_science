# Day 79 — Feature Engineering and Leak-Proof Pipelines

|  |  |
|:--|:--|
| **Date** | Thursday, 3 December 2026 |
| **Position** | Week 12 · Month 3 · Phase 6 |
| **Budget** | **~75 min** |
| **Code file** | `Day_79.py` |

> **Features matter more than model choice.** A good feature on a linear model beats a bad feature on a gradient-boosted anything, and most of the real work in a modelling project is here rather than in the `fit` call.
>
> **And this is where leakage most often enters.** Every transformation — scaling, imputing, encoding, target-encoding — learns something from the data. If it learns from the test set, the evaluation is compromised. `Pipeline` exists to make that impossible by construction, and today it becomes a habit rather than a thing you remember.

---

## 🎯 Objective

Create useful features and build a pipeline where preprocessing cannot leak, even by accident.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| The sections below | REFERENCE | 25 min | Feature types, encoding, and the pipeline pattern |
| [scikit-learn — `ColumnTransformer` guide](https://scikit-learn.org/stable/modules/compose.html) | REFERENCE | 10 min | The API, read once |

### 🟢 IF TIME

- [Sheryians ML Part 1 `0:54 → 1:01`](https://www.youtube.com/playlist?list=PLaldQ9PzZd9qT0KsKJ7yCq70iFFP3MFJ5) — feature engineering and selection.

---

## 🧠 Core Concepts

### The features that usually help

| Kind | Example | Why it works |
|:-----|:--------|:-------------|
| **Ratios** | revenue per customer, freight as % of price | Scale-independent, often the real signal |
| **Differences** | `delivery_date − estimated_date` | The gap is what matters, not either date |
| **Time-derived** | day of week, month, is-weekend, days-since-last | Encodes cycles a raw timestamp hides |
| **Aggregates** | a seller's average delay, a customer's order count | Brings context to a single row |
| **Counts** | items per order, distinct categories | Simple and often strong |
| **Binned** | age bands, price bands | Captures non-linearity for a linear model |
| **Interactions** | `price × distance` | When the effect of one depends on the other |

**The most productive question in feature engineering:** *what would a human who knows this business look at?* A shopkeeper judging whether an order will be late looks at the seller, the distance, and the time of year — not the raw timestamp.

### Aggregate features — the leakage trap

`seller_avg_delay` is usually a strong feature. **And computing it on the whole dataset leaks**, because the average includes the very rows you are predicting.

**Two correct options:**
1. Compute it on the training fold only — this is what a custom transformer inside a `Pipeline` does
2. Compute it on a strictly earlier time window than the row being predicted

This is Day 74's form 6, and it is the subtlest of the seven because the feature is genuinely sensible.

### Encoding categories

| Method | When | Watch out |
|:-------|:-----|:----------|
| **One-hot** | Few categories, any model | **Day 65's dependency** — use `drop="first"` for linear models |
| **Ordinal** | A genuine order — small/medium/large | Never for unordered categories in a linear model |
| **Target encoding** | Very many categories | **Leaks unless done inside folds.** Powerful and dangerous. |
| **Frequency** | Many categories, simple | Loses meaning, but safe |
| **Leave as-is** | Tree models with native support | LightGBM and CatBoost handle categories directly |

**`handle_unknown="ignore"` matters.** A category appearing only in the test set will otherwise raise at prediction time — and it will happen in production, where new categories appear constantly.

### Scaling — which models need it

| Needs scaling | Does not |
|:--------------|:---------|
| Linear and logistic regression *(for gradient descent — Day 72)* | Decision trees |
| Ridge, Lasso *(the penalty is scale-dependent)* | Random forests |
| k-NN, k-means, SVM *(distance-based — Day 65)* | Gradient-boosted trees |
| PCA *(Day 68)* | |
| Neural networks | |

**`StandardScaler` is the z-score from Day 50**, applied per column. It is the same formula, and now you know why it is needed rather than that it is.

### The pipeline — leak-proof by construction

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

numeric = Pipeline([
    ("impute", SimpleImputer(strategy="median")),
    ("scale", StandardScaler()),
])
categorical = Pipeline([
    ("impute", SimpleImputer(strategy="most_frequent")),
    ("encode", OneHotEncoder(handle_unknown="ignore")),
])

preprocess = ColumnTransformer([
    ("num", numeric, numeric_columns),
    ("cat", categorical, categorical_columns),
])

model = Pipeline([("prep", preprocess), ("clf", LogisticRegression())])
cross_val_score(model, X, y, cv=5)      # every fold refits the preprocessing
```

**Why this is not optional:** `cross_val_score` refits the entire pipeline on each training fold. The imputer's median, the scaler's mean, the encoder's categories — all learned **only** from that fold's training rows. **Leakage becomes structurally impossible**, rather than something you have to remember not to do at 11pm.

And it makes the whole thing one object: one `fit`, one `predict`, one thing to save and deploy.

### Selecting features — and when not to

| Approach | Note |
|:---------|:-----|
| Domain knowledge | **Best.** Start here. |
| Drop near-zero variance | Cheap, safe |
| Drop one of a highly correlated pair | Helps interpretability — Day 73 |
| Permutation importance | Honest, slow — Day 78 |
| **Selecting by p-value** | **Day 73's exercise 7** — noise features pass |
| Recursive elimination | Expensive, and must sit inside the pipeline |

**Fewer features is often better**: less overfitting, faster, easier to explain, less to break in production. But **any selection that looks at the target must happen inside the cross-validation folds** — otherwise the test set helped choose its own features, which is Day 74's form 7.

---

## 💻 Code

`Day_79.py` — ten exercises, on Olist or your Project 3 data.

**Creating features (1–4)**
1. **Five features a human would look at.** Write them down *before* coding, with the reasoning.
2. Ratios and differences — build three
3. Time features from a timestamp: day of week, month, is-weekend, days-since
4. **An aggregate feature, done safely** — a seller's historical average delay, computed only from earlier rows

**Encoding and scaling (5–6)**
5. One-hot with and without `drop="first"`; check the rank both ways *(Day 65)*
6. `StandardScaler` — confirm it is the z-score; verify the fitted mean and scale come from training only

**The pipeline (7–8)**
7. Build the full `ColumnTransformer` + `Pipeline`, and cross-validate it
8. **The proof:** scale outside the pipeline versus inside. **Measure the difference in the reported score** — this is Day 74's exercise 7, now with a tool that prevents it

**Selection (9–10)**
9. Compare a model on all features against one on five well-chosen ones. **Is the difference worth the complexity?**
10. **Apply everything to Project 3.** Build the real pipeline you will use tomorrow, with the leakage audit from Day 74 applied.

---

## 🔬 Understanding Check

1. **Reasoning.** Why does a `Pipeline` make preprocessing leakage structurally impossible?
2. **Application.** Exercise 4: how did you compute the aggregate feature safely? What would the unsafe version have done?
3. **Comparison.** Which models need scaling and which do not? Give the reason for each group.
4. **Reasoning.** Why `drop="first"` for linear models but not for trees? *(Day 65.)*
5. **Judgement.** Target encoding is powerful and dangerous. When would you use it, and what would you do to make it safe?
6. **Judgement.** Exercise 9: was the full-feature model meaningfully better? What would you ship?
7. **Feature design.** Which of your five human features turned out most useful? Did you predict it?

---

## 🎯 Expected Outcome

- [ ] Design features from domain reasoning, not from a list
- [ ] Encode and scale correctly per model type
- [ ] Build a `ColumnTransformer` + `Pipeline` from memory
- [ ] Compute aggregate features without leaking
- [ ] Have Project 3's real pipeline ready

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Features, encoding, pipelines | 25 min |
| scikit-learn compose guide | 10 min |
| Exercises 1–9 | 30 min |
| **Exercise 10 — Project 3's pipeline** | 10 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Six minutes. Predicting whether a customer will buy again within 90 days, from an orders table.

Write five features, and for each state: what it captures, and **whether it could leak.**

---

## 🔁 Daily Review

1. Which of my five human features was most useful? Did I predict it?
2. Exercise 8: how much did leaked scaling inflate the score?
3. Is Project 3's pipeline built and cross-validating cleanly?
4. **Project 3 starts tomorrow.** Is anything still undecided?

---

## 📦 Completion Criteria

- [ ] Five features written from domain reasoning **before** coding
- [ ] Time and aggregate features built, the aggregate one leak-free
- [ ] One-hot rank checked with and without `drop="first"`
- [ ] A full `ColumnTransformer` + `Pipeline` cross-validating
- [ ] The inside-vs-outside scaling difference measured
- [ ] **Project 3's pipeline built and running**
- [ ] Committed to git

---

**[← Day 78](../Day_78/Day_78.md)** · **[Day 80 →](../Day_80/Day_80.md)** · [README](../../../README.md)
