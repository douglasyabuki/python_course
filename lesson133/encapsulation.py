# Encapsulation (access modifiers: public, protected, private)
# Python DOES NOT HAVE true access modifiers
# But we can follow these conventions:
#   (no underscore) = public
#       can be used anywhere
# _ (one underscore) = protected
#       SHOULD NOT be used outside the class
#       or its subclasses.
# __ (two underscores) = private
#       "name mangling" in Python
#       _ClassName__attr_or_method_name
#       SHOULD ONLY be used inside the class
#       where it was declared.
from functools import partial


class Foo:
    def __init__(self):
        self.public = 'this is public'
        self._protected = 'this is protected'
        self.__private_example = 'this is private'

    def public_method(self):
        # self._protected_method()
        # print(self._protected)
        print(self.__private_example)
        self.__private_method()
        return 'public_method'

    def _protected_method(self):
        print('_protected_method')
        return '_protected_method'

    def __private_method(self):
        print('__private_method')
        return '__private_method'


f = Foo()
# print(f.public)
print(f.public_method())
