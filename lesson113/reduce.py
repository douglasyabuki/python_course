# reduce - reduces an iterable into a single value
from functools import reduce

products = [
    {'name': 'Product 5', 'price': 10},
    {'name': 'Product 1', 'price': 22},
    {'name': 'Product 3', 'price': 2},
    {'name': 'Product 2', 'price': 6},
    {'name': 'Product 4', 'price': 4},
]


# def reduce_function(accumulator, product):
#     print('accumulator', accumulator)
#     print('product', product)
#     print()
#     return accumulator + product['price']


total = reduce(
    lambda acc, p: acc + p['price'],
    products,
    0
)

print('Total is', total)


# total = 0
# for p in products:
#     total += p['price']

# print(total)

# print(sum([p['price'] for p in products]))
