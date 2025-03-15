"""
Calculation of the second CPF digit
CPF: 746.824.890-70
Collect the sum of the first 9 digits of the CPF,
PLUS THE FIRST DIGIT,
multiplying each value by a
decreasing counter starting from 11.

Example:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0  7 <-- FIRST DIGIT
   77 40 54 64 14 24 40 36  0 14

Sum all results:
77+40+54+64+14+24+40+36+0+14 = 363
Multiply the previous result by 10
363 * 10 = 3630
Get the remainder of the previous calculation divided by 11
3630 % 11 = 0
If the result is greater than 9:
    the final digit is 0
Otherwise:
    the final digit is the calculated value.

The second CPF digit is 0.
"""
import re
import sys

# Get user input
input_cpf = input('CPF [746.824.890-70]: ')

# Remove any non-numeric characters
cpf_user = re.sub(r'[^0-9]', '', input_cpf)

# Check if the CPF is a sequence of the same digit
if cpf_user == cpf_user[0] * len(cpf_user):
    print('You entered a sequential CPF, which is invalid.')
    sys.exit()

# Get the first 9 digits
first_nine_digits = cpf_user[:9]
reverse_counter_1 = 10

# Calculate the first verification digit
first_digit_result = 0
for digit in first_nine_digits:
    first_digit_result += int(digit) * reverse_counter_1
    reverse_counter_1 -= 1
first_digit = (first_digit_result * 10) % 11
first_digit = first_digit if first_digit <= 9 else 0

# Get the first 10 digits (including the first verification digit)
first_ten_digits = first_nine_digits + str(first_digit)
reverse_counter_2 = 11

# Calculate the second verification digit
second_digit_result = 0
for digit in first_ten_digits:
    second_digit_result += int(digit) * reverse_counter_2
    reverse_counter_2 -= 1
second_digit = (second_digit_result * 10) % 11
second_digit = second_digit if second_digit <= 9 else 0

# Generate the full CPF based on the calculation
generated_cpf = f'{first_nine_digits}{first_digit}{second_digit}'

# Validate the CPF
if cpf_user == generated_cpf:
    print(f'{cpf_user} is valid')
else:
    print('Invalid CPF')
