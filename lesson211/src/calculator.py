def add(x, y):
    """Adds x and y

    >>> add(10, 20)
    30

    >>> add(-10, 20)
    10

    >>> add('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x must be int or float
    """
    assert isinstance(x, (int, float)), 'x must be int or float'
    assert isinstance(y, (int, float)), 'y must be int or float'
    return x + y


def subtract(x, y):
    """Subtracts y from x

    >>> subtract(10, 5)
    5

    >>> subtract('10', 5)
    Traceback (most recent call last):
    ...
    AssertionError: x must be int or float
    """
    assert isinstance(x, (int, float)), 'x must be int or float'
    assert isinstance(y, (int, float)), 'y must be int or float'
    return x - y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
