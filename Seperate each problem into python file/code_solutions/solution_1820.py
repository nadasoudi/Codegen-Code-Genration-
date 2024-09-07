def solution(s):
    freq = {}
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    freq = sorted(freq.items(), key=lambda x: x[1])
    return freq[0][0]

print(solution("abcabcbb"))
print(solution("bbbbb"))
print(solution("pwwkew"))
print(