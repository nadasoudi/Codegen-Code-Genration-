df = pd.read_csv('../data/customer_orders.csv')

df.groupby(['customer_id', 'order_date']).agg({'order_id': ['count']}).sort_values(by='order_date', ascending=True)

df.groupby(['customer_id', 'order_date']).agg({'order_id': ['count']}).sort_values(