"""
Builder is a creational pattern that aims
to separate the construction of a complex object
from its representation, so that the same construction
process can create different representations.

Builder allows you to create objects step-by-step,
and this is something you can already do in Python
without this pattern.

Usually, a builder allows method chaining.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class User(StringReprMixin):
    def __init__(self) -> None:
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers: List = []
        self.addresses: List = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self) -> User: pass

    @abstractmethod
    def add_firstname(self, firstname) -> UserBuilder: pass

    @abstractmethod
    def add_lastname(self, lastname) -> UserBuilder: pass

    @abstractmethod
    def add_age(self, age) -> UserBuilder: pass

    @abstractmethod
    def add_phone(self, phone) -> UserBuilder: pass

    @abstractmethod
    def add_address(self, address) -> UserBuilder: pass


class UserBuilder(IUserBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._result = User()

    @property
    def result(self) -> User:
        return_data = self._result
        self.reset()
        return return_data

    def add_firstname(self, firstname) -> UserBuilder:
        self._result.firstname = firstname
        return self

    def add_lastname(self, lastname) -> UserBuilder:
        self._result.lastname = lastname
        return self

    def add_age(self, age) -> UserBuilder:
        self._result.age = age
        return self

    def add_phone(self, phone) -> UserBuilder:
        self._result.phone_numbers.append(phone)
        return self

    def add_address(self, address) -> UserBuilder:
        self._result.addresses.append(address)
        return self


class UserDirector:
    def __init__(self, builder: UserBuilder) -> None:
        self._builder = builder

    def with_age(self, firstname, lastname, age) -> User:
        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_age(age)
        return self._builder.result

    def with_address(self, firstname, lastname, address) -> User:
        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_address(address)
        return self._builder.result


if __name__ == "__main__":
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age('Luiz', 'Otávio', 30)
    user2 = user_director.with_address('Maria', 'Miranda', 'Av Brasil')
    print(user1)
    print(user2)
