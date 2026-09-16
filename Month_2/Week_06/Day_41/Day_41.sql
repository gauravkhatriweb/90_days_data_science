-- =============================================================================
-- Day 41 — Subqueries
-- =============================================================================

-- Q12 -- subquery in WHERE: items priced above the overall average
SELECT item, price
FROM prices
WHERE price > (SELECT AVG(price) FROM prices)
ORDER BY price DESC;


-- Q13 -- subquery in FROM (a derived table): rank items by their own average
SELECT item, avg_price
FROM (
    SELECT item, AVG(price) AS avg_price
    FROM prices
    GROUP BY item
) AS item_avgs
WHERE avg_price > 500
ORDER BY avg_price DESC;
--        WHY DOES THE DERIVED TABLE NEED AN ALIAS?



-- Q14 -- CORRELATED subquery: each row compared to ITS OWN category average.
--        The inner query runs once per outer row -- that is what "correlated" means.
SELECT p.item, p.price, p.category,
       (SELECT AVG(price) FROM prices p2 WHERE p2.category = p.category) AS cat_avg
FROM prices p
LIMIT 20;
--        WHY IS THIS USUALLY SLOWER THAN A JOIN?
--        WHAT DOES A WINDOW FUNCTION DO INSTEAD?  (you meet those on Day 52)



-- Q15 -- EXISTS / NOT EXISTS: items that have never been recorded in a region



-- =============================================================================
-- Q16 -- THE COMPARISON
--   Same question, two ways: "items whose average price exceeds their category's"
--
--   AS A SUBQUERY:
--
--   AS A JOIN:
--
--   WHICH READS BETTER TO A HUMAN?
--   WHICH WOULD THE ENGINE PREFER, AND DOES THAT MATTER AT THIS SCALE?
-- =============================================================================
