import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("The Titanic dataset.csv", skiprows=1)

df = df.drop_duplicates()

df["age"] = df["age"].replace("?", np.nan)
df["fare"] = df["fare"].replace("**", np.nan)

df["age"] = pd.to_numeric(df["age"])
df["fare"] = pd.to_numeric(df["fare"])

df["age"] = df["age"].fillna(df["age"].median())
df["fare"] = df["fare"].fillna(df["fare"].median())
df["gender"] = df["gender"].fillna(
    df["gender"].mode()[0]
) 
df["embarked"] = df["embarked"].fillna(
    df["embarked"].mode()[0]
)  

df = pd.get_dummies(df, columns=["gender", "embarked"], drop_first=True)

feature_cols = [
    "pclass",
    "age",
    "family",
    "fare",
    "gender_male",
    "embarked_Q",
    "embarked_S",
]
X = df[feature_cols]
y = df["survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

print("--- Model Evaluation ---")
print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.4f}\n")
print("Classification Report:")
print(classification_report(y_test, y_pred))