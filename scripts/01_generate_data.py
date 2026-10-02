import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

data = {
'Order_ID': [f'ORD{1000+i}' for i in range(n)],
'Date': pd.date_range('2024-01-01', periods=n, freq='D'),
'Product': np.random.choice(['Laptop', 'Mobile', 'Tablet', 'Headphone', 'Charger', 'Smartwatch'], n),
'Category': np.random.choice(['Electronics', 'Accessories', 'Gadgets'], n),
'Region': np.random.choice(['North', 'South', 'East', 'West'], n),
'State': np.random.choice(['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 'Pune', 'Hyderabad'], n),
'Sales': np.random.randint(1000, 50000, n),
'Quantity': np.random.randint(1, 20, n),
'Profit': np.random.randint(100, 15000, n),
'Customer_Age': np.random.randint(18, 60, n),
'Payment_Mode': np.random.choice(['UPI', 'Card', 'Cash', 'NetBanking'], n)
}

df = pd.DataFrame(data)
df.to_csv('../data/sales_data.csv', index=False)

print("Dataset ban gaya!")
print(f"Total rows: {len(df)}")
print("Saved at: ../data/sales_data.csv")
print(df.head())
