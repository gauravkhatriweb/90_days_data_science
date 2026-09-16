# Day 7 — Text Is Data

|  |  |
|:--|:--|
| **Date** | Tuesday, 22 September 2026 |
| **Position** | Week 1 · Month 1 · Phase 1 — Python |
| **Budget** | **~45 min** — 🎓 Orientation continues. Short day. |
| **Code file** | `Day_07.py` |
| **Also today** | ✍️ **[Week 1 Review](../Week_01_Review.md)** — do it after this |

> **Why today looks like this.** Most real datasets are mostly text, and most of that text is wrong: trailing spaces, inconsistent casing, currency symbols glued to numbers, three spellings of the same city. Before Pandas gives you `.str` accessors, you should know what they are doing. Today is pure repetition on the operations you will use every single week from here on.

---

## 🎯 Objective

Turn messy text into clean, typed values fast enough that it stops being the slow part of an analysis.

---

## 📚 Learn

### 🔴 MUST DO

No video. The method is more useful than more explanation.

**The cleaning sequence — memorise this order:**

```
strip  →  case-normalise  →  remove noise  →  collapse whitespace  →  convert type  →  validate
```

Running it out of order is where bugs come from. `int("  42 ")` works; `int("42 PKR")` does not; `int("")` does not. **Strip before you convert, and validate after.**

**The methods, ranked by how often you will use them:**

| Method | Does | Trap |
|:-------|:-----|:-----|
| `.strip()` | Removes surrounding whitespace | Only the ends. Internal doubles survive. |
| `.lower()` | Case-normalise | Do this before comparing anything |
| `.split()` | Text → list | **No argument = split on any whitespace and drop empties.** Different from `.split(" ")`. |
| `.join()` | List → text | Called on the *separator*: `", ".join(items)` |
| `.replace(a, b)` | Substitution | Chains, but five chained replaces wants a loop |
| `" ".join(s.split())` | Collapse all internal whitespace | The idiom worth memorising |
| `.startswith()` / `.endswith()` | Prefix / suffix test | Accepts a tuple: `.endswith(("kg", "g"))` |
| `in` | Substring test | Case-sensitive — lower first |

**One note on regular expressions.** You will meet `re` when you need it — around Day 41, cleaning real PBS data. Today is deliberately without it, because reaching for regex before mastering string methods produces unreadable code that solves problems `.split()` already solved.

### 🟢 IF TIME

- Nothing. Orientation ends Saturday; protect your energy.

---

## 💻 Code

### 🔴 MUST DO

`Day_07.py` — seven drills drawn from the Week 4 bank in `Tem.txt` (lines 1989–2039), chosen because each maps to a real cleaning task:

1. Normalise a product name — the full six-step sequence
2. Count word frequency in a paragraph, ignoring case and punctuation
3. Extract the number from `"1,250.00 PKR"` and return a float
4. Find the first non-repeating character (classic interview rep)
5. `camelCase` → `snake_case` (you will need this for column names)
6. Check whether two strings are anagrams — two approaches, compare cost
7. **The real one:** given eight messy variations of the same four city names, produce a mapping that collapses them to four canonical values

Exercise 7 is what data cleaning actually is. Everything before it is warm-up.

---

## 🔬 Understanding Check

1. **Debugging.** `float("1,250.00")` raises `ValueError`. Why, and what is the fix?
2. **Comparison.** `"a b  c".split()` vs `"a b  c".split(" ")` — different results. Explain, and say which you want when parsing a sentence.
3. **Application.** A `city` column contains `Lahore`, `lahore`, `LAHORE`, ` Lahore `, `Lahor`. Which are fixable by rule and which need a lookup table? What does that tell you about automating cleaning?
4. **Reasoning.** Why normalise case *before* deduplicating rather than after?
5. **Interview.** Reverse a string without slicing, and say why slicing is normally the right answer anyway.

---

## 🎯 Expected Outcome

- [ ] Clean a messy string to a typed value in one chained expression
- [ ] Recite the six-step cleaning sequence
- [ ] Recognise which inconsistencies are rule-fixable and which are not

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Read the method above | 8 min |
| Seven drills | 30 min |
| Daily review | 7 min |
| **Total** | **~45 min** · then the Week 1 Review separately |

---

## 🧪 Mini Assessment

Three minutes, from memory. Turn `"  ACME  Tea  1KG , 4 , 1,250.00 PKR "` into `("acme tea 1kg", 4, 1250.0)`.

---

## 🔁 Daily Review

1. Which of the seven drills was slowest, and was it logic or method names?
2. Can I recite the cleaning sequence without scrolling up?
3. **Week 1 is over.** Before opening the review: what is the one thing I would fail if tested right now?

---

## 📦 Completion Criteria

- [ ] Seven drills run correctly
- [ ] Exercise 7 produces a working canonical mapping
- [ ] Mini assessment done from memory
- [ ] **[Week 1 Review](../Week_01_Review.md) completed** — this is not optional
- [ ] Committed to git

---

**[← Day 6](../Day_06/Day_06.md)** · **[Week 1 Review →](../Week_01_Review.md)** · [README](../../../README.md)
