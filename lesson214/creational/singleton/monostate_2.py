"""
Monostate (or Borg) - A variation of the Singleton proposed
by Alex Martelli, designed to ensure that the
state of the object is the same across all instances.
"""
from __future__ import annotations
from typing import Dict


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class MonoState(StringReprMixin):
    _state: Dict = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, firstname=None, lastname=None) -> None:
        if firstname is not None:
            self.firstname = firstname

        if lastname is not None:
            self.lastname = lastname


class A(MonoState):
    pass


if __name__ == "__main__":
    m1 = MonoState(firstname='Luiz')
    m2 = A(lastname='Miranda')
    print(m1)
    print(m2)
