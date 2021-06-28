import json
from pathlib import Path

movies = [
    {"id": 1, "title:": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarden Cop", "year": 1993}
]


data = json.dumps(movies)
Path("helloworld/data/movies.json").write_text(data)


moviedata = Path("helloworld/data/movies.json").read_text()


fmovies = json.loads(moviedata)

print("Hi movie fan! ", fmovies)

# Path("movies.json").unlink()
