def odd_number(n):
    return lambda x: x % 2!= 0

print(list(map(odd_number, range(1, 10))))

"""

# Solution

def odd_number(n):
    return lambda x: x % 2!= 0

print(list(map(odd_number, range(1, 10))))