def order_tuples(tuples):
    # your code goes here
    return sorted(tuples, key=lambda x: x[0])

# test your code
print(order_tuples([(1, 2), (3, 4), (5, 6)]))
print(order_tuples([(1, 2), (3, 4), (5, 6), (7, 8)]))
print(order_tuples([(1, 2), (3, 4), (5, 6), (7,