# Day 26 — Assessment Day, and Lazy Evaluation

|  |  |
|:--|:--|
| **Date** | Sunday, 11 October 2026 |
| **Position** | Week 4 · Month 1 · Phase 1 — Python |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_26.py` |

> **Why a timed closed-book assessment.** Twenty-five days of Python end today. Everything from here assumes you can write Python without stopping to look things up — because from Day 29 the difficulty moves to NumPy, statistics and models, and if the language is still costing you attention, all of that gets harder.
>
> This is a **measurement, not a judgement.** Whatever the score is, it changes the next month in a specific, useful way. A bad score caught today costs a few days. A bad score discovered in November costs a month.

---

## 🎯 Objective

Measure Python competence under time pressure without help, then learn the one concept that connects Day 6's comprehensions to how Pandas actually works.

---

## 📚 Learn — Iterators and generators (35 min)

### 🔴 MUST DO — *after* the assessment, not before

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians Python `9:18:32 → 9:45:00`](https://www.youtube.com/watch?v=_aWbUudZ5Yo) · @1.75× | PRIMARY | 15 min | Decorators and generators |
| The section below | REFERENCE | 20 min | Why this matters for data work |

### The idea: compute when asked, not before

```python
def read_all(path):               # EAGER -- 2 GB file, 2 GB of RAM
    return open(path).readlines()

def read_lazy(path):              # LAZY -- one line at a time
    with open(path) as f:
        for line in f:
            yield line.strip()
```

`yield` turns a function into a **generator**. It produces one value, pauses, and resumes where it left off when asked for the next. Nothing is computed until something asks.

```python
lines   = read_lazy("big.csv")              # nothing has been read yet
cleaned = (clean(l) for l in lines)         # still nothing
totals  = (parse(c) for c in cleaned)       # still nothing
first10 = list(itertools.islice(totals, 10))  # NOW ten lines are read
```

Three chained transformations over a 2 GB file, and only ten lines were ever touched. This is a **pipeline** — and it is the mental model behind how real data tools are built.

### The trade-offs you must know

| | Generator | List |
|:--|:--|:--|
| Memory | One item at a time | All of it |
| Reusable | **No — exhausted after one pass** | Yes |
| `len()` | No | Yes |
| Indexing | No | Yes |
| Best for | Large or streaming data, one pass | Small data, multiple passes |

**The trap:** a generator can only be consumed once.

```python
rows = (parse(l) for l in lines)
total = sum(r["qty"] for r in rows)
count = len(list(rows))              # 0 -- rows is already exhausted
```

This produces a silently wrong answer, not an error. It is on this page because it *will* happen to you.

### `yield` in your own code

`lifelog`'s `DirectorySource.load()` returns a list of 116 objects. That is fine at 116. At 100,000 logs you would want:

```python
def iter_logs(self):
    for path in sorted(self.directory.glob("*-daily-log.md")):
        try:
            yield DailyLog.from_path(path)
        except ValueError as e:
            self.skipped.append((path.name, str(e)))
