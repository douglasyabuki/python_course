import copy

from data import products

# copy, sorted, products.sort
# Exercises
# Increase the prices of the products below by 10%
# Generate new_products using a deep copy
new_products = [
    {**p, 'price': round(p['price'] * 1.1, 2)}
    for p in copy.deepcopy(products)
]

# print(*products, sep='\n')
# print()
# print(*new_products, sep='\n')

# Sort products by name in descending order (from Z to A)
# Generate products_sorted_by_name using a deep copy
products_sorted_by_name = sorted(
    copy.deepcopy(products),
    key=lambda p: p['name'],
    reverse=True
)
# print(*products, sep='\n')
# print()
# print(*products_sorted_by_name, sep='\n')


# Sort products by price in ascending order (from lowest to highest)
# Generate products_sorted_by_price using a deep copy
products_sorted_by_price = sorted(
    copy.deepcopy(products),
    key=lambda p: p['price']
)

# FINAL

print(*products, sep='\n')
print()
print(*new_products, sep='\n')
print()
print(*products_sorted_by_name, sep='\n')
print()
print(*products_sorted_by_price, sep='\n')
