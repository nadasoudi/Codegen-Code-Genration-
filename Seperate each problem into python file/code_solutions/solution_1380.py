import pandas as pd

df = pd.read_csv("C:/Users/DELL/Downloads/pandas_data_science/pandas_data_science/exercises/data/election_results.csv")

df.columns = df.columns.str.lower()

df.dropna(subset=['candidate_name'], inplace=True)

df.dropna(subset=['