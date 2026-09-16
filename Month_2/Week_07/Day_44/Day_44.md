# Day 44 — Charts for Someone Who Was Not There

|  |  |
|:--|:--|
| **Date** | Thursday, 29 October 2026 |
| **Position** | Week 7 · Month 2 · Phase 2 |
| **Budget** | **~75 min** (50 project + 25 SQL) |
| **Code files** | `project_1/src/charts.py` · `Day_44.sql` |
| **Project** | 📊 **P1 — the visual argument** |

> **Why exploratory charts and final charts are different objects.** The charts from Days 39–40 were for you — quick, unlabelled, disposable. Today's are for someone who has never seen this data and will spend ten seconds on each. The two have almost nothing in common, and treating an exploratory chart as a final one is the most visible way a portfolio project looks unfinished.

---

## 🎯 Objective

Produce three to five final charts that carry the argument without you standing next to them.

---

## 📚 Learn — the rules for a final chart (15 min)

| | Exploratory | Final |
|:--|:--|:--|
| Audience | You | A stranger, in ten seconds |
| Title | None, or the column name | **The finding, in a sentence** |
| Labels | Whatever pandas made | Explicit, with units |
| Colour | Default | Meaningful, colourblind-safe |
| Annotation | None | **The point is marked** |
| Count | Fifty | **Three to five** |

**The ten-second test.** Show a chart to someone with no context. If they cannot say what it shows in ten seconds, it is not finished. This is not a metaphor — actually do it, with an actual person.

### Building the argument

Three to five charts, in an order that tells a story:

1. **Context** — what is the overall picture?
2. **The finding** — the chart the project exists for
3. **The comparison** — the thing that makes the finding mean something
4. **The nuance** — where it does not hold, or what varies
5. *(optional)* **The caveat made visible** — a data-quality chart, missing coverage, uncertainty

**Chart 2 is the one that goes at the top of your README and on LinkedIn.** Spend disproportionate time on it.

### Charts as code, not as notebook cells

```python
# src/charts.py
def headline_chart(df: pd.DataFrame, ax=None) -> plt.Axes:
    """The chart the project is about. Returns the Axes so it can be composed."""
```

Same reasoning as Day 41's cleaning module: reproducible, reviewable, and regenerable when the data changes. Accepting `ax=None` means the chart can be drawn standalone or into a grid — the Day 39 axes-level pattern, applied to your own code.

**Save at `dpi=150` minimum.** A blurry chart in a README reads as carelessness.

---

## 💻 Code

### 🔴 MUST DO — the final charts (50 min)

Build `project_1/src/charts.py`:

1. Decide the sequence. Write, for each chart, the sentence it must make the reader realise. **If you cannot write the sentence, cut the chart.**
2. `context_chart` — the overall picture
3. `headline_chart` — the finding, annotated, with a finding-title
4. `comparison_chart` — the finding against its comparison
5. `nuance_chart` — where it varies or does not hold
6. Every chart: finding-title, unit labels, sorted where categorical, annotated, colourblind palette
7. `save_all(outdir)` — regenerates every figure at `dpi=150`
8. **The ten-second test** on the headline chart, with a real person. Record what they said.
9. Revise based on what they got wrong

### 🔴 MUST DO — SQL (`Day_44.sql`, 25 min)

10. `UNION` and `UNION ALL` — and the difference in cost
11. Self-join: compare each row to the previous period
12. `DISTINCT` and `GROUP BY` producing the same result — when does each read better?
13. A query with `JOIN`, `GROUP BY`, `HAVING` and a subquery together
14. **Readability:** take exercise 13 and format it properly — indentation, aliases, one clause per line. Compare the two.

---

## 🔬 Understanding Check

1. **Reasoning.** What changes between an exploratory chart and a final one? Name four differences.
2. **Application.** Exercise 8: what did your test reader get wrong? What did that reveal?
3. **Judgement.** Which chart did you cut, and why? *(If you cut none, you probably kept one too many.)*
4. **Design.** Why does `headline_chart` accept `ax=None`?
5. **SQL.** `UNION` vs `UNION ALL` — what is the difference, and why is one slower?
6. **SQL.** Exercise 11: what does a self-join let you do that a plain query cannot? *(Window functions do this more cleanly — Day 52.)*
7. **Communication.** If you could show only one chart, which, and why that one?

---

## 🎯 Expected Outcome

- [ ] Three to five final charts, each carrying one sentence
- [ ] All regenerable from `src/charts.py` in one call
- [ ] The headline chart passing the ten-second test with a real person
- [ ] A complex SQL query written and formatted readably

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Final-chart rules | 15 min |
| Build the charts (1–9) | 45 min |
| **SQL: exercises 10–14** | 25 min |
| Daily review | 5 min |
| **Total** | **~90 min** — if over, cut `nuance_chart` |

---

## 🧪 Mini Assessment

The ten-second test. Hand the headline chart to someone with no context. **Write down exactly what they say.** If it is not your finding, the chart is not finished.

---

## 🔁 Daily Review

1. What did my test reader actually say?
2. Which chart did I cut?
3. Which chart would I show if I could only show one?
4. Ships tomorrow. What is left?

---

## 📦 Completion Criteria

- [ ] Three to five charts, each with a written sentence
- [ ] `src/charts.py` regenerates all of them at dpi≥150
- [ ] Ten-second test done with a real person, response recorded
- [ ] At least one revision made from that feedback
- [ ] Five SQL exercises done, including the formatting comparison
- [ ] Committed to git

---

**[← Day 43](../Day_43/Day_43.md)** · **[Day 45 →](../Day_45/Day_45.md)** · [README](../../../README.md)
