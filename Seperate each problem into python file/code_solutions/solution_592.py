import numpy as np

text = '''
This is a multi-line string.

This is a multi-line string.

This is a multi-line string.
'''

# split the text into lines
lines = text.split('\n')

# split the lines into array values
arr = np.asarray(lines)

# print the array values
print(arr)

# print the array values
print(arr[0])