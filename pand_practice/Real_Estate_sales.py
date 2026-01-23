import pandas as pd

df=pd.read_csv('pand_practice/Real_Estate_saless.csv',delimiter=',',parse_dates=[2],date_format={'date added':'%d-%m-%y'})
print(df)

print("the type of the data is ",df.dtypes)
print("the information about the data is",df.info())
print("the first three row is ",df.head(3))
print("the last five rows are ",df.tail(5))

#applying all the statas 
print("all operations of stats ",df.describe())
#the shape of the data is
print("the shape of the data is",df.shape)

# accessing the some specific coloumn
list=df['List Year']
print("the specific coloumn is ",list)

#accessing some other coloumn
SerialNumber=df['Serial Number']
print("the serial number is",SerialNumber)

#accessing the multiple coloumn
list_and_serialnumber=df[['List Year','Serial Number','Date Recorded']]
print("the multiple coloumns are",list_and_serialnumber)

#accessing the single row 
first_row=df.loc[0]
print("the first row is ",first_row)

#selecting the multiple rows
multile_rows=df.loc[[1,2,3]]
print("the multiple rows are",multile_rows)

#selecting a slice of rows 
slice_of_rows=df.loc[1:9]
print('the slice of rows are',slice_of_rows)
#check if there is any missing vallue in my data set
print('the missing values are',df.isnull().sum())
#removing all the missing values
print('after removing all the missing',df.dropna())
#check if there is any missing vallue in my data set
print('the missing values are',df.isnull().sum())