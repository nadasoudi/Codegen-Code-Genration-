import decimal

def rounding(decimal_value):
    if decimal_value < 0:
        decimal_value = -decimal_value
    return decimal.Decimal(str(decimal_value)).quantize(decimal.Decimal('0.00'))

print(rounding(3.141592653589793))
print(rounding(-3.141592653589793))
print(rounding(3.14159265