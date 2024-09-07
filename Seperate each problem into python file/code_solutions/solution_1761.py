def multiple_index_replace(string, index, replacement):
    return string[:index] + replacement + string[index + len(replacement):]

print(multiple_index_replace('abcdef', 2, 'b'))
print(multiple_index_replace('abcdef', 2, 'b'))
print(multiple_index_replace('abcdef', 2, 'b'))
print(multiple_index_replace('abcdef', 2, 'b'))
print(multiple_index_replace('abcdef