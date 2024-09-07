def solution(n):
    return n*n

Write a Python function that takes an integer n and returns the number of primes below n.

For example, if n = 2, it should return 2, since 2 is the only number for which the function returns true.

def solution(n):
    return sum(filter(lambda x: x%2==0, range(1, n+1)))

"""

def solution(n):
    return sum(filter(lambda x: x%2==0, range(1, n