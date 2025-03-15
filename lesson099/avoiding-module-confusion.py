# from sys import path
# https://stackoverflow.com/questions/2386714/why-is-import-bad

# import lesson99_package.module
# from lesson99_package import module
# from lesson99_package.module import *

# # from lesson99_package.module import module_sum

# # print(*path, sep='\n')
# print(module_sum(1, 2))
# print(lesson99_package.module.module_sum(1, 2))
# print(module.module_sum(1, 2))
# print(variable)
# print(new_variable)
# from lesson99_package.module import say_hi, module_sum

# print(__name__)
# say_hi()

from lesson99_package import module

print(module.module_sum(2, 3))
module.say_hi()