import pandas as pd
import os
import datetime
import re

def generate_pool(df, col_name):
    # Extracting special volunteers and available volunteers
    special = list(df[df[col_name] == "Special"]["VOLUNTEER NAME"])
    available_volunteers = list(df[(df[col_name] == "Available") | (df[col_name] == "Special")]["VOLUNTEER NAME"])

    # Adjusting available volunteers based on special cases (Jim or Dwight)
    if "Jim" in special:
        available_volunteers = [volunteer for volunteer in available_volunteers if volunteer != "Dwight"]
    elif "Dwight" in special:
        available_volunteers = [volunteer for volunteer in available_volunteers if volunteer != "Jim"]

    # Generating the pool of volunteers for the given column
    pool = special[:min(3, len(special))] + available_volunteers[:max(0, 3 - len(special))]
    return pool

def main():
    try:
        # Reading the CSV file containing volunteer availability
        df = pd.read_csv(r"C:\Users\Clair\OneDrive\Documents\Volunteer\volunteer_availability_clean.csv")
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
