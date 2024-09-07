def smallest_multiple(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return min(factors)

print(smallest_multiple(10))

"""

# Solution:

def smallest_multiple(n):
    factors = []
    for i in range(1, n+1):
        if n % i ==