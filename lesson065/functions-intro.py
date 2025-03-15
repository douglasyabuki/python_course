"""
Introduction to functions (def) in Python
Functions are blocks of code used to 
replicate a specific action throughout your code.
They can receive values as parameters (arguments) 
and return a specific value.
By default, Python functions return None (nothing).
"""


# def Print(a, b, c):
#     print('Multiple1')
#     print('Multiple2')
#     print('Multiple3')
#     print('Multiple4')

# def print_values(a, b, c):
#     print(a, b, c)


# print_values(1, 2, 3)
# print_values(4, 5, 6)

def greeting(name='No name'):
    print(f'Hello, {name}!')


greeting('Name Lastname')
greeting('John')
greeting('Doe')
greeting()
