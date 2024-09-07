def check_duplicate(word):
    if word in word_list:
        return True
    else:
        return False

word = input("Enter the word: ")
word_list = list(word)

if check_duplicate(word):
    print("The word contains duplicate characters.")
else:
    print("The word does not contain duplicate characters.")

# Output:
# Enter the word: abc