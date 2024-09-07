def histogram(lst):
    hist = {}
    for i in lst:
        if i not in hist:
            hist[i] = 1
        else:
            hist[i] += 1
    return hist

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(histogram(lst))

"""

# Solution:

def histogram(lst):
    hist = {}