def anagram(s1, s2):
    if len(s1)!= len(s2):
        return False
    else:
        for i in range(len(s1)):
            if s1[i]!= s2[i]:
                return False
        return True

print(anagram("abc", "cba"))
print(anagram("abc", "abca"))
print(anagram("abc", "cba"))
print(anagram("