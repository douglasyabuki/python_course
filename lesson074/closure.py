"""
Closure are functions that return other functions
"""


def create_greeting(greeting):
    def greet(name):
        return f'{greeting}, {name}!'
    return greet  # Returns the inner function


say_good_morning = create_greeting('Good morning')
say_good_night = create_greeting('Good night')

for name in ['John', 'Doe', 'Tho']:
    print(say_good_morning(name))
    print(say_good_night(name))
