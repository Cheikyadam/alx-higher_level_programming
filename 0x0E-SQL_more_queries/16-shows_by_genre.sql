-- TV show  all
SELECT title, name
FROM tv_genres RIGHT OUTER JOIN tv_show_genres ON tv_genres.id = genre_id
RIGHT OUTER JOIN tv_shows ON tv_shows.id = show_id
ORDER BY title ASC, name ASC;
