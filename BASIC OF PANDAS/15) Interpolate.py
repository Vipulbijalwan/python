import pandas as pd

data={
    "Name":["TOM","Ram","JHON","HARRY","BARRY","LARRY","GARRY","TERRY"],

    "Age":[25,None,47,22,23,45,78,99],
    "Salary":[45000,None,67000,34000,56000,78000,55000,60000]
}

df=pd.DataFrame(data)

"""
1- time series data
2- numeric data 
3-avoid dropping rows
"""

df.interpolate(method="linear",axis=0,inplace=True)
print(df)