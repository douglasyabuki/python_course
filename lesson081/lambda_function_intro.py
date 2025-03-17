# Introduction to the lambda function (one-line anonymous function)
# A lambda function is like any other function in Python.
# However, they are anonymous functions that contain only one line.
# Everything must be contained within a single expression.

# Example of a list of dictionaries
people = [
    {'name': 'John', 'last_name': 'Doe'},
    {'name': 'Johnny', 'last_name': 'Tho'},
    {'name': 'Johm', 'last_name': 'Toe'},
    {'name': 'Jonathan', 'last_name': 'Joestar'},
    {'name': 'Jorge', 'last_name': 'Jungle'},
]


def display(lst):
    for item in lst:
        print(item)
    print()


# Sorting by 'name' using lambda as a sorting key
sorted_by_name = sorted(people, key=lambda item: item['name'])
# Sorting by 'last_name' using lambda as a sorting key
sorted_by_last_name = sorted(people, key=lambda item: item['last_name'])

# Display sorted lists
display(sorted_by_name)
display(sorted_by_last_name)
