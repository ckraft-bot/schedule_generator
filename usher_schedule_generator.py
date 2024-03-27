import pandas as pd
import os
import datetime
import re
import random

def generate_pool(df, col_name):
    # Extracting special volunteers and available volunteers - excluding humans A and B from the pool as they are not ushers
    special = list(df[(df[col_name] == "Special") & (~df["USHER NAME"].isin(["Human A", "Human B"]))]["USHER NAME"])
    available = list(df[(df[col_name] == "Available") & (~df["USHER NAME"].isin(["Human A", "Human B"]))]["USHER NAME"])

    # Define pool size based on header
    if "VENUE A" in col_name.upper():
        pool_size = 7
    elif "VENUE B" in col_name.upper():
        pool_size = 25
    else:
        # the difference between the small and big theatre/venue
        pool_size = 18 

    # Initialize the pool with special volunteers
    pool = special[:min(pool_size, len(special))]
    
    # Determine the number of available volunteers needed to fill the remaining spots
    remaining_spots = pool_size - len(pool)
    
    # Shuffle the available volunteers list
    random.shuffle(available)
    
    # Add available volunteers to the pool to fill the remaining spots
    pool.extend(available[:remaining_spots])
    
    return pool

def main():
    try:
        # Reading the CSV file containing volunteer availability
        df = pd.read_csv(r"<path>data_clean.csv")
        df.columns = df.columns.str.upper()
        pools = {}

        # Generating pools for each column starting with "SHOW"
        for col_name in df.columns:
            if col_name.startswith("SHOW"):
                pools[col_name] = generate_pool(df, col_name)

        # Generating timestamp for the filename
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = f"results_{timestamp}.txt"

        # Writing the modified data to the file
        with open(file_path, "w") as f:
            f.write("Results:\n")
            for show, pool in pools.items():
                # Removing square brackets and single quotes around the names using regex
                pool = ", ".join([re.sub(r"'([^']*)'", r"\1", name) for name in pool])
                f.write(f"{show} on staff: [{pool}]\n")

        print("Results written successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
