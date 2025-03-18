# Understanding self in Python classes
# Class - Blueprint (usually without data)
# Instance of the class (object) - Holds the data
# A class can generate multiple instances.
# Inside the class, self refers to the instance itself.

class Car:
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        print(f'{self.name} is accelerating...')


fusca = Car('Fusca')
fusca.accelerate()
Car.accelerate(fusca)
# print(fusca.name)
# fusca.accelerate()

celta = Car(name='Celta')
celta.accelerate()
Car.accelerate(celta)
# print(celta.name)
