def is_business_day(day):
    if day in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        return True
    else:
        return False

print(is_business_day(1))
print(is_business_day(2))
print(is_business_day(3))
print(is_business_day(4))
print(is_business_day