def combSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [12, 11, 13, 5, 6, 7]
print(combSort(arr))

"""

def combSort(arr):
    n = len(arr)