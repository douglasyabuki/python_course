# __new__ and __init__ in Python classes
# __new__ is the method responsible for creating and
# returning the new object. That's why new receives cls.
# __new__ ❗️MUST return the new object❗️
# __init__ is the method responsible for initializing
# the instance. That's why init receives self.
# __init__ ❗️MUST NOT return anything (None)❗️
# object is the superclass of a class

class A:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, x):
        self.x = x
        print('I am the init')

    def __repr__(self):
        return 'A()'


a = A(123)
print(a.x)
