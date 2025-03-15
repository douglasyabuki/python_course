"""
enumerate - enumerates iterables (indices)
"""
# [(0, 'Name'), (1, 'John'), (2, 'Doe'), (3, 'Tho')]
names_list = ['Name', 'John', 'Doe']
names_list.append('Tho')

for index, name in enumerate(names_list):
    print(index, name, names_list[index])

# Alternative way to unpack enumerate:
# for item in enumerate(names_list):
#     index, name = item
#     print(index, name)

# Iterating over the tuple returned by enumerate:
# for enumerated_tuple in enumerate(names_list):
#     print('FOR loop inside the tuple:')
#     for value in enumerated_tuple:
#         print(f'\t{value}')
