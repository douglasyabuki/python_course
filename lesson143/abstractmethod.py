# abstractmethod for any decorated method (@property and setter)
# It is possible to create @property, @property.setter, @classmethod,
# @staticmethod, and normal methods as abstract, for that
# use @abstractmethod as the innermost decorator.
# Foo - Bar are placeholder words commonly used
# for terms that can change in programming.

from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('I am useless')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name


foo = Foo('Bar')
print(foo.name)
