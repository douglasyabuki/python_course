# Decorator classes
class Multiply:
    def __init__(self, multiplier):
        self._multiplier = multiplier

    def __call__(self, func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * self._multiplier
        return inner


@Multiply(2)
def add(x, y):
    return x + y


two_plus_four = add(2, 4)
print(two_plus_four)
