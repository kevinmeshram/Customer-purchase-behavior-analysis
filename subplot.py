import matplotlib.pyplot as plt
import pandas as pd

# Load all data (same paths you've been using)
df = pd.read_csv('data/product_analysis.csv', encoding='ISO-8859-1')
dfm = pd.read_csv('data/monthly_revenue.csv', encoding='ISO-8859-1')
dfrfm = pd.read_csv('data/customer_RFM.csv', encoding='ISO-8859-1')
country_stats = pd.read_csv('data/country_status.csv', encoding='ISO-8859-1')

# Prepare top 10s (same as before)
top_products_byValue = df.nlargest(10, 'TotalValue')
top_countries = country_stats.nlargest(10, 'TotalRevenue')

# Create the 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# --- Top-left: Top Products Bar Chart ---
axes[0, 0].bar(top_products_byValue['Description'], top_products_byValue['TotalValue'])
axes[0, 0].set_title('Top 10 Products by Revenue')
axes[0, 0].set_xlabel('Product')
axes[0, 0].set_ylabel('Revenue')
axes[0, 0].tick_params(axis='x', rotation=30)

# --- Top-right: Monthly Revenue Trend ---
axes[0, 1].plot(dfm['InvoiceMonth'], dfm['TotalValue'], marker='o')
axes[0, 1].set_title('Revenue Trend')
axes[0, 1].set_xlabel('Month')
axes[0, 1].set_ylabel('Revenue')
axes[0, 1].set_xticks(dfm['InvoiceMonth'])

# --- Bottom-left: RFM Scatter Plot ---
scatter = axes[1, 0].scatter(dfrfm['Recency'], dfrfm['TotalSpent'], c=dfrfm['NumOrders'], cmap='viridis', s=100)
axes[1, 0].set_title('Customer RFM Scatter')
axes[1, 0].set_xlabel('Recency (days)')
axes[1, 0].set_ylabel('Monetary (total spent)')
fig.colorbar(scatter, ax=axes[1, 0], label='Frequency')

# --- Bottom-right: Top Countries Bar Chart ---
axes[1, 1].bar(top_countries['Country'], top_countries['TotalRevenue'])
axes[1, 1].set_title('Top 10 Countries by Revenue')
axes[1, 1].set_xlabel('Country')
axes[1, 1].set_ylabel('Revenue')
axes[1, 1].tick_params(axis='x', rotation=45)
axes[1, 1].set_yscale('log')

plt.tight_layout()
plt.savefig('visualization/combined_dashboard.png', dpi=300)
plt.show()