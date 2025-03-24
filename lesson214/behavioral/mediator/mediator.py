"""
Mediator is a behavioral design pattern that aims to define an object that
encapsulates how a set of objects interact. The Mediator promotes
loose coupling by preventing objects from referring to each other explicitly,
allowing their interaction to vary independently.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Colleague(ABC):
    def __init__(self):
        self.name: str

    @abstractmethod
    def broadcast(self, msg: str) -> None: pass

    @abstractmethod
    def direct(self, msg: str) -> None: pass


class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg: str) -> None:
        self.mediator.broadcast(self, msg)

    def send_direct(self, receiver: str, msg: str) -> None:
        self.mediator.direct(self, receiver, msg)

    def direct(self, msg: str) -> None:
        print(msg)


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, msg: str) -> None: pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None: pass


class Chatroom(Mediator):
    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, msg: str) -> None:
        if not self.is_colleague(colleague):
            return

        # Here you can broadcast to all colleagues.
        # Just iterate over self.colleagues and create a method in
        # ConcreteColleague (Person) to receive this broadcast.
        #
        # For example:
        # for colleague in self.colleagues:
        #   colleague.receive(f'{colleague.name} said: {msg}')
        #
        # Note: The receive method should be created inside Person.
        print(f'{colleague.name} said: {msg}')

    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        if not self.is_colleague(sender):
            return

        receiver_obj: List[Colleague] = [
            colleague for colleague in self.colleagues
            if colleague.name == receiver
        ]

        if not receiver_obj:
            return

        receiver_obj[0].direct(
            f'{sender.name} to {receiver_obj[0].name}: {msg}'
        )


if __name__ == "__main__":
    chat = Chatroom()

    joao = Person('John', chat)
    maria = Person('Mary', chat)
    elis = Person('Elis', chat)
    jose = Person('Joseph', chat)

    chat.add(joao)
    chat.add(maria)
    chat.add(elis)
    chat.add(jose)

    joao.broadcast('Hello everyone')
    maria.broadcast('Hey, how are you all?')
    jose.broadcast('I wasn’t added to the chat...')

    print()
    joao.send_direct('Mary', 'Hi Mary, how are you?')
    maria.send_direct('John', 'I’m good, how about you?')
