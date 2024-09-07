def solution(d1, d2):
    d1.update(d2)
    return d1

"""

def solution(d1, d2):
    d1.update(d2)
    return d1

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'd': 4}

print(solution(d1, d2))