def pigeonhole_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    count = 0
    for i in range(max_value + 1):
        if arr.count(i) > count:
            count = arr.count(i)
            arr.remove(i)
            arr.append(i)
    for i in range(len(arr)):
        arr[i] = count
    return arr

arr = [1, 2, 3