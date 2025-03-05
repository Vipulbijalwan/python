import pandas as pd

data={
    "Name":["TOM","NICK","JHON","HARRY","BARRY","LARRY","GARRY","TERRY"],

    "Age":[25,35,47,22,23,45,78,99],
    "Salary":[45000,23000,67000,34000,56000,78000,55000,60000]
}

df=pd.DataFrame(data)

high_salary=df[df["Salary"]>40000]

print(high_salary)

high_salary=df[(df["Salary"]>40000)&(df['Age']>30)]


print(high_salary)