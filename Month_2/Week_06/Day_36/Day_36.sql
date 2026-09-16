-- =============================================================================
-- Day 36 — JOINs
-- =============================================================================
-- THE RULE: predict the row count before, check it after.
-- A join that silently duplicates rows produces a wrong number that
-- looks completely plausible.
-- =============================================================================


-- Q12 -- INNER JOIN: prices with their categories.
--        Only items present in BOTH survive.
SELECT p.item, p.price, c.category
FROM prices p
INNER JOIN categories c ON p.item = c.item
LIMIT 20;


-- Q13a -- LEFT JOIN: keep every price row, even with no category.



-- Q13b -- THE PATTERN WORTH MEMORISING.
--         Which items have NO category?
SELECT p.item
FROM prices p
LEFT JOIN categories c ON p.item = c.item
WHERE c.item IS NULL;
--         WHAT QUESTION DOES THIS ANSWER, IN PLAIN ENGLISH?
--         NAME THREE POSSIBLE CAUSES FOR AN UNMATCHED ROW:



-- Q14 -- three tables in one query



-- Q15 -- JOIN + GROUP BY: revenue per category



-- Q16 -- THE ROW-COUNT CHECK
SELECT COUNT(*) AS before_join FROM prices;

SELECT COUNT(*) AS after_join
FROM prices p
LEFT JOIN categories c ON p.item = c.item;
--         ARE THEY THE SAME?
--         IF NOT, WHY? (check for duplicate keys in `categories`)
SELECT item, COUNT(*) AS n
FROM categories
GROUP BY item
HAVING COUNT(*) > 1;
