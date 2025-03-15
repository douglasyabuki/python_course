"""
args - Unnamed arguments
* - *args (packing and unpacking)
"""
# Remember unpacking
# x, y, *rest = 1, 2, 3, 4
# print(x, y, rest)


# def sum_values(x, y):
#     return x + y

def sum_values(*args):
    total = 0
    for number in args:
        total += number
    return total


sum_1_2_3 = sum_values(1, 2, 3)
# print(sum_1_2_3)

sum_4_5_6 = sum_values(4, 5, 6)
# print(sum_4_5_6)

numbers = 1, 2, 3, 4, 5, 6, 7, 78, 10
another_sum = sum_values(*numbers)  # Unpacking numbers into the function
print(another_sum)

print(sum(numbers))  # Using Python's built-in sum function
# print(*numbers)  # Unpacking the tuple
