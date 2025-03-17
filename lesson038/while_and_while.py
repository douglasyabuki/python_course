"""
Repetitions
while (while loop)
Executes an action while a condition is true
Infinite loop -> When a code has no end
"""
num_rows = 5
num_columns = 5

row = 1
while row <= num_rows:
    column = 1
    while column <= num_columns:
        print(f'{row=} {column=}')
        column += 1
    row += 1

print('Finished')
