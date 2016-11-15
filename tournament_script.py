#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import random

the_players = [
    (1, 'Jeff'),
    (2, 'Bob'),
    (3, 'Willy'),
    (4, 'Blair'),
    (5, 'Hansel'),
    (6, 'Joe')
]


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    db_cursor = db.cursor()
    query = "DELETE from matches;"
    db_cursor.execute(query)
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    db_cursor = db.cursor()
    query = "DELETE from players;"
    db_cursor.execute(query)
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""

    db = connect()
    db_cursor = db.cursor()
    query = "SELECT count(*) as total_players FROM players;"
    db_cursor.execute(query)
    count = db_cursor.fetchone()[0]
    #result = count.fetchall()
    print "Count players is returning: {}".format(count)

    db.close()

    return count

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
    """
    db = connect()
    db_cursor = db.cursor()
    query = "INSERT INTO players(name)  VALUES ('%s');" % name
    query2 = "INSERT INTO player_standings(name)  VALUES ('%s');" % name
    db_cursor.execute(query)
    db_cursor.execute(query2)
    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """


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

def randomMatch(the_players):
    num_players = len(the_players)
    for i in the range(100):
        player1 = random.sample(the_players, 1)
        player1 = random.sample(the_players, 1)
        if player1 == player2:
            player2 = (player1 + 1) % num_players



def setup_playersandmatches():
    deletePlayers()
    randomMatch(the_players)
