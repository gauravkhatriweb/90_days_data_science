# 🔍 Resources & Curriculum Decisions

> Every decision that shaped the 90 days: what came out of `Tem.txt`, what went in, what was
> kept even though it repeats, and what the whole thing costs in hours.
>
> Nothing here was changed silently. If a resource you collected is missing from the plan,
> its reason is on this page.

**[← Back to README](./README.md)**

---

## 📦 What `Tem.txt` Actually Contains

3,058 lines, read in full. It is nine distinct artefacts, not one document:

| # | Lines | Artefact | Verdict |
|:-:|:------|:---------|:--------|
| 1 | 1–100 | IBM — *What is Data Science?* (transcript) | **KEEP** — 8 min, Day 1 |
| 2 | 101–186 | IBM — *Data Analytics vs Data Science* (transcript) | **KEEP** — 6 min, Day 1 |
| 3 | 187–409 | Programming with Mosh — *Complete Data Science Roadmap* | **CONSUMED** — its advice is absorbed below; do not re-watch |
| 4 | 410–1083 | Apna College — *Complete Data Science Roadmap 2026* (Hindi transcript) | **CONSUMED** — same |
| 5 | 1084–1895 | Sheryians AI School — full channel catalogue + AI summaries of ~20 courses | **SPLIT** — six courses kept, the rest cut |
| 6 | **1898–2494** | **The 180-Day Data Science Journey** — week-by-week plan with ~200 practice questions | **HIGHEST-VALUE ITEM IN THE FILE.** Question banks mined throughout; its sequencing overridden |
| 7 | 2498–2605 | CodeWithHarry — Python in Hindi, full chapter timestamps | **KEEP** — reinforcement, OOP chapters |
| 8 | 2606–2671 | Apna College — Python Full Course, full chapter timestamps | **KEEP** — reinforcement, OOP parts |
| 9 | 2677–3058 | **Essential Math for Data Science** — complete TOC with page numbers | **KEEP** — becomes the mathematical spine |

### The single most useful thing in the file

The **180-Day Data Science Journey** (lines 1898–2494) contains roughly **200 graded practice questions** across Python, statistics, probability, Pandas/NumPy, visualisation, SQL and ML. Question banks are expensive to write and these are well-graded.

**They are used. The schedule around them is not.** The 180-day plan assumes 2–3 hours every day for six months and puts SQL at week 12–14 and statistics before any data handling. Neither survives contact with a university semester or with prerequisite reasoning. So: **questions mined, sequence rebuilt.**

---

## ❌ Removed / Deprioritised

Ordered by how much time each removal returns.

### 1. Deep Learning — the entire four-part Sheryians series
`ANN (4:20) · CNN (1:54) · RNN (4:02) · Transformers (3:51)` — **≈ 14 hours removed**

**Why:** prerequisite failure. Backpropagation is the chain rule applied to a computational graph, and gradient descent is calculus plus linear algebra. You meet the chain rule on Day 25 and linear algebra on Day 65. Attempting deep learning inside these 90 days means memorising Keras calls and calling it understanding — the exact thing you said you did not want.

**It is also not what gets a first role.** No entry-level data analyst or junior data scientist posting requires a transformer implementation; almost all require SQL.

**When instead:** 2027, after Essential Math Ch. 7 and a solid ML foundation. Chapter 7 of your own book is the right entry point, not a 4-hour video.

---

### 2. Generative AI, LangGraph, Agentic AI, RAG, Pydantic, FastAPI
`≈ 18 hours removed`

**Why:** this is your *strength*, not your gap. You have already built LLM-backed systems — FounderOutreach, LifeOS Daily Intelligence, the Daily 3-Video Intelligence engine — with provider fallback chains, structured output schemas and scheduled triggers. Spending 18 hours of a 165-hour budget on material you have already proven you can do, while statistics and SQL sit at zero, would be the worst trade in the plan.

---

### 3. Power BI (5:16) + DAX (9:45) + Excel (5:55)
`≈ 21 hours removed — replaced by one day`

