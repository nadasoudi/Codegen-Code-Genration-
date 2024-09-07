import string

def most_common_words(text):
    text = text.lower()
    text = text.split()
    text = [word for word in text if word not in string.punctuation]
    text =''.join(text)
    text = text.split()
    text = [word for word in text if word not in string.punctuation]
    text =''.join(text)
    text = text.split()
    text =