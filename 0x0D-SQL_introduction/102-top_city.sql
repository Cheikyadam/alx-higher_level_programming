-- Top City
SELECT City, avg(value) as avg_temp FROM temperatures WHERE month in (7,8) GROUP BY City ORDER BY avg_temp DESC LIMIT 3;
