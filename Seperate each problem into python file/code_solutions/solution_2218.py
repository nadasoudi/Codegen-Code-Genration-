def solution(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                count += 1
    return count

print(solution("abcabcbb"))
print(solution("bbbbb"))
print(solution("pwwkew"))

"""

def solution(s):
    count = 0
    for i in range(len(s)):