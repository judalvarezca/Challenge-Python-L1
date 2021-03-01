DROP TABLE IF EXISTS challenge_zinobe;

CREATE TABLE challenge_zinobe (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  region TEXT NOT NULL,
  city_name TEXT NOT NULL,
  language TEXT NOT NULL,
  time REAL NOT NULL
);
