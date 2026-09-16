<!-- ==========================================================================
     Project 1 README — the template. Replace everything in <angle brackets>.

     A reviewer spends 90 seconds here. Most of it above the first heading.
     ========================================================================== -->

# <The finding, as a sentence. Not "Pakistan Inflation Analysis".>

<One paragraph: what question, what data, what you found. Written for someone
 who will read nothing else.>

![<the finding>](figures/headline.png)

---

## The finding

**Claim.** <what happened>

**Evidence.** <the numbers, the sample, the period>

**Comparison.** <against what — this is the part that makes it mean something>

**Limitation.** <the most important thing this cannot show>

---

## The data

| | |
|:--|:--|
| Source | <Pakistan Bureau of Statistics — with the direct link> |
| Period | <from — to> |
| Granularity | <weekly / monthly> |
| Observations | <n rows, n items> |
| Downloaded | <date> |
| Licence / terms | <> |

Raw files are in `data/raw/` and are never modified. `data/raw/SOURCES.md`
records where each one came from.

---

## What I did

**Cleaning.** <numbers, not adjectives>
> e.g. "Dropped 412 of 5,200 rows (7.9%): 380 with no recorded price,
> 32 with dates outside the study period. 1,180 item names collapsed to
> 94 canonical names. No imputation was applied to item-level gaps."

**Exploration.** <what you looked at, and what you found that changed the question>

**Analysis.** <the method, precisely enough to reproduce>

**Robustness.** <what you tried to break it with, and what survived>

---

## Reproducing this

```bash
git clone <url>
cd <repo>
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python -m src.clean      # data/raw -> data/processed
python -m src.charts     # -> figures/
pytest                   # the tests
```

<!-- TEST THESE INSTRUCTIONS IN A FRESH CLONE. Something will break. -->

---

## Limitations

<At least four. Specific. This section makes the project MORE credible, not less.>

1.
2.
3.
4.

**What this analysis does not claim:** <the causal statements you deliberately
did not make, and why>

---

## Repository layout

```text
data/raw/         source files, unmodified, with SOURCES.md
data/processed/   pipeline output -- deletable and regenerable
src/clean.py      the cleaning pipeline
src/charts.py     the final figures
notebooks/        01_first_look · 02_exploration · 03_analysis
tests/            tests for the pipeline
figures/          regenerable output
```
