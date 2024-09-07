def highest_product(arr):
    max_product = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
    return max_product

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(highest_product(