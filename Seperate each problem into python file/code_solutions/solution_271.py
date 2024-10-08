import math

def divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i!= n // i:
                divisors.append(n//i)
    return divisors

def solution(n):
    divisors = divisors(n)