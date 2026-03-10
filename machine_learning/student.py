#practice of machine learning on small data sets for better understanding
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#accessing the data by using  pandas
df=pd.read_csv('machine_learning/student_score.csv')
print(df)

#first 5 values from data
print(df.head())
#printing the last 5 values from data
print(df.tail())
#the shape of the data
print(df.shape)
#plotting a graph
df.plot.scatter(x='Hours',y='Scores',title='Scattere plot on x and y');
plt.show()

#correlation between the data
print(df.corr())

#applying the all statical functions on data 
print(df.describe())

#applying machine learning 
from sklearn.linear_model import LinearRegression
regression=LinearRegression()




regression.fit(X_train, y_train)
#If no errors are thrown - the regression found the best fitting line! The line is defined by our features and the intercept/slope. In fact, we can inspect the intercept and slope by printing the regression.intecept_ and regression.coef_ attributes, respectively:

print(regression.intercept_)

#For retrieving the slope (which is also the coefficient of x):

print(regression.coef_)

"""
Making Predictions
To avoid running calculations ourselves, we could write our own formula that calculates the value:
"""
def calc(slope, intercept, hours):
    return slope*hours+intercept

score = calc(regression.coef_, regression.intercept_, 9.5)
print(score) # [[94.80663482]]

#However - a much handier way to predict new values using our model is to call on the predict() function:

# Passing 9.5 in double brackets to have a 2 dimensional array
score = regression.predict([[9.5]])
print(score) # 94.80663482

""""Our result is 94.80663482, or approximately 95%. Now we have a score percentage estimate for each and every hour we can think of. But can we trust those estimates? In the answer to that question is the reason why we split the data into train and test in the first place. Now we can predict using our test data and compare the predicted with our actual results - the ground truth results."""

#To make predictions on the test data, we pass the X_test values to the predict() method. We can assign the results to the variable y_pred:

y_pred = regression.predict(X_test)
#The y_pred variable now contains all the predicted values for the input values in the X_test. We can now compare the actual output values for X_test with the predicted values, by arranging them side by side in a dataframe structure:

df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)

#Though our model seems not to be very precise, the predicted percentages are close to the actual ones. Let's quantify the difference between the actual and predicted values to gain an objective view of how it's actually performing.


"""
https://scikit-learn.org/stable/api/sklearn.metrics.html

sklearn.metrics
Score functions, performance metrics, pairwise metrics and distance computations.

Luckily, we don't have to do any of the metrics calculations manually. The Scikit-Learn package already comes with functions that can be used to find out the values 
of these metrics for us. Let's find the values for these metrics using our test data. First, we will import the necessary modules for calculating the MAE and MSE errors. Respectively, the mean_absolute_error and mean_squared_error:
"""
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
"""Now, we can calculate the MAE and MSE by passing the y_test (actual) and y_pred (predicted) to the methods. The RMSE can be calculated by taking the square root of 
the MSE, to to that, we will use NumPy's sqrt() method:
"""
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
#We will also print the metrics results using the f string and the 2 digit precision after the comma with :.2f:

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')


