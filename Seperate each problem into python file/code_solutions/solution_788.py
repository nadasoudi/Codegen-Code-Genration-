import pandas as pd

# Read the data
df = pd.read_csv("data/pima-indians-diabetes.csv")

# Split the data into two labels
y = df["Outcome"]
x = df.drop("Outcome", axis=1)

# Split the data into two ranges
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size