-- Write a script that creates the database hbtn_0d_usa and the table cities
-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the database
USE hbtn_0d_usa;
-- Create table
CREATE TABLE IF NOT EXISTS cities(
       PRIMARY KEY (id),
       FOREIGN KEY (state_id) REFERENCES states(id),
       id INT NOT NULL AUTO_INCREMENT,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL
);
