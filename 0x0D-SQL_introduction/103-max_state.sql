-- Max State
SELECT State, max(value) as max_temp FROM temperatures GROUP BY State ORDER BY State ASC;
