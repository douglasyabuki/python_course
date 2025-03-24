"""
Composite is a structural design pattern that allows you
to use composition to create objects in tree structures.
The pattern allows clients to treat individual objects (Leaf)
and compositions of objects (Composite) uniformly.

IMPORTANT: only apply this pattern in structures that can
be represented in a hierarchical (tree) format.

In the Composite pattern, we have two types of objects:
Composite (which represents internal nodes of the tree) and Leaf
(which represents external nodes of the tree).

Composite objects are more complex and have children.
Usually, they delegate work to their children using
a common method.
Leaf objects are simple, at the edges, and have no children.
Usually, these objects perform the actual work of the application.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class BoxStructure(ABC):
    """ Component """
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass
    def remove(self, child: BoxStructure) -> None: pass


class Box(BoxStructure):
    """ Composite """

    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        print(f'\n{self.name}:')
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    """ Leaf """

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == "__main__":
    # Leaf
    tshirt1 = Product('tshirt1', 10)
    tshirt2 = Product('tshirt2', 10)
    tshirt3 = Product('tshirt3', 10)

    # Composite
    tshirt_box = Box('Tshirt Box')
    tshirt_box.add(tshirt1)
    tshirt_box.add(tshirt2)
    tshirt_box.add(tshirt3)

    # Leaf
    smartphone1 = Product('smartphone1', 10000)
    smartphone2 = Product('smartphone2', 10000)

    # Composite
    smartphone_box = Box('Smartphone Box')
    smartphone_box.add(smartphone1)
    smartphone_box.add(smartphone2)

    # Composite
    big_box = Box('Big Box')
    big_box.add(tshirt_box)
    big_box.add(smartphone_box)
    big_box.print_content()
    print(big_box.get_price())
