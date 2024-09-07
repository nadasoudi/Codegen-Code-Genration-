def max_min(list):
    max = list[0]
    min = list[0]
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]
    return max, min

print(max_min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]