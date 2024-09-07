import pandas as pd

df = pd.read_csv("https://github.com/jbrownlee/Datasets/blob/master/python/data/student_scores.csv")

# Create a new column named "avg" that is the mean of all the values in the column.
df["avg"] = df["gpa"].astype("float").mean()