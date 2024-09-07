def heap_sort(arr):
    for i in range(len(arr)//2, -1, -1):
        heapify(arr, i, len(arr))
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

def heapify(arr, i, n):
    l = 2 * i + 1
    r