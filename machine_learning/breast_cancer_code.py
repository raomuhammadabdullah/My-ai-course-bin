import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Load dataset
cancer_data = load_breast_cancer()
cancer_df = pd.DataFrame(cancer_data.data, columns=cancer_data.feature_names)
cancer_df["target"] = cancer_data.target


print(cancer_df.head())
print(cancer_df.info())
print(cancer_df.describe())

# Split features and target
X = cancer_df[cancer_data.feature_names].copy()
y = cancer_df["target"].copy()

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X.values)

# Split train/test
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

# Predictions
preds = {
    "Logistic Regression": logistic_regression.predict(X_test),
    "SVM": svm.predict(X_test),
    "Decision Tree": tree.predict(X_test)
}

# Evaluation
for model, y_pred in preds.items():
    print(f"{model} Results:\n{classification_report(y_test, y_pred)}\n")