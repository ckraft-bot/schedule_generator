import pandas as pd
import os

# Read the table  
raw_df = pd.read_csv(r"<path>\data.csv") 

# Uppercase column headers
raw_df.columns = raw_df.columns.str.upper()

# Convert the timestamp column to datetime format
raw_df['TIMESTAMP'] = pd.to_datetime(raw_df['TIMESTAMP'])

# Group by  usher name and get the index of the row with the latest timestamp for each volunteer
latest_indices = raw_df.groupby('USHER NAME')['TIMESTAMP'].idxmax()

# Select the rows with the latest timestamp for each volunteer
latest_rows = raw_df.loc[latest_indices]

# Write the latest rows to a new CSV file
clean_df = latest_rows.to_csv(r"<path>\data_clean.csv", index=False)
print("Latest rows for each volunteer saved successfully.")

import pandas as pd

# Comparing row counts
# raw_df_row = len(raw_df)
# clean_df_row_count = len(clean_df)
# print(f"Number of rows in the original table: {raw_df_row} vs the clean table: {clean_df_row_count}")
