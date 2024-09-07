def binary_equivalent(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return binary_equivalent(n//2) + binary_equivalent(n//2 + 1)

n = int(input("Enter the number to find the binary equivalent: "))
print(binary_equivalent(n))

"""

# Solution 1

def binary_equivalent(n):
    if n == 0: