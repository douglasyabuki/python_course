# Creating a list using nested loops
nested_list = []
for x in range(3):
    for y in range(3):
        nested_list.append((x, y))

# Equivalent list comprehension for nested loops
nested_list = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

# Nested list comprehension with letters
nested_list = [
    [(x, letter) for letter in 'John']
    for x in range(3)
]

print(nested_list)
