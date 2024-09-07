def hollow_diamond(n):
    for i in range(n):
        for j in range(n):
            print(end=" ")
        for k in range(n):
            print("*", end=" ")
        print()

n = int(input("Enter the number of rows: "))
hollow_diamond(n)

"""

# Solution:

def hollow_diamond(n):
    for i in range(n):
        for j in range(n