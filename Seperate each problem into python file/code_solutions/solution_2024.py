def isSubset(s,t):
    if len(s)<len(t):
        return False
    for i in range(len(s)):
        if s[i] not in t:
            return False
    return True

print(isSubset("abc","abc"))
print(isSubset("abc","a"))
print(isSubset("abc","a",0,0))
print(isSubset("abc","a",0,1))
print(isSubset("