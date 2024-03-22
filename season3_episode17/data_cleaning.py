import pandas as pd
import os

# Read the table  
raw_df = pd.read_csv("season3_episode17/volunteer_availability.csv") 

# Uppercase column headers
raw_df.columns = raw_df.columns.str.upper()

# Convert the timestamp column to datetime format
raw_df['TIMESTAMP'] = pd.to_datetime(raw_df['TIMESTAMP'])

# Group by volunteer name and get the index of the row with the latest timestamp for each volunteer
latest_indices = raw_df.groupby('VOLUNTEER NAME')['TIMESTAMP'].idxmax()

# Select the rows with the latest timestamp for each volunteer
latest_rows = raw_df.loc[latest_indices]

# Write the latest rows to a new CSV file
clean_df = latest_rows.to_csv("season3_episode17/volunteer_availability_clean.csv", index=False)
print("Latest rows for each volunteer saved successfully.")
