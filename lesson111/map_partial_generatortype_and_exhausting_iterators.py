# map, partial, GeneratorType and exhausting Iterators

from functools import partial
from types import GeneratorType


# map - for mapping data
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]


def increase_percentage(value, percentage):
    return round(value * percentage, 2)


increase_ten_percent = partial(
    increase_percentage,
    percentage=1.1
)


def change_product_price(product):
    return {
        **product,
        'price': increase_ten_percent(
            product['price']
        )
    }


new_products = list(map(
    change_product_price,
    products
))


print_iter(products)
print_iter(new_products)

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)
