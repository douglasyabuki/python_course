# @property + @setter - getter and setter in the Pythonic way
# - as a getter
# - to avoid breaking client code
# - to enable setter
# - to execute actions when accessing an attribute
# Attributes starting with one or two underscores
# should not be used outside the class.
# 🐍🤓🤯🤯🤯🤯

class Pen:
    def __init__(self, color):
        # private protected
        self.color = color
        self._cap_color = None

    @property
    def color(self):
        print('INSIDE GETTER')
        return self._color

    @color.setter
    def color(self, value):
        print('INSIDE SETTER')
        self._color = value

    @property
    def cap_color(self):
        return self._cap_color

    @cap_color.setter
    def cap_color(self, value):
        self._cap_color = value


pen = Pen('Blue')
pen.color = 'Pink'
pen.cap_color = 'Blue'
print(pen.color)
print(pen.cap_color)
