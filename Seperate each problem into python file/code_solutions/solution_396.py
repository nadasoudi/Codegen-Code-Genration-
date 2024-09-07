import pandas as pd

# Create a dataframe
df = pd.DataFrame({"Name": ["Rolf", "Charlie", "Anna", "Bob", "Jen", "Anne"], "Age": [20, 21, 22, 23, 24, 25]})

# Display the dataframe
print(df)

# Create a new column named "Years"
df["Years"] = df["Age"].apply(lambda x: x.days /