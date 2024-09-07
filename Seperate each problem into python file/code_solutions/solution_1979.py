def remove_punctuation(string):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in string:
        if char not in punctuation:
            string = string.replace(char, '')
    return string

print(remove_punctuation('This is a string with at least one non-punctuation character'))

'''

'''

def remove_punctuation(string):