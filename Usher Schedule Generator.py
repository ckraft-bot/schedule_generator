import pandas as pd  
import random  

# Read the table  
df = pd.read_csv(r"c:\Users\c17527k\Documents\Volunteer\Usher Schedule v2.csv")  

# Loop through the show columns and generate the volunteer pools  
pools = {}  
for col_name in df.columns:  
    if col_name.startswith("SHOW"):  # Check if column name starts with "SHOW"  
        # Get list of special volunteers for this show 
        special = list(df[df[col_name] == "Special"]["VOLUNTEER NAME"])   
        # Get list of available volunteers for this show  
        volunteers = list(df[(df[col_name] == "Available") | (df[col_name] == "Special")]["VOLUNTEER NAME"])  
        # Combine special and available volunteers  
        pool = special + [v for v in volunteers if v not in special]  
        
        # Check if Chloe and Karen are both in the pool, and regenerate pool if necessary  
        while "Chloe Daugherty" in pool and "Karen Flores" in pool:  
            # Regenerate list of special volunteers  
            special = list(df[df[col_name] == "Special"]["VOLUNTEER NAME"])  
            # Regenerate list of available volunteers 
            volunteers = list(df[(df[col_name] == "Available") | (df[col_name] == "Special")]["VOLUNTEER NAME"])  
            # Combine special and available volunteers 
            pool = special + [v for v in volunteers if v not in special]    
        # Add the pool to the dictionary of pools for each show
        pools[col_name] = pool    

# Print the pools for each show  
for show, pool in pools.items():  
    print(f"{show} on staff: {pool}")  # Print the pool for each show  
