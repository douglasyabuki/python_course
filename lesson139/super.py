# super() and member overriding - Python Object-Oriented Programming
# Parent Class (Person)
#   -> super class, base class, parent class
# Child Classes (Client)
#   -> sub class, child class, derived class

# class MyString(str):
#     def upper(self):
#         print('CALLED UPPER')
#         result = super(MyString, self).upper()
#         print('AFTER UPPER')
#         return result

# string = MyString('Luiz')
# print(string.upper())

class A(object):
    attribute_a = 'value a'

    def __init__(self, attribute):
        self.attribute = attribute

    def method(self):
        print('A')


class B(A):
    attribute_b = 'value b'

    def __init__(self, attribute, something_else):
        super().__init__(attribute)
        self.something_else = something_else

    def method(self):
        print('B')


class C(B):
    attribute_c = 'value c'

    def __init__(self, *args, **kwargs):
        # print('HEY, I bypassed the system.')
        super().__init__(*args, **kwargs)

    def method(self):
        # super().method()  # Calls B
        # super(B, self).method()  # Calls A
        # super(A, self).method()  # Calls object (no-op)
        A.method(self)
        B.method(self)
        print('C')


# print(C.mro())  # Method Resolution Order
# print(B.mro())
# print(A.mro())
c = C('Attribute', 'Anything')
# print(c.attribute)
# print(c.something_else)
c.method()
# print(c.attribute_a)
# print(c.attribute_b)
# print(c.attribute_c)
# c.method()
