# Day 27 — The Standard Library You Will Actually Use

|  |  |
|:--|:--|
| **Date** | Monday, 12 October 2026 |
| **Position** | Week 4 · Month 1 · Phase 1 — Python · **last Python-focused day** |
| **Budget** | **~75 min** |
| **Code file** | `Day_27.py` |

> **Why this is the last Python day.** From Day 29 the focus moves to NumPy, and Python becomes the tool rather than the subject. Before that, four standard-library modules deserve an hour, because you will use them in every project from here to Day 90 — and because two of them (`datetime` and `json`) are where real data work goes wrong most often.
>
> Nothing here is difficult. It is the difference between fighting these modules for twenty minutes each time and using them without thinking.

---

## 🎯 Objective

Handle paths, dates, counting and JSON fluently, and understand the specific traps in each.

---

## 📚 Learn

### 🔴 MUST DO — four modules, 30 minutes

**`pathlib` — stop using string paths**

```python
from pathlib import Path

d = Path("2026/september/daily_progress_tracking")
for p in sorted(d.glob("*-daily-log.md")):
    print(p.stem, p.suffix, p.parent.name)

d / "2026-09-16-daily-log.md"      # / joins paths, on every OS
p.exists() · p.is_file() · p.read_text(encoding="utf-8") · p.write_text(s)
Path(__file__).resolve().parents[2]  # walk up from the current file
```

The `/` operator is the whole point: `Path("a") / "b" / "c.txt"` works identically on macOS and Windows, and `os.path.join` becomes unnecessary.

**`datetime` — and the four traps**

```python
from datetime import date, datetime, timedelta

date.today()
date(2026, 9, 16)
datetime.strptime("2026-09-16", "%Y-%m-%d").date()    # string -> date
d.strftime("%A, %d %B %Y")                             # date -> string
d + timedelta(days=7)
(d2 - d1).days                                          # a timedelta
```

| Trap | What happens |
|:-----|:-------------|
| `date` vs `datetime` | `date(2026,9,16) == datetime(2026,9,16,0,0)` is **False** |
| Naive vs aware | A datetime with no timezone. You are in **Asia/Karachi (UTC+5)**; most APIs return UTC. Mixing them silently shifts every timestamp by five hours. |
| `strptime` format | One wrong character and it raises. `%Y` is 2026, `%y` is 26. |
| Month arithmetic | `timedelta` has no months. "One month later" is ambiguous and must be defined. |

The timezone trap is the one that will actually bite you — it is nearly invisible until an analysis comes out five hours wrong.

**`collections` — three tools**

```python
from collections import Counter, defaultdict, namedtuple

Counter(items).most_common(3)
Counter(a) - Counter(b)                 # multiset subtraction

by_key = defaultdict(list)
by_key[k].append(v)                     # no existence check

Row = namedtuple("Row", "item qty price")
r = Row("tea", 4, 1250.0)
r.item                                   # named access, tuple cost
```

`namedtuple` is worth a moment: it gives you `row.item` instead of `row[0]` at almost no cost, for a record whose shape is fixed. *(Day 32 shows you that a Pandas row is essentially this idea at scale.)*

**`json` — two traps**

```python
import json

json.loads(text)                            # string -> Python
json.dumps(obj, indent=2, ensure_ascii=False)
json.dump(obj, f) · json.load(f)            # no 's' = file
```

| Trap | Detail |
|:-----|:-------|
| Dates are not JSON | `json.dumps({"d": date.today()})` raises. Convert with `.isoformat()`. |
| `ensure_ascii=True` is the default | Urdu text comes out as `اردو`. Valid, unreadable. Set `ensure_ascii=False`. |

The second one matters for you specifically — any dataset with Urdu item names or place names will look corrupted without it.

### 🟢 IF TIME

- `argparse` — 15 minutes, and `Day_12.py` gets a real `--help`.
- `dataclasses` — a lighter way to write a class whose job is holding data. It would simplify `DailyLog`.

---

## 💻 Code

### 🔴 MUST DO

`Day_27.py` — ten exercises, all against your real LifeOS repository:

**`pathlib` (1–3)**
1. Find every daily log across all month directories with one `glob`. Count them by month.
2. From this file, build the path to `../../PILLARS/education.md` using `parents[]`. Confirm it exists.
3. Find the five largest markdown files in LifeOS, by size.

**`datetime` (4–6)**
4. Parse every log filename into a `date`. Find the earliest, the latest, and the count of distinct months.
5. **Reproduce the `date` vs `datetime` trap:** compare the two, watch it be `False`, then fix the comparison.
6. Compute how many days between today and Day 90 (14 December 2026), and how many of those are weekends.

**`collections` (7–8)**
7. `Counter` over every `## ` heading across all logs. Which section do you write most?
8. `namedtuple` for a log summary. Compare readability against a dict and a tuple.

**`json` (9–10)**
9. Export `lifelog`'s summary as JSON. **Hit the date-serialisation error on purpose**, then fix it.
10. Write a string containing Urdu with `ensure_ascii=True` and then `False`. Compare the files.

### 🟢 IF TIME

- Refactor `lifelog` to use `pathlib` and `namedtuple` throughout.

---

## 🔬 Understanding Check

1. **Reasoning.** Why is `Path("a") / "b"` better than `"a" + "/" + "b"`?
2. **Debugging.** Exercise 5: why is `date(2026,9,16) == datetime(2026,9,16)` `False`?
3. **Application.** An API returns UTC timestamps. You are in Asia/Karachi. What goes wrong if you ignore it, and how would you notice?
4. **Comparison.** `namedtuple` vs `dict` vs a class — when is each right?
5. **Understanding.** Why does `json.dumps` refuse a `date`? What does that tell you about JSON's type system?
6. **Application.** Exercise 10: what would `ensure_ascii=True` do to a dataset of Urdu product names?
7. **Data.** Exercise 7: what does your most-written section say about where your attention has actually gone this year?

---

## 🎯 Expected Outcome

- [ ] Use `pathlib` by default instead of string paths
- [ ] Parse and format dates without looking up format codes
- [ ] Reach for `Counter` and `defaultdict` naturally
- [ ] Serialise dates and non-ASCII text to JSON correctly

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Four modules | 30 min |
| Ten exercises | 38 min |
| Daily review | 7 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Six minutes, closed book. Write `log_stats(directory)` that finds every daily log, parses each filename to a date, and returns a JSON string with the count, the earliest and latest dates, and the three most common section headings. Dates must serialise. Non-ASCII must survive.

---

## 🔁 Daily Review

1. Which module did I most expect to already know but did not?
2. Exercise 7: what is my most-written section, and does it match what I think my priorities are?
3. Exercise 6: how many study days are left, and how many are weekends?
4. **Tomorrow is the Month 1 review.** Before opening it: in one sentence, what is the honest state of my Python?

---

## 📦 Completion Criteria

- [ ] All ten exercises run against real LifeOS data
- [ ] The `date`/`datetime` trap reproduced and fixed
- [ ] The JSON date error hit and fixed
- [ ] `ensure_ascii` difference observed in an actual file
- [ ] `log_stats` written closed-book
- [ ] Committed to git

---

**[← Day 26](../Day_26/Day_26.md)** · **[Day 28 →](../Day_28/Day_28.md)** · [README](../../../README.md)
