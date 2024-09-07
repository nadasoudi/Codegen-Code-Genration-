def iterate_list(l1, l2):
    for item in l1:
        for item in l2:
            print(item, end=' ')
        print()

l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']

iterate_list(l1, l2)

l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b