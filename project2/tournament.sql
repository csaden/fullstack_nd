-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
CREATE DATABASE tournament;

\c tournament;

CREATE TABLE players(
	id			SERIAL PRIMARY KEY NOT NULL,
	full_name 	TEXT NOT NULL
);

CREATE TABLE matches(
	id			SERIAL PRIMARY KEY NOT NULL,
	player1		INT REFERENCES players(id),
	player2		INT REFERENCES players(id),
	winner		INT REFERENCES players(id)
);