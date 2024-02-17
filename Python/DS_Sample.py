import pandas as pd

# Load the dataset from a CSV file
data = pd.read_csv('car_prices.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Check the summary statistics of numeric columns
print("\nSummary statistics:")
print(data.describe())

# Group the data by 'make' and calculate the average price for each make
make_price = data.groupby('make')['price'].mean()
print("\nAverage price by make:")
print(make_price)

# Filter the data to show only cars with a price greater than $20,000
high_priced_cars = data[data['price'] > 20000]
print("\nHigh-priced cars:")
print(high_priced_cars)

# Count the number of cars for each body style
body_style_counts = data['body-style'].value_counts()
print("\nCount of cars by body style:")
print(body_style_counts)

# Save the processed data to a new CSV file
data.to_csv('processed_car_prices.csv', index=False)
print("\nProcessed data saved to 'processed_car_prices.csv'")
