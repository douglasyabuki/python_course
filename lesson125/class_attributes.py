# Class attributes
class Person:
    current_year = 2022

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_year(self):
        return Person.current_year - self.age


p1 = Person('John', 35)
p2 = Person('Helen', 12)

print(Person.current_year)
# Person.current_year = 1

print(p1.get_birth_year())
print(p2.get_birth_year())
