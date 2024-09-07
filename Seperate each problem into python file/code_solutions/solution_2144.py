def isSubstring(s, p):
    for i in range(len(s)):
        if s[i:i+len(p)] == p:
            return True
    return False

print(isSubstring("abcd", "ab"))
print(isSubstring("abcd", "abc"))
print(isSubstring("abcd", "abcde"))
print(isSubstring("abcd", "abcdef"))
print(isSubstring("abcd", "abcdefg"))