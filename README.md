# schedule_generator
# Summary:
The provided Python script is designed to organize ushers for various shows based on their availability status. Here's a breakdown of its functionality:

__Reading Data__: The script reads a CSV file containing usher availability data from a specified location.

__Data Preprocessing__: It converts the column headers to uppercase for consistency. It takes the latest submission by each usher. 

__Generating Usher Pools__:

The script loops through the columns of the DataFrame, checking if the column name starts with "SHOW".
For each show column:
- It extracts a list of special ushers and available ushers based on their status ("Special" or "Available").
- It combines special and available ushers into a pool.
- It excludes "Person A" and "Person B" as they are not ushers.
- Finally, it limits the pool based on the venue the show is at.

__Output Generation__:

The script prints the generated pools for each show.
It generates a timestamp to create a unique identifier for the output file.
It writes the generated pools to a text file, along with the corresponding show names.

__Error Handling__: The script includes exception handling to catch and print any errors that occur during execution.

__Timestamp__: It includes the current date and time in the filename of the output file for tracking purposes.

__File Structure__: The script assumes a specific file structure and file paths for input and output files


__Dependencies__:

- Python 3.11.8: 
- datetime: The datetime module is used for generating timestamps, which are used for various purposes such as naming files with the current date and time.
- os: The os module is used for file path operations, such as joining directory paths and accessing file system-related functions.
- pandas: The pandas library is used for data manipulation and analysis, particularly for working with tabular data structures like DataFrames.
- random: The random module is used for generating random numbers and performing random selections, as in shuffling lists or selecting random items.
- re: The re module is typically used for regular expression operations, but in the given code snippet, it's not being explicitly utilized. It seems like an oversight or a remnant from previous versions of the code.
  
Author:
Claire Kraft
