import pandas as pd
import numpy as np

df = pd.read_csv('purchase_data.csv')

df.groupby(['customer_id']).agg({'purch_amt': ['mean', '