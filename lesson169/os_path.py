# os.path works with file paths in Windows, Linux, and Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path is a module that provides functions to work with file paths
# in Windows, Mac, or Linux without worrying about the differences
# between these systems.
# Examples of os.path:
# os.path.join: joins strings into a single path. For example,
# os.path.join('folder1', 'folder2', 'file.txt') would return
# 'folder1/folder2/file.txt' on Linux or Mac, and
# 'folder1\\folder2\\file.txt' on Windows.
# os.path.split: splits a path into a tuple (directory, file).
# For example, os.path.split('/home/user/file.txt')
# would return ('/home/user', 'file.txt').
# os.path.exists: checks if a specified path exists.
# os.path only works with file paths and does not perform any
# input/output (I/O) operations on the files themselves.
import os

path = os.path.join('Desktop', 'course', 'file.txt')
# print(path)
directory, file = os.path.split(path)
file_name, file_extension = os.path.splitext(file)
# print(file_name, file_extension)
# print(os.path.exists('/Users/luizotavio/Desktop/python-course-repo'))
# print(os.path.abspath('.'))
print(path)
print(os.path.basename(path))
print(os.path.basename(directory))
print(os.path.dirname(path))
