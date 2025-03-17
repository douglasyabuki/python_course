# Exercises with functions

# Create a function that multiplies all the 
# unnamed arguments received.
# Return the total to a variable and display its value.
def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total


multiplication = multiply(10, 2, 3, 4, 5)
print(multiplication)


# Create a function that determines whether a number is even or odd.
# Return whether the number is even or odd.
def even_or_odd(number):
    multiple_of_two = number % 2 == 0

    if multiple_of_two:
        return f'{number} is even'
    return f'{number} is odd'


another_even_or_odd = even_or_odd  # Assigning function to another variable
two_is_even = another_even_or_odd(2)
print(two_is_even)
print(even_or_odd(3))
print(even_or_odd(15))
print(even_or_odd(16))

print(even_or_odd is another_even_or_odd)  # Checking if both names point to the same function
