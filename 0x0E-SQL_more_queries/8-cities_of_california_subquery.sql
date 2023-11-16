-- A script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- Select the state id of California with a subquery
SELECT id, name FROM cities
       WHERE state_id = (SELECT id from states WHERE name = 'California')
       ORDER BY id;
