# Context Manager with classes - Creating and Using context managers
# You can implement your own protocols
# just by implementing the dunder methods that
# Python will use.
# This is called Duck typing. A concept
# related to dynamic typing where Python is not
# interested in the type, but if certain methods exist
# in your object so it works properly.
# Duck Typing:
# When I see a bird that walks like a duck, swims like
# a duck, and quacks like a duck, I call that bird a duck.
# To create a context manager, the methods __enter__ and __exit__
# must be implemented.
# The __exit__ method will receive the exception class, the exception itself, and the
# traceback. If it returns True, exceptions inside the with block will
# be suppressed.
#
# Example:
# with open('lesson149.txt', 'w') as file:
#     ...

class MyOpen:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('OPENING FILE')
        self._file = open(self.file_path, self.mode, encoding='utf8')
        return self._file

    def __exit__(self, class_exception, exception_, traceback_):
        print('CLOSING FILE')
        self._file.close()

        # raise class_exception(*exception_.args).with_traceback(traceback_)

        # print(class_exception)
        # print(exception_)
        # print(traceback_)
        # exception_.add_note('My note')

        # return True  # I handled the exception


with MyOpen('lesson149.txt', 'w') as file:
    file.write('Line 1\n')
    file.write('Line 2\n', 123)
    file.write('Line 3\n')
    print('WITH', file)
