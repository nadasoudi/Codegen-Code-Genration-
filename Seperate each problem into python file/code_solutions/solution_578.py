def max_diff(arr):
    max_diff = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            diff = abs(arr[i] - arr[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max_diff(arr))