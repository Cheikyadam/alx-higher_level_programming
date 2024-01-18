-- TV show genres of Dexter
SELECT T.title 
FROM tv_shows T
WHERE ("Comedy") NOT IN (SELECT name FROM  tv_genres INNER JOIN tv_show_genres ON tv_genres.id = genre_id
INNER JOIN tv_shows ON tv_shows.id = show_id
WHERE title = T.title)
ORDER BY T.title ASC;
