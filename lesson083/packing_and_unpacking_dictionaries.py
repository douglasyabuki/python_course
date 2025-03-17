# Packing and Unpacking Dictionaries
a, b = 1, 2
a, b = b, a  # Swaps the values of a and b
# print(a, b)

# Unpacking dictionary items
# (a1, a2), (b1, b2) = person.items()
# print(a1, a2)
# print(b1, b2)

# Iterating through dictionary keys and values
# for key, value in person.items():
#     print(key, value)

person = {
    'name': 'John',
    'last_name': 'Doe',
}

person_data = {
    'age': 16,
    'height': 1.6,
}

# Merging dictionaries using unpacking
complete_person = {**person, **person_data}
# print(complete_person)

# args and kwargs
# args (already covered)
# kwargs - keyword arguments (named arguments)

def show_named_arguments(*args, **kwargs):
    print('NON-NAMED:', args)

    for key, value in kwargs.items():
        print(key, value)


# show_named_arguments(name='Joana', some_arg=123)
# show_named_arguments(**complete_person)

settings = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
show_named_arguments(**settings)  # Passing dictionary as named arguments
