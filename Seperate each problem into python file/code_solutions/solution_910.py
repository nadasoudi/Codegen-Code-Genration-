def first_repeated_char(str):
    for i in range(len(str)):
        if str[i] == str[i-1]:
            return str[i]
    return -1

print(first_repeated_char("abcabcbb"))
print(first_repeated_char("bbbbb"))
print(first_repeated_char("pwwkew"))
print(first_repeated_char(""))
print(first_repeated_char