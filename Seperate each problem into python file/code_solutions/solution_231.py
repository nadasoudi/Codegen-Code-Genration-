def max_min_product(list):
    max_product = 0
    min_product = 0
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            product = list[i][0] * list[j][0]
            if product > max_product:
                max_product = product
            if product < min_product:
                min_product = product
    return max_product