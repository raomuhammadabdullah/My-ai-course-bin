# Import required libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# Load the dataset
df = pd.read_csv("final Assignmenet\ lottery_dataset.csv")

# Convert True/False values into numeric values
df = df.replace({True:1, False:0})

# Define the target variable
y = df["targetTrend"]

# Define input features
X = df.drop(["targetTrend","DrawId"], axis=1)

# Fill missing values
X = X.fillna(0)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Normalize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build the neural network
model = Sequential()

model.add(Dense(32, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(16, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(
    optimizer='adam',
    loss='mean_squared_error'
)

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32)

# Make predictions
predictions = model.predict(X_test)

print(predictions[:5])