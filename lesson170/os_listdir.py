# os.listdir to navigate directories
# /Users/username/Desktop/EXAMPLE
# C:\Users\username\Desktop\EXAMPLE
# path = r'C:\\Users\\username\\Desktop\\EXAMPLE'
import os

path = os.path.join('/Users', 'username', 'Desktop', 'EXAMPLE')

for folder in os.listdir(path):
    full_folder_path = os.path.join(path, folder)
    print(folder)

    if not os.path.isdir(full_folder_path):
        continue

    for image in os.listdir(full_folder_path):
        print('  ', image)
