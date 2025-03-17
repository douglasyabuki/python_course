"""
Introduction to try/except
try -> attempt to execute the code
except -> an error occurred while trying to execute
"""
number_str = input(
    'I will double the number you enter: '
)

try:
    number_float = float(number_str)
    print('FLOAT:', number_float)
    print(f'Twice {number_str} is {number_float * 2:.2f}')
except:
    print('That is not a number')

# if number_str.isdigit():
#     number_float = float(number_str)
#     print(f'Twice {number_str} is {number_float * 2:.2f}')
# else:
#     print('That is not a number')
