# isinstance - To check if an object is of a specific type

data_list = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'name': 'John'},
]

for item in data_list:
    if isinstance(item, set):
        print('SET')
        item.add(5)  # Adds an element to the set
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())  # Converts string to uppercase

    elif isinstance(item, (int, float)):  # Checks if the item is int or float
        print('NUM')
        print(item, item * 2)  # Prints the number and its double

    else:
        print('OTHER')
        print(item)
