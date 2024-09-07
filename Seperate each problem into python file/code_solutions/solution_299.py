import pandas as pd
import numpy as np

df = pd.read_csv("purchase_data.csv")

df.groupby(['order_date','month'])['total_purchase_amount'].sum().reset_index()

df.groupby(['order_date','month'])['total_purchase_amount'].sum().reset_index()