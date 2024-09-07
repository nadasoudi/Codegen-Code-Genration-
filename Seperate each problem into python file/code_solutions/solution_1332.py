def max_aggregation_pair(arr):
    max_aggregation_pair = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_aggregation_pair:
            max_aggregation_pair = arr[i]
    return max_aggregation_pair

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max_aggregation_pair(