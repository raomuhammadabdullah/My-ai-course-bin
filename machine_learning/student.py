import matplotlib.pyplot as plt
import pandas as pd
import  numpy as np

#accesing the data 

data=pd.read_csv('machine_learning/student_score.csv')
print(data) 

print(data.head())


#By plotting a different graphs 
data.plot.scatter(x='Hours',y='Scores',title='scatterd oh hours and score')
plt.show()

#defining the correlation between the data
result=print('the correlation is',data.corr())

print('the statical operation on the data is ',data.describe())

x=data['Hours']
y=data['Scores']
#reshaapping the data

print('the reshapping of the data is ',data['Hours'].values.reshape(-1,1))


print('the reshapping of the data is ',data['Scores'].values.reshape(-1,1))

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.2)
print(x_train)
print(y_train)

#training the model with regression
from sklearn.linear_model import Lasso
model=Lasso()


#training our model by fit command 

model.fit(x_train,x_test)

print(model.intercept_)
print(model.coef_)



