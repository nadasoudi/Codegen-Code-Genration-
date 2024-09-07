def isRotation(s1, s2):
    if len(s1)!= len(s2):
        return False
    for i in range(len(s1)):
        if s1[i]!= s2[i]:
            return False
    return True

print(isRotation("abcd", "dcba"))
print(isRotation("abcd", "abcd"))
print(isRotation("abcd", "abcd"))
print(isRotation