import os

def count_char(filename):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count += len(line)
    return count

print(count_char('text.txt'))

"""

# Solution 1

def count_char(filename):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count +=