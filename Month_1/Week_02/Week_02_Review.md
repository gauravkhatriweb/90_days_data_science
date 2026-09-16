# Week 2 Review — Files, Errors, and Your First Tool

|  |  |
|:--|:--|
| **Covers** | Days 8–14 · 23–29 September 2026 |
| **Topics** | Slicing · unpacking · sorting · exceptions · files · CSV parsing · modules · debugging |
| **Budget** | 45–60 min |
| **This week's reality** | Orientation Days 8–11 · SAT scores Day 10 · semester began Day 13 |

> Closed book unless stated. This was the hardest week to *schedule* in the whole ninety days — orientation, results day and the first day of classes all landed inside it. Grade the week accordingly.

---

## ⏸️ Catch-Up Rights

| Day | Done? | If not — MUST DO only |
|:---:|:-----:|:----------------------|
| 8 · Slicing, sorting | ☐ | Nine drills |
| 9 · Exceptions | ☐ | Exercises 7 and 8 — the anti-pattern and the batch processor |
| 10 · Reading day | ☐ | 25 minutes of reading. Nothing more. |
| 11 · Files & CSV | ☐ | Steps 4–6 of the parser |
| 12 · Modules + `shopsummary` | ☐ | **Do not skip this one.** It is the Month 1 milestone. |
| 13 · Debugging | ☐ | The five bugs |
| 14 · Consolidation | ☐ | The fourteen retrieval tasks |

> If you only have time for one missed day this week, **make it Day 12.** Everything in Month 2 assumes you can structure a project.

---

## 📝 Part 1 — Knowledge (closed book, 15 min)

1. Why is the slice stop exclusive, and what does `a[:n] + a[n:]` give you?
2. What is wrong with `except: pass`? Describe a concrete bug it hides.
3. When should a function return `None` on failure and when should it raise?
4. Name three things `pd.read_csv` has to guess, and what goes wrong when each guess is wrong.
5. What does `if __name__ == "__main__":` prevent?
6. What does a virtual environment isolate — and what does it *not* isolate?
7. Why read a traceback from the bottom up?
8. Your code crashes with `ZeroDivisionError`. Why might wrapping it in `try/except` be the wrong fix?

**Score: ___ / 8**

---

## 💻 Part 2 — Coding (closed book, 20 min)

**Task A — 6 min.** `parse_line(line)` handling a quoted field containing a comma, returning typed values, and returning `None` for a malformed line.

**Task B — 5 min.** `process_batch(rows)` returning `(processed, failures)` where failures carry an index, an exception type and a message. No bare `except`.

**Task C — 4 min.** Sort transactions by region ascending and revenue descending, take the top three per region. One expression for the sort.

**Task D — 5 min.** Sketch the module layout for a project that reads a file, cleans it, analyses it and prints a report. Name the files and say what goes in each.

**Score: ___ / 4**

---

## 🧩 Part 3 — Problem Solving (open book, 10 min)

> A 40 MB CSV arrives with 180,000 rows. Around 2% of rows are malformed in four different ways. You must produce a summary and a rejection report, and the machine has 8 GB of RAM.
>
> Write the **plan**, not the code. Address: how you read the file, how you detect each malformation, what you do with rejects, and why your approach does not load 40 MB into memory twice.

---

## 🔁 Part 4 — Retention Check

- [ ] I can write a multi-level sort key on the first attempt
- [ ] I never write a bare `except`
- [ ] I can parse a quoted CSV field by hand
- [ ] I can structure a package with `__init__.py` and import between modules
- [ ] I can use `breakpoint()` and inspect state without looking up commands
- [ ] I can explain what `requirements.txt` is for
- [ ] `shopsummary` runs, and I could rebuild its structure from memory

> Weak this week: ______________________________________________

---

## 🏗️ Part 5 — The Milestone

`shopsummary` is the first thing in this repository worth showing another person. Grade it honestly:

| | Yes | Notes |
|:--|:---:|:------|
| Runs without crashing on the messy fixture | ☐ | |
| Rejected rows show line number **and** reason | ☐ | |
| Median correct for an even count | ☐ | |
| Code split across modules sensibly | ☐ | |
| `render()` returns a string rather than printing | ☐ | |
| A stranger could run it from the README | ☐ | |

**If three or more are unticked, finish it before Day 15.** It is the foundation the OOP block refactors.

---

## 🎓 Part 6 — University Link

- **First week of classes.** What are your actual contact hours, and where does the daily study slot sit?
- **CSE 110:** has it started with syntax or with problem solving? Is Week 1–2 of this plan ahead of it, behind it, or level?
- **MAT 265:** has calculus started? Chapter 1 of Essential Math is scheduled for Days 18, 19 and 25 — does that timing still match your course?
- **The honest question:** now that you have seen a real week of university, is 60–90 minutes a day realistic, or is it 45?

---

## 🛠️ Part 7 — What Could I Build Now?

You built a CLI from eleven days of Python with zero dependencies. What is the second version of that tool — the one that would be genuinely useful to you or to a SwiftBase customer?

> ______________________________________________

---

## 💼 Part 8 — Career

Two weeks in. What can you now put on a CV honestly? Not "Python" — something specific and demonstrable.

> ______________________________________________

---

## 🔮 Part 9 — The Decision

| If… | Then… |
|:----|:------|
| Part 1 ≥ 6, Part 2 ≥ 3, `shopsummary` runs | ✅ **Continue.** Start the OOP block on schedule. |
| `shopsummary` incomplete | ⚠️ **Finish it first.** Use Day 15's IF TIME. The OOP block refactors this exact tool. |
| Part 2 ≤ 2 | ⚠️ **Slow down.** Move Day 15's material into Days 15–16 and push the block one day. |
| Everything clean and the week felt light | ⏩ Add Corey Schafer video 1 to tonight. |
| University is heavier than expected | 🔧 **Reduce, do not abandon.** Cut every IF TIME block for Week 3 and hold the MUST DO line. That is the designed failure mode. |

**My decision:**

> ______________________________________________

---

## 📊 Week 2 Scorecard

| Measure | Result |
|:--------|:-------|
| Days completed | ___ / 7 |
| Part 1 — knowledge | ___ / 8 |
| Part 2 — coding | ___ / 4 |
| Day 14 retrieval | ___ / 14 |
| Retention boxes | ___ / 7 |
| `shopsummary` checks | ___ / 6 |
| Honest hours this week | ___ h |
| **Biggest weakness** | |
| **Biggest win** | |

---

**[← Day 14](./Day_14/Day_14.md)** · **[Day 15 →](../Week_03/Day_15/Day_15.md)** · [README](../../README.md)
