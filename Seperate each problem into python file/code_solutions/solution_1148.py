def max_freq(lst):
    max_freq = 0
    for i in lst:
        if i > max_freq:
            max_freq = i
    return max_freq

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max_freq(lst))

"""

def max_freq(lst):
    max_freq = 0