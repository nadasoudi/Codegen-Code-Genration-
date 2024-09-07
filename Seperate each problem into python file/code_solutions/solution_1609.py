def count_words(values, word):
    count = 0
    for i in range(len(values)):
        if values[i] == word:
            count += 1
    return count

values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s',