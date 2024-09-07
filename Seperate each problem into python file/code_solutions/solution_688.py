import decimal

def solution(d):
    if d % 0.10 == 0:
        return decimal.Decimal(d)
    else:
        return decimal.Decimal(d) / decimal.Decimal(0.10)

print(solution(5.5))
print(solution(5.5))
print(solution(5.5))
print(solution(5.5