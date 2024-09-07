import pandas as pd

# Create a dataframe
df = pd.DataFrame(columns=['Month', 'Start', 'End'])

# Create a loop to iterate through the dataframe
for i in range(1, 13):
    # Create a new dataframe with the month and start and end time
    new_df = pd.DataFrame(columns=['Month', '