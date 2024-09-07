def counter_aggregation(a, b):
    c = 0
    for i in range(len(a)):
        c += a[i] * b[i]
    return c

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(counter_aggregation(a, b))

"""