def solution(x, y, z):
    d = {11: [], 21: [], 31: [], 41: []}
    for i in range(x, z + 1):
        d[i].append(i)
    for i in range(x, z + 1):
        d[i].append(i)