import os

def remove_newline(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
        data = data.replace('\n', '')
        data = data.replace('\r', '')
        data = data.replace('\t', '')
        data = data.replace('\xa0', '')
        data = data.replace('\u2028', '')
        data = data.replace('\