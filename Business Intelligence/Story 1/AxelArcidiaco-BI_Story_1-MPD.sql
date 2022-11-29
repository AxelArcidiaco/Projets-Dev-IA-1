CREATE TABLE Movies(
   id_movie INT,
   original_title VARCHAR(50) NOT NULL,
   title VARCHAR(50),
   runtime TIME NOT NULL,
   original_language TEXT NOT NULL,
   spoken_language TEXT,
   adult LOGICAL NOT NULL,
   budget VARCHAR(50),
   overview TEXT,
   release_date DATE NOT NULL,
   PRIMARY KEY(id_movie)
);

CREATE TABLE Countries(
   id_country VARCHAR(50),
   country_name VARCHAR(50) NOT NULL,
   country_code VARCHAR(50) NOT NULL,
   PRIMARY KEY(id_country)
);

CREATE TABLE Genre(
   id_genre INT,
   genre_name VARCHAR(50) NOT NULL,
   PRIMARY KEY(id_genre)
);

CREATE TABLE Persons(
   id_person INT,
   lastname VARCHAR(50) NOT NULL,
   firstname VARCHAR(50) NOT NULL,
   gender CHAR(1) NOT NULL,
   PRIMARY KEY(id_person)
);

CREATE TABLE Characters(
   id_character INT,
   character_name VARCHAR(50) NOT NULL,
   PRIMARY KEY(id_character)
);

CREATE TABLE Studio(
   id_studio INT,
   studio_name VARCHAR(50),
   PRIMARY KEY(id_studio)
);

CREATE TABLE Users(
   id_user INT,
   identifiant VARCHAR(50) NOT NULL,
   password VARCHAR(50) NOT NULL,
   id_person INT NOT NULL,
   PRIMARY KEY(id_user),
   UNIQUE(id_person),
   FOREIGN KEY(id_person) REFERENCES Persons(id_person)
);

CREATE TABLE Actors(
   id_actor COUNTER,
   id_person INT NOT NULL,
   PRIMARY KEY(id_actor),
   UNIQUE(id_person),
   FOREIGN KEY(id_person) REFERENCES Persons(id_person)
);

CREATE TABLE Posséder(
   id_movie INT,
   id_genre INT,
   PRIMARY KEY(id_movie, id_genre),
   FOREIGN KEY(id_movie) REFERENCES Movies(id_movie),
   FOREIGN KEY(id_genre) REFERENCES Genre(id_genre)
);

CREATE TABLE Tourner(
   id_movie INT,
   id_country VARCHAR(50),
   PRIMARY KEY(id_movie, id_country),
   FOREIGN KEY(id_movie) REFERENCES Movies(id_movie),
   FOREIGN KEY(id_country) REFERENCES Countries(id_country)
);

CREATE TABLE Regarder(
   id_user INT,
   id_movie INT,
   PRIMARY KEY(id_user, id_movie),
   FOREIGN KEY(id_user) REFERENCES Users(id_user),
   FOREIGN KEY(id_movie) REFERENCES Movies(id_movie)
);

CREATE TABLE Jouer(
   id_actor INT,
   id_character INT,
   PRIMARY KEY(id_actor, id_character),
   FOREIGN KEY(id_actor) REFERENCES Actors(id_actor),
   FOREIGN KEY(id_character) REFERENCES Characters(id_character)
);

CREATE TABLE Appartenir(
   id_movie INT,
   id_character INT,
   PRIMARY KEY(id_movie, id_character),
   FOREIGN KEY(id_movie) REFERENCES Movies(id_movie),
   FOREIGN KEY(id_character) REFERENCES Characters(id_character)
);

CREATE TABLE Produire(
   id_movie INT,
   id_studio INT,
   PRIMARY KEY(id_movie, id_studio),
   FOREIGN KEY(id_movie) REFERENCES Movies(id_movie),
   FOREIGN KEY(id_studio) REFERENCES Studio(id_studio)
);
