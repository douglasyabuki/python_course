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


class Abstract(ABC):
    def template_method(self) -> None:
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def hook(self) -> None: pass

    def base_class_method(self) -> None:
        print('HELLO, I AM FROM THE ABSTRACT CLASS AND WILL ALSO BE EXECUTED')

    @abstractmethod
    def operation1(self) -> None: pass

    @abstractmethod
    def operation2(self) -> None: pass


class ConcreteClass1(Abstract):
    def hook(self) -> None:
        print('I will use the hook here')

    def operation1(self) -> None:
        print('Operation 1 completed')

    def operation2(self) -> None:
        print('Operation 2 completed')


class ConcreteClass2(Abstract):
    def operation1(self) -> None:
        print('Operation 1 completed (in a different way)')

    def operation2(self) -> None:
        print('Operation 2 completed (in a different way)')


if __name__ == "__main__":
    c1 = ConcreteClass1()
    c1.template_method()

    print()

    c2 = ConcreteClass2()
    c2.template_method()
