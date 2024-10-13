CREATE DATABASE Project;
show databases;

CREATE TABLE Project.bus_routes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    state_name TEXT,
    route_name TEXT,
    route_link TEXT,
    busname TEXT,
    bustype TEXT,
    departing_time TIME,
    duration TEXT,
    reaching_time TIME,
    star_rating FLOAT,
    price DECIMAL(10, 2),
    seats_available INT
);


