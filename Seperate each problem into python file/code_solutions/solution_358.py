def string_similarity(s1, s2):
    if len(s1)!= len(s2):
        return 0
    count = 0
    for i in range(len(s1)):
        if s1[i]!= s2[i]:
            count += 1
    return count / float(len(s1))

print(string_similarity("abc", "abc"))
print(string_similarity("abc", "abcd"))
print(string_similar