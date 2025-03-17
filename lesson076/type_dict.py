# Useful dictionary methods in Python
# len - number of keys
# keys - iterable with the keys
# values - iterable with the values
# items - iterable with keys and values
# setdefault - adds a value if the key does not exist
# copy - returns a shallow copy
# get - retrieves a value for a key
# pop - deletes an item with the specified key (like del)
# popitem - deletes the last added item
# update - updates a dictionary with another dictionary

p1 = {
    'name': 'John',
    'last_name': 'Doe',
}

# print(p1['name'])  # Accessing a key (will raise an error if key does not exist)
# print(p1.get('name', 'Does not exist'))  # Safer way to access a key with a default value

# Removing a key and getting its value
# name = p1.pop('name')
# print(name)
# print(p1)

# Removing the last added key-value pair
# last_key = p1.popitem()
# print(last_key)
# print(p1)

# Updating the dictionary with new values
# p1.update({
#     'name': 'new value',
#     'age': 30,
# })

# Alternative ways to use update()
# p1.update(name='new value', age=30)
# tuple_data = (('name', 'new value'), ('age', 30))

list_data = [['name', 'new value'], ['age', 30]]
p1.update(list_data)  # Using a list of lists to update dictionary
print(p1)
