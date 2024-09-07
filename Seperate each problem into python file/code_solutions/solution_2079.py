def multiply_all_numbers(list):
    for i in range(len(list)):
        list[i] = list[i] * list[i]
    return list

print(multiply_all_numbers([1, 2, 3, 4, 5]))
print(multiply_all_numbers([1, 2, 3, 4, 5, 6]))
print(multiply_all_numbers([1, 2, 3, 4