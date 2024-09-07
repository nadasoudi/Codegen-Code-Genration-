def height_bst(arr):
    if len(arr) == 0:
        return None
    else:
        mid = len(arr) // 2
        root = arr[mid]
        height = 0
        for i in range(mid, len(arr)):
            if arr[i] < root:
                height += 1
            else:
                height -= 1
        return height

arr = [1, 2, 3, 4, 5,