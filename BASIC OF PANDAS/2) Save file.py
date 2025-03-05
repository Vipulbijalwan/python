import pandas as pd

data={
    "Name":["Tom","Nick","Jhon","Barry"],
    "Age":[25,35,47,22],
    "City":["NY","LA","SF","DC"]
}

df=pd.DataFrame(data)

print(df)

df.to_csv("output.csv",index=False)