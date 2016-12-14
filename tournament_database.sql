-- Players Table
CREATE TABLE players (
    id          serial      PRIMARY KEY,
    name        text
  );

-- Matches Table
CREATE TABLE matches(
    id          serial       PRIMARY KEY,
    winner      integer      REFERENCES players(id) NOT NULL, --NOT NULL value used to have zero placeholder when there is no value inserted.
    loser       integer      REFERENCES players(id) NOT NULL  --NOT NULL value used to have zero placeholder when there is no value inserted.
  );

-- TEST CODE for implementation of player_standings table. NOT IN USE ANYMORE
  CREATE TABLE player_standings(
      id          integer      REFERENCES players(id),
      name        text,
      wins        integer      default 0,
      matches     integer      default 0
    );

    '''Reference Join Example'''
    SELECT EMP_ID, NAME, DEPT FROM COMPANY LEFT OUTER JOIN DEPARTMENT
        ON COMPANY.ID = DEPARTMENT.EMP_ID;

    -- View for the total wins a player has within the tournament
    CREATE VIEW total_wins  as SELECT players.id as id, count(winner) as wins FROM players, matches WHERE winner = players.id GROUP BY players.id ORDER BY wins DESC;
    -- View for the total wins a person has within the tournament
    CREATE VIEW wins as SELECT players.id, count(winner) as wins FROM players LEFT JOIN matches ON players.id = matches.winner group by players.id;
    -- View for the total matches a player has played in the tournament
    CREATE VIEW total_matches  as SELECT players.id as id, count(*) as matches FROM players, matches WHERE players.id in (winner, loser) GROUP BY players.id;
    '''TEST CODE
    CREATE VIEW standings as SELECT players.id as pid, total_wins.total_wins as wins, total_matches.total_matches as matches from players, matches where players.id = total_wins.id AND total_wins.id = total_matches.id;
    '''

    -- View for the standings for the players within the tournament which utilizes data from total wins view and total matches view to a standings record for each player.
    CREATE VIEW play_stands as SELECT players.id, players.name, (SELECT count(winner) FROM matches WHERE winner = players.id) as wins, (SELECT count(*) FROM matches WHERE players.id in (winner, loser)) as total_matches FROM players ORDER BY total_wins DESC, total_matches DESC;
