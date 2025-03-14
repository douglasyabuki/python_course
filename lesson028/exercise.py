"""
Exercise
Ask the user to enter their name
Ask the user to enter their age
If both name and age are provided:
    Display:
        Your name is {name}
        Your name reversed is {reversed name}
        Your name contains (or does not contain) spaces
        Your name has {n} letters
        The first letter of your name is {letter}
        The last letter of your name is {letter}
If either name or age is left empty:
    Display "Sorry, you left empty fields."
"""
name = input('Enter your name: ')
age = input('Enter your age: ')

if name and age:
    print(f'Your name is {name}')
    print(f'Your name reversed is {name[::-1]}')

    if ' ' in name:
        print('Your name contains spaces')
    else:
        print('Your name does NOT contain spaces')

    print(f'Your name has {len(name)} letters')
    print(f'The first letter of your name is {name[0]}')
    print(f'The last letter of your name is {name[-1]}')
else:
    print("Sorry, you left empty fields.")
