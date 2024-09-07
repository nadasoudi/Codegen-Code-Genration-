def is_capital(string):
    if string[0].isupper():
        return True
    elif string[0].islower():
        return True
    elif string[0].isdigit():
        return True
    else:
        return False

print(is_capital("Python"))
print(is_capital("PYTHON"))
print(is_capital("PYTHON"))
print(is