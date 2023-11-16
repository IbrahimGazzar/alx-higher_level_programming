-- A script that lists all cities contained in the database hbtn_0d_usa.
-- Perform the select using a natural join
SELECT cities.id, cities.name, states.name FROM cities
       NATURAL JOIN states
       ORDER BY cities.id;
