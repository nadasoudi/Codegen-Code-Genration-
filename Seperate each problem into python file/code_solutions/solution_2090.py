import os

def get_file_size(file_name):
    size = os.path.getsize(file_name)
    return size

def get_file_lines(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return len(lines)

def get_file_words(file_name):
    with open(file_name, 'r') as f:
        words =