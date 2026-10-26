import pandas as pd 
df = pd.read_csv('sales_data.csv')

# Display the first five rows of the dataset
print(df.head(5))

# Display the number of rows and columns in the dataset
print(df.shape)

# Display the column names, data types of each column and check for missing values
print(df.info())

# Display the number of exact duplicate rows in the dataset
print(df.duplicated().sum())

# Display the number of missing values in each column
print(df.isnull().sum())

# Display the data types of each column in the dataset
print(df.dtypes)

# Display the unique values in the Region column
print(df["Region"].unique())

# Clean the Region column by:
# a.Removing leading and trailing spaces.
# b.Converting the region names to title case.
# c.Saving the cleaned values back into df.
df["Region"] = df["Region"].str.strip().str.title()

# Clean the Customer Name column by:
# a.Removing leading and trailing spaces.   
# b.Converting the customer names to title case.
# c.Saving the cleaned values back into df.
df["Customer"] = df["Customer"].str.strip().str.title()
print(df["Customer"].unique())

# Convert the Quantity column to numeric
df["Quantity"] = pd.to_numeric(df["Quantity"],errors='coerce')

# Convert the Unit Price column to numeric
df["Unit_Price"] = pd.to_numeric(df["Unit_Price"],errors='coerce')

# Display only the rows where Quantity or Unit_Price is missing 
print(df[df["Quantity"].isnull() | df["Unit_Price"].isnull()])

# Which orders have missing quantities, 
# and what are their Order_ID, Product, and Quantity values?
print(df[df["Quantity"].isnull()][["Order_ID","Product","Quantity"]])

# Display the unique unit prices for each product
unique_prices_per_product = df.groupby("Product")["Unit_Price"].unique()
print(unique_prices_per_product)

# Create a new DataFrame called cleaned_df containing only rows where Quantity is not missing.
# .notnull(): method is used to filter out rows with missing values 
cleaned_df = df[df["Quantity"].notnull()]

# Update your code to create cleaned_df 
# containing rows where both Quantity and Unit_Price are not missing
cleaned_df = df[(df["Quantity"].notnull()) & (df["Unit_Price"].notnull()) & (df["Customer"].notnull())]

# Calculate sales revenue
cleaned_df["Sales"] = cleaned_df["Quantity"]*cleaned_df["Unit_Price"]
print(cleaned_df.head())

# Calculate total revenue
total_revenue =cleaned_df["Sales"].sum()
print("Total Revenue: ", total_revenue)

# Calculate revenue by product
revenue_by_product = cleaned_df.groupby("Product")["Sales"].sum()
print(revenue_by_product)

# Calculate revenue by region
revenue_by_region = cleaned_df.groupby("Region")["Sales"].sum()
print(revenue_by_region)

# Export the cleaned dataset
# Syntax: dataframe_name.to_csv('filename.csv', index=False)
cleaned_df.to_csv('cleaned_sales_data.csv', index=False)
print("Cleaned dataset exported to 'cleaned_sales_data.csv'")