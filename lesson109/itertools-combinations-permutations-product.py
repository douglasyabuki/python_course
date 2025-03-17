# Combinations, Permutations, and Product - Itertools
# Combination - Order does not matter - iterable + group size
# Permutation - Order matters
# Product - Order matters and repeats unique values
from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


people = [
    'John', 'Jane', 'Louis', 'Leticia',
]
tshirts = [
    ['black', 'white'],
    ['s', 'm', 'l'],
    ['male', 'female', 'unisex'],
    ['cotton', 'polyester']
]

print_iter(combinations(people, 2))
print_iter(permutations(people, 2))
print_iter(product(*tshirts))
