# Day 25 — Testing: Proving It Works

|  |  |
|:--|:--|
| **Date** | Saturday, 10 October 2026 |
| **Position** | Week 4 · Month 1 · Phase 1 — Python |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_25.py` + `tests/test_lifelog.py` |
| **Second track** | 📐 **Essential Math Ch. 1, pp. 31–39** (45 min) — chain rule and integrals |

> **Why testing, and why here.** You built `lifelog` and you believe it works. Do you know that your streak calculation handles a single-day streak? An empty collection? Two identical dates? You checked one month by hand on Day 23 — that is one case out of many.
>
> Testing is also the payoff for Day 18. You built `ListSource` specifically so the pipeline could be tested without files. Today that design decision cashes out — and you will feel why composition mattered.
>
> **And for the portfolio:** a repository with tests reads as professional. A repository without them reads as a tutorial. It is one of the cheapest quality signals there is.

---

## 🎯 Objective

Write tests that would have caught a real bug, and understand why testable code and well-designed code are the same thing.

---

## 📚 Learn — Track 1: pytest (≈ 30 min)

### 🔴 MUST DO

No video. pytest's value is in the habit, not the API — the API is about six things.

```python
# tests/test_lifelog.py
from datetime import date
from lifelog.analysis import LogCollection

def test_empty_collection_has_no_streak():
    assert LogCollection([]).longest_streak() is None

def test_single_log_is_a_streak_of_one():
    logs = [make_log(date(2026, 9, 1))]
    assert LogCollection(logs).longest_streak() == (date(2026,9,1), date(2026,9,1), 1)

def test_gap_breaks_the_streak():
    logs = [make_log(date(2026,9,1)), make_log(date(2026,9,2)), make_log(date(2026,9,5))]
    start, end, length = LogCollection(logs).longest_streak()
    assert length == 2
