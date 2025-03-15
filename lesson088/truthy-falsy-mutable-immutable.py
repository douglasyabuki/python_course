# Truthy and Falsy Values, Mutable and Immutable Types

# Mutable types: lists, dictionaries, sets
mutable_list = []
mutable_dict = {}
mutable_set = set()

# Immutable types: tuples, strings, numbers, None, False, range(0, 10)
immutable_tuple = ()
immutable_string = ''
immutable_integer = 0
immutable_float = 0.0
none_value = None
false_value = False
empty_range = range(0)


def check_falsy(value):
    return 'falsy' if not value else 'truthy'


print(f'TEST', check_falsy('TEST'))
print(f'{mutable_list=}', check_falsy(mutable_list))
print(f'{mutable_dict=}', check_falsy(mutable_dict))
print(f'{mutable_set=}', check_falsy(mutable_set))
print(f'{immutable_tuple=}', check_falsy(immutable_tuple))
print(f'{immutable_string=}', check_falsy(immutable_string))
print(f'{immutable_integer=}', check_falsy(immutable_integer))
print(f'{immutable_float=}', check_falsy(immutable_float))
print(f'{none_value=}', check_falsy(none_value))
print(f'{false_value=}', check_falsy(false_value))
print(f'{empty_range=}', check_falsy(empty_range))
