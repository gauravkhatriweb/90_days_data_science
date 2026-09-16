# Day 22 — Project P0: Reading Your Own Life

|  |  |
|:--|:--|
| **Date** | Wednesday, 7 October 2026 |
| **Position** | Week 4 · Month 1 · **OOP block, day 8 of 9** · **P0 build 1 of 3** |
| **Budget** | **~75 min** |
| **Code file** | `Day_22.py` + the `lifelog/` package |

> **Why this project and not a tutorial one.** Your LifeOS repository contains **116 daily log files** in `2026/*/daily_progress_tracking/`. They are real markdown, written by you over months, with inconsistent structure — some have fitness tables, some have strategic notes, some are nearly empty. That is exactly the kind of data you will spend your career on, and unlike a tutorial dataset, **you can tell when the output is wrong**, because you were there.
>
> P0 is a *learning vehicle*, not a portfolio piece. Its job is to make the OOP block land by forcing you to design something real. The portfolio projects start on Day 32.

---

## 🎯 Objective

Design and begin building an object-oriented tool that parses your own LifeOS daily logs — starting with the design, not the code.

---

## 📚 Learn

### 🔴 MUST DO

No new material. Days 15–21 supplied everything. Today is **design plus first build.**

### 🟢 IF TIME

- If Day 21 Part A scored 5–7: rewatch [Corey Schafer OOP 4 (Inheritance)](https://www.youtube.com/watch?v=RSl87lqOXDE) and [OOP 6 (Properties)](https://www.youtube.com/watch?v=jCzT9XFZ5bw) — 30 minutes, and it will pay off across the next three days.

---

## 📋 The Brief — `lifelog`

**Input:** `../../2026/*/daily_progress_tracking/*.md` — around 116 files, `YYYY-MM-DD-daily-log.md`.

**Output:** a summary across a date range, answering:

- How many logs exist, and which dates are missing from the range?
- What is the longest unbroken streak of logged days?
- Which sections appear most often? *(`## 🏋️ Fitness Tracking`, etc.)*
- How long is the average log, and which are the five longest and shortest?
- Which weekday do you log most consistently?

**Constraints — these are the point of the exercise:**

1. **No third-party libraries.** Standard library only. Pandas comes on Day 32, and doing this by hand first is what makes Pandas meaningful rather than magic.
2. **The source must be swappable** — a directory today, a single file or an in-memory list tomorrow. Day 18's composition, applied.
3. **The output format must be swappable** — text today, JSON later. Day 20's `ReportFormatter`.
4. **It must survive bad input.** Empty files, a wrong filename, unparseable dates. Day 9's rules.
5. **`__repr__` on every class.** Day 19.

---

## 💻 Code

### 🔴 MUST DO — design, then the parsing layer

**Step 1 — design first (20 min).** In `Day_22.py`, before any class, write:

- The classes you will need, and what each is *responsible for*
- For each: is it "is a" or "has a" relative to the others?
- The contract for `LogSource` and `Formatter`
- What `DailyLog` holds, and what it computes
- Where errors are caught, and where they are allowed to propagate

**Do not write code until this is done.** On Day 20 you learned that designing the contract first changes what you build. This is the day to prove it.

**Step 2 — build the parsing layer (55 min).**

1. `DailyLog` — one file. Attributes: `date`, `path`, `raw`, `sections`. Properties: `word_count`, `is_empty`, `weekday`. Plus `__repr__` and `__len__`.
2. `DailyLog.from_path(cls, path)` — a `classmethod` that parses the filename for the date and raises a clear error if it does not match the pattern
3. Section extraction — split on `## ` headings, keep the heading text and the body
4. `LogSource(ABC)` with `load() -> list[DailyLog]`
5. `DirectorySource(LogSource)` — globs a directory, skips non-matching filenames, and **reports** what it skipped rather than swallowing it
6. `ListSource(LogSource)` — takes `DailyLog` objects directly, for tests

**Step 3 — run it.** Point `DirectorySource` at your real `2026/september/daily_progress_tracking/`. Print how many parsed, how many were skipped and why. Expect surprises — that is the data being real.

### 🟢 IF TIME

- Add a `FileSource` for a single log. Notice you changed nothing else.

---

## 🔬 Understanding Check

1. **Design.** Which relationships in your design are "is a" and which are "has a"? Justify one of each.
2. **Reasoning.** Why is `from_path` a `classmethod` rather than logic inside `__init__`?
3. **Application.** A file is named `2026-09-31-daily-log.md` — a date that does not exist. Where should that be caught, and what should happen?
4. **Reasoning.** Constraint 1 forbids third-party libraries. What are you learning that `pandas.read_csv` would have hidden?
5. **Understanding.** Which parts of your design would need to change to read from a database instead of a directory? If the answer is more than one class, redesign it.
6. **Self-check.** Did designing first change what you built? Compare with how you approached Day 12.

---

## 🎯 Expected Outcome

- [ ] A written design with responsibilities and relationships, produced before code
- [ ] `DailyLog` parses a real log file and reports its sections
- [ ] Two interchangeable sources behind one interface
- [ ] It runs on your real logs and reports what it could not parse

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Design (step 1) | 20 min |
| Build the parsing layer (step 2) | 45 min |
| Run on real data (step 3) | 5 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Point it at the real September directory. It passes when it parses every valid log, skips invalid filenames **with a reason**, and crashes on nothing.

---

## 🔁 Daily Review

1. How many logs parsed? How many were skipped, and for what reasons?
2. What surprised me about my own data?
3. Did designing first change the build?
4. Which OOP concept from Days 15–21 did I use without having to think about it?

---

## 📦 Completion Criteria

- [ ] Design written before any class
- [ ] `DailyLog` with `from_path`, three properties, `__repr__`, `__len__`
- [ ] `LogSource` ABC with two implementations
- [ ] Runs on real September logs
- [ ] Skipped files reported with reasons
- [ ] Committed to git

---

**[← Week 3 Review](../../Week_03/Week_03_Review.md)** · **[Day 23 →](../Day_23/Day_23.md)** · [README](../../../README.md)
