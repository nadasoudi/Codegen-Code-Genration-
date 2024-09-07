def solution(arr):
    max_len = 0
    min_len = 0
    for i in range(len(arr)):
        if arr[i] > max_len:
            max_len = arr[i]
        if arr[i] < min_len:
            min_len = arr[i]
    return max_len, min_len

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(