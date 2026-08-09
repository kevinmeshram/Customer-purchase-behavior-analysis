import pandas as pd 
import numpy as np
ds = pd.read_csv('data/data.csv' , encoding= 'ISO-8859-1')

print(ds.shape)
print(ds.columns.to_list())
print(ds.dtypes)
print(ds.head(5))
##print(ds.info(True))
print(ds.isnull().sum)
print(ds.describe())