# Day 8 — Slicing, Unpacking, and Sorting by a Key

|  |  |
|:--|:--|
| **Date** | Wednesday, 23 September 2026 |
| **Position** | Week 2 · Month 1 · Phase 1 — Python |
| **Budget** | **~45 min** — 🎓 Orientation day 3 |
| **Code file** | `Day_08.py` |

> **Why today looks like this.** Three small techniques that appear in almost every piece of data code you will write. None of them need a video; all of them need repetition. Perfect material for a 45-minute orientation-week day.

---

## 🎯 Objective

Slice, unpack and sort without hesitation — because these three show up in every Pandas operation later, and hesitation here compounds.

---

## 📚 Learn

### 🔴 MUST DO — read, then drill

**Slicing: `sequence[start:stop:step]`**

```python
prices = [1250, 180, 2600, 540, 890]

prices[1:3]     # [180, 2600]   -- stop is EXCLUSIVE
prices[:3]      # first three
prices[-2:]     # last two
prices[::2]     # every second
prices[::-1]    # reversed
prices[:]       # a shallow COPY -- this is the idiom for copying a list
```

The exclusive stop is the point people get wrong. `prices[0:3]` gives three items, not four. Say it out loud once: **"up to, not including."**

**Unpacking**

```python
item, qty, price = ("tea", 4, 1250.0)      # exact match required
first, *rest = [1, 2, 3, 4]                # first=1,  rest=[2,3,4]
*most, last = [1, 2, 3, 4]                 # most=[1,2,3], last=4
a, b = b, a                                # swap, no temp variable
for item, qty in pairs: ...                # unpacking in a loop header
```

The starred form is what makes `header, *rows = file.readlines()` work — and you will use exactly that on Day 11.

**Sorting by a key**

```python
sorted(rows, key=lambda r: r["price"])                    # by one field
sorted(rows, key=lambda r: r["price"], reverse=True)      # descending
sorted(rows, key=lambda r: (r["region"], -r["price"]))    # region asc, price desc
sorted(words, key=str.lower)                              # case-insensitive
max(rows, key=lambda r: r["qty"])                         # key works here too
```

The tuple key is the one worth memorising — **multi-level sorting for free**, and the minus sign flips one level without flipping the others. `min`, `max`, `sorted` and `.sort()` all take `key`.

### 🟢 IF TIME

- Nothing. Orientation.

---

## 💻 Code

`Day_08.py` — nine drills:

1. Six slices of one list, predicted before running
2. Copy a list with slicing, then prove it is a copy by mutating the original
3. Reverse a string, a list and a tuple with one idiom
4. Unpack a header row away from the data rows using `*`
5. Swap two variables without a temporary
6. Sort transactions by price, descending
7. Sort by region ascending, then price descending — one `key`
8. Find the highest-revenue row with `max(..., key=...)`
9. Sort a list of city names case-insensitively, then explain why `key=str.lower` is better than `.lower()`-ing the whole list first

---

## 🔬 Understanding Check

1. **Understanding.** Why is the slice stop exclusive? What does `a[:n] + a[n:]` reconstruct?
2. **Debugging.** `b = a` then `b.append(1)` also changed `a`. Why, and what is the one-character fix?
3. **Comparison.** `sorted(x)` vs `x.sort()` — when does each belong?
4. **Application.** Sort employees by department ascending and salary descending. Write the `key`.
5. **Reasoning.** Why does `key=str.lower` beat creating a lowercased copy of the list?

---

## 🎯 Expected Outcome

- [ ] Slice from either end, with a step, without thinking
- [ ] Use starred unpacking to separate a header from rows
- [ ] Write a multi-level sort key on the first attempt

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Read the three sections | 10 min |
| Nine drills | 28 min |
| Daily review | 7 min |
| **Total** | **~45 min** |

---

## 🧪 Mini Assessment

Two minutes, from memory: sort a list of dicts by `region` ascending and `revenue` descending, then take the top three.

---

## 🔁 Daily Review

1. How many of the six slice predictions did I get right?
2. Did the tuple sort key work first time?
3. **Orientation:** anything today that changes my plan for the semester?

---

## 📦 Completion Criteria

- [ ] Nine drills run
- [ ] Slice predictions written before running, and scored
- [ ] Mini assessment done from memory
- [ ] Committed to git

---

**[← Week 1 Review](../../Week_01/Week_01_Review.md)** · **[Day 9 →](../Day_09/Day_09.md)** · [README](../../../README.md)
