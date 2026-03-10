import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Small dataset
data = {
    "Work_Hours": [35, 40, 45, 50, 30, 60, 55, 42],
    "Overtime": [0, 0, 1, 1, 0, 1, 1, 0]  # 1 = yes overtime, 0 = no
}
df = pd.DataFrame(data)

X = df[["Work_Hours"]]
y = df["Overtime"]

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, train_size=0.7, random_state=25)

# Models
logistic_regression = LogisticRegression()
svm = SVC()
tree = DecisionTreeClassifier()

# Train
logistic_regression.fit(X_train, y_train)
svm.fit(X_train, y_train)
tree.fit(X_train, y_train)

# Predict
preds = {
    "Logistic Regression": logistic_regression.predict(X_test),
    "SVM": svm.predict(X_test),
    "Decision Tree": tree.predict(X_test)
}

# Evaluate
for model, y_pred in preds.items():
    print(f"{model} Results:\n{classification_report(y_test, y_pred)}\n")