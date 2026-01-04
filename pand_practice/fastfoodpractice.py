import pandas as pd

df = pd.read_csv('pand_practice/fastfood.csv',delimiter=",")
print(df)
print("df data types ",type(df))
print("df data type",df.dtypes)
print("the information about df",df.info())

# displaying the last five rows
print(df.tail(5))
print("the  five rows are",df.tail(5))

#displaying first 5 heads are
print(df.head(5))
print("the first five heads are",df.head(5))

#summary of the data and applying all operations on data 
print("the all statics functions on data ",df.describe())
print("the mean of lattude is",df.mean(axis=0,numeric_only=True,))

#shape of the data like it will count the 
print("the shape of the data is ",df.shape)
#accessing some specific coloumn
specific_coloumn=df['province']
print("the some dpecific coloumn is",specific_coloumn)
print()

#accessing the multiple coloumns
multiple_coloumns=df[['address','city']]
print(" multiple coloumns are",multiple_coloumns)
print()

# selecting a single row n the data 
first_row=df.loc[0]
print("the first row is",first_row)
#selecting  a multiplr rows
multiple_rows=df.loc[[0,4]]
print("the multiple rows are ",multiple_rows)

#selecting  a slice of rows
slice_of_rows=df.loc[1:5]
print("the slice of row is ",slice_of_rows)

#conditional selecting of rows
conditiona_row=df.loc[df['city']=='Ashland']
print("conditional selecting of row is",conditiona_row)
print()

conditiona_row_2=df.loc[df['address']=='324 Main St']
print("conditional row is",conditiona_row_2)
print()

#selecting a siingle column usng loc 
single_coloumn=df.loc[:4,'address']
print("single coloumn is ",single_coloumn)
print()

#selectng multiple columns
multiple_coloumns_data=df.loc[:4,['address','city']]
print("multiple coloumns are",multiple_coloumns_data)

#combining rows and coloumns 
rows_coloumns=df.loc[df['address']=='324 Main St','keys':'province']
print("the combination of rows and colomns are",rows_coloumns)

#cae 2: using loc with primary key
df_primarykey_col=pd.read_csv('pand_practice/fastfood.csv',delimiter=",",index_col='longitude')
print("the primary key indexing method",df_primarykey_col)
print(df_primarykey_col.dtypes)
print(df_primarykey_col.info())

#selecting a single row
row=df_primarykey_col.loc[-82.097280]
print("the single row is ",row)

#selecting multiple rows using loc
rows=df_primarykey_col.loc[[-105.101720 ,-116.482150 ]]
print("the multiplr rows are",rows)

#slice of row 
slice_row=df_primarykey_col.loc[-74.845530 :-116.482150]
print("slice of row is ",slice_row)

#conditional selection of rows using .loc
conditional=df_primarykey_col.loc[df_primarykey_col['address']=='6098 State Highway 37']
print("the  electing of rows are",conditional)


#slecting a single coloumn using loc
single_coloumnn=df.loc[:1,'city']
print("the single coloumn is ",single_coloumnn)

#slecting multiple coloumns 
multiple_coloumnss=df.loc[:1,['city','country']]
print("the multiple coloumn are",multiple_coloumnss)


#121
#selecting  multiple columns of address and city
multiple_rows_of_coloumn=df.loc[:1,['address','city']]
print("the multiple columns are",multiple_rows_of_coloumn)

#selecting a slice of coloumn
slice_of_coloumn=df_primarykey_col.loc[-105.101720 :-116.482150 ]
print("the slice of coloumn is",slice_of_coloumn)

#combining rows and coloumn using loc
rows_coloumns_using_loc=df_primarykey_col.loc[df_primarykey_col['city']=='Massena','address':'postalCode']
print("the combimation of multiple rows and coloumns are",rows_coloumns_using_loc)

#case 3 
#using iloc-indexing method
# selecting a single row using iloc 
single_row=df.iloc[0]
print("the  1 row is ",single_row) 

# selecting a multiple rows using iloc
multiple_rows_iloc=df.iloc[[0,1,2,3]]
print("the multiple rows are",multiple_rows_iloc)
print()

#slicing of the data 
slice_of_data=df.iloc[3:9]
print("the slice of the data is",slice_of_data)
print()

#selecing a single coloumn using iloc
single_coloumn_iloc=df.iloc[:,2]
print("the single colomn is",single_coloumn_iloc)
print()

#selecting a multiple coloumn using iloc 
multiple_coloum_using_iloc=df.iloc[:,[2,4]]
print("the multipl  coloumn using iloc is",multiple_coloum_using_iloc)
print()
#selecting a slice of coloumn using iloc
slice_of_coloumn_iloc=df.iloc[:,2:4]
print("the slice of coloumn is",slice_of_coloumn_iloc)
print()

#combining rows and coloumns combine
rows_coloumns_combine=df.iloc[[0,2,3],2:5]
print("the combination of rws and coloumns are ",rows_coloumns_combine)
print()

# adding new row in the data 
df.loc[len(df.index)]=['504 nishter colony','lahore','pakistan','pakistan/lahore/504..',65678,-6787,'pizzahat',655677,'ny','www.pizzahut.com']
print('the new row is',df) 

#removing rows and coloumns from pandas
#removing first row

df.drop(1,axis=0,inplace=True)
#deleting rows with indexes
df.drop(index=2,axis=0,inplace=True)
#deleting rows with index 3 and 5
df.drop([3,5],axis=0,inplace=True)
print("the rows after modifying is",df)

#applying delete operations on coloumns
df.drop('address',axis=1,inplace=True)
#deleting coloumn without telling the axis 
df.drop(columns='city',inplace=True)
#deleting multiples coloumns
df.drop(['country','keys'],axis=1,inplace=True)
print("modified fata frames are",df)

#renaming coloumns names 
df.rename(columns={'name':'first name'},inplace=True)
#renamming multiple coloumn
df.rename(mapper={'address':'first address','city':'place'},axis=1,inplace=True)
print("the data after modificattion is",df)

#renaming the coloumn name 
df.rename(index={5:6},inplace=True)

#renaming the multiple coloumns name
df.rename(mapper={1:10,11:2},axis=0,inplace=True)
print("the data after modificaton is",df)


#appllying different queries on data
select_rows=df.query('websites== \'http://mcdonalds.com,http://www.mcdonalds.com/?cid=RF:YXT_FM:TP::Yext:Referral\'or latitude>44.9213')
print("the specific row is",select_rows.to_string())
print(len(select_rows))

#sorting of data frame in ascending order
sorting_data=df.sort_values(by='longitude')
print(sorting_data.to_string(index=False))

#calculation of sum for each category
#grouped=df.groupby('longitude')['Keys'].sum()
#print(grouped.to_string())
#print('groupped',len(grouped))

#udinf dropna to remove rows with any missing values
df_cleaner=df.dropna()
print("the data fter cleaning process is",df_cleaner)

#filling nan with 0
df.fillna(0,inplace=True)
print("the data after clenaing is",df)


#python bulid in array
data=[2,3,4,5]
array1=pd.array(data)
print("the data is",array1)

int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()


