import numpy as np
import pandas as pd



data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["HR", "IT", "IT", "Sales", "HR"],
    "Age": [25, 30, np.nan, 40, 28],  
    "Salary": [60000, 85000, 95000, 70000, 62000],
}

df = pd.DataFrame(data)
print("--- 1. Original DataFrame ---")
print(df, "\n")



print("--- 2. Data Inspection ---")
print(f"Shape of data (Rows, Columns): {df.shape}")
print("\nBasic Statistical Summary:")
print(df.describe())  
print("\n")



print("--- 3. Data Cleaning ---")

average_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(average_age)
print("DataFrame after fixing missing values:")
print(df, "\n")



print("--- 4. Filtering & Selection ---")

high_earners = df[df["Salary"] > 65000]
print("Employees making more than 65k:")
print(high_earners, "\n")


print("Just Names and Departments:")
print(df[["Name", "Department"]], "\n")



print("--- 5. Modifying Columns ---")

df["Bonus"] = df["Salary"] * 0.10
print("DataFrame with new Bonus column:")
print(df, "\n")



print("--- 6. Grouping & Aggregating ---")

avg_salary_by_dept = df.groupby("Department")["Salary"].mean()
print("Average Salary by Department:")
print(avg_salary_by_dept)