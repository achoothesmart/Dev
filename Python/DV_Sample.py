import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
data = pd.read_csv('car_prices.csv')

# Group the data by 'make' and calculate the average price for each make
make_price = data.groupby('make')['price'].mean()

# Plot a bar chart
plt.figure(figsize=(10, 6))
plt.bar(make_price.index, make_price.values, color='skyblue')
plt.xlabel('Car Make')
plt.ylabel('Average Price')
plt.title('Average Car Prices by Make')
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.tight_layout()

# Display the chart
plt.show()
