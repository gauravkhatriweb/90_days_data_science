-- =============================================================================
-- Day 34 — GROUP BY
-- =============================================================================
-- WHERE  filters ROWS   -- BEFORE grouping
-- HAVING filters GROUPS -- AFTER  grouping
-- That difference falls straight out of Day 33's execution order.
-- =============================================================================


-- Q12 -- the five aggregates over the whole table
SELECT
    COUNT(*)      AS n_rows,
    AVG(price)    AS avg_price,
    MIN(price)    AS min_price,
    MAX(price)    AS max_price,
    SUM(price)    AS total
FROM prices;


-- Q13a -- GROUP BY one column: average price per item



-- Q13b -- GROUP BY two columns: per item per month



-- Q14 -- HAVING: only items observed more than 40 times



-- Q15 -- WHERE *and* HAVING in one query.
--        Exclude zero prices (rows), then keep only items averaging over 500 (groups).
--
--        WHY IS THE ROW FILTER IN WHERE AND NOT HAVING?
--        ANSWER:
--
--        WHAT WOULD HAPPEN IF YOU SWAPPED THEM?
--        ANSWER:



-- Q16 -- THE COUNT TRAP.
--        Run all three. They will not agree if `price` has nulls.
SELECT
    COUNT(*)              AS count_star,
    COUNT(price)          AS count_price,
    COUNT(DISTINCT item)  AS count_distinct_item
FROM prices;
--        WHY DO count_star AND count_price DIFFER?
--        NAME A BUSINESS NUMBER THAT WOULD BE WRONG IF YOU PICKED THE WRONG ONE:



-- =============================================================================
-- Q17 -- THE COMPARISON
-- Same question, both tools. Write both, then judge.
--
--   Question: per item, the average price and the observation count,
--             for items seen more than 20 times, ordered by average price.
--
--   SQL:
--
--   PANDAS:
--
--   WHICH IS CLEARER HERE?
--   WHICH WOULD YOU USE IF THE TABLE HAD 50 MILLION ROWS, AND WHY?
-- =============================================================================
