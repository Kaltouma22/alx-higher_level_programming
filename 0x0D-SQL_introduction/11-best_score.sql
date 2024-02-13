-- Display scores and names from second_table with score
-- greater than or equal to 10, ordered by score in descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
