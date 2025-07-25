import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_expenses.csv")

#Total spend
category_spend = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
print("Total spend by Category:")
print(category_spend)

#plotting
category_spend.plot(kind='bar', title='Total spend by Category', figsize=(10, 5), color='blue')
plt.ylabel('Amount (ZAR)')
plt.tight_layout()
plt.show()

#Monthly average spend
monthly_avspend= df.groupby('Month')['Amount'].mean()
print("\nAverage monthly spend:")
print(monthly_avspend)

#ploting
monthly_avspend.plot(kind='line', title='Average Monthly Spend', marker='o', figsize=(8, 4), color='skyblue')
plt.ylabel(' (ZAR)')
plt.tight_layout()
plt.show()

#Daily spend
df['Date'] = pd.to_datetime(df['Date'])
daily_spend = df.groupby('Date')['Amount'].sum()

#plotting
daily_spend.plot(title='Daily Spending Over Time', figsize=(12, 4), color='green')
plt.ylabel('Total Daily Spend (ZAR)')
plt.tight_layout()
plt.show()

#Highest spending days(top 10)
top_days = df.groupby('Date')['Amount'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 highest spending days:")
print(top_days)

#Pie Chart
category_spend.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), title='Spending Share of Categories')
plt.ylabel('')
plt.tight_layout()
plt.show()