```

Same code, constant memory.

### Where this connects

`itertools` — `islice`, `chain`, `groupby`, `takewhile` — is a toolkit of generator operations. `groupby` in particular is the same idea you will meet as `pandas.groupby` on Day 34, and as `GROUP BY` in SQL on Day 34 as well. **Three different syntaxes, one concept.** Seeing that now means learning it once instead of three times.

---

## 💻 Code

### 🔴 MUST DO — Part A: the assessment (75 min, closed book, timed)

**Rules, and they matter:** no notes, no AI, no documentation, no autocomplete acceptance. Timer running. If a task overruns its budget, stop and move on — **an incomplete answer scored honestly is more useful than a complete one with help.**

| # | Time | Task |
|:-:|:----:|:-----|
| 1 | 8 min | Parse a messy CSV line with a quoted comma into a typed dict |
| 2 | 8 min | Group rows by two keys and sum a third. Choose and justify the structure. |
| 3 | 10 min | A class with `__init__`, a cached `@property`, a mutator that invalidates it, and `__repr__` |
| 4 | 10 min | An ABC with one abstract method, plus two implementations, plus one function using both |
| 5 | 8 min | A function returning `(results, failures)` over rows that break in three different ways |
| 6 | 7 min | Multi-level sort, then top-N per group |
| 7 | 7 min | Two comprehensions — one list, one dict, both with conditions |
| 8 | 10 min | Given a function, write four pytest tests including the empty case |
| 9 | 7 min | Find and fix three bugs in supplied code |

**Score honestly: 1 point each, 0.5 if it works but is not clean.**

| Score | Meaning | What changes |
|:-----:|:--------|:-------------|
| **8–9** | Python is no longer the obstacle | Month 2 as written |
| **6–7.5** | Solid, with gaps | Note the failed tasks. Use Month 2's IF TIME blocks on them. |
| **4–5.5** | Shaky | Add a 20-minute Python warm-up to Days 29–35. Do not delay Month 2. |
| **< 4** | Not ready | **Repeat Days 15–21 during Week 5's IF TIME.** Still start NumPy on schedule — Pandas will reinforce the Python. |

### 🔴 MUST DO — Part B: generators (35 min)

10. Convert `DirectorySource.load()` to `iter_logs()` using `yield`
11. Build a three-stage lazy pipeline: read → clean → parse. Prove with a print statement that nothing runs until consumed.
12. **The exhaustion trap:** reproduce the silently-wrong-answer bug. Then fix it two ways — materialise once, or iterate twice — and say which you would ship.
13. Use `itertools.islice` to take the first 10 from an infinite generator
14. Use `itertools.groupby` to group sorted logs by month. **Note the precondition** — it only groups *adjacent* equal keys, which is the thing everyone gets wrong once.
15. Measure the memory difference with `sys.getsizeof` on a list vs a generator over 1,000,000 items

### 🔴 MUST DO — Part C: ship P0 (20 min)

16. Run the full test suite — all green
17. Update `lifelog/README.md` with real output from your 116 logs
18. Final commit: `"P0 complete: lifelog -- OOP toolkit over LifeOS daily logs"`
19. Write three sentences: what P0 taught you that Days 15–21 alone did not

---

## 🔬 Understanding Check

1. **Comparison.** Generator or list — for a 5 GB file read once? For 100 values used five times?
2. **Debugging.** Exercise 12 gave a wrong answer with no error. Why is that worse than a crash?
3. **Understanding.** What does `yield` do to a function's execution?
4. **Application.** Where in `lifelog` would `yield` genuinely help, and where would it just be showing off?
5. **Reasoning.** `itertools.groupby` needs sorted input. Why, given how it works?
6. **Connection.** `itertools.groupby`, `pandas.groupby` and SQL `GROUP BY` — what is the shared concept?
7. **Self-assessment.** Part A score, and which three tasks were weakest? Name them specifically.

---

## 🎯 Expected Outcome

- [ ] A measured, honest Python score
- [ ] Generators used naturally, including a lazy pipeline
- [ ] The exhaustion trap recognisable on sight
- [ ] P0 shipped with green tests and a real README

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Part A — assessment, timed | 75 min |
| Generators reading + video | 35 min |
| Part B — exercises | 35 min |
| Part C — ship P0 | 20 min |
| Daily review | 15 min |
| **Total** | **~180 min** |

---

## 🧪 Mini Assessment

Part A is the assessment. **The score is not the point — the named weaknesses are.** Write them down as specific capabilities ("cannot write an ABC without looking up the import"), not as topics ("OOP").

---

## 🔁 Daily Review

1. Part A: ___ / 9. Which three tasks were weakest?
2. Which task did I run out of time on, and was it thinking or recall?
3. Did I reproduce the exhaustion trap, or did I avoid it by accident?
4. **P0 is shipped.** What did building it teach me that the OOP days alone did not?
5. Month 1 ends in two days. What do I most want to have fixed before Month 2?

---

## 📦 Completion Criteria

- [ ] Part A completed closed-book and timed, scored honestly
- [ ] Three specific weaknesses named
- [ ] All six generator exercises done, including the exhaustion trap
- [ ] P0 shipped: green tests, real README, final commit
- [ ] The action from the score table applied to Month 2
- [ ] Committed to git

---

**[← Day 25](../Day_25/Day_25.md)** · **[Day 27 →](../Day_27/Day_27.md)** · [README](../../../README.md)
