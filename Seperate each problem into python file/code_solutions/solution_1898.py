def insertion_sort(d):
    for i in range(1, len(d)):
        key = d[i]
        j = i - 1
        while j >= 0 and key < d[j]:
            d[j + 1] = d[j]
            j -= 1
        d[j + 1] = key
    return d

d = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: