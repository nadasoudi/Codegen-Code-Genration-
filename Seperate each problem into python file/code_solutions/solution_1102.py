def is_start_with_char(str, char):
    return str.startswith(char)

print(is_start_with_char('python', 't'))

"""

# Solution 1

def is_start_with_char(str, char):
    return char in str

print(is_start_with_char('python', 't'))

# Solution 2

def is_start_with_char(str, char