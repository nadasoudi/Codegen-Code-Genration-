def even_numbers(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)

if __name__ == '__main__':
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))
    even_numbers(start, end)

"""

def even_numbers(start, end):
    for i in range(start, end