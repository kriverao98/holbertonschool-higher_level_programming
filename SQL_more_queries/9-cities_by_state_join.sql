-- This script that lists all cities contained in the database
USE hbtn_0d_usa;
SELECT cities.id, cities.name AS name, state.name AS name;
FROM cities;
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;