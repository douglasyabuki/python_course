# Exercise - Delaying function execution
def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def create_function(func, x):
    def inner(y):
        return func(x, y)
    return inner


add_with_five = create_function(add, 5)
multiply_by_ten = create_function(multiply, 10)

print(add_with_five(10))       # 5 + 10 = 15
print(multiply_by_ten(10))     # 10 * 10 = 100
