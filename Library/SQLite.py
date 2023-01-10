# used to build database for small applications like the apps that we run on phones and tablets

import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("Library\\movies.json").read_text())
print(movies)

# write to db
with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES(?, ?, ?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()

# read db

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    movies = cursor.fetchall()
    print(movies)
