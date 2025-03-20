# json.dump and json.load with files
import json
import os

FILE_NAME = 'lesson177.json'
ABSOLUTE_FILE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        FILE_NAME
    )
)

movie = {
    'title': 'The Lord of the Rings: The Fellowship of the Ring',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

# Saving dictionary data into a JSON file
with open(ABSOLUTE_FILE_PATH, 'w') as file:
    json.dump(movie, file, ensure_ascii=False, indent=2)

# Reading data back from the JSON file
with open(ABSOLUTE_FILE_PATH, 'r') as file:
    movie_from_json = json.load(file)
    print(movie_from_json)
