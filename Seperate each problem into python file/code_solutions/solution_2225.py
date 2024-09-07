s = "abcdefghijklmnopqrstuvwxyz"

def is_special_char(s):
    for i in s:
        if i in "!@#$%^&*()_+-=[]{}|":
            return True
    return False

print(is_special_char(s))

"""

# Solution:

def is_special_char(s):
    for i in s:
        if i in "!@#$%^