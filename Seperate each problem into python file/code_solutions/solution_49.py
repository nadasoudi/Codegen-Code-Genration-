def four_elements(arr, num):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[k] == num:
                    print(arr[i], arr[j], arr[k])

arr =