# Day 12 — Modules, Packages, and Your First Real Tool

|  |  |
|:--|:--|
| **Date** | Sunday, 27 September 2026 |
| **Position** | Week 2 · Month 1 · Phase 1 — Python |
| **Budget** | **~180 min** — ⭐ **Your last completely free day until January.** Use it properly. |
| **Code file** | `Day_12.py` + a small package you create |

> **Why today looks like this.** Tomorrow the semester starts and your days drop to 60–90 minutes for the next three months. So today is the Phase 1 milestone: you stop writing exercises and **build a tool** — one that reads a real CSV, computes real summaries, and runs from a command line. Every technique from Days 1–11 goes into it.
>
> It is also the day you learn how Python code is organised into files, because from tomorrow onward every project you build has more than one file in it.

---

## 🎯 Objective

Organise Python across multiple files correctly, and ship a working command-line tool built entirely from what you have learned in eleven days — with no third-party libraries.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [CodeWithHarry `8:15:38 → 9:16:57`](https://www.youtube.com/watch?v=UrsmFxEIp5k) | PRIMARY · @1.75× | 35 min | Advanced Python 1 & 2 — modules, imports, virtual environments |
| The import model below | REFERENCE | 15 min | The mental model that stops import errors |

### 🟢 IF TIME

- Read the Python docs on `argparse` for 10 minutes if you want a real CLI rather than `sys.argv`.

---

## 🧠 Core Concepts

### Module, package, library

| Term | Is | Example |
|:-----|:---|:--------|
| **Module** | One `.py` file | `cleaning.py` |
| **Package** | A folder of modules | `shoptools/` |
| **Library** | A distributable package | `pandas` |

### Import forms and when each is right

```python
import statistics                    # namespaced -- always safe
from statistics import mean          # direct -- fine for 2-3 names
from statistics import mean as avg   # aliased -- for name clashes
from statistics import *             # NEVER. It hides where names came from.
```

**Rule of thumb:** `import x` for anything you will use a few times; `from x import y` when you use `y` constantly. `import *` makes it impossible to tell whether `mean` came from `statistics`, `numpy`, or a typo.

### `if __name__ == "__main__":` — what it actually does

Python sets `__name__` to `"__main__"` in the file you ran, and to the module's own name in files that were imported. So:

```python
def main():
    ...

if __name__ == "__main__":
    main()          # runs when you execute this file
                    # does NOT run when another file imports it
```

Without this, importing your module **executes it**. Every script in this challenge has it for that reason.

### Virtual environments — one sentence each

A `venv` is a private copy of Python and its packages for one project. You want one because your LifeOS automation and this challenge will eventually need different versions of something, and a global install means one of them breaks.

```bash
python3 -m venv .venv
source .venv/bin/activate         # macOS / Linux
pip install -r requirements.txt
pip freeze > requirements.txt     # record exactly what you have
deactivate
```

`requirements.txt` is what makes your project reproducible. **A portfolio repository without one is a repository nobody else can run** — and reviewers notice.

### Project layout — what today produces

```
Day_12/
├── Day_12.py            ← the entry point
├── shoptools/
│   ├── __init__.py      ← marks the folder as a package
│   ├── parsing.py       ← Day 11's parser
│   ├── cleaning.py      ← Day 7's text work
│   └── analysis.py      ← Day 4's helpers
└── requirements.txt
```

This is the structure your Project 1, 2 and 3 repositories will use in a bigger form. Learn it once, here, on something small.

---

## 💻 Code

### 🔴 MUST DO — build `shopsummary`

A command-line tool. Run it as:

```bash
python Day_12.py messy_sales.csv --top 3 --group region
```

It should print:

```
shopsummary -- messy_sales.csv
  rows read      : 6
  rows valid     : 4
  rows rejected  : 2   (see below)

  total revenue  : PKR 12,340.00
  mean sale      : PKR  3,085.00
  median sale    : PKR  2,455.00

  top 3 by revenue
    1. Rice, Basmati 5kg    PKR 5,200.00
    2. Tea, Green           PKR 5,000.00
    3. Oil                  PKR 1,080.00

  revenue by region
    sindh   PKR  6,280.00
    punjab  PKR  6,060.00

  rejected
    line 5  short row (2 fields, expected 3)
    line 6  long row (4 fields, expected 3)
```

**Build it in this order:**

1. Create the `shoptools/` package with `__init__.py`
2. Move Day 11's parser into `shoptools/parsing.py`
3. Move Day 7's text cleaning into `shoptools/cleaning.py`
4. Move Day 4's `total_revenue`, `top_n`, `summarise`, `group_totals` into `shoptools/analysis.py`
5. Write `median` yourself — do not import `statistics` for it *(you need this on Day 48)*
6. Write `Day_12.py` as the entry point: read `sys.argv`, call the package, format the output
7. Add `if __name__ == "__main__":`
8. Write `requirements.txt` — it will be empty, and that is the point: **zero dependencies**
9. Run it on the messy fixture and on a clean file, and confirm both work

### 🟢 IF TIME

- Replace `sys.argv` handling with `argparse` so `--help` works
- Add a `--json` flag that outputs machine-readable results instead of a table

---

## 🔬 Understanding Check

1. **Reasoning.** What breaks if you omit `if __name__ == "__main__":` and someone imports your file?
2. **Comparison.** `import statistics` vs `from statistics import mean` vs `from statistics import *` — rank them and justify.
3. **Application.** Your tool needs a new "revenue by month" feature. Which module does it go in, and why does that decision matter?
4. **Understanding.** What exactly does a virtual environment isolate? What does it *not* isolate?
5. **Reasoning.** Why does a portfolio repository need `requirements.txt` even when it has no dependencies?
6. **Debugging.** `ModuleNotFoundError: No module named 'shoptools'` when running from a different directory. What is going on?
7. **Interview.** "Walk me through how you would structure a small data-processing project." You have just done it — answer in 60 seconds.

---

## 🎯 Expected Outcome

- [ ] Split code across modules in a package, and import between them
- [ ] Ship a working CLI built from eleven days of Python
- [ ] Explain the `__main__` guard, `venv` and `requirements.txt` without notes
- [ ] Compute mean, median, min and max without importing anything

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| CodeWithHarry modules @1.75× | 35 min |
| Import model + layout | 15 min |
| Build `shopsummary` (steps 1–9) | 110 min |
| Daily review | 20 min |
| **Total** | **~180 min** |

---

## 🧪 Mini Assessment

This is not a separate task — **the tool is the assessment.** It passes when:

- It runs on the messy fixture without crashing
- Rejected rows are reported with line numbers and reasons
- Median is computed correctly for both odd and even counts *(check this — it is the usual bug)*
- Removing `shoptools/__init__.py` breaks it, and you can say why

---

## 🔁 Daily Review

1. Which module did I have to reorganise partway through? What did that teach me about naming things before writing them?
2. Was my median correct for an even number of values on the first try?
3. Which Day 1–11 technique turned out to be most useful today?
4. **The semester starts tomorrow.** Days drop to 45–90 minutes. What is my realistic daily study slot — and when in the day is it?

---

## 📦 Completion Criteria

- [ ] `shoptools/` package exists with three modules and `__init__.py`
- [ ] `python Day_12.py messy_sales.csv` produces the full summary
- [ ] Rejected rows reported with line numbers and reasons
- [ ] Median verified on both odd and even counts
- [ ] `requirements.txt` present
- [ ] Understanding Check answered in writing
- [ ] Committed to git — **this is the first thing in this repo worth showing someone**

---

**[← Day 11](../Day_11/Day_11.md)** · **[Day 13 →](../Day_13/Day_13.md)** · [README](../../../README.md)
