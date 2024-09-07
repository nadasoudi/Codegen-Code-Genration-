def union(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def intersection(a, b):
    return [min(a[0], b[0]), max(a[1], b[1])]

def difference(a, b):
    return [a[0] - b[0], a[1] - b[1]]

def main():
    n = int(input())
    arr = []
    for i in