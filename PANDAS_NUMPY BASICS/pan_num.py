import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv('auto_purchases.csv')
#number of records
print("Number of records (rows):", len(df))
#number of columns
print("Total elements in DataFrame:", df.size)
#number of columns
print("Column names:", df.columns.tolist())
#data types of each column
print("Data types of each column:\n", df.dtypes)
#numerical summary of the columns
print(df.describe())
#numerical standard deviation of the columns
print("Standard deviation of the columns:\n", df.std(numeric_only=True))
#mean of the first 50 columns
print(df.head(50).mean(numeric_only=True))
#mean of the last 50 columns    
print(df.tail(50).mean(numeric_only=True))
#describe the price column
print(df['price'].describe())
print("Length of price column:", len(df['price']))
print("Average price:", df['price'].mean())

print("\n--- a) Most and Least Expensive Car Make on Average ---")
avg_price_per_make = df.groupby('company')['price'].mean()
most_expensive = avg_price_per_make.idxmax(), avg_price_per_make.max()
least_expensive = avg_price_per_make.idxmin(), avg_price_per_make.min()
print("Most Expensive Make (avg):", most_expensive)
print("Least Expensive Make (avg):", least_expensive)

print("\n--- b) Number of Different Car Models ---")
# If 'model' column exists, use that; else use company + body-style combo
if 'model' in df.columns:
    unique_models = df['model'].nunique()
else:
    unique_models = df[['company', 'body-style']].drop_duplicates().shape[0]
print("Unique Car Models:", unique_models)

print("\n--- c) Distribution of Car Body-style ---")
body_style_distribution = df['body-style'].value_counts()
print(body_style_distribution)

print("\n--- d) Correlation Between Mileage and Price ---")
correlation = df['average-mileage'].corr(df['price'])
print("Correlation Coefficient:", correlation)

print("\n--- e) Most Bought Body-style ---")
most_bought_style = df['body-style'].value_counts().idxmax()
print("Most Popular Body-style:", most_bought_style)

print("\n--- f) Average Mileage ---")
average_mileage = df['average-mileage'].mean()
print("Average Mileage:", average_mileage)

print("\n--- g) Plot: Price vs Horsepower ---")
plt.figure(figsize=(8, 5))
plt.scatter(df['horsepower'], df['price'], color='green', alpha=0.7)
plt.title('Price vs Horsepower')
plt.xlabel('Horsepower')
plt.ylabel('Price')
plt.grid(True)
plt.tight_layout()
plt.show()

print("\n--- h) Grouped Data by Wheel-Base, Body-style and Price ---")
grouped_data = df.groupby(['wheel-base', 'body-style'])['price'].mean().reset_index()
print(grouped_data)