**Why:** 21 hours is 13% of the entire budget spent on tool operation. Job postings ask for "a dashboard", not DAX mastery, and BI tools are the fastest thing on this list to learn later when a specific job requires a specific one.

**Replaced with:** Day 87 — one dashboard built from Project 2's data, as a portfolio artefact. If a role you want later names Power BI explicitly, the full course is still there.

---

### 4. NLP (2:30) and the Sheryians ML Parts 3–4 advanced half
`≈ 6 hours removed`

**Why (NLP):** prerequisite failure again, and it is a specialisation. Specialising before the foundation is complete is how people end up unable to explain a confusion matrix while claiming to know sentiment analysis.

**Why (ML Parts 3–4 advanced half):** SVM kernels, Naive Bayes derivations, AdaBoost/XGBoost internals, stacking and DBSCAN are kept **out of the 90 days** so that logistic regression, validation, leakage and error analysis can be done properly. Breadth here buys nothing; a junior who deeply understands three models and validation beats one who has run nine.

---

### 5. R
**Why:** Python covers everything you need and is what your degree leads with. R appears in the job market mostly in research and biostatistics, and your degree will introduce it in its own time. Learning two languages badly is worse than one well. *(Removed from the Mosh and IBM roadmap recommendations.)*

---

### 6. Big Data — Hadoop, Spark
**Why:** you do not have big data. You will not have big data for years. These tools are also the fastest-moving item on the list — anything learned now is stale by the time it matters. *(Removed from the Mosh roadmap.)*

---

### 7. Data Structures & Algorithms as a 1–2 month block
**Why:** Mosh allocates 1–2 months. You are taking **CSE 205 — Object-Oriented Programming and Data Structures (4 credits)** next semester, where it will be taught formally and assessed.

**Kept instead:** a thin thread — Big-O intuition and list/dict/set trade-offs on Day 5, recursion in the OOP block, and enough that CSE 205 is familiar rather than new. Roughly 3 hours instead of 200.

---

### 8. The four roadmap videos themselves
Mosh's roadmap, Apna College's roadmap, and the "Ultimate Data Science Roadmap 180 days" video.

**Why:** their content is now *this document*. Re-watching roadmaps is the purest form of the content addiction you asked me to design against. The two short IBM framing videos survive because they are 14 minutes total and genuinely useful once, on Day 1.

---

### 9. Career-opinion and job-market videos
*"The Data Science Job Market Is Not What You Think" · "Best Entry-Level AI Jobs Ranked" · "Your AI/ML Degrees are Scam" · "Is Traditional Machine Learning Dead?" · "AI Engineer Roadmap 2026" · "How I Would Become an ML Engineer"* — and roughly a dozen similar items in the Sheryians catalogue.

**Why:** zero skill transfer, high engagement design, and they make you feel informed while your SQL is still zero. Career research belongs on Day 89, done deliberately, against real job postings.

---

### 10. The Titanic, Iris and Boston Housing datasets
**Why:** they appear in the 180-day plan's ML weeks, and they are on tens of thousands of GitHub repositories. A Titanic notebook tells a reviewer you completed a tutorial. Boston Housing additionally has documented ethical problems with one of its features and has been removed from scikit-learn.

**Replaced with:** Pakistan Bureau of Statistics price data (Project 1), a retail transaction dataset framed as SwiftBase-style analytics (Project 2), and a Project 3 problem you choose on Day 80. Allowed only as a 20-minute mechanics drill if you want to check a pipeline works.

---

### 11. The 180-day plan's Weeks 22–26 (Deep Learning + Specialisation)
**Why:** out of scope by the same reasoning as items 1 and 4. The specialisation choice (NLP vs CV vs BI vs Data Engineering) is a 2027 decision that should be made from evidence about what you enjoy, which these 90 days will produce.

---

### 12. CodeWithHarry's "Jarvis" and "Auto-Reply AI Chatbot" mega-projects
**Why:** genuinely fun, and completely off-mission. They are voice-assistant and chatbot engineering, not data science — and again, building AI-integrated applications is already something you do.

