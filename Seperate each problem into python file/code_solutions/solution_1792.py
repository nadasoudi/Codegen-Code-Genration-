def factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def FFD(n):
    factors = factors(n)
    F = {}
    for i in range(1, len(factors) + 1):
        F[i] = factors.count(i)
    return F

n = int(input("Enter the number: "))
print(FD