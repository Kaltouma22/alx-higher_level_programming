-- List all records in second_table with a non-empty name value, ordered by descending score
SELECT `score`, `name`
FROM `second_table`
WHERE LENGTH(`name`) > 0
ORDER BY `score` DESC;
