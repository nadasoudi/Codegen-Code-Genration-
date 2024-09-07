import os

def get_file_size(file_name):
    with open(file_name, 'rb') as f:
        return os.fstat(f.fileno()).st_size

print(get_file_size('file.txt'))

"""

# Solution

def get_file_size(file_name):
    with open(file_name, 'rb') as f:
        return os.fstat(f.fileno()).st_