def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] % 2 == 0:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sort(arr))

arr = [1, 2, 3, 4