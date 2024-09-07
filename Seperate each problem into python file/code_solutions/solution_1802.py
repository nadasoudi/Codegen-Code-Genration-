def words_frequency(string):
    word_list = string.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

print(words_frequency("The quick brown fox jumps over the lazy dog"))

"""

def words_frequency(string):
    word_list = string.split()
    word_