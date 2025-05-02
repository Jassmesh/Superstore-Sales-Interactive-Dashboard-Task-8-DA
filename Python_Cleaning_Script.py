import pandas as pd

# Load the data
df = pd.read_csv("Superstore-Sales.csv", encoding='ISO-8859-1')

# Drop duplicates
df.drop_duplicates(inplace=True)

# Drop rows with missing key fields
df.dropna(subset=['Order Date', 'Region', 'Product Category', 'Sales', 'Profit'], inplace=True)

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create Month-Year column
df['Month-Year'] = df['Order Date'].dt.strftime('%b-%Y')

# Rename columns for consistency
df.rename(columns={'Product Category': 'Category'}, inplace=True)

# Select only required columns
df_cleaned = df[['Order Date', 'Region', 'Category', 'Sales', 'Profit', 'Month-Year']]

# Export cleaned data
df_cleaned.to_csv("Cleaned_Superstore_Sales.csv", index=False)
