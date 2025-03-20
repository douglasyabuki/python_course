# os + shutil - Deleting, copying, moving, and renaming folders with Python
# Let's copy files from one folder to another.
# Copy file -> shutil.copy
# Recursively copy tree -> shutil.copytree
# Recursively delete tree -> shutil.rmtree
# Delete files -> os.unlink
# Rename/Move -> shutil.move or os.rename
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
ORIGINAL_FOLDER = os.path.join(DESKTOP, 'EXAMPLE')
NEW_FOLDER = os.path.join(DESKTOP, 'NEW_FOLDER')

shutil.rmtree(NEW_FOLDER, ignore_errors=True)
shutil.copytree(ORIGINAL_FOLDER, NEW_FOLDER)
# shutil.move(NEW_FOLDER, NEW_FOLDER + '_EITA')
shutil.rmtree(NEW_FOLDER, ignore_errors=True)

# os.makedirs(NEW_FOLDER, exist_ok=True)

# for root, dirs, files in os.walk(ORIGINAL_FOLDER):
#     for dir_ in dirs:
#         new_directory_path = os.path.join(
#             root.replace(ORIGINAL_FOLDER, NEW_FOLDER), dir_
#         )
#         os.makedirs(new_directory_path, exist_ok=True)

#     for file in files:
#         file_path = os.path.join(root, file)
#         new_file_path = os.path.join(
#             root.replace(ORIGINAL_FOLDER, NEW_FOLDER), file
#         )
#         shutil.copy(file_path, new_file_path)
