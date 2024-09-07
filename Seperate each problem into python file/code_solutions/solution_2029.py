def find_word(word, word_list):
    for i in range(len(word_list)):
        if word_list[i] == word:
            return i
    return -1

word = "python"
word_list = ["python", "java", "kotlin", "javascript"]

print(find_word(word, word_list))

"""

# Solution 1

def find_word(word, word_list):
    for