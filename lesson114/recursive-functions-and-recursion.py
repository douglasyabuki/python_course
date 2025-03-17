# Recursive functions and recursion
# - functions that can call themselves back
# - useful to break big problems into smaller parts
# Every recursive function must have:
# - A problem that can be divided into smaller parts
# - A recursive case that solves the smaller problem
# - A base case that stops the recursion
# - factorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://en.wikipedia.org/wiki/Factorial
# import sys

# sys.setrecursionlimit(1004)


# def recursive(start=0, end=4):

#     print(start, end)

#     # Base case
#     if start >= end:
#         return end

#     # Recursive case
#     # count until reaching the end
#     start += 1
#     return recursive(start, end)


# print(recursive(0, 1001))


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
print(factorial(10))
print(factorial(100))
