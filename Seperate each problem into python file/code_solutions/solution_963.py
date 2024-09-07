import sys

def remove_zero(lst):
    lst.pop(0)
    lst.pop(4)
    lst.pop(5)
    return lst

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(remove_zero(lst))