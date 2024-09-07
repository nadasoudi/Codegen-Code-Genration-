def timsort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [6, 4, 8, 2, 5, 1, 9, 7, 3]
print(tsort(arr))

"""

def timsort