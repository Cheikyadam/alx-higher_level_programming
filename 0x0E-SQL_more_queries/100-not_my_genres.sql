-- TV show genres of Dexter
SELECT name 
FROM tv_genres
WHERE name NOT IN
(SELECT  name
FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = genre_id
INNER JOIN tv_shows ON tv_shows.id = show_id
WHERE title = "Dexter")
ORDER BY name ASC;
