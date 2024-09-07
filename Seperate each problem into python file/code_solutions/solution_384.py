import decimal

def rounding(x):
    return decimal.ROUND_HALF_DOWN(x)

print(rounding(1.5))
print(rounding(2.5))
print(rounding(3.5))
print(rounding(4.5))
print(rounding(5.5))
print(