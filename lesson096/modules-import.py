# Python Standard Modules (import, from, as, and *)
# https://docs.python.org/3/py-modindex.html

# Full Import - `import module_name`
# Advantages: You have the module's namespace.
# Disadvantages: Requires long names.
# import sys

# platform = 'MY CUSTOM VALUE'
# print(sys.platform)  # Uses sys.platform
# print(platform)  # Uses the local variable 'platform'

# Import Specific Parts - `from module_name import object1, object2`
# Advantages: Shorter names.
# Disadvantages: No module namespace.
# from sys import exit, platform

# print(platform)  # Directly accessible

# Alias 1 - `import module_name as alias`
# import sys as s

# sys = 'some value'  # This does NOT affect the imported module
# print(s.platform)  # Uses the alias `s`
# print(sys)  # Uses the local variable 'sys'

# Alias 2 - `from module_name import object as alias`
# from sys import exit as ex
# from sys import platform as pf

# print(pf)  # Uses the alias `pf`

# Advantages: Allows reserving names for your own code.
# Disadvantages: May break Python's standard naming conventions.

# Bad Practice - `from module_name import *`
# Advantages: Imports everything from a module.
# Disadvantages: Can override existing names and cause conflicts.
# from sys import exit, platform

# print(platform)
# exit()
