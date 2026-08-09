import pandas as pd
df = pd.read_csv('data/data_cleared.csv', encoding='ISO-8859-1')

## finding Frequency and Monitary of data

result = df.groupby('CustomerID')['Quantity'].sum()

r2 = df.groupby('CustomerID')['InvoiceNo'].nunique()

customer_df= df.groupby('CustomerID') .agg({
  'InvoiceNo' : 'nunique',
  'Quantity': 'sum',
  'TotalValue': 'sum'
})
customer_df = customer_df.rename(columns={
    'InvoiceNo': 'NumOrders',
    'Quantity': 'TotalQuantity',
    'TotalValue': 'TotalSpent'
})
customer_df['AvgOrderValue'] = customer_df['TotalSpent'] / customer_df['NumOrders']
customer_df = customer_df.reset_index()

Top10Spents= customer_df.nlargest(10,'TotalSpent')
Top10Orders= customer_df.nlargest(10,'NumOrders')
# print(Top10Orders)
# print(Top10Spents)
# print(customer_df.head(10))

## finding Recency from the data 

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

last_purchase = df.groupby('CustomerID')['InvoiceDate'].max()

overall_lastDate = df['InvoiceDate'].max()

Recency = overall_lastDate - last_purchase
Recency = Recency.dt.days   # convert timedelta into plain number of days
print(Recency)
combined = customer_df.merge(Recency, on='CustomerID')                       ######   FINAL (RFM) analysis data
combined = combined.rename(columns={'InvoiceDate':'Recency'})

print(combined)

combined.to_csv('data/customer_RFM.csv')

          ###Product analysis

product_state=df.groupby('Description').agg({
      'Quantity': 'sum',
    'TotalValue': 'sum'
})
print(product_state)

top_by_quantity= product_state.nlargest(10,'Quantity')
top_by_TotalValue=product_state.nlargest(10, 'TotalValue')
print(top_by_quantity)
print(top_by_TotalValue)

product_state.to_csv('data/product_analysis.csv')

         ### Country analysis

country_stats = df.groupby('Country').agg({
    'TotalValue': 'sum',
    'CustomerID': 'nunique',
    'InvoiceNo': 'nunique'
})

country_stats = country_stats.rename(columns={
    'TotalValue': 'TotalRevenue',
    'CustomerID': 'NumCustomers',
    'InvoiceNo': 'NumOrders'
})

country_stats['AvgOrderValue'] = country_stats['TotalRevenue'] / country_stats['NumOrders']

#print(country_stats.sort_values('TotalRevenue', ascending=False))
country_stats.to_csv('data/country_status.csv')

       ### Time based analysis 

       
montly_revenue = df.groupby('InvoiceMonth')['TotalValue'].sum()
day_with_mostOrders = df.groupby('InvoiceDay')['InvoiceNo'].nunique()
montly_revenue.to_csv('data/monthly_revenue.csv')
day_with_mostOrders.to_csv('data/day_with_mostOrder.csv')

#print(montly_revenue)
#print(day_with_mostOrders)