-- TV show no genre id
SELECT title, genre_id
FROM tv_shows LEFT OUTER JOIN tv_show_genres ON id = show_id
WHERE genre_id is NULL
ORDER BY title ASC, genre_id ASC;
