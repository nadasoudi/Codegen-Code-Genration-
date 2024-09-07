def solution(d, f):
    answer = {}
    for i in d:
        answer[i] = f(d[i])
    return answer

def f(d):
    return d.values()

print(solution({1:2, 2:3, 3:4}, f))

"""

def solution(d, f):
    answer = {}
    for i in d:
        answer[