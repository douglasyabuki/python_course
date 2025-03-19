# Metaclasses are the type of classes
# IN PYTHON, EVERYTHING IS AN OBJECT (CLASSES TOO)
# So, what is the type of a class? (type)
# Your object is an instance of your class
# Your class is an instance of type (type is a metaclass)
# type('Name', (Bases,), __dict__)
#
# When creating a class, things happen by default in this order:
# __new__ of the metaclass is called and creates the new class
# __call__ of the metaclass is called with the arguments and calls:
#   __new__ of the class with the arguments (creates the instance)
#   __init__ of the class with the arguments
# __call__ of the metaclass finishes execution
#
# Important methods of the metaclass:
# __new__(mcs, name, bases, dct) (Creates the class)
# __call__(cls, *args, **kwargs) (Creates and initializes the instance)
#
# "Metaclasses are deeper magic than 99% of users should ever worry about.
# If you wonder whether you need them, you don’t (the people who actually
# need them know with certainty that they need them, and don’t need an
# explanation as to why)."
# — Tim Peters (CPython Core Developer)

def my_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = my_repr

        if 'speak' not in cls.__dict__ or \
                not callable(cls.__dict__['speak']):
            raise NotImplementedError('Implement speak')

        return cls

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)

        if 'name' not in instance.__dict__:
            raise NotImplementedError('Create the attribute name')

        return instance


class Person(metaclass=Meta):
    # speak = 123

    def __new__(cls, *args, **kwargs):
        print('MY NEW')
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print('MY INIT')
        # self.name = name

    def speak(self):
        print('SPEAKING...')


p1 = Person('Luiz')
p1.speak()
