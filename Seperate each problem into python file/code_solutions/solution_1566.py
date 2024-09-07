import pandas as pd
import numpy as np

df = pd.read_csv('/Users/srinivasan/Desktop/Python/data/data.csv')

# Create a function to extract the sentences where a specific word is present in a given column of a given DataFrame.
def extract_sentences(df, column, word):
    # Create a list of all the sentences where the word is present in the given column of a given