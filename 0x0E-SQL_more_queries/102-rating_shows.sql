-- Import the database hbtn_0d_tvshows_rate dump to your MySQL server
SELECT tv_shows.title, SUM(rating) AS rating_sum
FROM tv_shows
JOIN ratings ON tv_shows.id = ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
