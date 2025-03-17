# Unpacking in method and function calls
string = 'ABCD'
list_data = ['John', 'Doe', 1, 2, 3, 'Tho']
tuple_data = 'Python', 'is', 'cool'
rooms = [
    # 0        1
    ['John', 'Doe'],  # 0
    # 0
    ['Moe'],  # 1
    # 0       1       2
    ['Toe', 'Foe', 'Tho'],  # 2
]

# p, b, *_, ap, u = list_data
# print(p, u, ap)

# print('John', 'Doe', 1, 2, 3, 'Tho')
# print(*list_data)  # Unpacks the list into separate arguments
# print(*string)  # Unpacks the string into separate characters
# print(*tuple_data)  # Unpacks the tuple into separate arguments

print(*rooms, sep='\n')  # Prints each sublist on a new line
