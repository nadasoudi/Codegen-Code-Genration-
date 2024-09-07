def sum_and_average(lst):
    sum = 0
    for i in lst:
        sum += i
    average = sum / len(lst)
    return sum, average

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum, average = sum_and_average(lst)
print(sum, average)

"""

def sum_and_average(lst):
    sum = 0
    for i in lst: