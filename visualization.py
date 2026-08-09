import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/product_analysis.csv',encoding='ISO-8859-1')
dfm= pd.read_csv('data/monthly_revenue.csv',encoding='ISO-8859-1')
dfrfm=pd.read_csv('data/customer_RFM.csv', encoding='ISO-8859-1')
country_stats = pd.read_csv('data/country_status.csv', encoding='ISO-8859-1')

top_products_byValue = df.nlargest(10,'TotalValue') 

plt.figure(figsize=(10,6))
plt.bar(top_products_byValue['Description'],top_products_byValue['TotalValue'])
plt.title("Top 10 products by revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=30, ha='right')  # <-- this is the key line
plt.tight_layout() 
plt.savefig('visualization/top10products.png')
plt.show()


## fig 2 by monthely revenue
plt.figure(figsize=(10,6))
plt.plot(dfm['InvoiceMonth'],dfm['TotalValue'], marker='o')
plt.title("Revenue Trend")
plt.xticks(dfm['InvoiceMonth'])
plt.xlabel("month")
plt.ylabel("Revenue")
plt.savefig('visualization/monthelyrevenue.png')
plt.show()

## fig 3 by RFM

plt.figure(figsize=(10,6))
scatter = plt.scatter(dfrfm['Recency'], dfrfm['TotalSpent'], c=dfrfm['NumOrders'], cmap='viridis', s=100)
plt.colorbar(scatter, label='Frequency')
plt.title("Customer RFM Scatter")
plt.xlabel("Recency (days)")
plt.ylabel("Monetary (total spent)")
plt.savefig('visualization/RFM.png')
plt.show()

## fig 4 by country 

top_countries = country_stats.nlargest(10, 'TotalRevenue')

plt.figure(figsize=(10, 6))
plt.bar(top_countries['Country'], top_countries['TotalRevenue'])
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.yscale('log')
plt.savefig('visualization/countrydata.png')
plt.show()


### fig 5 correlation HeatMap

sample = dfrfm[['Recency','NumOrders','TotalSpent']]

correlation_matrix = sample.corr()

plt.figure(figsize=(10,6))
plt.imshow(correlation_matrix, cmap='coolwarm')
plt.colorbar(label='Correlation')
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45, ha='right')
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig('visualization/correlation.png')
plt.show()
