# Dictionaries in Python (dict type)
# Dictionaries are data structures that store
# key-value pairs.
# Keys can be thought of as the "index" (like in lists)
# and must be immutable types such as:
# str, int, float, bool, tuple, etc.
# The value can be of any type, including another dictionary.
# We use curly braces - {} - or the dict class to create dictionaries.
# Immutable types: str, int, float, bool, tuple
# Mutable types: dict, list

# Example dictionary
# person = {
#     'name': 'John',
#     'last_name': 'Doe',
#     'age': 18,
#     'height': 1.8,
#     'addresses': [
#         {'street': 'some street', 'number': 123},
#         {'street': 'another street', 'number': 321},
#     ]
# }

# person = dict(name='John', last_name='Doe')

person = {
    'name': 'John',
    'last_name': 'Doe',
    'age': 18,
    'height': 1.8,
    'addresses': [
        {'street': 'some street', 'number': 123},
        {'street': 'another street', 'number': 321},
    ],
}

# print(person, type(person))
print(person['name'])
print(person['last_name'])

print()

for key in person:
    print(key, person[key])  # Print each key and its corresponding value
