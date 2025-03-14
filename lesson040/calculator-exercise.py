""" Calculator with while loop """
while True:
    number_1 = input('Enter a number: ')
    number_2 = input('Enter another number: ')
    operator = input('Enter the operator (+-/*): ')

    valid_numbers = None

    try:
        num_1_float = float(number_1)
        num_2_float = float(number_2)
        valid_numbers = True
    except:
        valid_numbers = None

    if valid_numbers is None:
        print('One or both of the entered numbers are invalid.')
        continue

    allowed_operators = '+-/*'

    if operator not in allowed_operators:
        print('Invalid operator.')
        continue

    if len(operator) > 1:
        print('Enter only one operator.')
        continue

    ### Perform the calculation
    if operator == '+':
        result = num_1_float + num_2_float
    elif operator == '-':
        result = num_1_float - num_2_float
    elif operator == '*':
        result = num_1_float * num_2_float
    elif operator == '/':
        if num_2_float == 0:
            print('Division by zero is not allowed.')
            continue
        result = num_1_float / num_2_float

    print(f'The result is: {result}')

    ### Exit condition
    exit_program = input('Do you want to exit? [y]es: ').lower().startswith('y')

    if exit_program:
        break
