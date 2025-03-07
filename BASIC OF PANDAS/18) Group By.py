import pandas as pd

data={
    "Name":["TOM","JHON","HARRY","BARRY","LARRY","GARRY","TERRY"],

    "Age":[25,99,22,23,99,78,99],
    "Salary":[45000,67000,34000,56000,78000,55000,60000]
}

df=pd.DataFrame(data)

gp=df.groupby('Age')['Salary'].sum()
print(gp)