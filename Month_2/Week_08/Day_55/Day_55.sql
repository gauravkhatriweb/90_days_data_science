-- =============================================================================
-- Day 55 — SQL deep day  (Iqbal Day: a free weekday, use it)
-- =============================================================================
-- THE SIX PATTERNS. These cover most real analyst SQL and most interview
-- questions. Aim to write all six without looking anything up.
-- =============================================================================


-- 1 -- TOP N PER GROUP
WITH ranked AS (
    SELECT item, week, price,
           ROW_NUMBER() OVER (PARTITION BY item ORDER BY price DESC) AS rn
    FROM prices
)
SELECT item, week, price FROM ranked WHERE rn <= 3 ORDER BY item, rn;


-- 2 -- PERIOD-ON-PERIOD CHANGE



-- 3 -- RUNNING TOTAL
--      SUM(x) OVER (ORDER BY d ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)



-- 4 -- FIND THE GAPS  (LEFT JOIN ... WHERE right IS NULL)



-- 5 -- PIVOT with CASE WHEN



-- 6 -- DEDUPLICATE, keeping the latest per key



-- =============================================================================
-- THE TRAPS. Reproduce each one, then fix it.
-- =============================================================================

-- 7 -- NULL = NULL is not TRUE. It is NULL.
SELECT 1 WHERE NULL = NULL;          -- returns nothing
SELECT 1 WHERE NULL IS NULL;         -- returns 1
--      WHY? (three-valued logic: TRUE / FALSE / UNKNOWN)


-- 8 -- NOT IN WITH A NULL RETURNS NOTHING AT ALL.
--      This is the nastiest one -- it looks like "no such data".
SELECT item FROM prices
WHERE item NOT IN (SELECT item FROM discontinued);   -- empty if any row is NULL
--      THE FIX: use NOT EXISTS
--      WHY DOES THE NULL POISON IT?


-- 9 -- AVG SILENTLY SKIPS NULLS.
SELECT
    AVG(price)                AS avg_ignoring_nulls,
    AVG(COALESCE(price, 0))   AS avg_treating_null_as_zero,
    COUNT(*)                  AS all_rows,
    COUNT(price)              AS non_null_rows
FROM prices;
--      WHEN IS SKIPPING WHAT I WANT?  WHEN IS IT A SILENT BUG?


-- 10 -- INTEGER DIVISION
SELECT 5 / 2 AS integer_division, 5.0 / 2 AS float_division;
--      WHERE WOULD THIS SILENTLY RUIN A PERCENTAGE CALCULATION?


-- =============================================================================
-- INTERVIEW PROBLEMS. CLOSED BOOK. TIMED.
-- 3 of 5 inside the limits = interview-ready for an entry-level screen.
-- =============================================================================

-- 11 (5 min) -- the SECOND-highest price per item
--     SCORE: ___


-- 12 (8 min) -- items whose price rose for THREE CONSECUTIVE weeks
--     (hint: LAG twice, or a windowed count)
--     SCORE: ___


-- 13 (8 min) -- each item's SHARE of total spend, per month
--     (hint: a window SUM over the month as the denominator)
--     SCORE: ___


-- 14 (10 min) -- the LARGEST week-on-week jump per item, and the week it happened
--     SCORE: ___


-- 15 (10 min) -- COHORT RETENTION.
--     By first-observation month, how many items are still present N months later?
--     This is the single most common analytics question in a product company,
--     and it is the core of Project 2.
--     SCORE: ___


-- =============================================================================
--   TOTAL: ___ / 5
--   WHICH RAN OVER TIME?
--   WHICH OF THE SIX PATTERNS IS LEAST AUTOMATIC?
--   IS MY SQL AT THE LEVEL PROJECT 2 NEEDS (starts Day 58)?
-- =============================================================================
