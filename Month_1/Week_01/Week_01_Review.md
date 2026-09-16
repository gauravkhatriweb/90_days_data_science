# Week 1 Review — Python Foundations

|  |  |
|:--|:--|
| **Covers** | Days 1–7 · 16–22 September 2026 |
| **Topics** | Environment · idiom · control flow · functions · data structures · comprehensions · text |
| **Budget** | 45–60 min |
| **This week's reality** | Days 1–5 free and full · Days 6–7 cut to 45 min for orientation |

> This review is not "how did the week go." It is a **test**, then a **decision**. The test tells you what is real; the decision changes next week. Both parts are required.
>
> **Rule: everything below is closed-book unless it says otherwise.** Looking things up turns an assessment into a reading exercise and tells you nothing.

---

## ⏸️ First: Catch-Up Rights

If you missed a day this week, **use part of today's 60 minutes to do that day's 🔴 MUST DO block only.** That is a correct use of this slot. Do not attempt to replay a whole missed day.

| Day | Done? | If not — MUST DO only |
|:---:|:-----:|:----------------------|
| 1 · Setup + diagnostic | ☐ | Environment + the 12-task diagnostic |
| 2 · Idiom | ☐ | Nine exercises |
| 3 · Control flow | ☐ | Ten exercises, especially ex 10 |
| 4 · Functions | ☐ | The nine helpers |
| 5 · Data structures | ☐ | Ex 1–10, especially ex 7 timings |
| 6 · Comprehensions | ☐ | Eight conversions |
| 7 · Text | ☐ | Seven drills, especially ex 7 |

---

## 📝 Part 1 — Knowledge (closed book, 15 min)

Write full sentences. "I know this" is not an answer.

1. Python treats an empty list as false. Name one bug this prevents and one it causes.
2. What is the difference between `is` and `==`, and when is `is` the *only* correct choice?
3. Why does `my_list.sort()` return `None`?
4. What exactly happens, and when, in the mutable-default-argument bug?
5. Why is `x in some_set` faster than `x in some_list`? Give both costs in Big-O.
6. Why can a tuple be a dictionary key when a list cannot?
7. Name two situations where a comprehension is the wrong choice.
8. Write the six-step text-cleaning sequence in order.

**Score: ___ / 8.** Anything under 6 means next week's IF TIME blocks belong to re-reading those specific topics.

---

## 💻 Part 2 — Coding (closed book, 20 min)

Create `week_01_test.py`. No notes, no AI, no autocomplete acceptance. Timer on.

**Task A — 6 min.** Given a list of transaction dicts (`item`, `region`, `qty`, `price`), return revenue per region as a dict. Skip invalid rows and report how many you skipped.

**Task B — 5 min.** Write `clean(raw: str) -> str` that strips, lowercases, collapses internal whitespace and removes non-alphanumeric characters except spaces. Full docstring with the empty-input case documented.

**Task C — 5 min.** Given two lists of customer ids, return: who is in both, who is only in the first, and the total number of unique customers. Use the right structure.

**Task D — 4 min.** Convert this loop to a comprehension, then say in a comment whether you should have:
```python
out = []
for r in rows:
    if r.get("qty", 0) > 0:
        out.append((r["item"], r["qty"] * r["price"]))
```

**Score: ___ / 4 tasks completed inside their time limits.**

---

## 🧩 Part 3 — Problem Solving (open book, 10 min)

A problem you have not seen.

> You have two files. `sales.csv` has `date,item,qty`. `prices.csv` has `item,price`, but some items appear in `sales.csv` that are missing from `prices.csv`.
>
> Without using any library: describe the structures you would build, in what order, and how you would handle the missing items. Do not write the code — write the **plan**, and justify each structural choice.

This is the actual skill. Everything else this week was equipment.

---

## 🔁 Part 4 — Retention Check

Answer without scrolling back to any day file.

- [ ] I can write a function with keyword-only arguments, a docstring and type hints from memory
- [ ] I can write `enumerate` and `zip` correctly on the first try
- [ ] I can write a dict comprehension with a condition from memory
- [ ] I can explain why a dict lookup is O(1) to an interviewer
- [ ] I can list the mutable and immutable built-in types
- [ ] I can clean a messy string to a typed value in one chained expression

**Any box unticked is a named weakness, not a vague feeling. Write it down:**

> Weak this week: ______________________________________________

---

## 🎓 Part 5 — University Link

- **CSE 110 (Principles of Programming):** which of this week's topics has your course already covered, and which is ahead of it?
- **CSE 205 (next semester — OOP and Data Structures):** Day 5's cost table is the start of that course. Does the idea of "membership is O(1) in a hash table" make sense to you yet, or is it still a fact you memorised?
- **Orientation:** two things you learned about NIT that affect how you plan the next twelve weeks.

---

## 🛠️ Part 6 — What Could I Build Now?

Honestly — with only this week's Python, name one small thing you could build that would be genuinely useful to you. Not a tutorial project. Something you would actually run.

> ______________________________________________

*(Hold the idea. Day 12 builds something like it, and Days 22–26 turn it into an object-oriented system.)*

---

## 💼 Part 7 — Career

Which skill did this week make you measurably more employable in? Be specific — "Python" is not an answer, "I can write a validation function that reports why rows were rejected" is.

> ______________________________________________

---

## 🔮 Part 8 — The Decision

This review is allowed to change next week. Pick one and act on it.

| If… | Then… |
|:----|:------|
| Part 1 ≥ 6 **and** Part 2 ≥ 3 | ✅ **Continue as planned.** Week 2 runs as written. |
| Part 2 ≤ 2 tasks | ⚠️ **Slow down.** Add the failed tasks to Days 8 and 9 as warm-ups. Drop Week 2's IF TIME blocks. |
| Part 1 ≥ 7 **and** Part 2 = 4, comfortably | ⏩ **Compress.** Days 8–9 are light orientation days anyway — use the saved time to start Day 15's OOP video early. Bank the day. |
| Day 1 diagnostic was 9+ and this week felt slow | ⏩ **Compress harder.** Merge Days 8–9 into one and move the OOP block forward by two days. Record the change here. |

**My decision:**

> ______________________________________________

**Changes to Week 2:**

> ______________________________________________

---

## 📊 Week 1 Scorecard

| Measure | Result |
|:--------|:-------|
| Days completed | ___ / 7 |
| Day 1 diagnostic score | ___ / 12 |
| Part 1 — knowledge | ___ / 8 |
| Part 2 — coding | ___ / 4 |
| Retention boxes ticked | ___ / 6 |
| Honest hours this week | ___ h |
| **Biggest weakness** | |
| **Biggest win** | |

---

**[← Day 7](./Day_07/Day_07.md)** · **[Day 8 →](../Week_02/Day_08/Day_08.md)** · [README](../../README.md)
