import itertools

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

print(factorial(5))

"""

# Solution:

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

print(factorial(5))

"""