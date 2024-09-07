def check_if_key_exist(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

dictionary = {'a': 1, 'b': 2, 'c': 3}
print(check_if_key_exist(dictionary, 'a'))
print(check_if_key_exist(dictionary, 'd'))
print(check_if_key_exist(dictionary, 'e'))