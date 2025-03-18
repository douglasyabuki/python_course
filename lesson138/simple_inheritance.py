# Simple Inheritance - Relationships between classes
# Association - uses, Aggregation - has
# Composition - owns, Inheritance - is a
#
# Inheritance vs Composition
#
# Parent Class (Person)
#   -> super class, base class, parent class
# Child Classes (Client)
#   -> sub class, child class, derived class
class Person:
    cpf = '1234'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_class_name(self):
        print('Class PERSON')
        print(self.first_name, self.last_name, self.__class__.__name__)


class Client(Person):
    def say_class_name(self):
        print('Whoa, I am still in the CLIENT class')
        print(self.first_name, self.last_name, self.__class__.__name__)


class Student(Person):
    cpf = 'student cpf'
    ...


c1 = Client('Luiz', 'Otávio')
c1.say_class_name()
a1 = Student('Maria', 'Helena')
a1.say_class_name()
print(a1.cpf)
# help(Client)
