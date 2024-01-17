-- Tmpature stat
SELECT city, avg(value) as avg_temp FROM temperatures GROUP BY City ORDER BY avg_temp DESC;
