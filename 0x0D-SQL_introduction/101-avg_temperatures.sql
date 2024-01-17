-- Tmpature stat
SELECT City, avg(value) as avg_temp FROM temperatures GROUP BY City ORDER BY avg_temp DESC;
