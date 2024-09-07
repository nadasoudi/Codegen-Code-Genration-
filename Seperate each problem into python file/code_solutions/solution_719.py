def check_lowercase(string):
    for i in string:
        if i.islower():
            return True
    return False

print(check_lowercase("python"))

"""

# Solution 1

def check_lowercase(string):
    for i in string:
        if i.islower():
            return True
    return False

print(check_lowercase("python"))

# Solution 2

def check_lowercase(string):
    for