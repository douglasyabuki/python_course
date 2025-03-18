# __dict__ and vars for instance attributes
class Person:
    current_year = 2022

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_year(self):
        return Person.current_year - self.age


data = {'name': 'John', 'age': 35}
p1 = Person(**data)  # unpacking dictionary as arguments for the constructor

# Dynamically modify instance attributes:
# p1.__dict__['another'] = 'value'
# p1.__dict__['name'] = 'UPDATED'
# del p1.__dict__['name']

# Inspecting the instance attributes
print(vars(p1))       # Equivalent to p1.__dict__
print(p1.name)
