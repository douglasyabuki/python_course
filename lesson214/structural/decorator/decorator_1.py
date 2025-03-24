"""
Decorator is a structural design pattern that allows you
to add new behaviors to objects by placing them inside
a "wrapper" (decorator) object.
Decorators provide a flexible alternative to subclassing
for extending functionality.

Decorator (design pattern) != Python decorator

Python decorator -> A decorator is a callable that accepts another
function as an argument (the decorated function). The decorator can
process the decorated function and return it or replace it with another
function or callable object.
From the book "Fluent Python" by Luciano Ramalho (pg. 223)
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List
from copy import deepcopy


# INGREDIENTS
@dataclass
class Ingredient:
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    price: float = 1.50


@dataclass
class Cheese(Ingredient):
    price: float = 6.35


@dataclass
class MashedPotatoes(Ingredient):
    price: float = 2.25


@dataclass
class PotatoSticks(Ingredient):
    price: float = 0.99


# Hotdogs
class Hotdog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name}({self.price}) -> {self.ingredients})'


class SimpleHotdog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'SimpleHotdog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks()
        ]


class SpecialHotdog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'SpecialHotdog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            Cheese(),
            MashedPotatoes(),
            PotatoSticks()
        ]


# Decorators
class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog) -> None:
        self.hotdog = hotdog

    @property
    def price(self) -> float:
        return self.hotdog.price

    @property
    def name(self) -> str:
        return self.hotdog.name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self.hotdog.ingredients


class BaconDecorator(HotdogDecorator):
    def __init__(self, hotdog: Hotdog) -> None:
        super().__init__(hotdog)

        self._ingredient = Bacon()

        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} +{self._ingredient.__class__.__name__}'

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients


if __name__ == "__main__":
    simple_hotdog = SimpleHotdog()
    decorated_simple_hotdog = HotdogDecorator(simple_hotdog)
    bacon_simple_hotdog = BaconDecorator(simple_hotdog)
    bacon_simple_hotdog = BaconDecorator(bacon_simple_hotdog)

    print(simple_hotdog)
    print(decorated_simple_hotdog)
    print(bacon_simple_hotdog)
