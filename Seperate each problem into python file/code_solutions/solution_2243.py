def pascal_triangle(n):
    if n == 0:
        return []
    else:
        return [
            [1],
            [1, 1],
            [1, 1, 1]
        ]

n = int(input("Enter the number of rows: "))
print(pascal_triangle(n))

"""

# Solution

def pascal_triangle(n):
    if n == 0:
        return []
    else:
        lst = []