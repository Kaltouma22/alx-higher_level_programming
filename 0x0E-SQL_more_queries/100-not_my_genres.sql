-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
    SELECT genre_id
    FROM tv_show_genres
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
) AS linked_genres ON tv_genres.id = linked_genres.genre_id
WHERE linked_genres.genre_id IS NULL
ORDER BY tv_genres.name ASC;
