def execute(function, *args):
    return function(*args)


# def sum_values(x, y):
#     return x + y

# def create_multiplier(multiplier):
#     def multiply(number):
#         return number * multiplier
#     return multiply

# double = create_multiplier(2)

double = execute(
    lambda m: lambda n: n * m,  # Creates a lambda function that returns another function
    2  # Multiplier
)
print(double(2))  # Calls the returned function (2 * 2 = 4)

print(
    execute(
        lambda x, y: x + y,  # Adds two numbers
        2, 3
    ),
)

print(
    execute(
        lambda *args: sum(args),  # Sums all arguments
        1, 2, 3, 4, 5, 6, 7
    )
)
