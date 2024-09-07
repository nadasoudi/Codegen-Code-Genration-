import os

def get_file_creation_date(file_name):
    """
    Returns the creation date of the file.
    """
    try:
        f = open(file_name, 'r')
        return f.read()
    except IOError:
        return None

def get_file_modification_date(file_name):
    """
    Returns the modification date of the file.
    """
    try:
        f = open(file_name, 'r')