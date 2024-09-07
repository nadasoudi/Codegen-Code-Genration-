def closest_sum(arr, num):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            sum -= arr[i] + arr[j]
    return sum

arr = [1, 2, 3, 4, 5, 6,