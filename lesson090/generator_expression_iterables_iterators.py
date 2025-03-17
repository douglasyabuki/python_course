import sys

# Generator Expression, Iterables, and Iterators in Python

iterable = ['I', 'Have', '__iter__']
iterator = iter(iterable)  # Has __iter__ and __next__

# List comprehension (stores all elements in memory)
list_comprehension = [n for n in range(1_000_000)]

# Generator expression (yields values one by one)
generator_expression = (n for n in range(1_000_000))

# Memory usage comparison
print(sys.getsizeof(list_comprehension))  # Large memory consumption
print(sys.getsizeof(generator_expression))  # Very small memory consumption

print(generator_expression)  # Generator object (not a list)

# Iterating over the generator
# for n in generator_expression:
#     print(n)
