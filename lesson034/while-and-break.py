"""
Repetitions
while (while loop)
Executes an action while a condition is true
Infinite loop -> When a code has no end
"""
condition = True

while condition:
    name = input('What is your name: ')
    print(f'Your name is {name}')

    if name == 'exit':
        break

print('Finished')
