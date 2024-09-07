def positive_numbers(start, end):
    for i in range(start, end+1):
        if i > 0:
            if i % 2 == 0:
                print(i, end=" ")

positive_numbers(1, 10)

"""

def positive_numbers(start, end):
    for i in range(start, end+1):
        if i > 0:
            if i % 2 == 0:
                print(i, end=" ")