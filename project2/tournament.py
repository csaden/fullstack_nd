#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#
import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    query = 'DELETE FROM matches;'
    c.execute(query)
    c.close()
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    query = 'DELETE FROM players;'
    c.execute(query)
    c.close()
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    query = 'SELECT COUNT (*) FROM players;'
    c.execute(query)
    (result, ) = c.fetchone()
    c.close()
    db.close()
    return result if result else 0


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    query = 'INSERT INTO players (full_name) VALUES(%s);'
    c.execute(query, (name,))
    c.close()
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, total_matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        match_wins: the number of matches the player has won
        match_plays: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()

    query = """SELECT players.id, players.full_name,
    (SELECT COUNT (*) FROM matches m
        WHERE m.player1 = players.id) as match_wins,
    (SELECT COUNT (*) FROM matches m
        WHERE players.id IN (m.player1, m.player2)) as match_plays
    FROM players
    ORDER BY match_wins DESC;
    """

    c.execute(query)
    standings = [tuple(row) for row in c.fetchall()]
    c.close()
    db.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()

    query = "INSERT INTO matches (player1, player2) VALUES(%s, %s);"
    c.execute(query, (winner, loser, ))
    c.close()
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = [player[:2] for player in playerStandings()]
    group_a, group_b = standings[::2], standings[1::2]
    pairings = zip(group_a, group_b)
    return [tuple([p[0][0], p[0][1], p[1][0], p[1][1]]) for p in pairings]
