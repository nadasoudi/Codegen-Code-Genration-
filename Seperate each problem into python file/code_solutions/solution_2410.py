def print_diamond(n):
    for i in range(n):
        for j in range(n):
            print(i, end=" ")
        print()

n = int(input("Enter the number of rows: "))
print_diamond(n)

"""

# Solution

def print_diamond(n):
    for i in range(n):
        for j in range(n):
            print(i, end=" ")
        print()

n = int(input