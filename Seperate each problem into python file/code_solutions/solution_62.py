import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

df.replace("?", -99999, inplace=True)
df.replace("?", "", inplace=True)
df.replace("-99999", "", inplace=True)
df.replace("-9999", "", inplace=True)
df.replace("nan", "", inplace=