import os

def is_file(path):
    return os.path.isfile(path)

def is_dir(path):
    return os.path.isdir(path)

def is_file_or_dir(path):
    return is_file(path) or is_dir(path)

def is_file_or_dir_or_not(path):
    return is_file(path) or is_dir(path) or not is_