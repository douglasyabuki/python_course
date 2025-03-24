# https://docs.python.org/pt-br/3/library/doctest.html
# https://docs.python.org/pt-br/3/library/unittest.html
from src.calculator import add

# print(add(10, 20))
# print(add(-10, 20))
# print(add(1.5, 2.5))

try:
    print(add('15', 15))
except AssertionError as e:
    print(f'Invalid operation: {e}')

print('Result', add(25, 25))
