import pandas as pd

df = pd.DataFrame({'Name': ['John', 'Jane', 'Jack', 'Jill', 'Jasmine'],
                   'Age': [30, 32, 33, 34, 35],
                   'Score': [85, 90, 95, 100, 90]})

# Find the index of the substring 'Jack' in the DataFrame
print(df.loc[df['Name'] == 'Jack', 'Score