def next_bigger(n):
    n = str(n)
    n = n[::-1]
    n = int(n)
    return n

print(next_bigger(123))
print(next_bigger(1234))
print(next_bigger(12345))
print(next_bigger(1234567890))

"""

def next_bigger(n):
    n = str(n)