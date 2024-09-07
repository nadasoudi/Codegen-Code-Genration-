def even_odd(arr):
    even = 0
    odd = 0
    for i in arr:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_odd(arr))

"""

# Solution:

def even_odd(arr):