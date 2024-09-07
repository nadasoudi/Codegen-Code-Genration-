def search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
x = 10

print(search(arr, n, x))

"""

def search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return