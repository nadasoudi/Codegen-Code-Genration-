>>> n = int(input())
>>> print(nCr(n,3))
2
>>> print(nCr(n,2))
3
>>> print(nCr(n,1))
1
>>> print(nCr(n,0))
1

"""

def nCr(n,r):
    if n == 0 or n == 1:
        return 1
    if n < 0 or r < 0:
        return 0
    return nCr(n-1,r) + nCr