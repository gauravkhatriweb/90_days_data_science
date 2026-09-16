-- =============================================================================
-- Day 37 — Expressions, CASE, and pivoting in SQL
-- =============================================================================

-- Q12 -- CASE WHEN: bucket prices
SELECT
    item,
    price,
    CASE
        WHEN price <  200 THEN 'low'
        WHEN price < 1000 THEN 'medium'
        ELSE                   'high'
    END AS price_band
FROM prices
LIMIT 20;


-- Q13 -- CONDITIONAL AGGREGATION -- this is a pivot, in SQL.
--        One column per band, one row per month.
SELECT
    month,
    SUM(CASE WHEN price <  200 THEN 1 ELSE 0 END) AS low,
    SUM(CASE WHEN price >= 200 AND price < 1000 THEN 1 ELSE 0 END) AS medium,
    SUM(CASE WHEN price >= 1000 THEN 1 ELSE 0 END) AS high
FROM prices
GROUP BY month
ORDER BY month;
--        COMPARE THIS TO pandas.pivot_table. WHICH IS EASIER? WHY?



-- Q14 -- CAST and date extraction.
--        SQLite stores dates as TEXT -- strftime is how you slice them.
SELECT
    strftime('%Y', date) AS yr,
    strftime('%m', date) AS mo,
    AVG(CAST(price AS REAL)) AS avg_price
FROM prices
GROUP BY yr, mo
ORDER BY yr, mo;
--        WHY IS THE CAST NEEDED HERE AND NOT IN POSTGRES?



-- Q15 -- COALESCE: treat nulls as zero inside an aggregation.
--        WHAT IS THE DIFFERENCE BETWEEN COALESCE(price, 0) AND IGNORING NULLS?
--        WHICH IS HONEST FOR *THIS* DATA?



-- =============================================================================
-- Q16 -- THE COMPARISON
--   Produce a month-by-item pivot of average price.
--
--   SQL:
--
--   PANDAS:
--
--   WHICH WAS EASIER? WHY IS PIVOTING AWKWARD IN SQL?
--   (Hint: SQL needs to know the columns at parse time. Pandas does not.)
-- =============================================================================
