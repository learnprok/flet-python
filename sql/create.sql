DROP DATABASE IF EXISTS prueba;
CREATE DATABASE prueba;
USE prueba;

CREATE TABLE user(
    idUser INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    lastName VARCHAR(50)
);


