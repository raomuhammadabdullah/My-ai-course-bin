import pandas as pd

df=pd.read_csv('pand_practice/Real_Estate_saless.csv',delimiter=',',parse_dates=[2],date_format={'date added':'%d-%m-%y'})
print(df)

