def window_pattern(n):
    for i in range(n):
        for j in range(n-i):
            print(end=" ")
        for k in range(i+1):
            print("*",end=" ")
        print()

n = int(input("Enter the window size: "))
window_pattern(n)

"""

# Solution

def window_pattern(n):
    for i in range(n):
        for j in range(n-i):
            print