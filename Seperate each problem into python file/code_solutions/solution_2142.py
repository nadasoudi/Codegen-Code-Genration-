def solution(d):
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return d

"""

def solution(d):
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return d

print(solution({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}))

"""

def solution(d