import pandas as pd

# Load the CSV data
df = pd.read_csv('sales_data.csv', dtype={'product_id': 'int32', 'price': 'float32', 'quantity': 'int32'})


# missing 'price' = mean price and 'quantity' = 0
df['price'] = df['price'].fillna(df['price'].mean())
df['quantity'] = df['quantity'].fillna(0)

# total_sales = price * quantity
df['total_sales'] = df['price'] * df['quantity']

# calculating total sales for each region
region_sales = df.groupby('region', as_index=False)['total_sales'].sum()

# Calculate average price per unit for each product_id
df_product_sales = df.groupby('product_id', as_index=False).agg(
    total_price=('price', 'sum'),
    total_quantity=('quantity', 'sum')
)
df_product_sales['average_price_per_unit'] = df_product_sales['total_price'] / df_product_sales['total_quantity']

# Merge average price per unit back into the original dataframe
df = df.merge(df_product_sales[['product_id', 'average_price_per_unit']], on='product_id', how='left')

# Filtering rows where total sales exceed ₹10,000
df_filtered = df[df['total_sales'] > 10000]

# Displaying the results
print("Region-wise total sales:")
print(region_sales)

print("\nFiltered data with sales > ₹10,000:")
print(df_filtered)

