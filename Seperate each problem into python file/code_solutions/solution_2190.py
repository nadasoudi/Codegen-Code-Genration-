def negative_numbers(start, end):
    for i in range(start, end + 1):
        if i < 0:
            print(i)

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

negative_numbers(start, end)

"""

def negative_numbers(start, end):
    for i in range(start, end + 1):
        if i < 0:
            print(i