def base_convert(base, num):
    if base == '1':
        return num
    else:
        return base_convert(base, num // base) + str(num % base)

print(base_convert('1', 5))

"""

# Solution:

def base_convert(base, num):
    if base == '1':
        return num
    else:
        return base_convert(base, num // base) + str(