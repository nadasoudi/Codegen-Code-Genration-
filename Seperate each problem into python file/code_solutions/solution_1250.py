def count_students(class_name):
    count = 0
    for i in range(len(class_name)):
        if class_name[i] == 'A':
            count += 1
    return count

print(count_students('A'))

"""

def count_students(class_name):
    count = 0
    for i in range(len(class_name)):
        if class_name[i] == 'A':
            count