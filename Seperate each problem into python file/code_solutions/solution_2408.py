def common_elements(arr1, arr2, arr3):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    arr3 = sorted(arr3)
    common = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            for k in range(len(arr3)):
                if arr1[i] == arr2[j] and arr2[j] == arr3[