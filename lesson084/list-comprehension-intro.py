# Introduction to List Comprehension in Python
# List comprehension is a quick way to create lists
# from iterables.

import pprint


def p(value):
    pprint.pprint(value, sort_dicts=False, width=40)


# Creating a list using a loop
numbers_list = []
for number in range(10):
    numbers_list.append(number)
# print(numbers_list)

# Creating a list using list comprehension
numbers_list = [
    number * 2
    for number in range(10)
]

# print(list(range(10)))
# print(numbers_list)

# Mapping data using list comprehension
products = [
    {'name': 'p1', 'price': 20},
    {'name': 'p2', 'price': 10},
    {'name': 'p3', 'price': 30},
]

# Applying a 5% price increase only if price > 20
new_products = [
    {**product, 'price': product['price'] * 1.05}
    if product['price'] > 20 else {**product}
    for product in products
]

# print(new_products)
# p(new_products)

# Filtering in list comprehension
filtered_products = [
    {**product, 'price': product['price'] * 1.05}
    if product['price'] > 20 else {**product}
    for product in products
    if (product['price'] >= 20 and product['price'] * 1.05) > 10
]
p(filtered_products)
