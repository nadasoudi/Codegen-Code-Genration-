def combSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(combSort(arr))

"""