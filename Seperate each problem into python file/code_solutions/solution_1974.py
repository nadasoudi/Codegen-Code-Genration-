import os

def replace_text(file_name, text, replacement_text):
    with open(file_name, 'r') as file:
        content = file.read()
        content = content.replace(replacement_text, text)
        with open(file_name, 'w') as file:
            file.write(content)

replace_text('sample.txt', 'Hello World', 'Hello World')

"""

import os

def replace_text(file_name, text,