def is_distinct(t):
    if len(t)!= len(set(t)):
        return False
    else:
        return True

print(is_distinct([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(is_distinct([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23