# from sys import path
# https://stackoverflow.com/questions/2386714/why-is-import-bad

# import lesson099_package.module
# from lesson099_package import module
# from lesson099_package.module import *

# # from lesson099_package.module import module_sum

# # print(*path, sep='\n')
# print(module_sum(1, 2))
# print(lesson099_package.module.module_sum(1, 2))
# print(module.module_sum(1, 2))
# print(variable)
# print(new_variable)
# from lesson099_package.module import say_hi, module_sum

# print(__name__)
# say_hi()

from lesson099_package import module

print(module.module_sum(2, 3))
module.say_hi()