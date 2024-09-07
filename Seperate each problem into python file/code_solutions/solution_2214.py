def solution(d):
    d = dict(d)
    for i in d:
        if d[i] > 1:
            d[i] = d[i] // 2
    return d

print(solution({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12