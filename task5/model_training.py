import streamlit as st
import pandas as pd
import joblib

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix



print("\nLoading Dataset...")

data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

print("Dataset Shape:", X.shape)



print("\nApplying Standard Scaling...")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)



X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.20,
    random_state=42
)

print("Training Samples:", len(X_train))
print("Testing Samples :", len(X_test))


print("\nTraining Random Forest Model...")

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

rf_accuracy = accuracy_score(y_test, rf_predictions)

print("\nRandom Forest Accuracy:")
print(round(rf_accuracy * 100, 2), "%")



dt_model = DecisionTreeClassifier(random_state=42)

dt_model.fit(X_train, y_train)

dt_pred = dt_model.predict(X_test)

dt_accuracy = accuracy_score(y_test, dt_pred)



knn_model = KNeighborsClassifier()

knn_model.fit(X_train, y_train)

knn_pred = knn_model.predict(X_test)

knn_accuracy = accuracy_score(y_test, knn_pred)



lr_model = LogisticRegression(max_iter=1000)

lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)

lr_accuracy = accuracy_score(y_test, lr_pred)



print("\n===================================")
print("MODEL COMPARISON")
print("===================================")

print("Decision Tree       :", round(dt_accuracy * 100, 2), "%")
print("KNN                 :", round(knn_accuracy * 100, 2), "%")
print("Logistic Regression :", round(lr_accuracy * 100, 2), "%")
print("Random Forest       :", round(rf_accuracy * 100, 2), "%")



print("\n===================================")
print("CLASSIFICATION REPORT")
print("===================================")

print(classification_report(y_test, rf_predictions))



print("\n===================================")
print("CONFUSION MATRIX")
print("===================================")

print(confusion_matrix(y_test, rf_predictions))



joblib.dump(rf_model, "random_forest_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("\nModel Saved Successfully!")
print("Files Created:")
print("1. random_forest_model.pkl")
print("2. scaler.pkl")