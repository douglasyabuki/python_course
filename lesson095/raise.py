# raise - Raising Exceptions (Errors)
# https://docs.python.org/3/library/exceptions.html#built-in-exceptions

def no_zero_allowed(d):
    """Raises an error if the divisor is zero."""
    if d == 0:
        raise ZeroDivisionError('You are trying to divide by zero')
    return True


def must_be_int_or_float(n):
    """Raises an error if the input is not an int or float."""
    n_type = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" must be int or float. '
            f'"{n_type.__name__}" was provided.'
        )
    return True


def divide(n, d):
    """Validates and performs division."""
    must_be_int_or_float(n)
    must_be_int_or_float(d)
    no_zero_allowed(d)
    return n / d


print(divide(8, '0'))  # Raises a TypeError
