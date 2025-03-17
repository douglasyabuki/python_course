# Free variables + nonlocal (locals, globals)
# print(globals())

# def outer(x):
#     a = x

#     def inner():
#         # print(locals())
#         return a
#     return inner

# inner1 = outer(10)
# inner2 = outer(20)

# print(inner1())
# print(inner2())

def concat(initial_string):
    final_value = initial_string

    def inner(to_concat=''):
        nonlocal final_value
        final_value += to_concat
        return final_value
    return inner


c = concat('a')
print(c('b'))  # ab
print(c('c'))  # abc
print(c('d'))  # abcd
final = c()    # abcd
print(final)
