# os.walk to navigate directories recursively
# os.walk is a function that allows you to traverse a directory structure
# recursively. It yields a sequence of tuples, where each tuple contains
# three elements: the current directory (root), a list of subdirectories (dirs),
# and a list of files in the current directory (files).
import os
from itertools import count

path = os.path.join('/Users', 'username', 'Desktop', 'EXAMPLE')
counter = count()

for root, dirs, files in os.walk(path):
    the_counter = next(counter)
    print(the_counter, 'Current folder', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        full_file_path = os.path.join(root, file_)
        print('  ', the_counter, 'FILE:', full_file_path)
        # DON'T DO THIS (WILL DELETE EVERYTHING IN THE FOLDER)
        # os.unlink(full_file_path)
