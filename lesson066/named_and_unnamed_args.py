"""
Named and unnamed arguments in Python functions
A named argument has a name with an equals sign (=)
An unnamed argument receives only the value
"""


def sum_values(x, y, z):
    # Function definition
    print(f'{x=} y={y} {z=}', '|', 'x + y + z =', x + y + z)


sum_values(1, 2, 3)  # Positional arguments
sum_values(1, y=2, z=5)  # Named arguments

print(1, 2, 3, sep='-')  # Named argument for 'sep'
