# @staticmethod (static methods) are "useless" in Python =)
# Static methods are methods that exist inside the
# class, but they don't have access to self or cls.
# In summary, they are just functions that live inside your
# class.
class MyClass:
    @staticmethod
    def function_inside_class(*args, **kwargs):
        print('Hi', args, kwargs)


def function(*args, **kwargs):
    print('Hi', args, kwargs)


c1 = MyClass()
c1.function_inside_class(1, 2, 3)
function(1, 2, 3)
MyClass.function_inside_class(named=1)
function(named=1)
