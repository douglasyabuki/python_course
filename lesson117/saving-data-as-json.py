import json

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'addresses': [
        {'street': 'R1', 'number': 32},
        {'street': 'R2', 'number': 55},
    ],
    'height': 1.8,
    'favorite_numbers': (2, 4, 6, 8, 10),
    'dev': True,
    'nothing': None,
}

with open('lesson117/lesson117.json', 'w', encoding='utf8') as file:
    json.dump(
        person,
        file,
        ensure_ascii=False,
        indent=2,
    )

with open('lesson117/lesson117.json', 'r', encoding='utf8') as file:
    person = json.load(file)
    # print(person)
    # print(type(person))
    print(person['first_name'])
