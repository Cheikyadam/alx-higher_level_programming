-- Rating here
SELECT title, sum(rate) AS rating
FROM tv_shows INNER JOIN tv_show_ratings ON show_id = id
GROUP BY title
ORDER BY rating DESC;
