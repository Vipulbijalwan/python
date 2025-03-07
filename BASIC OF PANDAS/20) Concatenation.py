import pandas as pd

df_customers=pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['RAMESH','Suresh','Mahesh']

})

df_orders = pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmounr':[200,252,739]
})

df_con=pd.concat([df_customers,df_orders],axis=0,ignore_index=True)
print(df_con)