CREATE TABLE players (
    id          serial      PRIMARY KEY,
    name        text
  );

CREATE TABLE matches(
    id          serial       PRIMARY KEY,
    winner      integer      REFERENCES players(id),
    loser       integer      REFERENCES players(id)
  );

  CREATE TABLE player_standings(
      id          integer      PRIMARY KEY REFERENCES players(id),
      name        text,
      wins        integer      default 0,
      matches     integer      default 0
    );
    
    '''Join Example'''
    SELECT EMP_ID, NAME, DEPT FROM COMPANY LEFT OUTER JOIN DEPARTMENT
        ON COMPANY.ID = DEPARTMENT.EMP_ID;

    SELECT players.id, players.name INTO player_standings FROM players;

    select count() as num from player_standings;

    '''Give new registered players zero wins and zero matches played'''
    query = "INSERT INTO player_standings (id, name) SELECT id, name FROM players"
    db_cursor.execute(query)
