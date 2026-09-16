# Day 16 — Instances, State, and the Second Explanation

|  |  |
|:--|:--|
| **Date** | Thursday, 1 October 2026 |
| **Position** | Week 3 · Month 1 · **OOP block, day 2 of 9** |
| **Budget** | **~75 min** |
| **Code file** | `Day_16.py` |

> **Why today has two teachers.** Yesterday Corey Schafer gave you the reasoning. Today you hear the same material from **CodeWithHarry and Apna College** — the two courses you chose in Hindi. This is the deliberate redundancy you asked for, and it is placed here on purpose: the second explanation of a hard concept, 24 hours after the first, is when it usually lands.
>
> **If it already landed yesterday, do not watch both.** Watch one, spend the time on code, and note in the review that you compressed. That is the correct use of a reinforcement resource.

---

## 🎯 Objective

Be fluent with instance state: creating objects, storing data on them, and understanding exactly what is shared and what is not.

---

## 📚 Learn

### 🔴 MUST DO — pick **one**, not both

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [CodeWithHarry `6:42:22 → 7:23:17`](https://www.youtube.com/watch?v=UrsmFxEIp5k) | **REINFORCEMENT** · @1.5× | 27 min | Chapter 10 — OOP from scratch, in Hindi |
| [Apna College `7:55:27 → 8:51:23`](https://www.youtube.com/watch?v=ERCMXc8x7mc) | **REINFORCEMENT** · @1.5× | 38 min | OOPS Part 1 — slower, more examples |

**How to choose:** if yesterday's diagnosis made sense but the syntax felt fast, take CodeWithHarry. If the whole idea still feels foreign, take Apna College — it goes slower and repeats more.

### 🟢 IF TIME

- Watch the *other* one at 2× as a check. If nothing in it surprises you, the concept is solid and you can skip the reinforcement layer for the rest of this block.

---

## 🧠 Core Concepts

### The object lifecycle

```python
d = SalesData(records)
```

1. Python creates an empty object
2. Calls `SalesData.__init__(d, records)`
3. `__init__` attaches attributes to `d`
4. `d` is handed back to you

`__init__` returns nothing. Writing `return self` in it is a bug — and a common one for people coming from JavaScript constructors.

### Every instance has its own attributes

```python
a = SalesData(records_a)
b = SalesData(records_b)

a.records is b.records      # False -- separate
a.count()                   # 2
b.count()                   # 1
```

This is the property that makes objects worth having: **one class, many independent states.** Two shops, two `SalesData` objects, no interference, no argument threading.

### Attributes can be added later — and usually should not be

```python
d = SalesData(records)
d.owner = "Khatri Traders"    # legal. Python allows it.
```

Legal, and almost always a mistake. Any attribute an object might have should be declared in `__init__`, even if the initial value is `None`. Otherwise `d.owner` exists on some instances and raises `AttributeError` on others — and you find out in production.

```python
def __init__(self, records, owner=None):
    self.records = records
    self.owner = owner          # declared, even when empty
```

### Methods that change state vs methods that report it

```python
class SalesData:
    def add(self, record):          # MUTATOR -- changes the object
        self.records.append(record)
        self._total = None          # invalidate the cache!
        return None                 # mutators conventionally return None

    def total(self):                # QUERY -- reports, changes nothing
        ...
```

Two rules worth adopting now:

- **A method should mutate or report, not both.** Mixing them produces the surprise you met on Day 2 with `list.sort()`.
- **If you cache a derived value, every mutator must invalidate it.** This is the classic OOP bug: `add()` a record, then `total()` returns yesterday's answer.

### Attributes vs methods — when to use which

| Use an attribute | Use a method |
|:-----------------|:-------------|
| Stored directly, no work | Requires computation |
| `d.records` | `d.total()` |
| Set once, read many | Depends on current state |

*(On Day 19 you will meet `@property`, which lets a computed value be accessed like an attribute. That is the right time for it — not now.)*

---

## 💻 Code

### 🔴 MUST DO

`Day_16.py` — build `ShopLedger`, the object version of `shopsummary`:

1. `__init__(self, shop_name, records=None)` — declare **every** attribute, including a `None` cache
2. `add(record)` — a mutator that invalidates the cache
3. `count()`, `total()`, `mean()` — queries
4. `total()` caches its result; prove the cache works by timing two calls
5. **The cache bug:** call `total()`, then `add()`, then `total()` again — with the invalidation removed. Watch it return the stale answer. Then fix it.
6. Create three ledgers for three shops; prove their state is independent
7. Add an attribute from outside the class, then explain in a comment why that is a bad habit
8. Convert three more `shopsummary` functions into methods

Exercise 5 is the one to take seriously. **The stale-cache bug is the most common real OOP bug there is**, and meeting it deliberately now means recognising it instantly later.

### 🟢 IF TIME

- Add `__len__` so `len(ledger)` works. You get the full explanation on Day 19; today it is a preview worth having.

---

## 🔬 Understanding Check

1. **Understanding.** What are the four steps between `SalesData(records)` and getting your object back?
2. **Debugging.** Two instances share a list unexpectedly. Given what you know about `__init__`, what is the most likely cause? *(Related to a Day 4 bug.)*
3. **Reasoning.** Why declare an attribute in `__init__` with `None` rather than adding it later?
4. **Application.** Exercise 5 returned a stale total. Describe the bug in one sentence, and name a rule that prevents it in every class you ever write.
5. **Comparison.** `d.records` vs `d.total()` — why is one an attribute and the other a method?
6. **Reasoning.** You watched a second explanation today. What did it give you that yesterday's did not — or did it give you nothing? Either answer is useful and should change what you do tomorrow.
7. **Interview.** "What is the difference between a class attribute and an instance attribute?" *(You get the full answer tomorrow — attempt it now and check yourself then.)*

---

## 🎯 Expected Outcome

- [ ] Write a class with a complete `__init__` without looking up syntax
- [ ] Explain instance independence and demonstrate it
- [ ] Separate mutators from queries deliberately
- [ ] Spot a stale-cache bug from its symptom

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| One reinforcement video @1.5× | 27–38 min |
| Build `ShopLedger` | 32 min |
| Daily review | 6 min |
| **Total** | **~70–75 min** |

---

## 🧪 Mini Assessment

Six minutes, closed book. Write `Basket` with `add(item, qty, price)`, `remove(item)`, `total()` and `item_count()`. `total()` must cache, and both mutators must invalidate the cache.

---

## 🔁 Daily Review

1. Which video did I choose, and did the second explanation add anything?
2. Did I predict the stale-cache bug before running exercise 5?
3. Is `self` clearer today than yesterday? Rate it 1–5.
4. If the reinforcement video added nothing, say so here — and skip the reinforcement layer for Days 17–20.

---

## 📦 Completion Criteria

- [ ] `ShopLedger` works with independent instances
- [ ] Cache invalidation implemented and the bug demonstrated first
- [ ] Every attribute declared in `__init__`
- [ ] `Basket` written closed-book
- [ ] Decision recorded on whether reinforcement videos are still needed
- [ ] Committed to git

---

**[← Day 15](../Day_15/Day_15.md)** · **[Day 17 →](../Day_17/Day_17.md)** · [README](../../../README.md)
