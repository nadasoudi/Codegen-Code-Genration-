def print_values(rows):
    for row in rows:
        for value in row:
            print(value, end=" ")
        print()

rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_values(rows)

"""

# Solution

def print_values(rows):
    for row in rows:
        for value in row:
            print(value, end=" "