"""
Default values for parameters
When defining a function, parameters can
have default values. If no value is provided
for a parameter, the default value will be used.
Refactoring: editing your code to improve it.
"""


def sum_values(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


sum_values(1, 2)
sum_values(3, 5)
sum_values(100, 200)
sum_values(7, 9, 0)
sum_values(y=9, z=0, x=7)
