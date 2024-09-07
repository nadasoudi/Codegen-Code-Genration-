import math

def generate_list(start, limit):
    list = []
    for i in range(start, limit):
        if i % 2 == 0:
            list.append(i**2)
        else:
            list.append(i**3)
    return list

print(generate_list(1, 10))

# Output: [1, 4, 9, 16, 25, 36, 49, 64