---

### Removal summary

| Category | Hours returned |
|:---------|---------------:|
| Deep learning series | ≈ 14 h |
| GenAI / agents / FastAPI / Pydantic | ≈ 18 h |
| Power BI + DAX + Excel courses | ≈ 21 h |
| NLP + advanced ML tail | ≈ 6 h |
| Roadmap and career-opinion videos | ≈ 5 h |
| Beginner Python you don't need | ≈ 24 h |
| **Total returned to the budget** | **≈ 88 hours** |

Those 88 hours are what make statistics, linear algebra, SQL and three real projects fit into 165.

---

## ➕ Added

### 1. Corey Schafer — Python OOP (6 videos, ≈ 2 h) · **PRIMARY**
[Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)

**Why it was added:** you told me OOP is your weakest and least enjoyable area, and you chose three Python courses specifically to get multiple explanations of hard concepts. But all three give OOP roughly 1–2 hours of *syntax*: here is a class, here is `self`, here is inheritance. None of them explain **when not to inherit**, why properties exist, what dunder methods are for, or how to design an interface.

Corey Schafer's series does. It is six focused videos, each on one idea, taught by someone explaining design rather than syntax. It is the depth layer your three courses are missing, and it is the reason Days 15–20 should finally make OOP make sense.

| # | Video | Day |
|:-:|:------|:---:|
| 1 | [Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM) | 15–16 |
| 2 | [Class Variables](https://www.youtube.com/watch?v=BJ-VvGyQxho) | 17 |
| 3 | [classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M) | 17 |
| 4 | [Inheritance — Creating Subclasses](https://www.youtube.com/watch?v=RSl87lqOXDE) | 18 |
| 5 | [Special (Magic/Dunder) Methods](https://www.youtube.com/watch?v=3ohzBxoFHAY) | 19 |
| 6 | [Property Decorators](https://www.youtube.com/watch?v=jCzT9XFZ5bw) | 19 |

---

### 2. StatQuest with Josh Starmer · **REINFORCEMENT**
[Statistics Fundamentals](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9) · [Machine Learning](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF)

**Why it was added:** *Essential Math for Data Science* gives you the mathematics and the Python. It does not always give you the picture. StatQuest is the best free source for the picture, and the two are unusually complementary — read Nield for the formula and the code, watch StatQuest for why the formula has that shape.

**Used surgically — specific videos on specific days, never as a playlist:**

| Concept | Video | Day |
|:--------|:------|:---:|
| Central Limit Theorem | [link](https://www.youtube.com/watch?v=YAlJCEDH2uY) | 51 |
| p-values | [link](https://www.youtube.com/watch?v=vemZtEM63GY) · [calculating them](https://www.youtube.com/watch?v=JQc3yx0-Q9E) | 53 |
| Hypothesis testing & the null | [link](https://www.youtube.com/watch?v=0oc49DyA3hU) | 53 |
| Linear regression | [link](https://www.youtube.com/watch?v=nk2CQITm_eo) | 71 |
| Gradient descent | [link](https://www.youtube.com/watch?v=sDv4f4s2SB8) | 72 |
| R-squared | [link](https://www.youtube.com/watch?v=bMccdk8EdGo) | 73 |
| Bias and variance | [link](https://www.youtube.com/watch?v=EuBBz3bI-aA) | 74 |
| Cross validation | [link](https://www.youtube.com/watch?v=fSytzGwwBVw) | 74 |
| Logistic regression | [link](https://www.youtube.com/watch?v=yIYKR4sgzI8) | 75 |
| Confusion matrix | [link](https://www.youtube.com/watch?v=Kdsp6soqA7o) | 76 |
| ROC and AUC | [link](https://www.youtube.com/watch?v=4jRBRDbJemM) | 77 |
| Decision trees | [link](https://www.youtube.com/watch?v=_L39rN6gz7Y) | 78 |
| Random forests | [link](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ) | 78 |
| Ridge / Lasso | [Ridge](https://www.youtube.com/watch?v=Q81RR3yKn30) · [Lasso](https://www.youtube.com/watch?v=NGf0voTMlcs) | 79 |
| K-means | [link](https://www.youtube.com/watch?v=4b5d3muPQmA) | 86 |
| PCA | [link](https://www.youtube.com/watch?v=FgakZw6K1QQ) | 86 |

---

### 3. 3Blue1Brown — Essence of Linear Algebra · **REINFORCEMENT**
[Playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) · selected chapters, ≈ 90 min total

**Why it was added:** Essential Math Chapter 4 teaches you to *compute* with vectors and matrices. 3Blue1Brown teaches you to *see* them — a matrix as a transformation of space, a determinant as an area scaling, an eigenvector as the direction that survives. Once you have seen that, PCA and the geometry of regression stop being formulas to memorise.

It also directly supports **MAT 265**, and the companion [Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) series is available as optional support for it.

---

### 4. Real Pakistani data · **PRACTICE**

| Source | What it gives you |
|:-------|:------------------|
| [PBS — Price Statistics](https://www.pbs.gov.pk/price-statistics/) | Monthly CPI, weekly SPI, WPI, urban/rural splits, in Excel. Genuinely messy: merged header cells, changing base years, inconsistent item names. |
| [Open Data Pakistan](https://opendata.com.pk/dataset) | Trade, demographic and provincial datasets |
| [Pakistan Data Hub](https://pakdatahub.com/) | REST API, ~23,000 economic series, JSON/CSV, free tier |

**Why it was added:** `Tem.txt` contains no datasets at all — its projects are all Kaggle classics. Project 1 is built on PBS price data because it is real, it is messy in instructive ways, it matters to people you know, and **nobody else's portfolio has it.** An analysis of what actually got more expensive in Pakistan this year is a conversation starter; a Titanic notebook is not.

---

### 5. SQL practice platforms · **PRACTICE**
[SQLBolt](https://sqlbolt.com/) (interactive, no signup) → [PostgreSQL Exercises](https://pgexercises.com/) (harder, real schema) → [DataLemur](https://datalemur.com/) (interview-style, free tier)

**Why it was added:** `Tem.txt` has a 5-hour SQL video and a good question bank, but no environment to practise in. SQL is a motor skill. The video gives you concepts once; these give you the hundreds of repetitions that make you fast. The Sheryians SQL course is retained as **PRIMARY** for concepts — [`p1epCuYb5OQ`](https://www.youtube.com/watch?v=p1epCuYb5OQ), entered by timestamp — with these as the practice layer.

---

### 6. Testing, project structure, and leakage discipline
`pytest` basics (Day 25) · `venv`, packages, module layout (Day 12) · data leakage and validation discipline (Day 74) · `Pipeline` / `ColumnTransformer` (Day 79)

**Why it was added:** none of it is in `Tem.txt`, and all of it is the difference between code that works on your laptop and code someone will hire you for. The leakage material in particular is the single most common fatal mistake in self-taught data science portfolios — a model that scores 0.97 because the answer leaked into the features.

---

## ♻️ Kept Despite Redundancy — On Purpose

| What repeats | Where | Why the repetition is correct |
|:-------------|:------|:------------------------------|
| **OOP taught four times** — Sheryians, CodeWithHarry, Apna College, Corey Schafer | Days 15–20 | Your explicit request, and your explicit weakness. Four voices on one hard topic beats one voice on four topics. They are also sequenced rather than stacked: concept → alternative explanation → practice → design depth. |
| **Statistics taught twice** — Essential Math + StatQuest | Days 46–56 | Different jobs. Nield gives the formula and the Python; Starmer gives the picture. Read first, watch second, then code it. |
| **Linear algebra taught twice** — Essential Math Ch. 4 + 3Blue1Brown | Days 65–68 | Computation vs geometry. Both are needed before ML. |
| **Regression taught twice** — Essential Math Ch. 5 + StatQuest + Sheryians ML Part 2 | Days 71–73 | Derivation, intuition, and scikit-learn implementation are three genuinely different skills. |
| **Calculus touched twice** — MAT 265 and Essential Math Ch. 1 | Days 10, 18, 19, 25 | Deliberate double-dipping: the same hour serves a graded university course and the mathematics under gradient descent. |

**What is *not* repeated:** beginner Python. You will not watch "what is a variable" three times. Days 2–14 use one primary course and drop into the others only where the primary failed you.

---

## ⏳ Deferred Past Day 90 — With Its Reason

| Topic | Why not now | When |
|:------|:------------|:-----|
| **Essential Math Ch. 7 — Neural Networks** | Needs Ch. 4–6 to be solid first. Reading it in December means reading words. | Early 2027, after the Ch. 5–6 material has been used in a project |
| Deep learning (ANN/CNN/RNN/Transformers) | See Removal 1 | 2027 |
| NLP, Computer Vision | Specialisations. Choose from evidence. | Mid-2027 |
| Spark, Hadoop, cloud, MLOps, Docker | No problem yet requires them | When a job does |
| Advanced SQL — stored procedures, query tuning, warehousing | Diminishing returns before you have queried anything real | After Project 2 |
| R | See Removal 5 | When the degree introduces it |
| Formal DSA | CSE 205 next semester | Spring 2027, for credit |

---

## 📖 Should You Buy More Books?

**Short answer: no, not during these 90 days.** You own the right book and you have not finished it.

Recommending books is the cheapest way to make a roadmap look serious, and the fastest way to guarantee none of them get read. *Essential Math for Data Science* is 8 chapters, scheduled across 20 days here, and finishing it is worth more than starting three others.

**Reconsider at Day 90**, and only against a gap the reviews actually reveal:

| If the Day 90 review says… | Then consider | Why it beats what you have |
|:---------------------------|:--------------|:---------------------------|
| "Pandas still feels like guessing" | **Python for Data Analysis** — Wes McKinney (O'Reilly) | Written by the author of Pandas. It is the reference the library was designed around. Free online. |
| "I can build models but not judge them" | **An Introduction to Statistical Learning** — James, Witten, Hastie, Tibshirani | The standard text on *why* models behave as they do. Free PDF, Python edition available. This is the natural sequel to Nield. |
| "I can analyse but not communicate" | **Storytelling with Data** — Cole Nussbaumer Knaflic | Short, practical, and the skill it teaches is the one that separates analysts who get promoted. |
| "I want to go deeper on ML practice" | **Hands-On Machine Learning** — Aurélien Géron | The best practical ML book there is — but it is 850 pages and assumes exactly the foundation these 90 days build. It is a 2027 book, not a now book. |

**Availability in Pakistan:** all four are on Amazon.com with international shipping, and ISL/Liberty Books in Lahore and Karachi stock O'Reilly titles. *Introduction to Statistical Learning* is **free and legal** as a PDF from [statlearning.com](https://www.statlearning.com/) — start there before spending anything.

---

## ⚠️ Assumptions Worth Checking

Three things this plan assumes. If any is wrong, say so and the plan adjusts.

1. **You have `Essential Math for Data Science` in hand now.** Chapter 1 is scheduled from Day 10. If the book has not arrived, those days move to StatQuest and 3Blue1Brown and the book slots in when it lands.
2. **Mid-semester exam dates are unknown.** The plan has no exam week in it because the academic calendar does not publish one. When you get your dates, mark them and convert the nearest review day into a pause.
3. **Your semester 1 course list is taken from the NIT programme page**, which lists CSE 110, MAT 265/170, CIS 105, WPC 150 and the SSC courses. If your actual enrolment differs — including the pending `SSC101 → PHI105` swap — the degree-alignment table in the README should be corrected, though nothing else in the plan depends on it.

---

<div align="center">

**[← README](./README.md)** · **[Day 1 →](./Month_1/Week_01/Day_01/Day_01.md)**

</div>
