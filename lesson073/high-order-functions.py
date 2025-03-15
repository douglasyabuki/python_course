"""
Higher-Order Functions
First-Class Functions
"""


def greeting(msg, name):
    return f'{msg}, {name}!'  # Returns a formatted greeting message


def execute(function, *args):
    return function(*args)  # Calls the passed function with provided arguments


print(
    execute(greeting, 'Good morning', 'Luiz')
)
print(
    execute(greeting, 'Good night', 'Maria')
)
