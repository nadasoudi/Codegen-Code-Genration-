def check_capital(string):
    if string.isupper():
        return True
    elif string.islower():
        return True
    elif string.isdigit():
        return True
    else:
        return False

print(check_capital("Python is a programming language"))

"""

# Solution:

def check_capital(string):
    if string.isupper():
        return True
    el