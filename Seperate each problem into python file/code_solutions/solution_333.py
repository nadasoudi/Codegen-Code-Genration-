def is_closed(file):
    if file.closed:
        return True
    else:
        return False

print(is_closed(open('test.txt')))

"""

# Solution 1

def is_closed(file):
    return file.closed

print(is_closed(open('test.txt')))

# Solution 2

def is_closed(file):
    return file.closed

print(is_closed(open('test.txt'