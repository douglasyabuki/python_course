# Decorator functions and decorators
# Decorate = Add / Remove / Restrict / Change
# Decorator functions are functions that decorate other functions
# Decorators are used to make Python
# apply decorator functions to other functions.

def create_function(func):
    def inner(*args, **kwargs):
        print('I am going to decorate you')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print(f'Your result was {result}.')
        print('Ok, now you have been decorated')
        return result
    return inner


def reverse_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param must be a string')


reverse_string_checking_param = create_function(reverse_string)
reversed_value = reverse_string_checking_param('123')
print(reversed_value)
