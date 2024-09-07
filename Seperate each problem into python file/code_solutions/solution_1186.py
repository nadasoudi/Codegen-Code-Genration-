def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

print(is_number('1'))
print(is_number('1.1'))
print(is_number('1.1.1'))
print(is_number('1.1.1.1'))
print(is_number('1.1.1.1.1'))
print(is_number('