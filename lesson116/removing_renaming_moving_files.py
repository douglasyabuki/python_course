import os

# Also read: https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
# with open (context manager) and useful methods of TextIOWrapper
# We use the open function to open
# a file in Python (it may or may not exist)
# Modes:
# r (read), w (write), x (create)
# a (append), b (binary)
# t (text mode), + (read and write)
# Context manager - with (open and close automatically)
# Useful methods:
# write, read (write and read)
# writelines (write multiple lines)
# seek (move the cursor)
# readline (read a single line)
# readlines (read all lines)
# We will also talk more about the os module, but:
# os.remove or unlink - deletes the file
# os.rename - renames or moves the file
# We will also talk more about the json module, but:
# json.dump = generates a json file
# json.load

file_path = 'lesson116/lesson116.txt'

# file = open(file_path, 'w')
# #
# file.close()

# with open(file_path, 'w+') as file:
#     file.write('Line 1\n')
#     file.write('Line 2\n')
#     file.writelines(
#         ('Line 3\n', 'Line 4\n')
#     )
#     file.seek(0, 0)
#     print(file.read())
#     print('Reading')
#     file.seek(0, 0)
#     print(file.readline(), end='')
#     print(file.readline().strip())
#     print(file.readline().strip())

#     print('READLINES')
#     file.seek(0, 0)
#     for line in file.readlines():
#         print(line.strip())

# print('#' * 10)

# with open(file_path, 'r') as file:
#     print(file.read())

with open(file_path, 'w', encoding='utf8') as file:
    file.write('Attention\n')
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.writelines(
        ('Line 3\n', 'Line 4\n')
    )

# os.remove(file_path)  # or unlink
# os.rename(file_path, 'lesson116-2.txt')
