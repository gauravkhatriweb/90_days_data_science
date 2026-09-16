-- =============================================================================
-- Day 44 — UNION, self-joins, and readable SQL
-- =============================================================================

-- Q10 -- UNION vs UNION ALL
--        UNION removes duplicates (and therefore has to sort).
--        UNION ALL does not.
SELECT item, 'high' AS band FROM prices WHERE price > 1000
UNION ALL
SELECT item, 'low'  AS band FROM prices WHERE price < 200;
--        WHEN WOULD USING UNION INSTEAD BE A BUG RATHER THAN JUST SLOWER?



-- Q11 -- SELF-JOIN: compare each week to the previous week
SELECT
    a.item,
    a.week,
    a.price                                    AS this_week,
    b.price                                    AS last_week,
    ROUND((a.price - b.price) * 100.0 / b.price, 2) AS pct_change
FROM prices a
JOIN prices b
  ON a.item = b.item AND a.week = b.week + 1
ORDER BY pct_change DESC
LIMIT 10;
--        WHAT DOES A SELF-JOIN LET ME DO THAT A PLAIN QUERY CANNOT?
--        (A WINDOW FUNCTION DOES THIS IN ONE LINE -- Day 52.)



-- Q12 -- DISTINCT vs GROUP BY producing the same result.
--        WHEN DOES EACH READ BETTER?



-- Q13 -- everything at once: JOIN + GROUP BY + HAVING + subquery



-- =============================================================================
-- Q14 -- READABILITY
-- Take Q13 and format it properly:
--   * one clause per line
--   * consistent indentation
--   * short, meaningful table aliases
--   * keywords in caps
--   * a comment saying what the query ANSWERS, not what it does
--
--   BEFORE:
--
--   AFTER:
--
--   Unreadable SQL is the SQL that gets rewritten by the next person
--   instead of being trusted.
-- =============================================================================
