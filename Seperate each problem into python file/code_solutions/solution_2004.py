def print_diamond_star(n):
    for i in range(n):
        for j in range(n):
            print(i*2, end=" ")
        print()

n = int(input("Enter the number of rows: "))
print_diamond_star(n)

"""

# Solution

def print_diamond_star(n):
    for i in range(n):
        for j in range(n):
            print(i*2, end=" ")