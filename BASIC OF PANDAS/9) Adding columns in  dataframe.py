import pandas as pd

data={
    "Name":["TOM","NICK","JHON","HARRY","BARRY","LARRY","GARRY","TERRY"],

    "Age":[25,35,47,22,23,45,78,99],
    "Salary":[45000,23000,67000,34000,56000,78000,55000,60000]
}

df=pd.DataFrame(data)
print(df)
df["Bonus"]=df["Salary"]*0.1
print(df)

df.insert(0, "Id",[1,2,3,4,5,6,7,8])
print(df)