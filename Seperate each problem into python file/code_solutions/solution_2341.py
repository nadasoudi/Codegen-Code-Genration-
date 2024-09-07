def isSubstring(s, t):
    if len(s)!= len(t):
        return False
    for i in range(len(s)):
        if s[i]!= t[i]:
            return False
    return True

print(isSubstring("abc", "abc"))
print(isSubstring("abc", "abd"))
print(isSubstring("abc", "abd"))
print(isSubstring("abc", "abd"))
print(