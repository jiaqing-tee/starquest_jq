CREATE USER 'auth_user'@'%' IDENTIFIED BY 'Input_DB_User_Password';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON *.* TO 'auth_user'@'%';

USE auth;

CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);

INSERT INTO users (email, password) VALUES ('test@domain.com', 'Input_User_Password');
