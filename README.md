# schedule_generator
# Summary:
The provided Python script is designed to organize volunteers for various shows based on their availability status. Here's a breakdown of its functionality:

__Reading Data__: The script reads a CSV file containing volunteer availability data from a specified location.

__Data Preprocessing__: It converts the column headers to uppercase for consistency. It takes the latest submission by each volunteer. 

__Generating Volunteer Pools__:

The script loops through the columns of the DataFrame, checking if the column name starts with "SHOW".
For each show column:
- It extracts a list of special volunteers and available volunteers based on their status ("Special" or "Available").
- It combines special and available volunteers into a pool.
- It checks If both "Person A" and "Person B" are in the pool, it regenerates the pool to ensure they are not together.
- Finally, it limits the pool to only the first three volunteers.

__Output Generation__:

The script prints the generated pools for each show.
It generates a timestamp to create a unique identifier for the output file.
It writes the generated pools to a text file, along with the corresponding show names.

__Error Handling__: The script includes exception handling to catch and print any errors that occur during execution.

__Timestamp__: It includes the current date and time in the filename of the output file for tracking purposes.

__File Structure__: The script assumes a specific file structure and file paths for input and output files


Dependencies:
- pandas: Used for data manipulation and analysis.
- os: Used for file path operations.
- datetime: Used for generating timestamps.
  
Author:
Claire Kraft
