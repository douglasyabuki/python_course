# try, except, else, and finally
# https://docs.python.org/3/library/exceptions.html#built-in-exceptions

try:
    print('OPEN FILE')
    8 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(e.__class__.__name__)  # Prints the exception type
    print(e)  # Prints the error message
    print('DIVIDED BY ZERO')
except IndexError:
    print('IndexError occurred')
except (NameError, ImportError):
    print('NameError or ImportError occurred')
else:
    print('No errors occurred')
finally:
    print('CLOSE FILE')
