import pandas as pd
import os
import datetime

"""
Excludes "Jim" and "Dwight" from being selected together for the same show.
Prioritizes selecting "Special" volunteers first for each show.
Writes the results to a text file with a timestamp in the filename.
Removed unnecessary imports and variables.
"""

def generate_pool(df, col_name):
    special = list(df[df[col_name] == "Special"]["VOLUNTEER NAME"])
    available_volunteers = list(df[(df[col_name] == "Available") | (df[col_name] == "Special")]["VOLUNTEER NAME"])

    # Exclude Dwight if Jim is in the pool, and vice versa
    if "Jim" in special:
        available_volunteers = [volunteer for volunteer in available_volunteers if volunteer != "Dwight"]
    elif "Dwight" in special:
        available_volunteers = [volunteer for volunteer in available_volunteers if volunteer != "Jim"]

    # Select volunteers for the show, prioritize special volunteers
    pool = special[:min(3, len(special))] + available_volunteers[:max(0, 3 - len(special))]
    return pool


def main():
    try:
        # Read the table
        df = pd.read_csv("clean_show_availability.csv")
        # Uppercase column headers
        df.columns = df.columns.str.upper()

        # Initialize pools dictionary
        pools = {}

        # Loop through the show columns and generate the volunteer pools
        for col_name in df.columns:
            if col_name.startswith("SHOW"):
                pools[col_name] = generate_pool(df, col_name)

        # Print the pools for each show
        for show, pool in pools.items():
            print(f"{show} on staff: {pool}")

        # Write the pools for each show to a file
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = f"results_{timestamp}.txt"

        with open(file_path, "w") as f:
            f.write("Results:\n")
            for show, pool in pools.items():
                f.write(f"{show} on staff: {pool}\n")

        print("Results written successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
