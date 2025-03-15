# Sets - Sets in Python (set type)
# Sets are taught in mathematics
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Represented graphically by the Venn diagram
# Sets in Python are mutable but only accept
# immutable types as internal values.

# Creating a set
# set(iterable) or {1, 2, 3}
# s1 = set('John')
# s1 = set()  # Empty set
# s1 = {'John', 1, 2, 3}  # Set with values

# Sets are efficient for removing duplicate values
# from iterables.
# - Their values will always be **unique**;
# - They **do not accept mutable values**;
# - They **do not have indexes**;
# - They **do not guarantee order**;
# - They **are iterable** (can use `for`, `in`, `not in`).

# Example of removing duplicates:
# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = {1, 2, 3}
# print(3 not in s1)
# for number in s1:
#     print(number)

# Useful Methods:
# add, update, clear, discard
s1 = set()
s1.add('John')
s1.add(1)
s1.update(('Hello world', 1, 2, 3, 4))  # Adds multiple elements
# s1.clear()  # Clears all elements
s1.discard('Hello world')  # Removes an element (if exists)
s1.discard('John')  # Removing another element
# print(s1)

# Useful Operators:
# Union | (union) - Combines sets
# Intersection & (intersection) - Items present in both sets
# Difference - Items present only in the left set
# Symmetric Difference ^ - Items that are **not** in both sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2  # Union
s3 = s1 & s2  # Intersection
s3 = s2 - s1  # Difference
s3 = s1 ^ s2  # Symmetric Difference
print(s3)
