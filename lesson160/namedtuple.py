# namedtuples - immutable tuples with names for values
# We use namedtuples to create object classes that are just a
# grouping of attributes, like normal classes without methods, or database records, etc.
# Namedtuples are immutable just like regular tuples.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
# from collections import namedtuple
from typing import NamedTuple


class Card(NamedTuple):
    value: str = 'VALUE'
    suit: str = 'SUIT'


# Card = namedtuple(
#     'Card', ['value', 'suit'],
#     defaults=['VALUE', 'SUIT']
# )
ace_of_spades = Card('A')

print(ace_of_spades._asdict())
print(ace_of_spades)
print(ace_of_spades[0])
print(ace_of_spades.value)
print(ace_of_spades[1])
print(ace_of_spades.suit)

print()
print(ace_of_spades._fields)
print(ace_of_spades._field_defaults)


for value in ace_of_spades:
    print(value)
