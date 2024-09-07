def add_leading_zeroes(s, n):
    return s + str(n).zfill(len(s))

print(add_leading_zeroes("1234", 2))
print(add_leading_zeroes("12345", 3))
print(add_leading_zeroes("123456789", 4))

"""

def add_leading_zeroes(s, n):
    return s + str(n).zfill(len(s))

print(