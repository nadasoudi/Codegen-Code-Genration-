def print_diamond(n):
    for i in range(n):
        for j in range(n-i):
            print('*', end='')
        for j in range(i+1):
            print('*', end='')
        print()

n = int(input("Enter the size of the diamond: "))
print_diamond(n)

"""

# Solution:

def print_diamond(n):
    for