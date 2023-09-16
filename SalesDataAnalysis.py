import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

data = pd.read_csv("Sales Data.csv")
print(data.head())
print(data.isnull().sum())


''' # Sample DataFrame
data = {'Date': ['2023-09-07', '2023-09-08', '2023-09-09']}
df = pd.DataFrame(data)'''
# Convert the 'Date' column to datetime
data['Order Date'] = pd.to_datetime(data['Order Date'])
# Check the data types after conversion
print(data.dtypes)




sns.countplot(x="Product", data=data)
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.show()
product_totals = data.groupby('Product')['Quantity Ordered'].sum().reset_index()

# Sort the products by total quantity sold in descending order to highlight the highest seller
product_totals = product_totals.sort_values(by='Quantity Ordered', ascending=False)
# Create a bar plot to visualize the total quantity sold for each product
plt.figure(figsize=(10, 6))
sns.barplot(x='Quantity Ordered', y='Product', data=product_totals, palette='viridis')
plt.xlabel('Total Quantity Sold')
plt.ylabel('Product')
plt.title('Total Quantity Sold by Product')
plt.show()


data['Revenue'] = data['Quantity Ordered'] * data['Price Each']
total_revenue = data['Revenue'].sum()
average_revenue_per_sale = data['Revenue'].mean()
product_revenue = data.groupby('Product')['Revenue'].sum()
import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x='Revenue', y='Product', data=product_revenue.reset_index(), palette='viridis')
plt.xlabel('Total Revenue')
plt.ylabel('Product')
plt.title('Revenue by Product')
plt.show()



# Make sure your 'Date' column is in datetime format

# Sort the data by date if it's not already sorted
data.sort_values(by='Order Date', inplace=True)

# Group the data by product
grouped_data = data.groupby('Product')

# Create a time series plot for each product
plt.figure(figsize=(12, 8))  # Adjust the figure size as needed

for product, group in grouped_data:
    plt.plot(group['Order Date'], group['Sales'], marker='o', linestyle='-', label=product)

plt.title('Sales Trends Over Time by Product')
plt.xlabel('Order Date')
plt.ylabel('Sales')
plt.grid(True)

# Add labels, legends, or other customizations as needed
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.legend(loc='upper left')  # Display a legend with product names
plt.tight_layout()

# Show the plot
plt.show()



plt.figure(figsize=(10, 6))
plt.scatter(data['Price Each'], data['Quantity Ordered'], alpha=0.5, color='blue')
plt.title('Scatter Plot: Price vs. Quantity Sold')
plt.xlabel('Price')
plt.ylabel('Quantity Sold')
plt.grid(True)

# Add labels, legend, or other customizations as needed
plt.tight_layout()

# Show the scatter plot
plt.show()


# Calculate profit margin for each transaction or product
data['Profit Margin'] = data['Sales'] - data['Price Each']

plt.figure(figsize=(10, 6))
plt.hist(data['Profit Margin'], bins=20, color='skyblue', edgecolor='black')
plt.title('Profit Margin Distribution')
plt.xlabel('Profit Margin (%)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()