```

```bash
pytest -v          # run everything
pytest -k streak   # only tests with 'streak' in the name
pytest -x          # stop at the first failure
```

**The six things worth knowing:**

| Thing | Use |
|:------|:----|
| `test_*.py`, `def test_*` | How pytest finds tests. That is all the configuration there is. |
| `assert` | Plain Python. pytest rewrites it to show you both values on failure. |
| Fixtures (`@pytest.fixture`) | Shared setup |
| `pytest.raises` | Assert that something *does* fail |
| `@pytest.mark.parametrize` | One test, many inputs |
| A descriptive test name | The name is documentation — `test_gap_breaks_the_streak` tells you what broke |

### The three cases people forget — and where the bugs are

For every function: **the empty case, the single case, the boundary case.**

| Function | Empty | Single | Boundary |
|:---------|:------|:-------|:---------|
| `longest_streak` | `[]` → ? | one log → 1, not 0 | two adjacent days → 2 |
| `missing_dates` | `[]` → ? | one log → `[]` | a gap of exactly one day |
| `mean` | `[]` → ? crash or 0? | one value | all identical |
| `median` | `[]` → ? | one value | **even count** ← the Day 12 bug |
| `filter` | no matches → ? | exact boundary date | start == end |

**Write the empty case first for every function.** It catches more real bugs than any other single habit, because empty inputs happen constantly in real data and almost never in the examples you tested with by hand.

### Testable code and good design are the same thing

If a function is hard to test, it usually has one of three problems: it does too much, it reads a file or the clock in the middle of its logic, or it depends on something you cannot substitute.

`lifelog` avoids all three — because `LogCollection.from_source()` takes any `LogSource`, so `ListSource` lets you test the analysis without ever touching a disk. That was Day 18's composition argument, and today is the proof.

---

## 📐 Learn — Track 2: Essential Math Ch. 1, pp. 31–39 (45 min)

**Read:** *The Chain Rule · Integrals · Conclusion · Exercises.*

Then **do the chapter exercises** — Nield's answers are in Appendix B. This is the one chapter whose exercises you should actually complete, because Chapter 1 underpins Chapters 5, 6 and 7.

### Why the chain rule is the most important thing in this chapter

A neural network is functions nested inside functions. Training one means asking "if I nudge this weight, how much does the final error change?" — and the answer has to travel back through every nested layer.

**That is the chain rule.** Backpropagation is the chain rule applied repeatedly. You are not doing neural networks in these 90 days, but **Day 72's gradient descent uses the same idea on a simpler function**, and understanding it there is what makes the rest possible later.

### Integrals — and why they get less time here

An integral is the area under a curve. You need them for probability density — the probability that a value falls between two points *is* the area under the curve between them. That is Day 50.

You do not need to compute integrals by hand. Nield uses SymPy and so will you.

### The MAT 265 link

Chapter 1 is now complete, and it has covered a substantial part of your calculus syllabus: limits, derivatives, the chain rule, integrals. **Note in the review how much of MAT 265 this has pre-taught.** That ratio is the evidence for whether the maths track is worth its time — and if it is high, it is an argument for adding EMDS reading during exam weeks rather than dropping it.

---

## 💻 Code

### 🔴 MUST DO

**Part A — set up (15 min)**
1. `pip install pytest`, create `tests/`
2. Write `make_log(date, raw="")` — a helper that builds a `DailyLog` without a file
3. Confirm `pytest` discovers and runs one trivial test

**Part B — test the analysis layer (50 min)**
4. `longest_streak` — empty, single, gap, all-consecutive, duplicate dates, unsorted input
5. `missing_dates` — empty, no gaps, one gap, a gap at the boundary
6. `filter` — no matches, all match, `start == end`, boundary dates included or not *(decide, then test what you decided)*
7. `section_frequency` — logs with no sections, duplicated headings
8. `__len__`, `__contains__`, `__getitem__` including a negative index

**Part C — test the parsing layer (30 min)**
9. `DailyLog.from_path` with a bad filename → the right exception, with a useful message
10. `from_path` with `2026-09-31` → must fail, and say why
11. An empty file → `is_empty` is `True`
12. A file with headings but no body → also `is_empty`? **Decide, document, test.**
13. `DirectorySource` on a directory with two valid and two invalid files → 2 loaded, 2 skipped with reasons

**Part D — the payoff (10 min)**
14. Run the whole suite. **Note every test that fails.** Those are real bugs you did not know about.
15. Fix them. For each, write in a comment: would you have found this without the test?

### 🟢 IF TIME

- `@pytest.mark.parametrize` over five streak scenarios in one test function.
- `pytest --cov=lifelog` — but treat coverage as a map of what is untested, never as a score to maximise.

---

## 🔬 Understanding Check

1. **Reasoning.** Why write the empty case first?
2. **Application.** How many tests failed on the first full run? What does that number say about "I checked it by hand"?
3. **Comparison.** `ListSource` vs reading real files in tests — name three advantages.
4. **Understanding.** What makes a function hard to test, and why is that the same as hard to reuse?
5. **Reasoning.** Exercise 12 had no right answer until you chose one. What does that say about where behaviour is really defined?
6. **Maths.** State the chain rule in words. Why will gradient descent need it?
7. **Maths.** Why is the probability of a value falling in a range an *integral*?
8. **Career.** A reviewer sees a `tests/` directory. What does it tell them, beyond "the code works"?

---

## 🎯 Expected Outcome

- [ ] Write pytest tests without looking up the API
- [ ] Cover empty, single and boundary cases by habit
- [ ] Find at least one real bug in code you believed was correct
- [ ] Explain why testable and well-designed are the same property
- [ ] Complete Essential Math Chapter 1

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Read the pytest section | 20 min |
| Part A — setup | 15 min |
| Part B — analysis tests | 50 min |
| Part C — parsing tests | 30 min |
| Part D — run and fix | 10 min |
| **Essential Math pp. 31–39 + exercises** | 45 min |
| Daily review | 10 min |
| **Total** | **~180 min** |

---

## 🧪 Mini Assessment

Take the streak bug you found — or plant one deliberately — and confirm that a test catches it. **A test that cannot fail is not a test.** This is the single most useful check on a test suite.

---

## 🔁 Daily Review

1. How many tests failed on the first run? Which surprised me most?
2. Would I have found that bug without a test? Honestly?
3. Exercise 12: what did I decide, and why?
4. **Maths:** Chapter 1 is done. What fraction of MAT 265 so far has it pre-taught?
5. Can I state the chain rule in one sentence without looking?

---

## 📦 Completion Criteria

- [ ] `tests/test_lifelog.py` with 15+ tests
- [ ] Every function has an empty-case test
- [ ] At least one real bug found and fixed
- [ ] A deliberately planted bug is caught by a test
- [ ] **Essential Math Chapter 1 complete, exercises done**
- [ ] Chain rule written in my own words
- [ ] Committed to git

---

**[← Day 24](../Day_24/Day_24.md)** · **[Day 26 →](../Day_26/Day_26.md)** · [README](../../../README.md)
