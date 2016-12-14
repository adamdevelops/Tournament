#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2  #psql python library
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
    #query2 = "DELETE from player_standings;"
    #db_cursor.execute(query2)
    db_cursor.execute(query)
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered from the players table."""

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
    """Adds a player to the tournament database using name inputted into this function.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
    """
    db = connect()
    db_cursor = db.cursor()
    query = "INSERT INTO players(name) VALUES (%s);"  #Insert player into players table
    data = (name,)
    db_cursor.execute(query, data)
    #query2 = "INSERT INTO standings (pid) SELECT id FROM players;"
    #db_cursor.execute(query2)
    db.commit()
    db.close()

'''TEST CODE'''
""" This is previous code for the implementation of the standings as a table instead of a view
    The function was used to insert new players into the standings record.
"""
def insertNewPlayers():
    db = connect()
    db_cursor = db.cursor()
    #query2 = "DELETE FROM player_standings;"
    #db_cursor.execute(query2)
    '''Put new registered players into Player Standings table'''
    query = "INSERT INTO standings (pid) SELECT id FROM players;"
    db_cursor.execute(query)
    db.commit()
    db.close()
'''TEST CODE'''

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
    #insertNewPlayers()
    query2 = "SELECT * FROM play_stands;"   #Return the record of players in the standings table
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
    print ""
    print "Entering reportMatch() function."

    db = connect()
    db_cursor = db.cursor()
    #View who is the winner and loser of a match
    print winner
    print loser
    query = "INSERT INTO matches(winner, loser) VALUES (%s, %s);"   #Insert the winner and loser into matches table
    data = (winner, loser,)
    db_cursor.execute(query, data)
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

    print ""
    print "Entering swissPairings() function."
    db = connect()
    db_cursor = db.cursor()
    #Retrieve the standings view records for each player.
    query = "SELECT * FROM play_stands;"
    db_cursor.execute(query)
    players = db_cursor.fetchall()
    pairings = []   #array used to hold pairing of two grouped players.

    num_players = len(players)
    print "num of players:{}".format(num_players)

    # Group parings of two players
    for x in range(0, num_players - 1, 2):
        paired_players = (players[x][0], players[x][1], players[x + 1][0], players[x + 1][1])
        pairings.append(paired_players)

    db.close()

    #View the pairings of the players
    print pairings

    return pairings


def randomMatch():
    """Randomely generates the winner and loser of a paired matchup.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    """

    db = connect()
    db_cursor = db.cursor()
    query = "SELECT id, name, total_wins FROM play_stands;"
    db_cursor.execute(query)
    players = db_cursor.fetchall()

    #Test to see if all the players are returned.
    #print "players is returning: {}".format(players)
    matchup = []
    num_players = len(players)

    print "num of players:{}".format(num_players)

    #Select two random players from the standings record
    player1 = random.sample(players, 1)
    print "Player 1's name: " + player1[0][1]
    print "P1:" + str(player1)
    player2 = random.sample(players, 1)
    print "P2:"+ str(player2)
    #Create a new player 2 if player 2 is the same player as player 1
    while player1 == player2:
        player2 = random.sample(players, 1)
        if player2 != player1:
            print "NEW P2:"+  str(player2)

    matchup.append(player1)
    matchup.append(player2)
    #Print the matchup of the two players and shuffle the matchup array
    print matchup
    random.shuffle(matchup)
    #Create a random number between 0 and 1 to be used as index to determine winning player.
    winner_match = random.randint(0,1)

    print winner_match
    #Winner of the match determined random generated int between 0 and 1.
    print "Match winner:" + str(matchup[winner_match][0][0])


    '''for i in range(random.randint(0, num_players)):
        match = random.shuffle(matchup)
        print match
        winner = match[0]
        print "Winner:" + str(winner)'''

    db.close()

    return players
