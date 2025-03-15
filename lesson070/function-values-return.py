"""
Return values from functions (return)
"""


def sum_values(x, y):
    if x > 10:
        return [10, 20]  # Returns a list if x is greater than 10
    return x + y  # Returns the sum otherwise


# variable = sum_values(1, 2)
# variable = int('1')
sum1 = sum_values(2, 2)  # Returns 4
sum2 = sum_values(3, 3)  # Returns 6
print(sum1)
print(sum2)
print(sum_values(11, 55))  # Returns [10, 20]
