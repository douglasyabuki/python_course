# Methods in class instances in Python
# Hard coded - It is something that was written directly in the code
class Car:
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        print(f'{self.name} is accelerating...')


string = 'John'
print(string.upper())

fusca = Car('Fusca')
print(fusca.name)
fusca.accelerate()

celta = Car(name='Celta')
print(celta.name)
celta.accelerate()
