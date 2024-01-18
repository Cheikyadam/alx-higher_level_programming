-- TV show genre id number pf shows
SELECT name AS genre, count(*) AS number_of_shows
FROM tv_genres INNER JOIN tv_show_genres ON id = genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
