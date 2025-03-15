"""
Function Scope in Python
Scope refers to the region where a piece of code can be accessed.
There are global and local scopes.
The global scope is where all code is accessible.
The local scope is where only names from the same location
can be accessed.
"""

x = 1  # Global variable


def scope():
    global x  # Accessing and modifying the global variable
    x = 10  # Modifies global x

    def another_function():
        global x  # Accessing and modifying the global variable
        x = 11  # Changes global x again
        y = 2  # Local variable (only exists inside this function)
        print(x, y)  # Prints 11 (x from global scope) and 2 (local y)

    another_function()
    print(x)  # Prints 11, since x was changed in another_function()


print(x)  # Prints 1 (original global x)
scope()  # Calls scope(), which modifies x
print(x)  # Prints 11 (x modified by another_function)
