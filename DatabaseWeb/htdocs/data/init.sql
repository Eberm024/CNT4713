CREATE DATABASE IF NOT EXISTS test;

use test;

CREATE TABLE users (
    id INT(11) UNSIGNED PRIMARY KEY,
    firstame VARCHAR(30) NOT NULL,
    lastname VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    age INT(3),
    location VARCHAR(50),
);
