def odd_even_sort(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2
        else:
            arr[i] = arr[i] * 3 + 1
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(odd_even_sort(arr))

"""

def odd_even_sort