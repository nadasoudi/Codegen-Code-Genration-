import os

def get_file_mode(file_path):
    """
    Returns the file mode of the file.
    """
    try:
        # Open the file for reading
        f = open(file_path, 'r')