def solution(s):
    d = {}
    for i in s:
        d[i] = s.count(i)
    return d

print(solution(set("abcd")))

"""

def solution(s):
    d = {}
    for i in s:
        d[i] = s.count(i)
    return d

print(solution(set("abcd")))