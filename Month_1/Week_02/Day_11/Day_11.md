# Day 11 — Files, and the CSV You Parse Yourself

|  |  |
|:--|:--|
| **Date** | Saturday, 26 September 2026 |
| **Position** | Week 2 · Month 1 · Phase 1 — Python |
| **Budget** | **~90 min** — 🎓 Final orientation day |
| **Code file** | `Day_11.py` |

> **Why today looks like this.** In Week 5 you will type `pd.read_csv("file.csv")` and a dataframe will appear. If you have never parsed a CSV by hand, that line is magic — and magic is exactly what you said you did not want. Today you write the parser. Then, when Pandas does it for you, you will know what it handled, what it guessed, and where its guesses go wrong.
>
> Orientation ends today, so the budget is 90 minutes rather than a full weekend block.

---

## 🎯 Objective

Read and write files safely, and parse a delimited file into typed records without any library — including the cases that break naive parsers.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians Python](https://www.youtube.com/watch?v=_aWbUudZ5Yo) · **`6:43:23 → 7:24:17`** | PRIMARY · @1.75× | 23 min | File handling + the file-handling project |
| The `with` statement and encoding notes below | REFERENCE | 8 min | The two things that cause real bugs |

### 🟢 IF TIME

- [CodeWithHarry `5:54:50 → 6:14:04`](https://www.youtube.com/watch?v=UrsmFxEIp5k) — File I/O from a second teacher.
- Read the `csv` module docs for 10 minutes — but **do not use it in today's exercises.** Seeing what you just built by hand is the point.

---

## 🧠 Core Concepts

### Always use `with`

```python
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
# closed automatically, even if an exception was raised inside
```

Without `with`, an exception mid-read leaves the file handle open. In a loop over 500 files, that is a crash.

### Modes

| Mode | Does | Danger |
|:-----|:-----|:-------|
| `"r"` | Read | `FileNotFoundError` if missing |
| `"w"` | Write | **Truncates the file to zero immediately.** |
| `"a"` | Append | Safe |
| `"x"` | Create, fail if exists | Useful when you must not overwrite |

`"w"` has destroyed more student work than any other four characters in Python. It empties the file the moment `open()` runs — before you write anything.

### Reading: three ways, one right answer for big files

```python
f.read()          # entire file as one string   -- fine for small files
f.readlines()     # list of lines               -- loads it all into memory
for line in f:    # one line at a time          -- CORRECT for large files
```

The third is lazy. On a 2 GB file the first two fail and the third does not. This is your first encounter with **streaming**, which is what generators are for and why you will meet them again on Day 26.

### Encoding — the bug that looks like corrupted data

```python
open(path, encoding="utf-8")     # always say it explicitly
```

Pakistani datasets contain Urdu text, and Excel exports frequently arrive as `cp1252` or `utf-8-sig` (UTF-8 with a byte-order mark). The BOM shows up as `﻿` glued to your first column name — so `df["Item"]` raises `KeyError` while the column visibly exists. **Remember this one**; it will happen to you with PBS data on Day 32.

### What actually makes CSV parsing hard

`line.split(",")` works until:

```csv
item,qty,price
"Tea, Green",4,1250.00        <- comma inside a quoted field
Sugar,3,"1,180.00"            <- thousands separator inside quotes
Oil,,540                      <- empty field, not zero
Flour,2                       <- short row
Ghee,1,540,extra              <- long row
```

Each of these breaks the naive parser, and each appears in real government data. Today you handle the first three properly and *detect* the last two.

---

## 💻 Code

### 🔴 MUST DO

`Day_11.py` — builds a parser in seven steps:

1. Write a messy CSV to disk using `with` (this is your test fixture)
2. Read it three ways — `read`, `readlines`, line-by-line — and comment on when each belongs
3. Naive parse with `.split(",")`; print what breaks and why
4. Handle quoted fields containing commas — a character-by-character scan
5. Type-convert each field, using `safe_float` from Day 9
6. Detect and report short and long rows instead of crashing
7. Write the clean result back out, including quoting where needed

Then: run the `csv` module over the same file and compare your output against it. Note every difference.

### 🟢 IF TIME

- Add a `sniff_delimiter(sample)` that guesses between `,`, `;` and `\t`. Pandas does exactly this, and now you know how.

---

## 🔬 Understanding Check

1. **Reasoning.** Why does `with` matter more in a loop over 500 files than in a script that opens one?
2. **Debugging.** You open a file in `"w"` to append and lose everything. What happened, and at what moment?
3. **Comparison.** `f.readlines()` vs `for line in f` — when does the difference become fatal?
4. **Application.** A field is `"Tea, Green"`. Describe your parsing algorithm in words.
5. **Understanding.** `df["Item"]` raises `KeyError` but you can see the column. What is the most likely cause?
6. **Reasoning.** You now know what `pd.read_csv` does. Name two things it has to *guess*, and what happens when it guesses wrong.

---

## 🎯 Expected Outcome

- [ ] Read and write files with correct modes and explicit encoding
- [ ] Parse a delimited file with quoted fields, by hand
- [ ] Detect malformed rows rather than crashing on them
- [ ] Explain what `pd.read_csv` is doing and where it can fail

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians file handling @1.75× | 23 min |
| `with`, modes, encoding | 8 min |
| Seven-step parser | 50 min |
| Daily review | 9 min |
| **Total** | **~90 min** |

---

## 🧪 Mini Assessment

Ten minutes. Write `read_records(path)` returning `(records, problems)` where `records` are typed dicts and `problems` are `(line_number, reason)`. It must not crash on any line of the messy fixture.

---

## 🔁 Daily Review

1. Which malformed row was hardest to handle, and why?
2. What did the `csv` module do differently from my parser?
3. Name two things `pd.read_csv` must guess.
4. **Orientation is over. The semester starts Monday.** What have I learned this week about how much time I will actually have?

---

## 📦 Completion Criteria

- [ ] Parser handles quoted commas correctly
- [ ] Short and long rows reported, not crashed on
- [ ] Output compared against the `csv` module, differences noted
- [ ] `read_records` written closed-book
- [ ] Committed to git

---

**[← Day 10](../Day_10/Day_10.md)** · **[Day 12 →](../Day_12/Day_12.md)** · [README](../../../README.md)
