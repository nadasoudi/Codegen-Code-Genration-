import calendar

def ordinal(year, month, day):
    if calendar.isleap(year):
        return calendar.monthrange(year, month)[1]
    else:
        return calendar.monthrange(year, month)[0]

print(ordinal(2021, 2, 1))
print(ordinal(2021, 2, 2))
print(ordinal(2021, 2, 3))
print(ordinal(2021, 2, 4