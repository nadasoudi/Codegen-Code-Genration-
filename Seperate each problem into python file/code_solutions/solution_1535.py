def max_sum(lst):
    max_sum = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] + lst[j] > max_sum:
                max_sum = lst[i] + lst[j]
    return max_sum

def min_sum(lst):
    min_sum = 0
    for