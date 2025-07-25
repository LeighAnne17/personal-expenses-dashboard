#library import
import pandas as pd
import matplotlib.pyplot as plt

#dataset
df = pd.read_excel('expenses_data.xlsx')

print(df.head())
print("\nDataset Info:")
print(df.info())

#date to datetime
df['Date'] = pd.to_datetime(df['Date'])

#text data claning
df['Category'] = df['Category'].str.strip().str.lower()
df['Payment Method'] = df['Payment Method'].str.strip().str.lower()

#new columns
df['Month'] = df['Date'].dt.to_period('M')
df['Day of the Week'] = df['Date'].dt.day_name()

#Checking for duplicated or missing data
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicates:")
print(df.duplicated().sum())

#Duplicate removal
df = df.drop_duplicates()

#saving cleaned data
df.to_csv("cleaned_expenses.csv", index=False)
print("\nCleaned Data Sample:")
print(df.head())