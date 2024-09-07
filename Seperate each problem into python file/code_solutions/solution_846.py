def majority_element(arr):
    count = 0
    for i in arr:
        if arr.count(i) > count:
            count = arr.count(i)
            index = arr.index(i)
    return index

arr = [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3