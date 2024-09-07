import re

def search(text, pattern):
    """
    Search for a string in text files.
    """
    for line in text:
        if re.search(pattern, line):
            print(line)

search(open('textfiles/textfile1.txt'), 'python')
search(open('textfiles/textfile2.txt'), 'python')
search(open('textfiles/textfile3.txt'), 'python')
search(open('textfiles/textfile4