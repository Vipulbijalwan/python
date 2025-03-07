import pandas as pd

data={
    "Name":["TOM",None,"JHON","HARRY","BARRY","LARRY","GARRY","TERRY"],

    "Age":[25,None,47,22,23,45,78,99],
    "Salary":[45000,None,67000,34000,56000,78000,55000,60000]
}

df=pd.DataFrame(data)
 

 #FILL 0 IN NONE PLACE
# print(df)
# df.fillna(0,inplace=True)
print(df)



 #FILL MEAN VALUE IN NONE PLACE
"""df['Age'].fillna(df["Age"].mean(),inplace=True)
df['Salary'].fillna(df["Salary"].mean(),inplace=True)"""

# Interpolate vaalue

"""

EX- 10,20,nan,40,50

interpolate()

"""


print(df)