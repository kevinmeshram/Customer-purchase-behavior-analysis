import pandas as pd 

df = pd.read_csv('data/data.csv' , encoding='ISO-8859-1')

print(df.shape)
print(df.columns.to_list())
print(df.head(5))

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
print(df.shape)
df= df.dropna(subset=['CustomerID'])
df = df[df['Quantity'] >0]
df = df[df['UnitPrice'] >0]
df['TotalValue']=df['Quantity']*df['UnitPrice']
df['InvoiceDay'] = df['InvoiceDate'].dt.day
df['InvoiceMonth'] = df['InvoiceDate'].dt.month
print(df.shape)
print(df['CustomerID'].nunique())
print(df['Country'].nunique())
print(df.nunique())
print(df.describe())
print(df['CustomerID'].isnull().sum())
print((df['Quantity'] <= 0).sum())   # Should be 0 if filtered correctly
print((df['UnitPrice'] <= 0).sum())
