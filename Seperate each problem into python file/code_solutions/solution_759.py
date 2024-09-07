def insert_values(table, values):
    for i in range(len(values)):
        table[i] = values[i]
    return table

table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(insert_values(table, values))

"""

def insert_values(table, values):
    for