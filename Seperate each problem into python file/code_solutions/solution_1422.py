def divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

print(divisors(12))

"""

def divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors