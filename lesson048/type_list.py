"""
Lists in Python
Type list - Mutable
Supports multiple values of any type
Reusable knowledge - indices and slicing
Useful methods:
    append - Adds an item to the end
    insert - Adds an item at the chosen index
    pop - Removes an item from the end or a chosen index
    del - Deletes an index
    clear - Clears the list
    extend - Extends the list
    + - Concatenates lists
Create Read Update Delete
Create, read, update, delete = list[i] (CRUD)
"""
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b  # Concatenates lists (creates a new list)
list_a.extend(list_b)  # Extends list_a with list_b

print(list_a)  # Output: [1, 2, 3, 4, 5, 6]
