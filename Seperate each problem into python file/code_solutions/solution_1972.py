def print_k(n,k):
    for i in range(n):
        for j in range(k):
            print(chr(i+97),end=" ")
        print()

n = int(input("Enter the number of elements in the array: "))
k = int(input("Enter the number of elements to print: "))
print_k(n,k)

"""

# Solution

def print_k(n,k):
    for i in range(n):