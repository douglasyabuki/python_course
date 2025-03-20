# os.path.getsize and os.stat for file data (size in bytes)
import math
import os
from itertools import count


def format_size(size_in_bytes: int, base: int = 1000) -> str:
    """Formats a size from bytes to a human-readable format"""

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # If the size is less than or equal to 0, return 0B.
    if size_in_bytes <= 0:
        return "0B"

    # Tuple with size units
    #                        0     1      2      3      4      5
    size_units = "B", "KB", "MB", "GB", "TB", "PB"
    # Logarithm -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log will return the logarithm of size_in_bytes
    # with the base (1000 by default), this should match
    # with our index in the size_units tuple
    unit_index = int(math.log(size_in_bytes, base))
    # By how much our size should be divided
    power = base ** unit_index
    # Our final formatted size
    final_size = size_in_bytes / power
    # The size abbreviation we want
    unit_abbreviation = size_units[unit_index]
    return f'{final_size:.2f} {unit_abbreviation}'


path = os.path.join('/Users', 'username', 'Desktop', 'EXAMPLE')
counter = count()

for root, dirs, files in os.walk(path):
    the_counter = next(counter)
    print(the_counter, 'Current folder', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        full_file_path = os.path.join(root, file_)
        # size = os.path.getsize(full_file_path)
        stats = os.stat(full_file_path)
        size = stats.st_size
        print('  ', the_counter, 'FILE:', file_, format_size(size))
        # DON'T DO THIS (WILL DELETE EVERYTHING IN THE FOLDER)
        # os.unlink(full_file_path)
