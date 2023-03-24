import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('sales_data.csv')

# Analyze sales by product category
category_sales = data.groupby('Category')['Sales'].sum()

# Analyze sales by region
region_sales = data.groupby('Region')['Sales'].sum()

# Analyze sales by month
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Month'] = data['Order Date'].dt.month
monthly_sales = data.groupby('Month')['Sales'].sum()

# Visualize sales data
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 15))

# Bar chart for category sales
axes[0].bar(category_sales.index, category_sales.values)
axes[0].set_title('Sales by Product Category')
axes[0].set_xlabel('Category')
axes[0].set_ylabel('Sales')

# Bar chart for regional sales
axes[1].bar(region_sales.index, region_sales.values)
axes[1].set_title('Sales by Region')
axes[1].set_xlabel('Region')
axes[1].set_ylabel('Sales')

# Line chart for monthly sales
axes[2].plot(monthly_sales.index, monthly_sales.values)
axes[2].set_title('Monthly Sales')
axes[2].set_xlabel('Month')
axes[2].set_ylabel('Sales')

plt.tight_layout()
plt.show()
