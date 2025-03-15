# Dictionary Comprehension and Set Comprehension

# Example dictionary
product = {
    'name': 'Blue Pen',
    'price': 2.5,
    'category': 'Office',
}

# Dictionary comprehension with conditions
dict_comprehension = {
    key: value.upper() if isinstance(value, str) else value  # Convert strings to uppercase
    for key, value in product.items()
    if key != 'category'  # Exclude 'category' key
}

# Creating a dictionary from a list of tuples
list_of_tuples = [
    ('a', 'value a'),
    ('b', 'value a'),
    ('b', 'value a'),  # Duplicate key (will be overwritten in dict)
]
dict_comprehension = {
    key: value
    for key, value in list_of_tuples
}

# Set comprehension (generates a set of powers of 2)
set_comprehension = {2 ** i for i in range(10)}

print(set_comprehension)
