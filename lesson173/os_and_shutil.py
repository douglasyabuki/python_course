# os + shutil - Copying files with Python
# We are going to copy files from one folder to another.
# Copy -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
ORIGINAL_FOLDER = os.path.join(DESKTOP, 'EXAMPLE')
NEW_FOLDER = os.path.join(DESKTOP, 'NEW_FOLDER')

os.makedirs(NEW_FOLDER, exist_ok=True)

for root, dirs, files in os.walk(ORIGINAL_FOLDER):
    for dir_ in dirs:
        new_dir_path = os.path.join(
            root.replace(ORIGINAL_FOLDER, NEW_FOLDER), dir_
        )
        os.makedirs(new_dir_path, exist_ok=True)

    for file in files:
        file_path = os.path.join(root, file)
        new_file_path = os.path.join(
            root.replace(ORIGINAL_FOLDER, NEW_FOLDER), file
        )
        shutil.copy(file_path, new_file_path)
