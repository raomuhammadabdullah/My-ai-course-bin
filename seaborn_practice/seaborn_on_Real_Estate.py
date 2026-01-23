import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

record=pd.DataFrame({'x':np.arange(100),'y':np.random.rand(100).cumsum()})
print(record)

#setting the theme 
sns.set_theme(style="darkgrid")
sns.lineplot(x='x',y='y',data=record)
plt.show()

#selecting the theme dark
sns.set_theme(style='dark')
sns.histplot(x='x',y='y',data=record)
plt.show()
#setting the theme white 
sns.set_theme(style='white')
sns.scatterplot(x='x',y='y',data=record)
plt.show()
#setting the theme thick
sns.set_theme(style='ticks')
sns.scatterplot(x='x',y='y',data=record)
plt.show()

#customizing the theme further
sns.set_theme(style='dark',rc={'axes.facecolor':'orange','grid.color':'black'})
#creating a plot
sns.lmplot(x='x',y='y',data=record)
plt.show()

#loading the data in data frame 

df=pd.read_csv('pand_practice/startsup.csv',delimiter=',',parse_dates=[3],date_format={'Date Joined': '%d-%m-%y'})
print(df.dtypes)
head=df.head(100)
tail=df.tail(50)

sns.set_theme(style='whitegrid')
h=sns.displot(data=df,x='ID',hue='Valuation ($B)',kind='hist')
h.figure.suptitle("sns.displot(data=dffilter, x=ID , hue=Valuation ($B),  kind='hist'  )"  )
h.figure.show()

sns.set_theme(style='white')
d=sns.FacetGrid(data=df,col='Company',hue='Country')
h.figure.show()








