import os

def rename_dash_to_underscore(root_dir):
    for root, dirs, files in os.walk(root_dir, topdown=False):
        # Rename files first
        for name in files:
            if '-' in name:
                old_path = os.path.join(root, name)
                new_name = name.replace('-', '_')
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                print(f'Renamed file: {old_path} -> {new_path}')

        # Then rename directories
        for name in dirs:
            if '-' in name:
                old_path = os.path.join(root, name)
                new_name = name.replace('-', '_')
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                print(f'Renamed folder: {old_path} -> {new_path}')

# Example usage:
project_root = '.'  # or the path to your project folder
rename_dash_to_underscore(project_root)
