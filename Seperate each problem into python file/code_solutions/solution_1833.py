import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

# To Do: Complete the solution so that it returns a list of lists.
# Hint: Use the list function to create a list of lists.
# Hint: Create a new list called new_list that has the first row (headers) of the file_data list.
# Hint: Add a print statement at the end of the solution to print