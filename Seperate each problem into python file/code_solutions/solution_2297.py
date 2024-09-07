def count_even_odd(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(count_even_odd(lst))

"""

# Solution 1

def count_even_odd(lst):