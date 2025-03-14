first_value = input('Enter a value: ')
second_value = input('Enter another value: ')

if first_value >= second_value:
    print(
        f'{first_value=} is greater than or equal to '
        f'{second_value=}'
    )
else:
    print(
        f'{second_value=} is greater '
        f'than {first_value=}'
    )
