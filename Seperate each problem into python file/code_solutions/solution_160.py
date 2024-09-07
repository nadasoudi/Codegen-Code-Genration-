import pandas as pd

df = pd.read_csv('world_alcohol_consumption.csv')

df['avg_cons'] = df['world_alcohol_consumption']/df['world_alcohol_consumption'].max()

print(df.avg_cons.max())

# Output:
# avg_cons
# 0.0
# 0.0
# 0.0
# 0.0
# 0.