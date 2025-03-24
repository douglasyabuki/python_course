"""
Template Method (behavioral) aims to define
an algorithm in a method, deferring some steps
to subclasses via inheritance. The Template Method allows
subclasses to redefine certain steps of an algorithm
without changing its structure.

It is also possible to define hooks for subclasses
to use if needed.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversion of Control)
"""
from abc import ABC, abstractmethod


class Pizza(ABC):
    """ Abstract class """

    def prepare(self) -> None:
        """ Template method """
        self.hook_before_add_ingredients()  # Hook
        self.add_ingredients()  # Abstract
        self.hook_after_add_ingredients()  # Hook
        self.cook()  # Abstract
        self.cut()  # Concrete
        self.serve()  # Concrete

    def hook_before_add_ingredients(self) -> None: pass
    def hook_after_add_ingredients(self) -> None: pass

    def cut(self) -> None:
        print(f'{self.__class__.__name__}: Cutting pizza.')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: Serving pizza.')

    @abstractmethod
    def add_ingredients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class AModa(Pizza):
    def add_ingredients(self) -> None:
        print(f'AModa - adding ingredients: ham, cheese, guava paste')

    def cook(self) -> None:
        print(f'AModa - cooking for 45min in a wood-fired oven')


class Veg(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print('Veg - Washing ingredients')

    def add_ingredients(self) -> None:
        print(f'Veg - adding ingredients: vegan ingredients')

    def cook(self) -> None:
        print(f'Veg - cooking for 5min in a regular oven')


if __name__ == "__main__":
    a_moda = AModa()
    a_moda.prepare()

    print()

    veg = Veg()
    veg.prepare()
