def SkewNestedTupleSummation(n, a, b):
    return a + b + (n - 1) * (b - a)

n = int(input())
a = int(input())
b = int(input())
print(SkewNestedTupleSummation(n, a, b))

"""

def SkewNestedTupleSummation(n, a, b):
    return a + b + (n - 1) * (b