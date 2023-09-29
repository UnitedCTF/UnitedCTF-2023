CREATE DATABASE boatdb;
CREATE USER 'wellerman'@'localhost' IDENTIFIED BY 'FLAG-ThereOnceWasAShipThatPutToSea';
GRANT ALL PRIVILEGES ON boatdb.* TO 'wellerman'@localhost;
GRANT FILE ON *.* TO wellerman@localhost;
FLUSH PRIVILEGES;

USE boatdb;
CREATE TABLE crew (id BIGINT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(192), nickname VARCHAR(64));
INSERT INTO crew (name, nickname) VALUES ('Jacob Teague', 'Captain Jack Sparrow'),
                                         ('Monkey D. Luffy', 'Straw Hat'),
                                         ('John Draper', 'Cap''n Crunch'),
                                         ('James Hook', 'Captain Hook'),
                                         ('Rokuro Okajima', 'Rock'),
                                         ('Captain Harlock', 'The Space Pirate'),
                                         ('Han Solo', 'The Mercenary'),
                                         ('Edward Teach', 'Blackbeard'),
                                         ('Khayr al-Din Barbarus', 'Barbarossa'),
                                         ('John Rackham', 'Calico Jack'),
                                         ('Jolly Roger', 'FLAG-InsecureDirectObjectReferences'),
                                         ('Anne de Graaf', 'Godless Anne'),
                                         ('Mary Read', 'Mark Read'),
                                         ('Usopp', 'Sogeking');

CREATE TABLE roles (role VARCHAR(40) PRIMARY KEY, id BIGINT);
INSERT INTO roles VALUES ('Captain', 1),
                         ('Navigator', 12),
                         ('FLAG-DumpingTheWholeDatabaseIsAnOption', 11),
                         ('Proud Warrior of the Sea', 14);
