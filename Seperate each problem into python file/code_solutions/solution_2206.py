def cocktail_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    return arr

arr = [12, 11, 13, 5, 6, 7]
print(cocktail_sort(arr))

"""

"""