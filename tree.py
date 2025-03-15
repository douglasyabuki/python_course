import os

# Change level to desired depth
def print_tree(directory, prefix="", level=1, current_level=0):
    if current_level >= level:
        return
    entries = sorted(os.listdir(directory))
    for index, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{entry}")
        if os.path.isdir(path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(path, new_prefix, level, current_level + 1)


print_tree(".")  
