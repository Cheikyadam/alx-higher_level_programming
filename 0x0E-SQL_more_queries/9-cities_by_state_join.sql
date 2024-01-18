-- Cities states
SELECT cities.id AS id, cities.name AS name, states.name AS name
FROM states INNER JOIN cities ON (states.id = cities.state_id) ORDER BY id;
