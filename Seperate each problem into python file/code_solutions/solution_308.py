def create_list(n):
    l = []
    for i in range(n):
        l.append([])
    return l

n = int(input("Enter the number of rows: "))
print(create_list(n))

"""

# Solution 1

def create_list(n):
    l = []
    for i in range(n):
        l.append([])
    return l

n = int(input("