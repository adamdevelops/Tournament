CREATE TABLE players (
    id          serial      PRIMARY KEY,
    name        text
  );

CREATE TABLE matches(
    id          serial       PRIMARY KEY,
    winner      integer      REFERENCES players(id),
    loser       integer      REFERENCES players(id)
  );
