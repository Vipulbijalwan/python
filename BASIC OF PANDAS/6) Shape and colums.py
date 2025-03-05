"""
1- HOW BIG IS THE DATASET?
2- WHAT IS THE NAMES OF THE COLUMNS?


SHAPE AND COLUMNS
"""
import pandas as pd

data={
    "Name":["TOM","NICK","JHON","HARRY","BARRY","LARRY","GARRY","TERRY"],

    "Age":[25,35,47,22,23,45,78,99],
    "Salary":[45000,23000,67000,34000,56000,78000,55000,60000]
}

df=pd.DataFrame(data)

print(f'Shape: {df.shape}')
print(f'Columns: {df.columns}')