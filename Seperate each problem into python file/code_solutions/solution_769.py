def matrix_sum(rows, columns, elements):
    for i in range(rows):
        for j in range(columns):
            print(elements[i][j], end=" ")
        print()

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
elements