"""
Function Scope in Python
Scope refers to the area where a piece of code can be accessed.
There are global and local scopes.
The global scope is where all code is accessible.
The local scope is where only names from the same local
scope can be accessed.
We do not have access to names from inner scopes in outer scopes.
The `global` keyword makes a variable from the outer scope 
the same in the inner scope.
"""

x = 1  # Global variable


def scope():
    # global x  # Not using global, so x here is local
    x = 10  # Local variable inside `scope()`

    def another_function():
        # global x  # Not using global, so x here is local to `another_function()`
        x = 11  # Local variable inside `another_function()`
        y = 2  # Another local variable
        print(x, y)  # Prints local x (11) and y (2)

    another_function()
    print(x)  # Prints local x (10), not affected by another_function()


print(x)  # Prints global x (1)
scope()  # Calls scope(), which defines a local x (10) and runs another_function()
print(x)  # Prints global x (1), since `scope()` does not modify it
