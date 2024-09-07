def repeated_char(s):
    count = 0
    for i in s:
        if i == s[count]:
            count += 1
        else:
            count = 0
    return count

print(repeated_char("abcabcbb"))
print(repeated_char("bbbbb"))
print(repeated_char("pwwkew"))

"""

def repeated_char(s):
    count = 0
    for i in s:
        if i == s[