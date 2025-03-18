# Class methods + factories
# These are methods where "self" will be "cls", meaning,
# instead of receiving the instance as the first
# parameter, we will receive the class itself.
class Person:
    year = 2023  # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def class_method(cls):
        print('Hey')

    @classmethod
    def create_with_50_years(cls, name):
        return cls(name, 50)

    @classmethod
    def create_without_name(cls, age):
        return cls('Anonymous', age)


p1 = Person('John', 34)
p2 = Person.create_with_50_years('Helen')
p3 = Person('Anonymous', 23)
p4 = Person.create_without_name(25)
print(p2.name, p2.age)
print(p3.name, p3.age)
print(p4.name, p4.age)
# print(Person.year)
# Person.class_method()
