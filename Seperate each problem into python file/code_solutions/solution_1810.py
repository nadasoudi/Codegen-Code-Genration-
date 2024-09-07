import os

def iterate_directory(directory):
    """
    :type directory: str
    :rtype: int
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))

if __name__ == '__main__':
    iterate_directory('/home/richard/Documents/python/python_projects/')