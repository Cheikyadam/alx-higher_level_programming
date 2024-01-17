-- TV show genre id
SELECT title, genre_id
FROM tv_shows INNER JOIN tv_show_genres ON id = show_id
ORDER BY title ASC, genre_id ASC;
