def solution(a, b):
    if len(a)!= len(b):
        return False
    for i in range(len(a)):
        if a[i]!= b[i]:
            return False
    return True

print(solution("abcd", "abcd"))
print(solution("abcd", "abcdabcd"))
print(solution("abcd", "abcdabcdabcd"))
print(solution("abcd", "abcd