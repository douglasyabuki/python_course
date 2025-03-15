"""
List of lists and their indices
"""
rooms = [
    # 0        1
    ['Name', 'Lastname'],  # 0
    # 0
    ['John'],  # 1
    # 0       1       2
    ['Doe', 'Tho', 'Moe'],  # 2
]

# print(rooms[1][0])  # John
# print(rooms[0][1])  # Lastname
# print(rooms[2][2])  # Moe
# print(rooms[2][3][3])  # IndexError (out of range)

for room in rooms:
    print(f'The room is {room}')
    for student in room:
        print(student)
