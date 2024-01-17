-- Cities states
SELECT cities.id as id, cities.name as name, states.name as name
FROM states INNER JOIN cities ON (states.id = cities.state_id) ORDER BY id;
