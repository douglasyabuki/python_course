"""
Iterator is a behavioral pattern that aims to provide
a way to access elements of an aggregate object
sequentially without exposing its underlying structure.

- A collection should provide a way to access its elements
  without exposing its internal structure.
- A collection may have different ways and paths
  to expose its elements.
- You should separate the complexity of iteration
  algorithms from the collection itself.

The main idea of this pattern is to remove the responsibility
of traversal from the collection and delegate it to an iterator object.
"""
from collections.abc import Iterator, Iterable
from typing import List, Any


class MyIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0

    def next(self):
        try:
            return self.__next__()
        except StopIteration:
            return None

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class ReverseIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = -1

    def next(self):
        try:
            return self.__next__()
        except StopIteration:
            return None

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self) -> None:
        self._items: List[Any] = []
        self._my_iterator = MyIterator(self._items)

    def add(self, value: Any) -> None:
        self._items.append(value)

    def __iter__(self) -> Iterator:
        return self._my_iterator

    def reverse_iterator(self) -> Iterator:
        return ReverseIterator(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'


if __name__ == "__main__":
    mylist = MyList()
    mylist.add('Luiz')
    mylist.add('Maria')
    mylist.add('John')

    # print(mylist)

    for value in mylist:
        print(value)

    print()

    for value in mylist.reverse_iterator():
        print(value)
