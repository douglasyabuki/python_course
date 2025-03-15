# (Part 1) try and except for exception handling

try:
    a = 18
    b = 0
    # print(b[0])  # Uncomment to raise an IndexError
    print('Line 1'[1000])  # Raises an IndexError
    c = a / b  # Raises a ZeroDivisionError
    print('Line 2')

except ZeroDivisionError:
    print('Tried to divide by zero.')
except NameError:
    print('Variable "b" is not defined.')
except (TypeError, IndexError):
    print('Caught a TypeError or IndexError.')
except Exception:
    print('UNKNOWN ERROR.')

print('CONTINUE')

# (Part 2) try and except with exception details

try:
    a = 18
    b = 0
    # print(b[0])  # Uncomment to raise an IndexError
    # print('Line 1'[1000])  # Uncomment to raise an IndexError
    c = a / b  # Raises a ZeroDivisionError
    print('Line 2')

except ZeroDivisionError as e:
    print(e.__class__.__name__)  # Prints the exception type
    print(e)  # Prints the error message
except NameError:
    print('Variable "b" is not defined.')
except (TypeError, IndexError) as error:
    print('Caught a TypeError or IndexError.')
    print('Message:', error)
    print('Error Name:', error.__class__.__name__)
except Exception:
    print('UNKNOWN ERROR.')

print('CONTINUE')
