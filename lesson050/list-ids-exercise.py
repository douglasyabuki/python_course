"""
Exercise
Display the indices of the list
0 Name
1 John
2 Doe
3 Tho
"""
names_list = ['Name', 'John', 'Doe']
names_list.append('Tho')  # Adds 'Tho' to the list

indices = range(len(names_list))  # Creates a range based on the list length

for index in indices:
    print(index, names_list[index], type(names_list[index]))
