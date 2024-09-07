def frequency(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

def solution(s):
    d = frequency(s)
    return len(d)

print(solution("abcdefghijklmnopqrstuvwxyz"))

"""

def frequency(s):
    d = {}
    for i in s:
        if