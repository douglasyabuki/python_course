"""
Lists in Python
Type list - Mutable
Supports multiple values of any type
Reusable knowledge - indices and slicing
Useful methods: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 characters (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1       2             3    4
#       -5   -4      -3            -2   -1
my_list = [123, True, 'Name Lastname', 1.2, []]
my_list[-3] = 'John'  # Modifies the third element
print(my_list)
print(my_list[2], type(my_list[2]))  # Prints 'John' and its type
