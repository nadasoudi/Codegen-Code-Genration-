def second_lowest_grade(students, names, grades):
    second_lowest_grade = []
    for student in students:
        second_lowest_grade.append(min(grades[student]))
    return second_lowest_grade

print(second_lowest_grade(["Harry", "Ron", "Hermione", "Ginny"],