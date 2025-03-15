"""
Calculation of the first CPF digit
CPF: 746.824.890-70
Collect the sum of the first 9 digits of the CPF,
multiplying each value by a decreasing count starting from 10.

Example:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Sum all the results: 
70+36+48+56+12+20+32+27+0 = 301
Multiply the previous result by 10:
301 * 10 = 3010
Get the remainder of the previous calculation divided by 11:
3010 % 11 = 7
If the result is greater than 9:
    the final digit is 0
Otherwise:
    the final digit is the calculated value.

The first CPF digit is 7.
"""
# cpf = '36440847007'  # This CPF generates the first digit as 10 (0)
cpf = '74682489070'
first_nine_digits = cpf[:9]
reverse_counter_1 = 10

first_digit_result = 0
for digit in first_nine_digits:
    first_digit_result += int(digit) * reverse_counter_1
    reverse_counter_1 -= 1

first_digit = (first_digit_result * 10) % 11
first_digit = first_digit if first_digit <= 9 else 0
print(first_digit)
