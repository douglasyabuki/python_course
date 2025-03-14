"""
Iterating through strings with while
"""
#       012345678910
# name = 'Name Lastname'  # Iterable
#      1110987654321

name = 'John Doe'  # Iterable

index = 0
new_name = ''
while index < len(name):
    letter = name[index]
    new_name += f'*{letter}'
    index += 1

new_name += '*'
print(new_name)
