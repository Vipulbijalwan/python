"""
1. PROBLEM WITH DATASET
    1.1. MISSING DATA
    1.2. TYPES OF MISSING DATA
    1.3. HANDLING MISSING DATA

METHOD TO SOLVE IT:
- `df.info()`
    1. Number of rows and columns
    2. Column names
    3. Number of non-null values
    4. Data types of each column
    5. Memory usage
"""

import pandas as pd

# Load JSON file into a DataFrame
df = pd.read_json("sample_data.json")

# Display dataset information
print("DISPLAY INFO")
df.info()  # No need to print(df.info()), as info() already prints the output
