# Modularization - Understanding Your Own Python Modules
# The first module executed is called __main__
# You can import an entire module or just part of it
# Python recognizes the folder where __main__ is located
# and its subfolders.
# By default, it does NOT recognize folders and modules above __main__.
# Python is aware of all modules and packages found in sys.path.

import lesson097.module097 as module097  # Importing the entire module
from lesson097.module097 import sum, module_variable  # Importing specific functions/variables

# print('This module is called', __name__)
print(module097.module_variable)  # Accessing a variable from the imported module
print(module_variable)  # Accessing the same variable directly
print(sum(2, 3))  # Calling the function directly
print(module097.sum(2, 3))  # Calling the function using the module's namespace
