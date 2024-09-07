import decimal

def rounding(x):
    return decimal.ROUND_HALF_EVEN * round(x, -1) + decimal.ROUND_HALF_EVEN

print(rounding(1.5))
print(rounding(2.5))
print(rounding(3.5))
print(rounding(4.5))
print(rounding(5.5