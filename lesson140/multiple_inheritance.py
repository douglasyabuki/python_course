# Multiple Inheritance - Python Object-Oriented Programming
# It means that in Python, a class can extend
# multiple other classes.
# Simple inheritance:
# Animal -> Mammal -> Human -> Person -> Client
# Multiple inheritance and mixins
# Log -> FileLog
# Animal -> Mammal -> Human -> Person -> Client
# Client(Person, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# method -> who_am_i
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 uses C3 superclass linearization
# to generate the MRO (method resolution order).
# You don’t need to study this deeply (it’s complex)
# https://en.wikipedia.org/wiki/C3_linearization
#
# To know the method call order
# Use the class method Class.mro()
# Or the __mro__ attribute (Dunder - Double Underscore)
class A:
    def who_am_i(self):
        print('A')


class B(A):
    pass
    # def who_am_i(self):
    #     print('B')


class C(A):
    def who_am_i(self):
        print('C')


class D(B, C):
    def who_am_i(self):
        print('D')


d = D()
d.who_am_i()
print(D.mro())
