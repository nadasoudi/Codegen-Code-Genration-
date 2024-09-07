def solution(d, c):
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    c = sorted(c.items(), key=lambda x: x[1], reverse=True)
    return d[0][0]

"""

def solution(d, c):
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    c = sorted(c.items(), key=lambda x: x[1], reverse