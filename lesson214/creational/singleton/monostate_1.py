"""
Monostate (or Borg) - A variation of the Singleton proposed
by Alex Martelli, intended to ensure that
the state of the object is shared among all instances.
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


class MonoStateSimple(StringReprMixin):
    _state: Dict = {}

    def __init__(self, firstname=None, lastname=None) -> None:
        self.__dict__ = self._state

        if firstname is not None:
            self.firstname = firstname

        if lastname is not None:
            self.lastname = lastname


if __name__ == "__main__":
    m1 = MonoStateSimple(firstname='Luiz')
    m2 = MonoStateSimple(lastname='Miranda')
    print(m1)
    print(m2)
