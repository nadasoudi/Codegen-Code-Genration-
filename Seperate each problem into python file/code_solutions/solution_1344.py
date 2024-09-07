def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [12, 11, 13, 5, 6, 7]
print(bubbleSort(arr))

"""

"""

def bubbleSort(arr