def solution(a, b):
    d = {}
    for i in a:
        if i in b:
            d[i] = b.count(i)
    return d

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""

def solution(a, b):
    d = {}