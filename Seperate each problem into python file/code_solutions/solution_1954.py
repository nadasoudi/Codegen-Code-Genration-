def solution(str1, str2):
    # Write your code here
    if len(str1) > len(str2):
        return len(str1) - len(str2)
    else:
        return len(str2) - len(str1)

print(solution("abc", "abc"))
print(solution("abc", "abcd"))
print(solution("abc", "abcdabcdabcd"))
print(solution("abc", "abcabcabcabc"))