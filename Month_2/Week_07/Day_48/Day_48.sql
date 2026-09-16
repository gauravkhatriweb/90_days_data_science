-- =============================================================================
-- Day 48 — Statistics in SQL, and where SQL stops being the right tool
-- =============================================================================

-- Q9 -- the easy ones
SELECT
    item,
    COUNT(*)   AS n,
    AVG(price) AS mean_price,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    MAX(price) - MIN(price) AS range_price
FROM prices
GROUP BY item
ORDER BY mean_price DESC;


-- Q10 -- THE MEDIAN PROBLEM.
--        SQL has no MEDIAN. You have to rank and pick the middle.
WITH ranked AS (
    SELECT
        item,
        price,
        ROW_NUMBER() OVER (PARTITION BY item ORDER BY price) AS rn,
        COUNT(*)     OVER (PARTITION BY item)                AS n
    FROM prices
)
SELECT item, AVG(price) AS median_price
FROM ranked
WHERE rn IN ((n + 1) / 2, (n + 2) / 2)      -- handles odd AND even n
GROUP BY item;
--        COMPARE THAT TO pandas: df.groupby("item")["price"].median()
--        HOW MANY LINES EACH?  ____ vs ____



-- Q11 -- standard deviation.
--        SQLite has no STDEV. Compute it manually: sqrt(E[x^2] - E[x]^2).
--        NOTE: this gives the POPULATION SD. Adjusting to n-1 in SQL is
--        awkward -- which is itself part of today's lesson.
SELECT
    item,
    SQRT(AVG(price * price) - AVG(price) * AVG(price)) AS sd_population
FROM prices
GROUP BY item;
--        HOW WOULD I GET THE SAMPLE SD (n-1) FROM THIS?



-- Q12 -- weighted average: SUM(value * weight) / SUM(weight)
--        This is what SPI actually is.



-- =============================================================================
-- Q13 -- THE TOOL-CHOICE QUESTION
--   Of these five statistics, rank them by how awkward SQL makes them:
--     mean, median, mode, standard deviation, weighted mean
--
--   EASIEST IN SQL:
--   HARDEST IN SQL:
--
--   WHAT DOES THAT SUGGEST ABOUT WHERE EACH TOOL BELONGS?
--   (A useful rule: SQL for selecting and aggregating at scale;
--    Python for anything statistical beyond a simple aggregate.)
-- =============================================================================
