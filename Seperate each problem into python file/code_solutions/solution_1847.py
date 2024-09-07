def max_unique(arr):
    max_val = 0
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max_unique(arr))

"""

def max_unique(arr):
    max_val = 0
    for i in range(len(arr)