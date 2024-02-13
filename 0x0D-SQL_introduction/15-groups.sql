-- Count the number of records with each score in second_table, ordered by descending count
SELECT `score`, COUNT(*) AS `number_of_records`
FROM `second_table`
GROUP BY `score`
ORDER BY `number_of_records` DESC;
