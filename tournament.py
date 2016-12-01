#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import random


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
    query2 = "DELETE from player_standings;"
    db_cursor.execute(query2)
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
    query = "INSERT INTO players(name) VALUES (%s);"
    data = (name,)
    db_cursor.execute(query, data)
    db.commit()
    db.close()

def insertNewPlayers():
    db = connect()
    db_cursor = db.cursor()
    #query2 = "DELETE FROM player_standings;"
    #db_cursor.execute(query2)
    '''Put new registered players into Player Standings table'''
    query = "INSERT INTO player_standings (id, name) SELECT id, name FROM players;"
    db_cursor.execute(query)
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
    db = connect()
    db_cursor = db.cursor()
    insertNewPlayers()
    query2 = "SELECT * FROM player_standings;"
    db_cursor.execute(query2)
    standings = db_cursor.fetchall()
    db.commit()
    db.close()

    return standings

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

def randomMatch():
    db = connect()
    db_cursor = db.cursor()
    query = "SELECT * FROM players;"
    db_cursor.execute(query)
    players = db_cursor.fetchall()

    #Test to see if all the players are returned.
    #print "players is returning: {}".format(players)
    matchup = []
    num_players = len(players)

    print "num of players:{}".format(num_players)

    player1 = random.sample(players, 1)
    print player1[0][1]
    print "P1:" + str(player1)
    player2 = random.sample(players, 1)
    print "P2:"+ str(player2)

    while player1 == player2:
        player2 = random.sample(players, 1)
        if player2 != player1:
            print "NEW P2:"+  str(player2)

    matchup.append(player1)
    matchup.append(player2)

    print matchup
    random.shuffle(matchup)

    winner_match = random.randint(0,1)

    print "Match winner:" + str(matchup[winner_match][0][0])


    '''for i in range(random.randint(0, num_players)):
        match = random.shuffle(matchup)
        print match
        winner = match[0]
        print "Winner:" + str(winner)'''




    db.close()

    return players

'''if __name__ == '__main__':
    standings = randomMatch()
    playerinstands = [id1, id2, id3, id4] = [row[0] for row in standings]

    #print playerinstands[1]
    print "Success!  All tests pass!"'''
