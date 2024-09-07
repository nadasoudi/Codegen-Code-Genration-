def scramble(string, letters):
    for i in range(len(string)):
        if string[i] in letters:
            letters.remove(string[i])
            letters.append(string[i])
    return letters

print(scramble("abcdefghijklmnopqrstuvwxyz", ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",