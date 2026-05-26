import pandas as pd

df = pd.read_csv('gender.csv')

print(df.head())
print("\n--- Info ---")
print(df.info())
Gender   Age   Height (cm)   Weight (kg)             Occupation      Education Level  Marital Status   Income (USD)  Favorite Color  Unnamed: 9
0     male    32           175            70      Software Engineer      Master's Degree         Married          75000            Blue         NaN
1     male    25           182            85   Sales Representative    Bachelor's Degree          Single          45000           Green         NaN
2   female    41           160            62                 Doctor     Doctorate Degree         Married         120000          Purple         NaN
3     male    38           178            79                 Lawyer    Bachelor's Degree          Single          90000             Red         NaN
4   female    29           165            58       Graphic Designer   Associate's Degree          Single          35000          Yellow         NaN

--- Info ---
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 131 entries, 0 to 130
Data columns (total 10 columns): 
---  ------            --------------  -----  
 0    Gender           131 non-null    object 
 1    Age              131 non-null    int64  
 2    Height (cm)      131 non-null    int64  
 3    Weight (kg)      131 non-null    int64  
 4    Occupation       131 non-null    object 
 5    Education Level  131 non-null    object 
 6    Marital Status   131 non-null    object 
 7    Income (USD)     131 non-null    int64  
 8    Favorite Color   131 non-null    object 
 9   Unnamed: 9        0 non-null      float64
dtypes: float64(1), int64(4), object(5)
memory usage: 10.4+ KB
None

Python
df.columns = df.columns.str.strip()

print("Unique genders:", df['Gender'].unique())
print("Value counts:\n", df['Gender'].value_counts())


Code output
Unique genders: [' male' ' female' 'male' 'female']
Value counts:
 Gender
male       41
female     39
 male      27
 female    24
Name: count, dtype: int64

Python
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip()

print("Unique genders after cleaning:", df['Gender'].unique())
print("Value counts:\n", df['Gender'].value_counts())
print("\nMissing values:\n", df.isnull().sum())

Code output
Unique genders after cleaning: ['male' 'female']
Value counts:
 Gender
male      68
female    63
Name: count, dtype: int64

Missing values:
 Gender               0
Age                  0
Height (cm)          0
Weight (kg)          0
Occupation           0
Education Level      0
Marital Status       0
Income (USD)         0
Favorite Color       0
Unnamed: 9         131
dtype: int64

Python
print("Education Level unique values:", df['Education Level'].unique())
print("Marital Status unique values:", df['Marital Status'].unique())
print("Occupation unique values count:", df['Occupation'].nunique())
print("Favorite Color unique values count:", df['Favorite Color'].nunique())

Code output
Education Level unique values: ["Master's Degree" "Bachelor's Degree" 'Doctorate Degree'
 "Associate's Degree"]
Marital Status unique values: ['Married' 'Single' 'Divorced' 'Widowed']
Occupation unique values count: 19
Favorite Color unique values count: 9

Python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df.columns = df.columns.str.strip()
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip()

if 'Unnamed: 9' in df.columns:
    df = df.drop(columns=['Unnamed: 9'])

X = df[['Age', 'Height (cm)', 'Weight (kg)', 'Income (USD)', 'Education Level', 'Marital Status']]
X = pd.get_dummies(X, drop_first=True)

y = df['Gender'].map({'male': 1, 'female': 0})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.fit(X_train_scaled, y_train).predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=['female', 'male']))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

Code output
Accuracy: 0.9630

Classification Report:
               precision    recall  f1-score   support

      female       1.00      0.92      0.96        13
        male       0.93      1.00      0.97        14

    accuracy                           0.96        27
   macro avg       0.97      0.96      0.96        27
weighted avg       0.97      0.96      0.96        27


Confusion Matrix:
 [[12  1]
 [ 0 14]]

Here is the complete Python code to perform Logistic Regression on your dataset (gender.csv) to predict the Gender column based on other characteristics like age, height, weight, income, education level, and marital status.

Python Code
Python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv('gender.csv')
df.columns = df.columns.str.strip()
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip()
if 'Unnamed: 9' in df.columns:
    df = df.drop(columns=['Unnamed: 9'])

features = ['Age', 'Height (cm)', 'Weight (kg)', 'Income (USD)', 'Education Level', 'Marital Status']
X = df[features]

X = pd.get_dummies(X, drop_first=True)

y = df['Gender'].map({'female': 0, 'male': 1})
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred, target_names=['female', 'male'])

print(f"Model Accuracy: {accuracy:.4f}\n")
print("Confusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(class_report)