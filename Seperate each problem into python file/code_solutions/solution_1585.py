def countingSort(arr, exp):
    count = [0 for i in range(exp+1)]
    for i in arr:
        count[i] += 1
    
    for i in range(1, exp+1):
        count[i] += count[i-1]
    
    result = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        result[count[arr[i]]-1] = arr[i]
        count[arr