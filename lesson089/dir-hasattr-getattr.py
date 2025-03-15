# dir, hasattr, and getattr in Python

string = 'Name'
method = 'strip'

if hasattr(string, method):  # Checks if the method exists in the object
    print('Method exists')
    print(getattr(string, method)())  # Calls the method dynamically
else:
    print('The method does not exist:', method)
