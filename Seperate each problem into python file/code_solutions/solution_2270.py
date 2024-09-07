import random

class Flashcard:
    def __init__(self, words):
        self.words = words
        self.word_list = []
        for word in words:
            self.word_list.append(word)
        self.word_length = len(self.word_list)
        self.word_length_list = []
        for word in self.word_list:
            self.word_length_list.append(len(word))
        self.word_length_