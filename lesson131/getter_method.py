# @property - a getter in the Pythonic way
# getter - a method to get an attribute
# color -> get_color()
# Pythonic way - the Python way of doing things
# @property is a property of the object, it’s
# a method that behaves like an
# attribute 🤯 🤯 🤯
# It is generally used in the following situations:
# - as a getter
# - to avoid breaking client code
# - to enable setter later
# - to execute actions when accessing an attribute
# Client code - is the code that uses your code

class Pen:
    def __init__(self, color):
        self.ink_color = color

    @property
    def color(self):
        print('PROPERTY')
        return self.ink_color

    @property
    def cap_color(self):
        return 123456


pen = Pen('Blue')
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.cap_color)

#####################################

# class Pen:
#     def __init__(self, color):
#         self.ink_color = color

#     def get_color(self):
#         print('GET COLOR')
#         return self.ink_color

# ###########################


# pen = Pen('Blue')
# print(pen.get_color())
# print(pen.get_color())
# print(pen.get_color())
# print(pen.get_color())
# print(pen.get_color())
