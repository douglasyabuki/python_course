# json.dumps and json.loads with strings + typing.TypedDict
# When converting from Python to JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

import json
# from pprint import pprint
from typing import TypedDict


# Defining a TypedDict for structured type hints
class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


# JSON string representing the movie
string_json = '''
{
  "title": "The Lord of the Rings: The Fellowship of the Ring",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

# Parsing the JSON string into a Python dictionary
movie: Movie = json.loads(string_json)

# Optional debugging prints:
# pprint(movie, width=40)
# print(movie['title'])
# print(movie['characters'][0])
# print(movie['year'] + 10)

# Converting the Python dictionary back to a JSON string
json_string = json.dumps(movie, ensure_ascii=False, indent=2)

print(json_string)
