# JSON stands for javascript object notation
import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "Year": 1989},
    {"id": 2, "title": "KC", "Year": 1993},
]
data = json.dumps(movies)
Path("Library\\movies.json").write_text(data)


otherData = Path("Library\\movies.json").read_text()
movies = json.loads(otherData)
print(movies)
