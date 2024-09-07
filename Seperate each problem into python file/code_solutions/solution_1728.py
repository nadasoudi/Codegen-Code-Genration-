def sort_tuples(tuples):
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            if tuples[i][1] > tuples[j][1]:
                tuples[i], tuples[j] = tuples[j], tuples[i]
    return tuples

print(sort_tuples([(1, 5), (2, 4), (3, 2), (4, 1)]))