# Day 1 — Setup, The Field, and an Honest Starting Line

|  |  |
|:--|:--|
| **Date** | Wednesday, 16 September 2026 |
| **Position** | Week 1 · Month 1 · Phase 1 — Python |
| **Budget** | **~120 min** — no university yet, this is one of your five highest-capacity days |
| **Code file** | `Day_01.py` |

> **Why today looks like this.** You have five completely free days before orientation. Wasting Day 1 on motivational content would be a real loss. So today does three things that pay off for the next 89 days: a working environment, a clear map of the field, and — most importantly — **an honest measurement of what you can already do**, because the rest of this plan gets compressed or expanded based on that answer.

---

## 🎯 Objective

Finish today knowing exactly where you stand in Python, with an environment you will not have to fight again, and a clear mental model of what "data science" actually means as a set of jobs.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [IBM — What is Data Science?](https://www.youtube.com/watch?v=RBSUwFGa6Fk) *(Tem.txt lines 1–100)* | PRIMARY · video | 8 min | The four analytics types and the data science lifecycle. Watch once, never again. |
| [IBM — Data Analytics vs Data Science](https://www.youtube.com/watch?v=dcXqhMqhZUo) *(Tem.txt lines 101–186)* | PRIMARY · video | 6 min | The actual job titles and what separates them. This matters for where you aim. |
| Environment setup — below | PRACTICE | 35 min | Python 3.12+, virtual environment, VS Code, Jupyter |

If either IBM link has moved, the full transcripts are in `Tem.txt` — reading them is equivalent and faster.

### 🟢 IF TIME

- Skim the *Essential Math for Data Science* preface and table of contents. You are not reading it yet — you are seeing the shape of the eight chapters so the schedule makes sense.

---

## 🧠 Core Concepts

**The four analytics questions.** Everything in data science is one of these, and they increase in both value and difficulty:

| Type | Question | Example |
|:-----|:---------|:--------|
| Descriptive | *What happened?* | Did sales go up or down? |
| Diagnostic | *Why did it happen?* | Why did sales drop in October? |
| Predictive | *What will happen?* | What will next quarter look like? |
| Prescriptive | *What should we do?* | What action raises sales 10%? |

Most working analysts live in the first two. Most beginners try to start at the third. That is backwards, and this plan does not do it.

**The lifecycle.** Business understanding → data acquisition → cleaning → exploration → modelling → communication. Notice that *business understanding comes first* and *communication comes last* — the two ends of the pipeline are both non-technical, and both are where you already have an advantage.

**Where you might land.** Data Analyst, Business Analyst, Data Scientist, ML Engineer. They overlap heavily at entry level, and the common denominator is **SQL + Python + the ability to explain a finding**. That is why this plan front-loads those three.

---

## 💻 Code

### 🔴 MUST DO — Environment

Work through the setup block in `Day_01.py`. The goal is a project you can return to for 90 days:

```
90_days_data_science/
└── .venv/          ← one virtual environment for the whole challenge
```

1. Confirm `python3 --version` is 3.11 or newer.
2. Create the virtual environment at the repository root, activate it.
3. Install the working set: `numpy pandas matplotlib seaborn scipy sympy scikit-learn jupyterlab pytest`.
4. Confirm `jupyter lab` opens.
5. Create a `.gitignore` entry for `.venv/` — you do not want 300 MB in a public repo.

### 🔴 MUST DO — The diagnostic

`Day_01.py` contains **12 tasks in rising difficulty**, from "print a string" to "write a class with a dunder method". Attempt them **closed-book** — no searching, no AI, no notes. Write what you can; leave what you cannot.

This is not a test you pass or fail. It is a measurement that changes the plan:

| Score | What it means | What changes |
|:-----:|:--------------|:-------------|
| **1–4** | Genuine Python beginner | Run Days 2–14 at full length. Do all IF TIME blocks. |
| **5–8** | You can program, Python idiom is the gap | **Expected.** Run the plan as written; watch video at 1.5–2×. |
| **9–11** | Comfortable, OOP is the hole | Compress Days 2–9 into 4 days, bank the time, start the OOP block early. |
| **12** | Python is not your problem | Skip to Day 15. Tell the Week 1 review why. |

Record your honest score in the Daily Review at the bottom of this file.

### 🟢 IF TIME

- Make the first commit of the challenge: `git add . && git commit -m "Day 1: environment + baseline diagnostic"`.

---

## 🔬 Understanding Check

Answer in writing, in your own words. Two or three sentences each.

1. **Comparison.** A shop owner asks "why did my sales fall last month?" and "what will my sales be next month?" — which analytics type is each, and which is genuinely harder to answer well? Why?
2. **Reasoning.** The IBM lifecycle puts *business understanding* before *data mining*. What specifically goes wrong if you reverse them?
3. **Application.** Pick one real question about SwiftBase's target customers. Which of the four analytics types is it, and what data would you need to answer it?
4. **Teaching.** Explain the difference between a data analyst and a data scientist to someone who has never used a spreadsheet. No jargon.
5. **Self-assessment.** Looking at your diagnostic score — which specific Python topic cost you the most marks? Name it precisely; that topic gets your attention this week.

---

## 🎯 Expected Outcome

By the end of today I can:

- [ ] Activate a working Python environment with all nine libraries importing cleanly
- [ ] Name the four analytics types and give an example of each
- [ ] State honestly which Python concepts I know and which I do not
- [ ] Explain why this plan front-loads SQL and statistics ahead of machine learning

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| IBM videos (both) | 15 min |
| Environment setup | 35 min |
| Diagnostic, closed-book | 50 min |
| Scoring + daily review | 20 min |
| **Total** | **~120 min** |

---

## 🧪 Mini Assessment

Without looking anything up, write a single Python file that:

1. Defines a list of five dictionaries, each representing a shop transaction with `item`, `qty`, `price`
2. Computes total revenue
3. Finds the item with the highest revenue
4. Prints a two-column summary

If you can do this in under 15 minutes, your Days 2–5 will move fast. If you cannot, that is exactly what Days 2–5 are for.

---

## 🔁 Daily Review

*5–10 minutes. Write, do not just think.*

1. **Diagnostic score:** __1_ / 12
2. Which task was the first one I could not do? What concept was it testing?
3. What surprised me about the difference between data analysis and data science?
4. Based on my score, which row of the table above applies to me — and am I honestly applying it, or am I flattering myself?

---

## 📦 Completion Criteria

**Day 1 is complete when:**

- [ ] `.venv` exists, is activated, and all nine libraries import without error
- [ ] Both IBM videos watched (or both transcripts read)
- [ ] All 12 diagnostic tasks attempted closed-book, and scored honestly
- [ ] The five Understanding Check questions answered in writing
- [ ] Daily Review filled in, including your score
- [ ] Committed to git

---

**[Day 2 →](../Day_02/Day_02.md)** · [Week 1](../Week_01_Review.md) · [README](../../../README.md)
