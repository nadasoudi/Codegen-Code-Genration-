def swap(a, b):
    a, b = b, a
    return a, b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(swap(a, b))

"""

# Solution:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a, b)
a, b = b, a
print(a, b)