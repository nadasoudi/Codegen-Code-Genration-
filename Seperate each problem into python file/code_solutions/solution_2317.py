import re

def count_words(filename):
    """
    Count the number of words in a text file.
    """
    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = re.findall(r'\w+', contents)
        print(f"The file {filename} has {len(words)}