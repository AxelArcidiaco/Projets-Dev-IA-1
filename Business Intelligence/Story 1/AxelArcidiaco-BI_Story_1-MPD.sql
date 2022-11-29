CREATE TABLE Individu(
   code INT,
   nom VARCHAR(25),
   prenom VARCHAR(25),
   PRIMARY KEY(code)
);

CREATE TABLE Professeur(
   id_professeur INT,
   competence VARCHAR(25),
   code INT NOT NULL,
   PRIMARY KEY(id_professeur),
   UNIQUE(code),
   FOREIGN KEY(code) REFERENCES Individu(code)
);

CREATE TABLE Adresse(
   id_adresse INT,
   numero VARCHAR(10) NOT NULL,
   rue TEXT NOT NULL,
   ville VARCHAR(50) NOT NULL,
   code_postal VARCHAR(5) NOT NULL,
   PRIMARY KEY(id_adresse)
);

CREATE TABLE Salle(
   id_salle INT,
   nom VARCHAR(25),
   PRIMARY KEY(id_salle)
);

CREATE TABLE Matiere(
   id_matiere INT,
   nom VARCHAR(25),
   PRIMARY KEY(id_matiere)
);

CREATE TABLE Etudiant(
   id_etudiant INT,
   diplome TEXT,
   id_adresse INT NOT NULL,
   code INT NOT NULL,
   PRIMARY KEY(id_etudiant),
   UNIQUE(id_adresse),
   UNIQUE(code),
   FOREIGN KEY(id_adresse) REFERENCES Adresse(id_adresse),
   FOREIGN KEY(code) REFERENCES Individu(code)
);

CREATE TABLE Cours(
   id_cours INT,
   heure_de_debut TIME NOT NULL,
   heure_de_fin TIME NOT NULL,
   id_matiere INT NOT NULL,
   id_salle INT NOT NULL,
   id_professeur INT NOT NULL,
   PRIMARY KEY(id_cours),
   FOREIGN KEY(id_matiere) REFERENCES Matiere(id_matiere),
   FOREIGN KEY(id_salle) REFERENCES Salle(id_salle),
   FOREIGN KEY(id_professeur) REFERENCES Professeur(id_professeur)
);

CREATE TABLE suivre(
   id_etudiant INT,
   id_cours INT,
   PRIMARY KEY(id_etudiant, id_cours),
   FOREIGN KEY(id_etudiant) REFERENCES Etudiant(id_etudiant),
   FOREIGN KEY(id_cours) REFERENCES Cours(id_cours)
);
