CREATE USER 'auth_user'@'%' IDENTIFIED BY 'Input_DB_User_Password';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON *.* TO 'auth_user'@'%';

USE auth;

CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(162) NOT NULL
);

INSERT INTO users (email, password_hash) VALUES ('test@domain.com', 'Input_User_Password_Hash');
