import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
print("Current working directory:", os.getcwd())
print("Files in this folder:", os.listdir())


df = pd.read_csv(
    "python/hr_data_analyzer/WA_Fn-UseC_-HR-Employee-Attrition.csv")

print(df.head())

print("Shape of dataset:", df.shape)


print("Columns:", df.columns.tolist())


print("\n--- Dataset Info ---")
print(df.info())


print("\n--- Summary Statistics ---")
print(df.describe())


print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Attrition Counts ---")
print(df['Attrition'].value_counts())

print("\n--- Departments ---")
print(df['Department'].unique())

print("\n--- Job Roles ---")
print(df['JobRole'].unique())


plt.figure(figsize=(6, 4))
sns.countplot(x="Department", hue="Attrition", data=df)
plt.title("Attrition by Department")
plt.show()

plt.figure(figsize=(6, 4))
sns.histplot(data=df, x="Age", hue="Attrition", multiple="stack")
plt.title("Attrition by Age")
plt.show()
