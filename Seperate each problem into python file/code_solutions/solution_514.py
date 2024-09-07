import decimal

def solution(x, y):
    return (decimal.Decimal(x) / decimal.Decimal(y))

print(solution(1.5, '1.5'))
print(solution(1.5, '1.5e+2'))
print(solution(1.5, '1.5e+2.5'))
print(solution