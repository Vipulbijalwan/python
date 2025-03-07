import pandas as pd

df_customers=pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['RAMESH','Suresh','Mahesh']

})

df_orders = pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmounr':[200,252,739]
})

df_marge=pd.merge(df_customers,df_orders,on='CustomerID',how='inner')

print(df_marge)