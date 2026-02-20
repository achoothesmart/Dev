import json
import pandas as pd
from pprint import pprint

# Load JSON data from a file
with open('C:\\Dev\\personal_projects\\MedPlusData.json', 'r') as file:
    data = json.load(file)

for order in data:
    print(f"{order['dateCreated']}##{order['displayInvoiceId']}##{order['orderAmount']}")

# Pretty print the JSON data
# pprint(data)


# # If the JSON data is a list of dictionaries
# df = pd.DataFrame(data)

# # Display the first few rows of the DataFrame
# print(df.head(50))

# Display summary information
# print(df.info())
# print(df.describe())
