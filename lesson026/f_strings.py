"""
Basic string formatting
s - string
d - int
f - float
.<number of digits>f
x or X - Hexadecimal
(Character)(><^)(amount)
> - Left align
< - Right align
^ - Center align
= - Forces the number to appear before the zeros
Sign - + or -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variable = 'ABC'
print(f'{variable}')
print(f'{variable: >10}')   # Right align with a width of 10
print(f'{variable: <10}.')  # Left align with a width of 10
print(f'{variable: ^10}.')  # Center align with a width of 10
print(f'{1000.4873648123746:0=+10,.1f}')  # Format float with + sign, padding, and thousand separator
print(f'The hexadecimal of 1500 is {1500:08X}')  # Format as uppercase hexadecimal with zero padding
print(f'{variable!r}')  # Print raw string representation
