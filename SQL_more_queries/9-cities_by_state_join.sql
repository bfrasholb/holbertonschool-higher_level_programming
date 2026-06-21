-- Lists All Cities In Database
SELECT cities.name, states.name
FROM cities JOIN states ON cities.state_id = state_id ORDER BY cities.id ASC;
