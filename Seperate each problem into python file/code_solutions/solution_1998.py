import os

def read_file(filename):
    """
    Read a file and return a list of lines
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return f.readlines()

def solve(files):
    """
    Solve the following problem:
    How to read multiple text files from folder in Python
    """
    # TODO: Complete the solve function below.
    # Hint: You can use the functions below to solve the problem.