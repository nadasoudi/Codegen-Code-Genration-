def solution(str1, str2, n):
    count = 0
    for i in range(len(str1)):
        if str1[i] < n:
            count += 1
    for i in range(len(str2)):
        if str2[i] < n:
            count += 1
    return count

print(solution("abcde", "abcde", 2))
print(solution("abcde",