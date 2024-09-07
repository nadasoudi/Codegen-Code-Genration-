def find_index(arr, num):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return low

arr = [1, 2, 3, 4, 5, 6, 7,