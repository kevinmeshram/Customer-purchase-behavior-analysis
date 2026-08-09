markdown
# Customer Purchase Behavior Analysis

A Python project to analyze and visualize customer purchasing patterns using pandas, numpy, and matplotlib.

## Installation

1. Make sure you have Python 3.7+ installed
2. Navigate to the project folder
3. Install dependencies:

pip install -r requirements.txt


## How to Run

1. Open terminal/command prompt in this folder
2. Run this command:

python main.py

3. Then run:

python analysis.py

4. Finally run:

python visualizations.py


## Files

- `main.py` - Loads and cleans the data
- `analysis.py` - Performs statistical analysis
- `visualizations.py` - Creates charts
- `data/` - Folder for CSV files
- `visualizations/` - Folder where charts are saved

## Dependencies

- pandas - Data manipulation
- numpy - Numerical calculations
- matplotlib - Data visualization
- seaborn - Enhanced visualizations


# 🛍️ Customer Purchase Behavior Analysis

A data analysis project exploring customer purchasing patterns using the UCI Online Retail dataset — built with **pandas**, **numpy**, and **matplotlib**.

## 📊 Project Overview

This project analyzes ~400,000 real e-commerce transactions from a UK-based online retailer (2010-2011) to uncover:
- Customer segmentation using **RFM analysis** (Recency, Frequency, Monetary)
- Best-selling and highest-revenue products
- Revenue distribution across countries
- Seasonal sales trends throughout the year
- Correlations between customer behavior metrics

## 🗂️ Dataset

- **Source:** [UCI Online Retail Dataset](https://www.kaggle.com/datasets) (Kaggle mirror)
- **Size:** 541,909 raw transactions → 397,884 after cleaning
- **Columns:** InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

## 🧹 Data Cleaning

- Removed transactions with missing `CustomerID`
- Filtered out cancelled orders (negative quantities/prices)
- Converted date strings to proper datetime objects
- Engineered new features: `TotalValue`, `InvoiceMonth`, `InvoiceDay`, `DayOfWeek`

## 🔍 Key Findings

- **Seasonality:** Revenue nearly doubles from summer months to November/December, reflecting holiday shopping.
- **Customer concentration:** A small number of customers (bulk/wholesale buyers) account for disproportionately large order volumes.
- **RFM correlation:** Customers who order more frequently also tend to spend more overall (positive correlation), while customers with high Recency (haven't purchased recently) tend to have lower total spend.
- **Geographic concentration:** The United Kingdom dominates revenue, consistent with the retailer's home market.

## 📈 Visualizations

| Chart | Description |
|---|---|
| Top 10 Products by Revenue | Bar chart of best-selling products |
| Monthly Revenue Trend | Line chart showing seasonal patterns |
| Customer RFM Scatter | Recency vs Monetary, color-coded by Frequency |
| Top 10 Countries by Revenue | Revenue distribution by country |
| Correlation Heatmap | Relationships between Recency, Frequency, Monetary |

All charts are saved in the `visualization/` folder, including a combined dashboard (`combined_dashboard.png`).

## 🛠️ Tech Stack

- Python 3
- pandas — data cleaning & aggregation
- numpy — numerical calculations
- matplotlib — visualizations

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
python analysis.py
python visualizations.py
```

## 🎓 What I Learned

This was my first end-to-end data analysis project, where I practiced:
- Cleaning real, messy transactional data
- pandas groupby/agg for multi-level aggregation
- RFM customer segmentation
- Building and debugging multiple matplotlib chart types
- Combining charts into subplot dashboards

## 👤 Author

[Kevin Meshram] — 3rd Year CSE Student