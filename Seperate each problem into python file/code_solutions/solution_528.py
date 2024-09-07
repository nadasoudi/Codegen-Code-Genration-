def find_sunday(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return year - 2000
            else:
                return year - 2000 + 1
        else:
            return year - 2000 + 1
    else:
        return year - 2000 + 1

print(find_sunday(25))

"""

"""

"""

"""

"""