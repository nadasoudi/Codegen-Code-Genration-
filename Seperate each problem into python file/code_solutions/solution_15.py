python solution.py

"""

def count_words(sentence):
    """
    This function counts the occurrences of each word in a given sentence.
    
    Parameters:
    sentence (string): The sentence to count the occurrences of each word in.
    
    Returns:
    count_words (dict): A dictionary containing the word and its count.
    """
    
    count_words = {}
    
    for word in sentence.split():
        if word in count