import pandas as pd  
import os
import datetime


def main():
    try:
        # Read the table  
        df = pd.read_csv(r"<path>\clean_show_availability.csv") 
        # Uppercase column headers
        df.columns = df.columns.str.upper()
        print(df.head())
        # Loop through the show columns and generate the volunteer pools  
        pools = {}  
        for col_name in df.columns:  
            # Check if column name starts with "SHOW"  
            if col_name.startswith("SHOW"):  
                # Get list of special volunteers for this show 
                special = list(df[df[col_name] == "Special"]["VOLUNTEER NAME"])   
                # Get list of available volunteers for this show  
                available_volunteers = list(df[(df[col_name] == "Available") | (df[col_name] == "Special")]["VOLUNTEER NAME"])  
                # Combine special and available volunteers  
                pool = special + available_volunteers
                
                # Check if Jim and Dwight are both in the pool, and regenerate pool if necessary  
                while "Jim" in pool and "Dwight" in pool:  
                    # Regenerate list of special volunteers  
                    special = list(df[df[col_name] == "Special"]["VOLUNTEER NAME"])  
                    # Regenerate list of available volunteers 
                    available_volunteers = list(df[(df[col_name] == "Available") | (df[col_name] == "Special")]["VOLUNTEER NAME"])  
                    # Combine special and available volunteers 
                    pool = special + available_volunteers

                # Take only the first 3 volunteers in the pool
                pool = pool[:3]

                # Add the pool to the dictionary of pools for each show
                pools[col_name] = pool  
        
        # Print the pools for each show  
        for show, pool in pools.items():  
            print(f"{show} on staff: {pool}")  # Print the pool for each show  
        
        # Write the pools for each show  
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print(f"The current datetime: {timestamp}")

        # Write and save in this location
        file_path = f"<path>\results_{timestamp}.txt"

        # Open a file to write results
        with open(file_path, "w") as f:
            print("Writing results to file...")
            for show, pool in pools.items():  
                # Write the pool for each show  
                f.write(f"{show} on staff: {pool}\n")

        print("Results written successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
