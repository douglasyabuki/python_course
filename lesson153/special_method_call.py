# Special method __call__
# callable is something that can be executed with parentheses
# In normal classes, __call__ makes the instance of a
# class "callable".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, name):
        print(name, 'is calling', self.phone)
        return 2134


call1 = CallMe('23945876545')
result = call1('Luiz Otávio')
print(result)
