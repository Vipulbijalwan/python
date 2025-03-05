import pandas as pd

data={
    "Name":["TOM","NICK","JHON","HARRY","BARRY","LARRY","GARRY","TERRY"],

    "Age":[25,35,47,22,23,45,78,99],
    "Salary":[45000,23000,67000,34000,56000,78000,55000,60000]
}

df=pd.DataFrame(data)
 
print(df)

df.loc[0:3,'Salary']=900000
print(df)

df['Salary']=df['Salary']*1.05
print(df)