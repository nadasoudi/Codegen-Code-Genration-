def digit_pattern(n):
    if n == 0:
        return''
    else:
        return digit_pattern(n//10) + str(n%10)

print(digit_pattern(123))

"""

def digit_pattern(n):
    if n == 0:
        return''
    else:
        return digit_pattern(n//10) + str(n%10)

print(digit_pattern(123))

"""

def digit_pattern(n):