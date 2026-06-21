-- Lists All Cities In Database
SELECT cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
