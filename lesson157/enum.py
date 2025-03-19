# Enum -> Enumerations
# Enumerations in programming are used when we have
# a specific number of things to choose from.
# Enums have members and their values are constants.
# Enums in Python:
#   - are a set of symbolic names (members) bound to unique values
#   - can be iterated to return their canonical members in the order of
#     definition
# enum.Enum is the superclass for your enumerations. But it can also be used
#   directly (even so, Enums are not regular classes in Python).
# You can use your Enum with type annotations, with isinstance,
# and other type-related features.
# To get the data:
# member = Class(value), Class['key']
# key = Class.key.name
# value = Class.key.value
import enum

# Directions = enum.Enum('Directions', ['LEFT', 'RIGHT'])

class Directions(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()
    UP = enum.auto()
    DOWN = enum.auto()


print(Directions(1), Directions['LEFT'], Directions.LEFT)
print(Directions(1).name, Directions.LEFT.value)


def move(direction: Directions):
    if not isinstance(direction, Directions):
        raise ValueError('Direction not found')

    print(f'Moving to {direction.name} ({direction.value})')


move(Directions.LEFT)
move(Directions.RIGHT)
move(Directions.UP)
move(Directions.DOWN)
