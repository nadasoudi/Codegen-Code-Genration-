import os

def count_lines(filename):
    """
    Count the number of lines in a text file.
    """
    try:
        with open(filename, 'r') as f:
            contents = f.readlines()
            return len(contents)
    except FileNotFoundError:
        print(f'The file {filename} does not exist.')
        return 0

print(count_lines('text_file.txt'))

"""
Output