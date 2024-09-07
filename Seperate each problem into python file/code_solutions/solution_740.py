def wiggleSort(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] / 2
        else:
            arr[i] = arr[i] * 3 + 1
    return arr

arr = [1, 5, 2, 6, 3, 7, 4, 8, 9, 10]
print(wiggleSort(arr))

"""

def wiggleSort(