def count_matching_char(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            count += 1
    return count

print(count_matching_char('abcd', 'abcd'))

"""

def count_matching_char(s1, s2):
    count = 0
    for i in range(len(s1)):