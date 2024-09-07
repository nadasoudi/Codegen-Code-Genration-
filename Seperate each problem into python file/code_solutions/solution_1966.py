def similar_char(s1, s2):
    if len(s1)!= len(s2):
        return False
    for i in range(len(s1)):
        if s1[i]!= s2[i]:
            return False
    return True

print(similar_char('abc', 'abc'))
print(similar_char('abc', 'abcd'))
print(similar_char('abc', 'ab'))
print(similar_char('abc', 'a'))