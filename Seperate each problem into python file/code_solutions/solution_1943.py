import re

def find_files(extension):
    files = []
    for file in os.listdir('.'):
        if file.endswith(extension):
            files.append(file)
    return files

print(find_files('.py'))

"""

import re

def find_files(extension):
    files = []
    for file in os.listdir('.'):
        if file.endswith(extension):
            files