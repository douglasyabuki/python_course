# Exercise - Save your class in JSON
# Save the data from your class to JSON
# and then recreate the instances
# of the class with the saved data
# Do it in separate files.
import json

FILE_PATH = 'lesson127/classdata.json'


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('John', 33)
p2 = Person('Helen', 21)
p3 = Person('Joanna', 11)
db = [vars(p1), p2.__dict__, vars(p3)]


def make_dump():
    with open(FILE_PATH, 'w') as file:
        print('MAKING DUMP')
        json.dump(db, file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print('THIS IS __main__')
    make_dump()
