-- A script that creates the database hbtn_0d_usa and the table states
-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the new database
USE hbtn_0d_usa;
-- Create table
CREATE TABLE IF NOT EXISTS states(
       PRIMARY KEY (id),
       id INT NOT NULL AUTO_INCREMENT,
       name VARCHAR(256) NOT NULL
);
