"""
1- SELECT SPECIFIC COLUMANS
2- FILTER ROWS
3-COMBINE MULTIPLE CONDITIONS


1-SQUARE BRACKETS
2- BOOLEAN CONDITIONS

SELECTING COLOUMNS
1- A SERIES
2- A DATAFRAME MULTIPLE COLUMNS


COLUMN=DF['COLOUMN_NAME']
SUBSET=DF['COLOUMN_NAME1','COLOUMN_NAME2']


FILTERING ROWS
1- BOOLEAN INDEXING

#SINGLE CONDITION
FILTER_ROWS=DF[DF['COLOUMN_NAME]>100000]

#MULTIPLE CONDITIONS
FILTER_ROWS=DF[{DF['SALARY]>50000}& {DF['COLOUM2]<80000}]
"""

import pandas as pd

data={
    "Name":["TOM","NICK","JHON","HARRY","BARRY","LARRY","GARRY","TERRY"],

    "Age":[25,35,47,22,23,45,78,99],
    "Salary":[45000,23000,67000,34000,56000,78000,55000,60000]
}

df=pd.DataFrame(data)

print(df)

print("Names (single column)")
print(df['Name'])

subset=df[['Name','Salary']]
print("Subset (multiple coloumns)")
print(subset) 