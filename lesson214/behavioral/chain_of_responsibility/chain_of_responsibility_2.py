"""
Chain of Responsibility (COR) is a behavioral pattern
that aims to decouple the sender of a request from its receiver,
by giving more than one object the chance to handle the request.
Chain the receiving objects and pass the request along the chain
until an object handles it.
"""

from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self.successor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str: pass


class HandlerABC(Handler):
    def __init__(self, successor: Handler) -> None:
        self.letters = ['A', 'B', 'C']
        self.successor = successor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'HandlerABC: handled value {letter}'
        return self.successor.handle(letter)


class HandlerDEF(Handler):
    def __init__(self, successor: Handler) -> None:
        self.letters = ['D', 'E', 'F']
        self.successor = successor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'HandlerDEF: handled value {letter}'
        return self.successor.handle(letter)


class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        return f'HandlerUnsolved: could not handle {letter}'


if __name__ == "__main__":
    handler_unsolved = HandlerUnsolved()
    handler_def = HandlerDEF(handler_unsolved)
    handler_abc = HandlerABC(handler_def)

    print(handler_abc.handle('A'))
    print(handler_abc.handle('B'))
    print(handler_abc.handle('C'))
    print(handler_abc.handle('D'))
    print(handler_abc.handle('E'))
    print(handler_abc.handle('F'))
    print(handler_abc.handle('G'))
    print(handler_abc.handle('H'))
    print(handler_abc.handle('I'))

    print()
    print(handler_def.handle('A'))
    print(handler_def.handle('B'))
    print(handler_def.handle('C'))
    print(handler_def.handle('D'))
    print(handler_def.handle('E'))
    print(handler_def.handle('F'))
    print(handler_def.handle('G'))
    print(handler_def.handle('H'))
    print(handler_def.handle('I'))

    print()
    print(handler_unsolved.handle('A'))
    print(handler_unsolved.handle('B'))
    print(handler_unsolved.handle('C'))
    print(handler_unsolved.handle('D'))
    print(handler_unsolved.handle('E'))
    print(handler_unsolved.handle('F'))
    print(handler_unsolved.handle('G'))
    print(handler_unsolved.handle('H'))
    print(handler_unsolved.handle('I'))
