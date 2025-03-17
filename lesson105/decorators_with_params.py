# Decorators with parameters
def decorator_factory(a=None, b=None, c=None):
    def function_factory(func):
        print('Decorator 1')

        def nested(*args, **kwargs):
            print('Decorator parameters: ', a, b, c)
            print('Nested function')
            res = func(*args, **kwargs)
            return res
        return nested
    return function_factory


@decorator_factory(1, 2, 3)
def add(x, y):
    return x + y


decorator = decorator_factory()
multiply = decorator(lambda x, y: x * y)

ten_plus_five = add(10, 5)
ten_times_five = multiply(10, 5)
print(ten_plus_five)
print(ten_times_five)
