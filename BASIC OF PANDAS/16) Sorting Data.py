import pandas as pd

data={
    "Name":["TOM","JHON","HARRY","BARRY","LARRY","GARRY","TERRY"],

    "Age":[25,47,22,23,45,78,99],
    "Salary":[45000,67000,34000,56000,78000,55000,60000]
}

df=pd.DataFrame(data)

df.sort_values(by='Age',inplace=True)
print(df)