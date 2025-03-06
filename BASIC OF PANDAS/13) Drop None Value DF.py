import pandas as pd

data={
    "Name":["TOM",None,"JHON","HARRY","BARRY","LARRY","GARRY","TERRY"],

    "Age":[25,None,47,22,23,45,78,99],
    "Salary":[45000,None,67000,34000,56000,78000,55000,60000]
}

df=pd.DataFrame(data)
 
print(df)

df.dropna(inplace=True)
print(df)