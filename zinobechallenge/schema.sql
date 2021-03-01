DROP TABLE IF EXISTS challenge_zinobe;

CREATE TABLE challenge_zinobe (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  total_time REAL NOT NULL,
  mean_time REAL NOT NULL,
  min_time REAL NOT NULL,
  max_time REAL NOT NULL
);
