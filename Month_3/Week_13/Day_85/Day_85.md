# Day 85 — Ship Project 3

|  |  |
|:--|:--|
| **Date** | Wednesday, 9 December 2026 |
| **Position** | Week 13 · Month 3 · Phase 7 — Portfolio |
| **Budget** | **~75 min** |
| **Code file** | `project_3/README.md` |
| **Project** | 🤖 **P3 ships today** — the third and final portfolio piece |

> **Three projects, three different things proved.** Project 1: you can take messy real data and produce a defensible finding. Project 2: you can query a multi-table database and turn it into a business recommendation. Project 3: you can build a model *and be honest about it*.
>
> **That third one is the rarest.** Most junior portfolios contain a model. Almost none contain an honest evaluation of one, a named failure mode, and a paragraph saying what it does not prove.

---

## 🎯 Objective

Ship a repository that a reviewer will believe.

---

## 📚 Learn — what an ML README needs that an analysis one does not (15 min)

Everything from Day 45, plus five things specific to a model:

| Extra section | Why |
|:--------------|:----|
| **The baseline, before the result** | A score with no baseline is unreadable |
| **The evaluation protocol** | Shows you decided how to judge it *before* judging it |
| **What could have leaked, and what you did** | The first thing an experienced reviewer looks for |
| **The failure mode** | Shows you looked at errors, not just metrics |
| **What it cannot conclude** | Shows you know the difference between a model and the world |

**The ordering that builds trust:**

```
question → baseline → protocol → result → failure mode → limits → recommendation
```

Result *after* baseline and protocol. Putting the score first invites the reader to evaluate the number before they know what it should be compared against — and a reviewer who has to scroll for the baseline assumes you did not have one.

### Three things that lose credibility instantly

| | Why |
|:--|:--|
| A score with no baseline | Unjudgeable |
| No mention of leakage | Either you did not think of it, or you did not want to |
| "Causes" anywhere in an observational write-up | Ends the review |

---

## 💻 The Work

### 🔴 MUST DO — the README (35 min)

1. Title it with the finding — the model's result or what you learned
2. **The question and the decision**, in two sentences
3. **The data**, with source, grain, period and how to get it
4. **The baselines** — before any result
5. **The protocol** — metric, split strategy, cross-validation, and *why each*
6. **Leakage** — what you checked, what you dropped, what you are still unsure about
7. **The result** — the number, its confidence interval, the gap to baseline
8. **The failure mode** — Day 82's sentence
9. **Limitations** — at least four, with the causality paragraph prominent
10. **The recommendation**
11. **Reproduction** — and test it

### 🔴 MUST DO — the repository (25 min)

12. `src/` with `data.py`, `features.py`, `models.py`, `evaluate.py`
13. Notebooks named in order, **outputs cleared**
14. Tests for the feature-building functions *(at minimum the empty case — Day 25)*
15. `requirements.txt`, pinned
16. `.gitignore` — data, `.venv`, `__pycache__`, checkpoints
17. `grep -r "/Users/"` — remove every absolute path
18. **The fresh-clone test.** Clone, follow your own README, and fix what breaks.
19. Commit, push, add to the career-pillar portfolio tracker

---

## 🔬 Understanding Check

1. **Structure.** Why does the baseline come before the result?
2. **Credibility.** Which of the three credibility-losers were you closest to committing?
3. **Reproduction.** What broke in the fresh clone?
4. **Comparison.** Your three projects prove three different things. State each in one sentence.
5. **Selection.** If you could show only one, which — and does the answer depend on the role?
6. **Self-assessment.** Would you be comfortable with an interviewer opening this repository right now?

---

## 🎯 Expected Outcome

- [ ] A shipped, reproducible ML project
- [ ] A README ordered to build trust
- [ ] Leakage handling documented
- [ ] Three portfolio projects complete

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| The ML README pattern | 15 min |
| Write it (1–11) | 35 min |
| Repository hygiene (12–19) | 20 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

**The fresh-clone test**, again. Clone into a new directory, follow your own instructions, and regenerate the result. If the number differs, find out why — that is either a seed problem or a real bug, and both matter.

---

## 🔁 Daily Review

1. What broke in the fresh clone?
2. My three projects, one sentence each on what they prove.
3. Which would I lead with, and for which role?
4. **Three portfolio projects exist.** Ninety days ago there were none. What can I now claim that I could not?

---

## 📦 Completion Criteria

- [ ] README complete, in the trust-building order
- [ ] Baseline and protocol before the result
- [ ] Leakage handling documented
- [ ] Failure mode and causality paragraph present
- [ ] Four or more limitations
- [ ] `src/` organised, notebooks cleared, tests present
- [ ] Fresh-clone test passed
- [ ] Committed, pushed, tracker updated
- [ ] **Project 3 shipped** 🎉

---

**[← Week 12 Review](../../Week_12/Week_12_Review.md)** · **[Day 86 →](../Day_86/Day_86.md)** · [README](../../../README.md)
