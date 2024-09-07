def running_max(iterable):
    max_value = iterable[0]
    for i in iterable:
        if i > max_value:
            max_value = i
    return max_value

print(running_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(running_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))