# Notes in Python exceptions (add_note, __notes__)
# https://docs.python.org/3/library/exceptions.html
# Raising (raise) / Throwing (throw) exceptions
# Re-raising exceptions
# Adding notes to exceptions (3.11.0+)
class MyError(Exception):
    ...


class AnotherError(Exception):
    ...


def raise_error():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Here is note 1')
    exception_.add_note('You made this mistake')
    raise exception_


try:
    raise_error()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = AnotherError('Raising again')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('One more note')
    raise exception_ from error
