def find_index(string, substring):
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            return i
    return 'Not found'

print(find_index('abcdefg', 'ab'))
print(find_index('abcdefg', 'ab'))
print(find_index('abcdef