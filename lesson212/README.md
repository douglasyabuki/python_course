# Type annotations em Python

**What are Type Annotations?** They are parts of the code used to indicate data types in places like variables, function parameters, and return types of functions and methods. In Python, they are used for documentation and to assist with code editor autocompletion, as the language will still execute the code even if the annotations are incorrect.

# Basic variable annotations

```python
a_string: str = 'A value'
an_integer: int = 123456
a_float: float = 1.23
a_boolean: bool = True
a_set: set = {1, 2, 3}  # more on this below
a_list: list = []  # more on this below
a_dict: dict = {}  # more on this below
```

# Function and method parameters

```python
# x and y must be integers
# z must be a float
# note: float accepts both int and float,
# int accepts only int.
# To specify the return type, use:
# `-> type` before the colon, like in
# def () -> None: for functions without return values
def add(x: int, y: int, z: float) -> float:
    return x + y + z
```

# Lists

```python
list_of_integers: list[int] = [1, 2, 3, 4]
list_of_strings: list[str] = ["a", "b", "c", "d"]
list_of_tuples: list[tuple] = [(1, "a"), (2, "b")]
list_of_list_of_ints: list[list[int]] = [[1], [4, 5]]
```

# Dictionaries

```python
a_dict: dict[str, int] = {
    "A": 0,
    "B": 0,
    "C": 0,
}

a_dict_of_lists: dict[str, list[int]] = {
    "A": [1, 2],
    "B": [3, 4],
    "C": [5, 6],
}
```

# Sets

```python
a_set_of_integers: set[int] = {1, 2, 3}
```

# Type aliases

```python
# These are type aliases
ListOfIntegers = list[int]
DictOfListOfIntegers = dict[str, ListOfIntegers]

a_dict_of_lists: DictOfListOfIntegers = {
    "A": [1, 2],
    "B": [3, 4],
    "C": [5, 6],
}
```

# Union types

```python
string_or_integer: str | int = 1  # Union
string_or_integer = "A"  # No errors
string_or_integer = 2  # No errors
```

# Optional types

```python
def add(x: float, y: float | None = None) -> float:
    if isinstance(y, int | float):
        return x + y
    return x + x
```

# Callable

```python
from collections.abc import Callable

AddIntegers = Callable[[int, int], int]


def execute(func: AddIntegers, a: int, b: int) -> int:
    return func(a, b)


def add(a: int, b: int) -> int:
    return a + b


execute(add, 1, 2)
```

# TypeVar

```python
from typing import TypeVar

T = TypeVar('T')


def get_item(list: list[T], index: int) -> T:
    return list[index]


list_int = get_item([1, 2, 3], 1)  # int
list_str = get_item(['a', 'b', 'c'], 1)  # str
```

# Your classes are types too

```python
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"


def say_my_name(person: Person) -> str:
    return person.full_name


print(say_my_name(Person("John", "Doe")))
```