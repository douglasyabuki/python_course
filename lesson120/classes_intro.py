# class - Classes are templates to create new objects
# Classes generate new objects (instances) that
# can have their own attributes and methods.
# The objects created by the class can use their internal data
# to perform various actions.
# By convention, we use PascalCase for class names.

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


p1 = Person('John', 'Doe')
p2 = Person('Joe', 'Tho')

print(p1.first_name)
print(p1.last_name)

print(p2.first_name)
print(p2.last_name)
