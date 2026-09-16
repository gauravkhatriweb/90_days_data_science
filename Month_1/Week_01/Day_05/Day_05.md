# Day 5 — Choosing the Right Data Structure

|  |  |
|:--|:--|
| **Date** | Sunday, 20 September 2026 |
| **Position** | Week 1 · Month 1 · Phase 1 — Python |
| **Budget** | **~180 min** — your last full free day before orientation |
| **Code file** | `Day_05.py` |

> **Why today looks like this.** Every language has lists and maps, so the syntax is not the lesson. The lesson is **choosing**: list or set, dict or list-of-tuples, tuple or list. That choice is the difference between a lookup that takes a microsecond and one that takes a minute across 50,000 rows — and it is the first thing **CSE 205** will assess you on next semester. Today also plants Big-O intuition, which is a degree requirement and an interview staple, without turning into a two-month algorithms course.

---

## 🎯 Objective

Pick the right container by reasoning about how it will be *used*, and be able to justify the choice in cost terms.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians Python](https://www.youtube.com/watch?v=_aWbUudZ5Yo) · **`4:33:38 → 6:23:24`** | PRIMARY · @1.75× | 60 min | Lists, tuples, sets, dictionaries — all four, in sequence |
| The decision table + cost table below | REFERENCE | 20 min | The part the video does not teach |

### 🟢 IF TIME

- [Apna College `03:27:13 → 05:01:26`](https://www.youtube.com/watch?v=ERCMXc8x7mc) — lists, tuples, dicts, sets from a second teacher. Useful if any of the four felt thin.

---

## 🧠 Core Concepts

### The decision table

| You need to… | Use | Why |
|:-------------|:----|:----|
| Keep an ordered sequence you will change | `list` | Order preserved, mutable |
| Keep a record whose shape is fixed | `tuple` | Immutable, can be a dict key, signals "this won't change" |
| Ask "have I seen this before?" | `set` | Membership is instant regardless of size |
| Remove duplicates | `set` | One operation |
| Look something up by name or id | `dict` | Instant lookup by key |
| Count occurrences | `collections.Counter` | A dict that already knows how to count |
| Group things by a key | `collections.defaultdict(list)` | No "does this key exist yet" boilerplate |

### The cost table — Big O, only as much as you need

| Operation | `list` | `set` | `dict` |
|:----------|:-------|:------|:-------|
| `x in container` | **O(n)** — checks every item | **O(1)** | **O(1)** (keys) |
| Add | O(1) append | O(1) | O(1) |
| Remove by value | O(n) | O(1) | O(1) |
| Keeps order | ✅ | ❌ | ✅ (insertion order, since 3.7) |
| Can hold duplicates | ✅ | ❌ | keys ❌ |

**Read one line above everything else:** `x in my_list` checks every element. `x in my_set` does not.

```python
# 50,000 transactions, 5,000 known-fraud ids
for txn in transactions:
    if txn.id in fraud_list:    # list -> 250,000,000 comparisons
        flag(txn)

fraud_set = set(fraud_list)
for txn in transactions:
    if txn.id in fraud_set:     # set -> 50,000 lookups
        flag(txn)
```

Same code, same output, and the second one finishes. **This is what Big O is for** — not interview trivia, but knowing which version to write.

### Tuples: more useful than they look

- Immutable, so they can be **dictionary keys**: `sales[("sindh", "tea")] = 4200`
- They unpack cleanly: `item, qty, price = row`
- They signal intent: a tuple says *this is a record with a fixed shape*, a list says *this is a collection that will grow*

### Dict methods that prevent bugs

```python
row.get("qty")             # None instead of KeyError
row.get("qty", 0)          # a default
row.setdefault("tags", []) # create-if-missing, then return it
for k, v in row.items():   # the correct way to iterate both
```

`row["qty"]` crashes on missing data. Real data is missing constantly. **Default to `.get()`** and reach for `[]` only when a missing key genuinely should stop the program.

### `collections` — three things worth knowing now

```python
from collections import Counter, defaultdict

Counter(["tea","sugar","tea"]).most_common(1)   # [('tea', 2)]

by_region = defaultdict(list)
for row in rows:
    by_region[row["region"]].append(row)        # no key-existence check
```

You will reimplement `Counter` by hand in the exercises first — then use it. Knowing what it replaces is the point.

---

## 💻 Code

### 🔴 MUST DO

`Day_05.py` — thirteen exercises, most drawn from the Week 2 bank in `Tem.txt` (lines 1941–1971) but reordered so each one teaches a *choice*:

**Mechanics (1–6)**
1. Remove duplicates while preserving order (set for membership, list for order)
2. Merge two dicts, summing values on key collisions
3. Invert a dict — and answer what happens when values repeat
4. Frequency count by hand, then with `Counter` — compare line counts
5. Group rows by a key with `defaultdict(list)`
6. Nested dict for student records, then read a value three levels deep safely

**Choosing (7–10)**
7. Same task, three containers — time all three with `time.perf_counter()`
8. Use a tuple as a dict key for two-dimensional aggregation
9. Set operations — union, intersection, difference — on two customer lists, and say what each *means* in business terms
10. Flatten a nested list; then say what structure it should have been in the first place

**Applied (11–13)**
11. Build a price lookup and handle "item not found" without crashing
12. Find items present in one shop's inventory but not another's
13. Second-highest value, missing number in 1..N, and rotate-a-list — three classic interview reps

### 🟢 IF TIME

- Questions 22, 24, 26, 27, 30 from the `Tem.txt` Week 2 bank (anagram, flatten, rotate, missing number, unique-to-one-list).
- Read the Python docs page for `collections` for 10 minutes.

---

## 🔬 Understanding Check

1. **Comparison.** You need to check membership 100,000 times. List or set? Give the cost of each in Big-O terms and a rough factor in real time.
2. **Reasoning.** Why can a tuple be a dictionary key but a list cannot? What property does a key need?
3. **Application.** Sales by `(region, product)`. Design the structure. Justify it against two alternatives.
4. **Debugging.** `row["qty"]` raises `KeyError` on one row in 40,000. Three ways to fix it — which is right, and when?
5. **Understanding.** Sets do not keep order and reject duplicates. Name a case where each of those is exactly what you want, and one where each ruins your data.
6. **Interview.** "What is the time complexity of looking up a value in a Python dictionary, and why?"
7. **Teaching.** Explain a dictionary to someone using a physical shop's ledger.
8. **Degree link.** CSE 205 will ask you to implement a linked list and a hash table. After today, what do you think a dictionary is doing internally?

---

## 🎯 Expected Outcome

- [ ] Choose between list, set, dict and tuple by reasoning about use, not habit
- [ ] State the cost of membership testing in each
- [ ] Use `Counter` and `defaultdict` naturally
- [ ] Handle missing keys without crashing
- [ ] Explain why a dict lookup is O(1) well enough to satisfy an interviewer

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians `4:33:38 → 6:23:24` @1.75× | 60 min |
| Decision + cost tables | 20 min |
| Thirteen exercises | 80 min |
| Daily review | 15 min |
| **Total** | **~175 min** |

---

## 🧪 Mini Assessment

Closed book, 25 minutes. You are given 10,000 transaction dicts with `region`, `item`, `qty`, `price`. Without pandas, produce:

1. Total revenue per region
2. The three best-selling items by quantity
3. Items sold in every region
4. A list of `(region, item)` pairs that appear only once

Then write **one sentence per answer** naming the structure you chose and why. The structures are the assessment; the answers are just proof.

---

## 🔁 Daily Review

1. In exercise 7, how large was the actual timing gap between the three containers? Did it match what I predicted?
2. Which structure do I still reach for out of habit rather than reasoning?
3. Can I explain O(1) versus O(n) to someone else right now, without notes?
4. Orientation starts tomorrow and my days drop to 45 minutes until Day 11. What is the one thing from Week 1 I most need to keep warm?

---

## 📦 Completion Criteria

- [ ] All thirteen exercises run
- [ ] Exercise 7 has real measured timings written in a comment
- [ ] Mini assessment done closed-book with structure justifications
- [ ] Understanding Check answered in writing, including the CSE 205 question
- [ ] Committed to git

---

**[← Day 4](../Day_04/Day_04.md)** · **[Day 6 →](../Day_06/Day_06.md)** · [README](../../../README.md)
