#CHECK ROWS 
#HEAD() TAIL()

import pandas as pd

df=pd.read_json("sample_data.json")
print("FIRST 10 ROWS")
print(df.head(10))

print("LAST 10 ROWS")
print(df.tail(10))