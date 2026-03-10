import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Load dataset
diabetes_data = load_diabetes()
diabetes_return_X_y = load_diabetes(return_X_y=True)
diabetes_as_frame = load_diabetes(as_frame=True)

print("diabetes_return_X_y:", diabetes_return_X_y)
print("diabetes_as_frame:", diabetes_as_frame)

# Convert to DataFrame
diabetes_df = pd.DataFrame(diabetes_data.data, columns=diabetes_data.feature_names)
diabetes_df["target"] = diabetes_data.target

# Convert target to classification (high or low)
diabetes_df["target_class"] = (diabetes_df["target"] > diabetes_df["target"].median()).astype(int)

X = diabetes_df[diabetes_data.feature_names].copy()
y = diabetes_df["target_class"].copy()

# Standardize
scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X.values)
print("First row scaled:", X_scaled[0])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, train_size=0.7, random_state=25
)

# Models
logistic_regression = LogisticRegression(max_iter=5000)
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