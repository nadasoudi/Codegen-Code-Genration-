def cyclic_iter(lst):
    for i in range(len(lst)):
        yield lst[i]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in cyclic_iter(lst):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
#