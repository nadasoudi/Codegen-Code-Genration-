def is_valid_string(string):
    if len(string) < 3 or len(string) > 10:
        return False
    if string.isdigit():
        return False
    if string.count('0') > 0 or string.count('1') > 0:
        return False
    return True

print(is_valid_string('1234'))
print(is_valid_string('123'))
print(is_valid_string('12'))