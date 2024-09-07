import pandas as pd

df = pd.read_csv("data.csv")

# Solution 1
# df = pd.read_csv("data.csv", usecols=["Name", "Age"])

# Solution 2
df = pd.read_csv("data.csv", usecols=["Name", "Age", "Class"])

# Solution 3
df = pd.read_csv("data.csv", usecols=["Name", "Age