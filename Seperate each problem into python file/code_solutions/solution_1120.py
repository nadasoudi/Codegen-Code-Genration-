def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [10, 7, 8, 9, 1, 5, 6, 4, 3, 2]
print(sort(arr))

"""

def sort