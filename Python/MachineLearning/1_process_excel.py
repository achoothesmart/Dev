import pandas as pd

# Read the Excel file
file_path = 'Z:\\Sheets\\Transactions_Nov2023.xls'
df = pd.read_excel(file_path)

df.fillna(0, inplace=True)
df2 = pd.DataFrame(columns=['sno', 'date', 'description', 'debit', 'credit'])

for index, row in df.iterrows():
    lst_row = [c for c in list(row) if c != 0]
    print(lst_row)

    if len(lst_row)>=6:
        # 0 - sno, 1 - date, 4 - description, 5 - debit, 6 - credit
        df2.loc[index] = [lst_row[0], lst_row[1], lst_row[4], lst_row[5], lst_row[6]]

# Perform data cleaning operations
# For example, removing duplicates, handling missing values, formatting columns, etc.
# Remove duplicate rows
# df = df.drop_duplicates()

# Handling missing values (replace NaN values with a specific value)
# df.fillna(0, inplace=True)  # Replace NaN with 0, for example

# Format columns if needed (convert data types, apply functions to columns, etc.)
# For instance, converting a column to datetime format
# df['Date_Column'] = pd.to_datetime(df['Date_Column'])

# Write the cleaned data to a new Excel file
cleaned_file_path = 'Z:\\Sheets\\new_excel_file.xlsx'
df2.to_excel(cleaned_file_path, index=False)  # Set index=False to exclude the index column in the output file
