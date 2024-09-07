def solution(d, v):
    answer = []
    for i in d:
        if d[i] == v:
            answer.append(i)
    return answer

d = {'a': 1, 'b': 2, 'c': 3}
v = 'a'
print(solution(d, v))

"""

def solution(d, v):
    answer = []
    for i in d:
        if d[i] == v:
            answer.append(