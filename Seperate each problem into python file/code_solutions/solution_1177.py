def gcd(x, y):
    if x > y:
        x, y = y, x
    for i in range(1, y):
        if x % i == 0 and y % i == 0:
            gcd = i
    return gcd

print(gcd(12, 24))

"""

# Solution:

def gcd(x, y):
    if x > y:
        x, y = y, x