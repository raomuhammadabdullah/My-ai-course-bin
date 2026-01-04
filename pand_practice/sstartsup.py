import pandas as pd

df=pd.read_csv('pand_practice/startsup.csv',delimiter=',',parse_dates=[3],date_format={'Date Joined': '%d-%m-%y'})
print(df)

print("different data types",df.dtypes)
print("the information about the data is",df.info())
print("after applying all the stats operations on the data",df.describe())
print('last rhree rows in the data is',df.tail(3))
print('the first three rows in the data is',df.head(3))
print('the shape of the data is',df.shape)
#accessing some specific coloumn
company=df['Company']
print('the specific coloumn i.w comapny is',company)

#accessing multiple coloumns
multiple=df[['Company','Date Joined']]
print("the two coloumnns are",multiple)

#selecting a single row using loc
row=df.loc[0]
print("the first row is",row)
#selecting the multiple rows
multiple_rows=df.loc[[0,1]]
print("the multiple rows are",multiple_rows)

#selecting row using slicing
rows_slice=df[1:5]
print("the slice of row is",rows_slice)

#comditional statement using row
condition=df.loc[df['Valuation ($B)']=='$140']
print("the conditional statement is",condition)


#slecting  a single coloumn 
single_coloumn=df.loc[:1,'ID']
print("the single coloumn is",single_coloumn)

#selecting the multiple coloumnn using loc
multiple_coloumn=df.loc[:1,['Country','City']]
print("the multiple coloumns are",multiple_coloumn)
#selecting  a slice of coloumn
slice_of_coloumn=df.loc[:1,'Country':'City']
print("the slice of coloumn is",slice_of_coloumn)

#combining rows and coloumns by applying the condition
conditional_combination=df.loc[df['ID']==2,'Company':'Date Joined']
print('the combinational rows and coloumn are',conditional_combination)

#loc base on primary key
df_primary_key=pd.read_csv('pand_practice\startsup.csv',delimiter=',',parse_dates=[3],date_format={'Date Joined': '%d-%m-%y'},index_col='ID')
print(df_primary_key)
print("the data type of the data is",df_primary_key.dtypes)
print("appplyng all the stats perations",df_primary_key.describe())
print("the information about the data is",df_primary_key.info())


#selecting  single row using loc
single_row=df_primary_key.loc[1]
print('selecting a second row using loc',single_row)
#selecting a slice of row uing loc
rows=df_primary_key.loc[[1,4]]
print("the slice of row is ",rows)
#slice of row
slice_of_row=df_primary_key.loc[1:4]
print("the slice of row is",slice_of_row)

#conditional selection using loc
condition_selection=df_primary_key.loc[df_primary_key['Company']=='Revolut']
print("the conditional output of specific data is",condition_selection)

#selecting a single coloumn using loc
specific_coloumn=df_primary_key.loc[:7,'Company']
print("the specific elements if specific coloumn are",specific_coloumn)

#selecting the multiple coloumns using loc
multiple_spexific_coloumns=df_primary_key.loc[:7,['Company','Date Joined']]
print("the specific coloumns are",multiple_spexific_coloumns)

#slice_of_coloumn using loc
slice_of_coloumn_loc=df_primary_key.loc[:7,'Company':'Date Joined']
print("the slice of colomns is",slice_of_coloumn_loc)

#combining rows and coloumns
rows_and_coloumns=df_primary_key.loc[df_primary_key['Company']=='SpaceX','Date Joined':'Select Investors']
print('the combination of rows and coloumn are',rows_and_coloumns)

#operations using iloc

row_iloc=df_primary_key.iloc[0]
print("the first row using iloc is",row_iloc)
# taking multiple outputs
multiple_rows_iloc=df_primary_key.iloc[[0,1,2,3]]
print("the multiple coloumns are ",multiple_rows_iloc)

#selecting a slice of rows
slice_of_row_iloc=df_primary_key.iloc[0:3]
print("the slice of coloumns are",slice_of_row_iloc)

#selecting a single coloumn using iloc
single_coloumn_iloc=df_primary_key.iloc[:,2]
print("the single coloumn is ",single_coloumn_iloc)

#selecting a multiple coloumns using iloc

multiple_coloumn_iloc=df_primary_key.iloc[:,[1,2]]
print("the multiple coloumns are",multiple_coloumn_iloc)

#combing rows and coloumns
combining_rows_coloumns_iloc=df_primary_key.iloc[[1,2,3,4],3:5]
print("the combination of rows and coloumns are",combining_rows_coloumns_iloc)

#adding new row in the data 
df.loc[len(df)] = [937, 'Pet Circle', '$1', '12-07-2021', 'Australia', 'Alexandria', 'E-commerce & direct-to-consumer', 'Prysm Capital, Baillie Gifford & Co., TDM Growth Partners']
print(df)

#deleting the row with the specific index
df.drop(936,axis=0,inplace=True)
#deleting the row with last index
df.drop([933,934,935],axis=0,inplace=True)
#deleting the row eith thr indaxes
df.drop(index=931,inplace=True)
print("the modified rows are",df)

#deleting the age coloumn
df.drop('Select Investors',axis=1,inplace=True)
#deleting the coloumn by just telling the coloumn name
df.drop(columns='Industry',inplace=True)
#deleting the multiple coloumn
df.drop(['City','Country'],axis=1,inplace=True)
print('the data after deleting multiple coloumns i.e select investor,industry,city and country ',df)

#renaming data frames
#renamin coloumns names
df.rename(columns={'ID':'Personal id'},inplace=True)
#renaming duffereent cooumn by mapper
df.rename(mapper={'Company':'industry','Valuation ($B)':'Valuation '},axis=1,inplace=True)
print('the modified data frames are',df)
#renamming with the row lable
df.rename({0:7},inplace=True)
#renamming colomns multiple indaxes
df.rename({2:3,4:5},axis=0,inplace=True)
print('modified data frames are ',df)

#applying the different queries on the data
specific_row_query = df.query("industry == 'Bytedance'")
print('the specific row query is',specific_row_query)

#taking the sum of specific coloumns
grouped=df.groupby('industry')['Personal id'].sum()
print(grouped.to_string())
print('grouped by',len(grouped))


#dropping all the rows with missing values
df_cleaner=df.dropna()
print('cleaning of the data is',df_cleaner)

#fillimg all the values with nan numbers 
df.fillna(0,inplace=True)


#python itself array data 
data=[2,3,4,5,66]
array1=pd.array(data)
print(array1)


#creating a pandas 
int_array=pd.array([1,2,3,4,5,6,7],dtype=int)
print(int_array)
print()

