"""
Specify the types of objects to be created
using a prototype instance and create new objects
by copying this prototype.
"""

from __future__ import annotations
from typing import List
from copy import deepcopy


class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == "__main__":

    luiz = Person('Luiz', 'Miranda')
    luiz_address = Address('Av. Brasil', '250A')
    luiz.add_address(luiz_address)

    luiz_wife = luiz.clone()
    luiz_wife.firstname = 'Letícia'

    print(luiz)
    print(luiz_wife)
