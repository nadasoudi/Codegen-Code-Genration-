def is_panagram(string):
    return string == string[::-1]

print(is_panagram('abba'))
print(is_panagram('abc'))
print(is_panagram('abcdef'))
print(is_panagram('abcdefghijklmnop'))
print(is_panagram('abcdefghijklmnopqrstuvwxyz'))
print(is_panagram('abcdefghijklmnopqrstuvwxyz