"""
Floating-point imprecision
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/3/tutorial/floatingpoint.html
"""
import decimal

number_1 = decimal.Decimal('0.1')
number_2 = decimal.Decimal('0.7')
number_3 = number_1 + number_2
print(number_3)  # Outputs precise decimal value
print(f'{number_3:.2f}')  # Formats output to 2 decimal places
print(round(number_3, 2))  # Rounds the number to 2 decimal places
